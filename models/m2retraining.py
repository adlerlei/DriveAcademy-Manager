# M2 補訓名冊 功能邏輯介面
import sqlite3
import os
from tkinter import messagebox


# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 驗證學員資料輸入欄位
validation_fields = {
    'exam_type_name': '筆路',
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
                exam_code = :exam_code, -- 來源類別編號
                exam_name = :exam_name, -- 來源類別名稱
                transmission_type_code = :transmission_type_code, -- 手自排類別編號
                transmission_type_name = :transmission_type_name, -- 手自排類別名稱
                instructor_number = :instructor_number, -- 教練編號
                instructor_name = :instructor_name, -- 教練名稱
                exam_type_name = :exam_type_name  -- 筆試路試
            WHERE id = :id
        ''', data)
    messagebox.showinfo('訊息', '已加入 M2 補訓名冊！')

    conn.commit()
    conn.close()
