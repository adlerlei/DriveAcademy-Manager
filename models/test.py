# 筆試，場考，道考
import sqlite3
import os
# import csv
from tkinter import messagebox
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