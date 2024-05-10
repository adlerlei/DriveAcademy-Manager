# student.py
import sqlite3
import os
import customtkinter as ctk
from tkinter import messagebox

# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 抓取教練資料表信息（編號，名稱）
def get_instructors():
    # 連接到資料庫
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    # 從教練資料表中獲取教練編號和教練名稱
    c.execute("SELECT number, name FROM instructor")
    instructors = c.fetchall()

    # 關閉資料庫連接
    conn.close()

    instructor_numbers = [instructor[0] for instructor in instructors]
    instructor_names = [instructor[1].strip() for instructor in instructors]  # 去除名稱中的空白字符

    return instructor_numbers, instructor_names

def on_instructor_selected(event, instructor_number, instructor_numbers, instructor_names, instructor_name):
    selected_number = event.widget.get()
    index = instructor_numbers.index(selected_number)

    # Clear the entry before inserting the new name
    instructor_name.delete(0, ctk.END)

    instructor_name.insert(0, instructor_names[index])