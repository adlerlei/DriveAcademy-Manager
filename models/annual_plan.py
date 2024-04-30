# 期別新增 - 年度計畫表與期別新增
import sqlite3
import os
from tkinter import messagebox

# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 將年度計畫表與期別新增資料庫中
def insert_annual_plan_data(year, term, term_class_code, batch, training_type_code, training_type_name, start_date, end_date):
    
    # 連接資料庫
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    # 新增期別資料
    c.execute("INSERT INTO annual_plan (year, term, term_class_code, batch, training_type_code, training_type_name, start_date, end_date) VALUES (?,?,?,?,?,?,?,?)", (year, term, term_class_code, batch, training_type_code, training_type_name, start_date, end_date))

    # 提交變更並關閉連線
    conn.commit()
    conn.close()

    messagebox.showinfo("成功", "新增期別資料成功！")


# 取得年度計畫表與期別新增資料
def fetch_and_populate_treeview(treeview):
    # 連接到資料庫
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    # 執行 SQL 查詢
    c.execute("SELECT * FROM annual_plan")
    results = c.fetchall()

    # 清除 Treeview 中的所有數據
    treeview.delete(*treeview.get_children())

    # 插入數據到 Treeview
    for row in results:
        treeview.insert("", "end", values=(row[6], row[1], row[2], row[7], row[8], row[3]))

    # 關閉資料庫連線
    conn.close()