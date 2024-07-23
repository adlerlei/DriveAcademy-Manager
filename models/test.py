# 筆試，場考，道考
import sqlite3
import os
import csv
from tkinter import messagebox, filedialog
from tkinter import filedialog
# 導入 re 模組,用於處理字符串的正則表達式操作
import re

# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

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
    if uid == 1: # 場考 , 道考
        cursor.execute('''
            UPDATE student SET
                road_test_date = :road_test_date, -- 路試日期38
                driving_test_group = :driving_test_group, -- 組別39
                road_test_items_type = :road_test_items_type, -- 路考項目40
                driving_test_number = :driving_test_number -- 號碼42
            WHERE id = :id
        ''', data)
        messagebox.showinfo('訊息', '已加入 道考 名冊！')
    elif uid == 2: # 筆試
        cursor.execute('''
            UPDATE student SET
                written_exam_date = :written_exam_date, -- 筆試日期36
                driving_test_code = :driving_test_code, -- 代碼44
                driving_test_session = :driving_test_session, -- 場次43
                driving_test_number = :driving_test_number -- 號碼42
            WHERE id = :id
        ''', data)
        messagebox.showinfo('訊息', '已加入 筆試 名冊')

    conn.commit()
    conn.close()

# 路考清冊 - 匯出 csv 文件按鈕觸發
# 匯出內容 (上課期別代碼 / 身分證字號 / 出生日期 / 組別 / 路試日期 / 號碼 / 路考項目 )
# def export_selected_data(treeview):
#     # 獲取所選行
#     # selected_items = treeview.get_children()
#     selected_items = treeview.get_children() # 直接取得所有行
#     if not selected_items:
#         messagebox.showwarning("警告", "資料列表為空！請先加入路考清冊的學員！")
#         return

#     # 獲取學員資料庫中的手機欄位
#     conn = sqlite3.connect(database_path)
#     cursor = conn.cursor()
#     cursor.execute("SELECT national_id_no, mobile_phone FROM student")
#     mobile_phone_data = cursor.fetchall()
#     conn.close()

#     # 獲取所選行的數據
#     data = []
#     register_number = None  # 初始化 register_number 變量
#     for item in selected_items:
#         item_values = treeview.item(item)["values"]
#         national_id_no = str(item_values[9])  # 獲取身分證字號
#         birth_date = str(item_values[8])  # 獲取生日
#         student_name = str(item_values[3])  # 獲取姓名
#         mobile_phone = ""
#         for student_id, phone in mobile_phone_data:
#             if student_id == national_id_no:
#                 mobile_phone = str(phone)
#                 break
#         register_number = str(item_values[0])  # 獲取名冊號碼
#         register_number = register_number[:-3]  # 移除最後三個字符 001 ~ xxx
#         exam_code = str(item_values[4])  # 獲取來源類別編號
#         transmission_type_code = str(item_values[5])  # 獲取手自排類別編號
#         instructor_number = str(item_values[6]).zfill(3) # 獲取教練編號
#         training_type_code = str(item_values[13]) # 獲取訓練班別代號

#         # 獲取教練身分證號碼和出生日期
#         conn = sqlite3.connect(database_path)
#         cursor = conn.cursor()
#         cursor.execute("SELECT national_id_no, birth_date FROM instructor WHERE number = ?", (instructor_number,))
#         instructor_data = cursor.fetchone()
#         conn.close()

#         if instructor_data:
#             instructor_national_id_no, instructor_birth_date = instructor_data
#         else:
#             instructor_national_id_no, instructor_birth_date = "", ""


#         data.append(f"{national_id_no},{birth_date},{student_name},{mobile_phone},{register_number},{exam_code},{transmission_type_code},{instructor_national_id_no},{instructor_birth_date}")
    
#     if register_number is not None:
#         year_from_data = register_number
#         file_name = generate_csv_filename(year_from_data, training_type_code)

#         # 創建文件保存對話框
#         file_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile=file_name)
#         if file_path:
#             try:
#                 # 將數據寫入文件
#                 with open(file_path, "w", newline='', encoding="utf-8") as f:
#                     f.write("\n".join(data))
#                 messagebox.showinfo("成功", "匯出文件成功!")
#             except Exception as e:
#                 messagebox.showerror("錯誤", f"匯出文件失敗: {str(e)}")
#     else:
#         messagebox.showerror("錯誤", "未找到任何數據!")

# # 創建 CSV 自動生成文件名稱
# def generate_csv_filename(register_number, training_type_code):
#     # 根據你的固定格式生成文件名稱
#     return f"400032{training_type_code}{register_number}_B.csv"


import csv
import sqlite3
from tkinter import filedialog, messagebox

def export_driving_test_data(database_path):
    try:
        # 连接到数据库
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # 获取最新的上课期别代码
        cursor.execute("SELECT MAX(term_class_code) FROM annual_plan")
        latest_term_class_code = cursor.fetchone()[0]

        if not latest_term_class_code:
            messagebox.showerror("错误", "未找到有效的上课期别代码")
            return

        # 构造文件名
        filename = f"400032{latest_term_class_code}_E.csv"

        # 打开文件对话框
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile=filename)
        if not file_path:
            return  # 用户取消了保存

        # 查询所有需要导出的数据
        cursor.execute("""
            SELECT s.register_term, s.national_id_no, s.birth_date, s.driving_test_group, 
                   s.road_test_date, s.driving_test_number, s.road_test_items_type
            FROM student s
            WHERE s.road_test_date IS NOT NULL
            ORDER BY s.register_term, s.driving_test_number
        """)
        data = cursor.fetchall()

        # 写入CSV文件
        with open(file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                # 确保每个字段都有值，如果为None则替换为空字符串
                processed_row = [str(item) if item is not None else '' for item in row]
                writer.writerow(processed_row)

        messagebox.showinfo("成功", f"数据已成功导出到 {file_path}")

    except Exception as e:
        messagebox.showerror("错误", f"导出文件时发生错误：{str(e)}")
        print(f"错误详情: {e}")  # 打印详细错误信息

    finally:
        if conn:
            conn.close()