# 開訓結訓名冊 功能邏輯介面
# 對應介面 ui/opening_training_rester.py , closing_training_roster.py
import sqlite3
import os
# import csv
from tkinter import messagebox
from tkinter import filedialog
import re

# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 驗證學員資料輸入欄位
validation_fields = {
    'exam_code': '來源類別編號',
    'exam_name': '來源類別名稱',
    'transmission_type_code': '手自排類別編號',
    'transmission_type_name': '手自排類別名稱',
    'instructor_number': '教練編號',
    'instructor_name': '教練名稱',
    'register_term': '期別',
    'register_number': '名冊號碼',
    'dropout': '退訓'
}

# 抓取教練資料表（編號，名稱）下拉選單監聽
def get_instructor_data():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute("SELECT number, name FROM instructor")
    instructor_data = cursor.fetchall()

    conn.close()

    instructor_numbers = []
    instructor_names = []
    instructor_dict = {}

    for item in instructor_data:
        instructor_numbers.append(item[0])
        instructor_names.append(item[1])
        instructor_dict[item[0]] = item[1]

    return instructor_numbers, instructor_names, instructor_dict

# 抓取期別資料表下拉選單值
def get_term_data():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT term FROM annual_plan")
    term_data = cursor.fetchall()

    conn.close()

    term_list = []
    for item in term_data:
        term_list.append(item[0])

    return term_list


# 根據指定的條件查詢學員資料
def get_student_data(identifier, value):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    query = f"SELECT * FROM student WHERE {identifier} = ?"
    cursor.execute(query, (value,))
    result = cursor.fetchone()

    conn.close()
    return result


# 更新學員資料
def update_student_data(data, uid):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # 處理名冊號碼並生成 student_term_class_code
    register_number = data.get('register_number', '')
    training_type_code = data.get('training_type_code', '')
    student_term_class_code = ''
    
    if register_number and training_type_code: 
        # 生成完整的 student_term_class_code
        student_term_class_code = f"{training_type_code}{register_number}"

    if uid == 1:
        cursor.execute('''
            UPDATE student SET
                register_number = :register_number,
                register_term = :register_term,
                exam_code = :exam_code,
                exam_name = :exam_name,
                transmission_type_code = :transmission_type_code,
                transmission_type_name = :transmission_type_name,
                instructor_number = :instructor_number,
                instructor_name = :instructor_name,
                register_batch = :register_batch,
                student_term_class_code = :student_term_class_code
            WHERE id = :id
        ''', {**data, 'student_term_class_code': student_term_class_code})
        messagebox.showinfo('訊息', '已加入開訓名冊！')
    elif uid == 0:
        cursor.execute('''
            UPDATE student SET
                register_number = :register_number,
                register_term = :register_term,
                dropout = :dropout,
                transmission_type_code = :transmission_type_code,
                transmission_type_name = :transmission_type_name,
                instructor_number = :instructor_number,
                instructor_name = :instructor_name,
                register_batch = :register_batch,
                student_term_class_code = :student_term_class_code
            WHERE id = :id
        ''', {**data, 'student_term_class_code': student_term_class_code})
        messagebox.showinfo('訊息', '已加入結訓名冊！')

    conn.commit()
    conn.close()


# 匯出 csv 文件按鈕觸發
def export_selected_data(treeview):
    # 獲取所選行
    selected_items = treeview.get_children()
    if not selected_items:
        messagebox.showwarning("警告", "資料列表為空！請先加入開訓名冊的學員！")
        return

    # 獲取學員資料庫中的手機欄位
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT national_id_no, mobile_phone FROM student")
    mobile_phone_data = cursor.fetchall()
    conn.close()

    # 獲取所選行的數據
    data = []
    register_number = None  # 初始化 register_number 變量
    for item in selected_items:
        item_values = treeview.item(item)["values"]
        national_id_no = str(item_values[9])  # 獲取身分證字號
        birth_date = str(item_values[8])  # 獲取生日
        student_name = str(item_values[3])  # 獲取姓名
        mobile_phone = ""
        for student_id, phone in mobile_phone_data:
            if student_id == national_id_no:
                mobile_phone = str(phone)
                break
        register_number = str(item_values[0])  # 獲取名冊號碼

        # 移除這一行，因為我們現在需要完整的 register_number
        # register_number = register_number[:-3]  # 移除最後三個字符 001 ~ xxx

        exam_code = str(item_values[4])  # 獲取來源類別編號
        transmission_type_code = str(item_values[5])  # 獲取手自排類別編號
        instructor_number = str(item_values[6]).zfill(3) # 獲取教練編號
        training_type_code = ""
        if len(item_values) > 13:
            training_type_code = str(item_values[13])  # 獲取訓練班別代號
        # student_term_class_code = str(item_values[45])

        # 獲取教練身分證號碼和出生日期
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute("SELECT instructor_number, birth_date FROM instructor WHERE number = ?", (instructor_number,))
        instructor_data = cursor.fetchone()
        conn.close()

        if instructor_data:
            instructor_national_id_no, instructor_birth_date = instructor_data
        else:
            instructor_national_id_no, instructor_birth_date = "", ""


        data.append(f"{national_id_no},{birth_date},{student_name},{mobile_phone},0{training_type_code}{register_number},{exam_code},{transmission_type_code},{instructor_national_id_no},{instructor_birth_date}")
    
    if register_number is not None:
        # 找到第一個字母的位置
        alpha_index = next((i for i, c in enumerate(register_number) if c.isalpha()), None)
        if alpha_index is not None:
            # 保留到字母（包括字母）用於文件名
            register_number_for_filename = register_number[:alpha_index+1]
        else:
            register_number_for_filename = register_number

        file_name = generate_csv_filename(register_number_for_filename, training_type_code)

        # 創建文件保存對話框
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile=file_name)
        if file_path:
            try:
                # 將數據寫入文件
                with open(file_path, "w", newline='', encoding="utf-8") as f:
                    f.write("\n".join(data))
                messagebox.showinfo("成功", "匯出文件成功!")
            except Exception as e:
                messagebox.showerror("錯誤", f"匯出文件失敗: {str(e)}")
    else:
        messagebox.showerror("錯誤", "未找到任何數據!")

# 創建 CSV 自動生成文件名稱
def generate_csv_filename(register_number, training_type_code):
    # 根據你的固定格式生成文件名稱
    return f"400032{training_type_code}{register_number}_B.csv"