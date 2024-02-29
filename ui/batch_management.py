# 期別管理界面
import tkinter as tk
from tkinter import ttk
from utils.utility_functions import clear_frame, ui_font


# 建立期別介面
def create_batch_window(frame_main):
    clear_frame(frame_main)

    # 視窗標題 - 年度計畫編排文字 ###########################
    frame_title = tk.Frame(frame_main)
    frame_title.pack( fill="x")
    frame_title_label = tk.Label(frame_title, text="期別新增作業 / 年度計畫編排", font=ui_font())
    frame_title_label.pack(side="left", padx=20, pady=7)

    
    # row1 - 新增，修改，刪除按鈕 ###########################
    frame_btn = tk.Frame(frame_main)
    frame_btn.pack( fill="x")
    
    add_btn = tk.Button(frame_btn, font=ui_font(), text="新增", width=8, height=3)
    add_btn.pack(side="left", padx=(20, 0), pady=7)
    
    fix_btn = tk.Button(frame_btn, font=ui_font(), text="修改", width=8, height=3)
    fix_btn.pack(side="left", pady=7)
    
    delete_btn = tk.Button(frame_btn, font=ui_font(), text="刪除", width=8, height=3)
    delete_btn.pack(side="left", pady=7)
    
    # row2 - 輸入欄位表單 ###########################
    frame_form = tk.Frame(frame_main)
    frame_form.pack( fill="x")
    
    tk.Label(frame_form, text="訓練班別：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)

    # 訓練班別代號下拉選單
    training_var = ['1','2','3']
    training_box = ttk.Combobox(
        frame_form, 
        width=3, 
        font=ui_font(),
        values=training_var)
    training_box.pack(side="left", pady=7)

    
    # 顯示訓練班別的值
    training_data = tk.Entry(frame_form, width=15, font=ui_font())
    training_data.pack(side="left", pady=7)
    
    # 年度輸入欄位
    tk.Label(frame_form, font=ui_font(), text="年度：").pack(side="left", padx=(20, 0), pady=7)
    year = tk.Entry(frame_form, width=7, font=ui_font())
    year.pack(side="left", pady=7)
    
    # 期別
    tk.Label(frame_form, font=ui_font(), text="期別：").pack(side="left", padx=(20, 0), pady=7)
    term = tk.Entry(frame_form, font=ui_font(), width=7)
    term.pack(side="left", pady=7)
    
    # 梯次
    class_var = ['A','B']
    class_box = ttk.Combobox(
        frame_form,
        width=3,
        font=ui_font(),
        values=class_var)
    class_box.pack(side="left", pady=7)
    
    # 開訓日期
    tk.Label(frame_form, font=ui_font(), text="開訓日期：").pack(side="left", padx=(20, 0), pady=7)
    training_date = tk.Entry(frame_form, font=ui_font(),  width=10)
    training_date.pack(side="left", pady=7)
    
    # 結訓日期
    tk.Label(frame_form, font=ui_font(), text="結訓日期：").pack(side="left", padx=(20, 0), pady=7)
    training_date_end = tk.Entry(frame_form, font=ui_font(), width=10)
    training_date_end.pack(side="left", pady=7)
    
    # row3 - 資料顯示列表 ###########################
    display_data = tk.Frame(frame_main)
    display_data.pack( fill="x")
    
    # 年度計畫編排 - Treeview資料顯示列表
    tree_view = ttk.Treeview(display_data, columns=("1", "2", "3", "4", "5", "6", "7", "8"), show="headings")
    