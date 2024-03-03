# 期別管理界面
import tkinter as tk
from tkinter import ttk
# from utils.utility_functions import clear_frame, ui_font, label_function, button_function, frame_function, combobox_function
from utils.utility_functions import *


# 建立期別介面
def create_batch_window(frame_main):
    clear_frame(frame_main)

    # 視窗標題 - 年度計畫編排文字
    frame_title = frame_function(frame_main, 'x')
    label_function(frame_title, '期別新增作業 / 年度計畫編排', 'left', 20, 7)
    
    # 新增，修改，刪除按鈕
    frame_btn = frame_function(frame_main, 'x')
    button_function(frame_btn, '新增', 8, 3, 'left', (20,0), 7)
    button_function(frame_btn, '修改', 8, 3, 'left', 0, 7)
    button_function(frame_btn, '刪除', 8, 3, 'left', 0, 7)
    
    # 輸入欄位表單
    frame_form = frame_function(frame_main, 'x')

    label_function(frame_form, '訓練班別：', 'left', (20,0), 7)
    # 訓練班別代號下拉選單
    training_var = ['1','2','3']
    combobox_function(frame_form, 3, training_var, 'left', 0, 7)

    # 顯示訓練班別的值
    entry_function(frame_form, 15, 'left', 0, 7)

    
    # 年度輸入欄位
    label_function(frame_form, '年度：', 'left', (20,7), 7)
    entry_function(frame_form, 7, 'left', 0, 7)
    
    # 期別
    label_function(frame_form, '期別：', 'left', (20, 0), 7)
    entry_function(frame_form, 7, 'left', 0, 7)
    
    # 梯次
    echelones_var = ['A','B']
    combobox_function(frame_form, 3, echelones_var, 'left', 0, 7)
    
    # 開訓日期
    label_function(frame_form, '開訓日期：', 'left', (20, 0), 7)
    entry_function(frame_form, 10, 'left', 0, 7)
    
    # 結訓日期
    label_function(frame_form, '結訓日期：', 'left', (20, 0), 7)
    entry_function(frame_form, 10, 'left', 0, 7)
    
    # 資料顯示列表
    frame_yearly_plans = frame_function(frame_main, 'both', padx=(20,20), pady=20, expand=True)

    # 年度計畫編排 - Treeview資料顯示列表
    style = ttk.Style()
    style.configure("Custom.Treeview", foreground="#626262", background="#F9F9F9")
    yearly_plans_list = ttk.Treeview(frame_yearly_plans, columns=("training_name", "yearly", "term_num", "training_start", "training_end", "class_term_num"), show="headings", style="Custom.Treeview")
   
    yearly_plans_list.heading("training_name", text="訓練班別名稱")
    yearly_plans_list.heading("yearly", text="年度")
    yearly_plans_list.heading("term_num", text="期別編號")
    yearly_plans_list.heading("training_start", text="開訓日期")
    yearly_plans_list.heading("training_end", text="結訓日期")
    yearly_plans_list.heading("class_term_num", text="上課期別代碼")
    
    yearly_plans_list.column("training_name", width=100, anchor='w')
    yearly_plans_list.column("yearly", width=20, anchor='w')
    yearly_plans_list.column("term_num", width=100, anchor='w')
    yearly_plans_list.column("training_start", width=100, anchor='w')
    yearly_plans_list.column("training_end", width=100, anchor='w')
    yearly_plans_list.column("class_term_num", width=100, anchor='w')
     
    yearly_plans_list.pack(side="left", fill="both", expand=True)    
    
    # 在 treeview 右邊垂直顯示Scrollbar滾動條
    yearly_plans_list_scroll = tk.Scrollbar(frame_yearly_plans, command=yearly_plans_list.yview)
    yearly_plans_list_scroll.pack(side="right", fill="y")
    yearly_plans_list.configure(yscrollcommand=yearly_plans_list_scroll.set)
    
    # 添加随机数据进行测试
    for i in range(100):  # 生成100行数据来测试滚动条
        yearly_plans_list.insert("", "end", values=(f"訓練班別{i}", f"202{i % 10}", f"{i}", f"202{i % 10}-01-01", f"202{i % 10}-12-31", f"代碼{i}"))
    
    