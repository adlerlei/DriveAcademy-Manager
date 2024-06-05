# 開訓結訓名冊
import sqlite3
import os
from tkinter import messagebox

# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 驗證學員資料輸入欄位
validation_fields = {
    'exam_code': '來源類別編號',
    'exam_name': '來源類別名稱',
    'transmission_type_code': '手自排類別編號',
    'transmission_type_name': '手自排類別名稱',
    'instructor_number': '教練編號',
    'instructor_name': '教練名稱'
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

    # 將數據從元組轉換為列表
    term_list = [item[0] for item in term_data]
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
def update_student_data(data):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE student SET
            register_term = :register_term,
            exam_code = :exam_code,
            exam_name = :exam_name,
            transmission_type_code = :transmission_type_code,
            transmission_type_name = :transmission_type_name,
            instructor_number = :instructor_number,
            instructor_name = :instructor_name
        WHERE id = :id
    ''', data)

    conn.commit()
    conn.close()
    messagebox.showinfo('訊息', '已更新學員資料！')