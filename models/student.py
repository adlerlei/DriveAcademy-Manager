# student.py
import sqlite3
import os
import customtkinter as ctk
from tkinter import messagebox

# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 抓取期別資料表（梯次）下拉選單 ######
def get_annual_plan_batch_data():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # 查詢期別資料表中的梯次
    cursor.execute("SELECT batch FROM annual_plan")
    batch_data = cursor.fetchall()

    # 關閉資料庫連接
    conn.close()

    # 創建一個空列表存儲梯次
    batch_data_list = []

    # 遍歷查詢結果，將梯次添加到列表中
    for item in batch_data:
        batch_data_list.append(item[0])

    return batch_data_list


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