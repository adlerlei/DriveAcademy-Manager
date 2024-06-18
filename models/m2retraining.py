# 補訓名冊
import sqlite3
import os
# import csv
from tkinter import messagebox
from tkinter import filedialog
# 導入 re 模組,用於處理字符串的正則表達式操作
import re

# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')


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

    return term_list