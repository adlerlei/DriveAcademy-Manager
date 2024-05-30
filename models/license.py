# 學照日期送件，登錄
import sqlite3
import os
from tkinter import messagebox
import customtkinter as ctk


# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 更新學員資料庫



# 搜尋學員資料庫
# 根據指定的條件查詢學員資料
def get_student_data(identifier, value):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    query = f"SELECT * FROM student WHERE {identifier} = ?"
    cursor.execute(query, (value,))
    result = cursor.fetchone()
    
    conn.close()
    # 打印終端機顯示資料是否正確
    print(result)
    return result