# 期別新增 - 年度計畫表與期別新增
import sqlite3
import os
from tkinter import messagebox

# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 將年度計畫表與期別新增資料庫中
def insert_annual_plan_data(year, term, batch, training_type_code, training_type_name, start_date, end_date):
    
    # 連接資料庫
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    # 新增期別新增資料
    c.execute("INSERT INTO term (year, term, batch, training_type_code, training_type_name, start_date, end_date) VALUES (?,?,?,?,?,?,?)", (year, term, batch, training_type_code, training_type_name, start_date, end_date))

    # 提交變更並關閉連線
    conn.commit()
    conn.close()

    messagebox.showinfo("成功", "新增期別資料成功！")