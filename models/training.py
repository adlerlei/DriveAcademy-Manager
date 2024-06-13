# 開訓結訓名冊
import sqlite3
import os
import csv
from tkinter import messagebox
from tkinter import filedialog
# 導入 re 模組,用於處理字符串的正則表達式操作
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

    # DISTINCT 是 SQL 查詢語句中的一個關鍵字，用於去除查詢結果中的重複值。
    # 當你在一個資料表中查詢某個欄位時，如果該欄位中有重複的數據，使用 DISTINCT 關鍵字可以確保查詢結果中每個值都是唯一的
    # cursor.execute("SELECT term FROM annual_plan")
    cursor.execute("SELECT DISTINCT term FROM annual_plan")
    term_data = cursor.fetchall()

    conn.close()

    term_list = []
    for item in term_data:
        term_list.append(item[0])

    # 將數據從元組轉換為列表
    # term_list = [item[0] for item in term_data]
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

    if uid == 1:
        cursor.execute('''
            UPDATE student SET
                register_number = :register_number, -- 名冊號碼
                register_term = :register_term, -- 名冊期別
                exam_code = :exam_code, -- 來源類別編號
                exam_name = :exam_name, -- 來源類別名稱
                transmission_type_code = :transmission_type_code, -- 手自排類別編號
                transmission_type_name = :transmission_type_name, -- 手自排類別名稱
                instructor_number = :instructor_number, -- 教練編號
                instructor_name = :instructor_name, -- 教練名稱
                register_batch = :register_batch -- 名冊梯次
            WHERE id = :id
        ''', data)
        messagebox.showinfo('訊息', '學照登錄完成！')
    elif uid == 0:
        cursor.execute('''
            UPDATE student SET
                register_number = :register_number, -- 名冊號碼
                register_term = :register_term, -- 名冊期別
                dropout = :dropout, -- 退訓
                transmission_type_code = :transmission_type_code, -- 手自排類別編號
                transmission_type_name = :transmission_type_name, -- 手自排類別名稱
                instructor_number = :instructor_number, -- 教練編號
                instructor_name = :instructor_name, -- 教練名稱
                register_batch = :register_batch -- 名冊梯次
            WHERE id = :id
        ''', data)
        messagebox.showinfo('訊息', '學照送件完成！')

    conn.commit()
    conn.close()


# 匯出 csv 文件按鈕觸發
def export_selected_data(treeview):
    # 獲取所選行
    selected_items = treeview.selection()
    if not selected_items:
        messagebox.showwarning("警告", "請先選擇要匯出的行!")
        return

    # 獲取所選行的數據
    data = []
    for item in selected_items:
        item_values = treeview.item(item)["values"]
        start_date = str(item_values[3])  # 確保開訓日期為字符串
        end_date = str(item_values[4])  # 確保結訓日期為字符串
        term_class_code = str(item_values[5])

        rowid = treeview.item(item)["text"]  # 獲取 rowid
        
        start_date = re.sub(r'/', '', start_date)  # 去除開訓日期中的 /
        end_date = re.sub(r'/', '', end_date)  # 去除結訓日期中的 /
        data.append(f"{start_date},{end_date},{term_class_code}")

        # 從資料庫中獲取 training_type_code
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.execute("SELECT training_type_code FROM annual_plan WHERE rowid=?", (rowid,))
        training_type_code = c.fetchone()[0]
        conn.close()

    year_from_data = str(item_values[1])
    # 生成文件名稱
    file_name = generate_csv_filename(year_from_data, training_type_code)

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


# 創建 CSV 自動生成文件名稱
def generate_csv_filename(year, training_type_code):
    # 根據你的固定格式生成文件名稱
    return f"400032{year}{training_type_code}_A.csv"