# student.py
import sqlite3
import os
from tkinter import messagebox

# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 抓取郵局地址信息資料表
def address_data():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # 查詢郵遞區號 zip_code 資料表
    cursor.execute("SELECT zip_code, city FROM address_data")
    zip_code_data = cursor.fetchall()

    # 關閉資料庫連接
    conn.close()

    # 創建一個空列表存儲郵遞區號
    address_zip_code_lists = []
    # 創建一個空字典存儲區域
    address_city_lists = []
    # 創建一個空字典存儲郵遞區號和區域的對應關係
    address_dict = {}

    # 遍歷查詢結果，將郵遞區號添加到列表中
    for r_address_zip_code in zip_code_data:
        address_zip_code_lists.append(r_address_zip_code[0])
        address_city_lists.append(r_address_zip_code[1])
        address_dict[r_address_zip_code[0]] = r_address_zip_code[1]

    return address_zip_code_lists, address_city_lists, address_dict


# 抓取教練資料表（編號，名稱）下拉選單監聽 ######
def get_instructor_data():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # 查詢教練資料表中的編號和名稱
    cursor.execute("SELECT number, name FROM instructor")
    instructor_data = cursor.fetchall()

    # 關閉資料庫連接
    conn.close()

    # 創建一個空列表存儲教練編號
    instructor_numbers = []
    # 創建一個空列表存儲教練名稱
    instructor_names = []
    # 創建一個空字典存儲教練編號和名稱的對應關係
    instructor_dict = {}

    # 遍歷查詢結果，將教練編號添加到列表中，將教練編號和名稱添加到字典中
    for item in instructor_data:
        instructor_numbers.append(item[0])
        instructor_names.append(item[1])
        instructor_dict[item[0]] = item[1]

    return instructor_numbers, instructor_names, instructor_dict


# student_all.py 用戶輸入寫入資料表中
# def insert_student_data(student_number, student_name, student_gender, student_birthday, student_email, student_phone, student_address_zip_code, student_instructor_number):