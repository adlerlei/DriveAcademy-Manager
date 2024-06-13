# 開訓結訓名冊
import sqlite3
import os
import csv
from tkinter import messagebox
from tkinter import filedialog
# 導入 re 模組,用於處理字符串的正則表達式操作
import re


# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

def export_to_csv(treeview, data_list):
    # 獲取TreeView的數據
    tree_data = data_list.get_children()
    # selected_items = treeview.selection() # 針對用戶選取的行做處理
    # selected_items = treeview.get_children() # 直接取得所有行


    # 準備要匯出的數據
    data_to_export = []

    # 循環TreeView的數據
    for row in tree_data:
        # 獲取 treeview 中各個欄位的數據
        row_values = data_list.item(row)['values']
        national_id_no = row_values[9] # 身分證字號