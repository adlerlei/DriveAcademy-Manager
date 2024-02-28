# 期別管理界面
import tkinter as tk
from tkinter import font
from utils.utility_functions import clear_frame


# 建立期別介面
def create_batch_window(frame_main):
    clear_frame(frame_main)
    
    myfont = font.Font(family='burnfont-1.1', size=40)

    # 視窗標題 - 年度計畫編排文字
    frame_title = tk.Frame(frame_main)
    frame_title.pack( fill="x")
    frame_title_label = tk.Label(frame_title, text="年度計畫編排", font=myfont)
    frame_title_label.pack(side="left", padx=20)

    
    # row1 - 新增，修改，刪除按鈕
    frame_btn = tk.Frame(frame_main)
    frame_btn.pack( fill="x")
    
    add_btn = tk.Button(frame_btn, text="新增", width=8, height=3)
    add_btn.pack(side="left", padx=(20, 0), pady=7)
    
    fix_btn = tk.Button(frame_btn, text="修改", width=8, height=3)
    fix_btn.pack(side="left", pady=7)
    
    delete_btn = tk.Button(frame_btn, text="刪除", width=8, height=3)
    delete_btn.pack(side="left", pady=7)
    
    # row2 - 輸入欄位表單
    frame_form = tk.Frame(frame_main)
    frame_form.pack( fill="x")
    
    tk.Label(frame_form, text="訓練班別：").pack(side="left", padx=(20, 0), pady=7)

    # 建立一個 tk 變數，用來儲存下拉選單的選取值
    training_type_op = tk.StringVar()
    # 建立一個下拉選單，並指定選取值變數為 select_var
    training_type_op = tk.OptionMenu(frame_form, training_type_op, "1", "2", "3")
    training_type_op.pack(side="left", pady=7)
    # 顯示下拉選單的預設選取值
    training_type_op.set("1")
    
    # 顯示訓練班別的值
    training_type = tk.Entry(frame_form)
    training_type.pack(side="left", pady=7)
    
    # 年度輸入欄位
    tk.Label(frame_form, text="年度：").pack(side="left", padx=(20, 0), pady=7)
    year = tk.Entry(frame_form)
    year.pack(side="left", pady=7)
    
    # 期別
    tk.Label(frame_form, text="期別：").pack(side="left", padx=(20, 0), pady=7)
    term = tk.Entry(frame_form)
    term.pack(side="left", pady=7)
    
    # 梯次
    tk.Label(frame_form, text="梯次：").pack(side="left", padx=(20, 0), pady=7)
    
    
    
    