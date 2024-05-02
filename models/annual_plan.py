# 期別新增 - 年度計畫表與期別新增
import sqlite3
import os
from tkinter import messagebox

# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 將年度計畫表寫入資料庫中
def insert_annual_plan_data(year, term, term_class_code, batch, training_type_code, training_type_name, start_date, end_date):
    
    # 連接資料庫
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    # 新增期別資料
    c.execute("INSERT INTO annual_plan (year, term, term_class_code, batch, training_type_code, training_type_name, start_date, end_date) VALUES (?,?,?,?,?,?,?,?)", (year, term, term_class_code, batch, training_type_code, training_type_name, start_date, end_date))

    # 提交變更並關閉連線
    conn.commit()
    conn.close()

    messagebox.showinfo("成功", "已新增期別資料！")


# 讀取年度計畫表資料
def fetch_and_populate_treeview(treeview):
    # 連接到資料庫
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    # 執行 SQL 查詢
    c.execute("SELECT rowid, * FROM annual_plan")
    results = c.fetchall()

    # 清除 Treeview 中的所有數據
    treeview.delete(*treeview.get_children())

    # 插入數據到 Treeview
    for row in results:
        treeview.insert("", "end", text=str(row[0]), values=(row[7], row[2], row[3], row[8], row[9], row[4]))

    # 關閉資料庫連線
    conn.close()


# 刪除按鈕觸發
def delete_btn_click(treeview):
    # 獲取所選擇的行
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showwarning("警告", "請先選擇要刪除的行!")
        return

    # 獲取所選行的數據
    item_values = treeview.item(selected_item)["values"]
    training_type_name, year, term, start_date, end_date, term_class_code = item_values

    # 從資料庫中刪除對應記錄
    delete_from_db(training_type_name, year, term, start_date, end_date, term_class_code)

    # 更新 Treeview
    fetch_and_populate_treeview(treeview)


# 從資料庫中刪除記錄
def delete_from_db(training_type_name, year, term, start_date, end_date, term_class_code):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("DELETE FROM annual_plan WHERE training_type_name=? AND year=? AND term=? AND start_date=? AND end_date=? AND term_class_code=?",
              (training_type_name, year, term, start_date, end_date, term_class_code))
    conn.commit()
    conn.close()
    messagebox.showinfo("成功", "刪除記錄成功!")


# 更新資料庫記錄
# def update_record_in_db(record_id, new_training_type_name, new_year, new_term, new_start_date, new_end_date, new_term_class_code, new_batch, new_training_type_code):
#     conn = sqlite3.connect(database_path)
#     c = conn.cursor()
#     c.execute("UPDATE annual_plan SET training_type_name=?, year=?, term=?, start_date=?, end_date=?, term_class_code=?, batch=?, training_type_code=? "
#               "WHERE rowid=?",
#               (new_training_type_name, new_year, new_term, new_start_date, new_end_date, new_term_class_code, new_batch, new_training_type_code, record_id))
#     conn.commit()
#     conn.close()
#     messagebox.showinfo("成功", "修改記錄成功!")