# 期別新增 - 年度計畫表與期別新增
import sqlite3
import os
from tkinter import messagebox
from tkinter import filedialog
# 導入 re 模組,用於處理字符串的正則表達式操作
import re

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
        treeview.insert("", "end", text=str(row[0]), values=(row[7], row[2], row[3], row[8], row[9], row[4], row[5]))

    # 關閉資料庫連線
    conn.close()


# 匯出 csv 文件按鈕觸發
def export_selected_data(treeview):
    # 獲取所選行
    selected_items = treeview.selection()
    if not selected_items:
        messagebox.showwarning("警告", "請先選擇要匯出的行!")
        return

    # 獲取所選行的數據
    data = []
    for item in selected_items:
        item_values = treeview.item(item)["values"]
        start_date = str(item_values[3])  # 確保開訓日期為字符串
        end_date = str(item_values[4])  # 確保結訓日期為字符串
        term_class_code = str(item_values[5])

        rowid = treeview.item(item)["text"]  # 獲取 rowid
        
        start_date = re.sub(r'/', '', start_date)  # 去除開訓日期中的 /
        end_date = re.sub(r'/', '', end_date)  # 去除結訓日期中的 /
        data.append(f"{start_date},{end_date},{term_class_code}")

        # 從資料庫中獲取 training_type_code
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.execute("SELECT training_type_code FROM annual_plan WHERE rowid=?", (rowid,))
        training_type_code = c.fetchone()[0]
        conn.close()

    year_from_data = str(item_values[1])
    # 生成文件名稱
    file_name = generate_csv_filename(year_from_data, training_type_code)

    # 創建文件保存對話框
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile=file_name)
    if file_path:
        try:
            # 將數據寫入文件
            with open(file_path, "w", newline='', encoding="utf-8") as f:
                f.write("\n".join(data))
            messagebox.showinfo("成功", "匯出文件成功!")
        except Exception as e:
            messagebox.showerror("錯誤", f"匯出文件失敗: {str(e)}")


# 創建 CSV 自動生成文件名稱
def generate_csv_filename(year, training_type_code):
    # 根據你的固定格式生成文件名稱
    return f"400032{year}{training_type_code}_A.csv"


# 刪除 treeview 資料列表以及相關資料庫欄位
def delete_btn_click(data_list):
    selected = data_list.selection()
    if selected:
        # 抓取 資料庫 term '期別' 來尋找該資料行 id
        record_id = data_list.item(selected[0], 'values')[2] 

        conn = sqlite3.connect(database_path)
        c = conn.cursor()

        # 刪除針對選取的 term 該行資料 id，從資料庫移除
        c.execute("DELETE FROM annual_plan WHERE term = ?", (record_id,))
        conn.commit()

        # 刪除 treeview 資料列表中的資料
        data_list.delete(selected)
        conn.close()