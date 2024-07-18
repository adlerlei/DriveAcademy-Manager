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
            road_test_date = :road_test_date,
            driving_test_group = :driving_test_group,
            road_test_items_type = :road_test_items_type,
            driving_test_number = :driving_test_number
        WHERE id = :id
    ''', data)
    messagebox.showinfo('訊息', '已加入 道路考試 名冊！')

    conn.commit()
    conn.close()