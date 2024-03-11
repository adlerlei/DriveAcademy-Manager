# 學員資料介面 StudentAdditionInterface
import tkinter as tk
from tkinter import ttk
from utils.utility_functions import *


def StudentAdditionInterface(frame_main):
    clear_frame(frame_main)
    
    # 學員資料新增 標題 frame
    add_students_data = label_frame_fun(frame_main, ' ✏️ 新增 - 學員資料', fg='#4ea1d3')
    add_students_data.pack(fill='x', padx=(20,20), pady=7)
    
    # add_students_data_row1 #######################
    add_students_data_row1 = frame_fun(add_students_data)
    add_students_data_row1.pack(fill='x', pady=(0,10))
    
    # 訓練班別
    required(add_students_data_row1)
    label_fun(add_students_data_row1, '訓練班別：').pack(side='left')
    class_type_code_var = ['1','2','3']
    combobox_fun(add_students_data_row1, width=3, values=class_type_code_var).pack(side='left',pady=7)
    entry_fun(add_students_data_row1, width=15).pack(side='left')
    
    # 考照類別
    required(add_students_data_row1)
    label_fun(add_students_data_row1, '考照類別：').pack(side='left')
    license_type_var = ['0','1','2','3','4','5','6','7']
    combobox_fun(add_students_data_row1, values=license_type_var, width=3).pack(side='left')
    entry_fun(add_students_data_row1, width=15).pack(side='left')
    
    # 性別
    required(add_students_data_row1)
    label_fun(add_students_data_row1, '性別：').pack(side='left')
    gender_var = ['男','女','無性別']
    combobox_fun(add_students_data_row1, values=gender_var, width=3).pack(side='left')

    # 梯次
    required(add_students_data_row1)
    label_fun(add_students_data_row1, '梯次：').pack(side='left')
    text_batch_var = ['A','B']
    combobox_fun(add_students_data_row1, values=text_batch_var, width=3).pack(side='left')
    
    # add_students_data_row2 #######################
    add_students_data_row2 = frame_fun(add_students_data)
    add_students_data_row2.pack(fill='x',  pady=(0,10))
    
    # 學員姓名
    required(add_students_data_row2)
    label_fun(add_students_data_row2, '學員姓名：').pack(side='left')
    entry_fun(add_students_data_row2, width=10).pack(side='left')
    
    # label 學員編號
    required(add_students_data_row2)
    label_fun(add_students_data_row2, '學員編號：').pack(side='left')
    entry_fun(add_students_data_row2, width=5).pack(side='left')
    label_fun(add_students_data_row2, '-').pack(side='left')
    entry_fun(add_students_data_row2, width=5).pack(side='left')

    # 身分證字號
    required(add_students_data_row2)
    label_fun(add_students_data_row2, '身分證字號：').pack(side='left')
    entry_fun(add_students_data_row2, width=10).pack(side='left')
    
    # 出生日期
    required(add_students_data_row2)
    label_fun(add_students_data_row2, '出生日期：').pack(side='left')
    entry_fun(add_students_data_row2, width=10).pack(side='left')
    
    # add_students_data_row3 #######################
    add_students_data_row3 = frame_fun(add_students_data)
    add_students_data_row3.pack(fill='x',  pady=(0,10))
    
    # 戶籍地址
    required(add_students_data_row3)
    label_fun(add_students_data_row3, '戶籍地址：').pack(side='left')
    registered_address_var = ['台北市','新北市','板橋區']
    combobox_fun(add_students_data_row3, values=registered_address_var, width=5).pack(side='left')
    entry_fun(add_students_data_row3, width=29).pack(side='left')
    
    # 信箱
    tk.Label(add_students_data_row3, text='㊒', fg='#eb9f9f').pack(side='left', padx=(16,0))
    label_fun(add_students_data_row3, '信箱：').pack(side='left')
    entry_fun(add_students_data_row3, width=15).pack(side='left')
    
    # 行動電話
    required(add_students_data_row3)
    label_fun(add_students_data_row3, '行動電話：').pack(side='left')
    entry_fun(add_students_data_row3, width=10).pack(side='left')

    # add_students_data_row4 #######################
    add_students_data_row4 = frame_fun(add_students_data)
    add_students_data_row4.pack(fill='x',  pady=(0,10))
    
    # 通訊地址
    label_fun(add_students_data_row4, '通訊地址：').pack(side='left', padx=(20,0))
    address_var = ['台北市','新北市','板橋區']
    combobox_fun(add_students_data_row4, values=address_var, width=5).pack(side='left')
    entry_fun(add_students_data_row4, width=37).pack(side='left')
    
    # 室內電話
    label_fun(add_students_data_row4, '室內電話：').pack(side='left', padx=(20,0), pady=7)
    entry_fun(add_students_data_row4, width=10).pack(side='left', pady=7)
    
    # 學歷文憑
    label_fun(add_students_data_row4, '學歷文憑：').pack(side='left', padx=(20,0))
    diploma_var = ['大學','碩士','博士']
    combobox_fun(add_students_data_row4, values=diploma_var, width=5).pack(side='left', pady=7)
    
    # 指導教練
    label_fun(add_students_data_row4, '指導教練：').pack(side='left', padx=(20,0))
    teacher_var = ['AAA','BBB','CCC']
    combobox_fun(add_students_data_row4, values=teacher_var, width=9).pack(side='left')
    
    # 欠資料
    label_fun(add_students_data_row4, '欠資料：').pack(side='left', padx=(20,0), pady=7)
    entry_fun(add_students_data_row4, width=29).pack(side='left', pady=7)
    
    add_students_data_row5 = frame_fun(add_students_data)
    add_students_data_row5.pack(fill='x', padx=(20, 20), pady=(0,10))
    
    # 水平線
    # hr_fun(add_students_data_row5, height=2, bd=1, relief='sunken').pack(fill='x',pady=(0,10))
    
    # 新增學員資料按鈕
    button_fun(add_students_data_row5, '✓ 新增學員資料', fg='#4ea1d3', width=10, height=3).pack(side='left', pady=(20,20)) 
    
    # 查詢 / 修改 / 刪除 - 學員資料 frame 標題
    search_students_data = label_frame_fun(frame_main, ' 🔎 查詢 - 學員資料', fg='#a79c8e')
    search_students_data.pack(fill='x', padx=(20, 20), pady=(50,0))
    
    # search_students_data_row1 #######################
    search_students_data_row1 = frame_fun(search_students_data)
    search_students_data_row1.pack(fill='x', pady=(0,10))
    
    # 使用學員姓名，手機，學員編號，身分證號來查詢學員
    label_fun(search_students_data_row1, '學員姓名查詢：').pack(side='left', padx=(20,0))
    entry_fun(search_students_data_row1, width=15).pack(side='left')
    label_fun(search_students_data_row1, '學員手機查詢：').pack(side='left', padx=(20,0))    
    entry_fun(search_students_data_row1, width=15).pack(side='left')
    label_fun(search_students_data_row1, '學員編號查詢：').pack(side='left', padx=(20,0))
    entry_fun(search_students_data_row1, width=15).pack(side='left')

    search_students_data_row2 = frame_fun(search_students_data)
    search_students_data_row2.pack(fill='x', pady=(0,10))
    
    # hr_fun(search_students_data_row2, height=2, bd=1, relief='sunken').pack(fill='x', padx=(20, 20), pady=(0,10))
    
    # 查詢按鈕
    button_fun(search_students_data_row2, '🔎 查詢', width=10, height=3, fg='#a79c8e').pack(side='left', padx=(20,0), pady=(20,20))
    
    # search_delete_students_data #######################
    search_delete_students_data = label_frame_fun(frame_main, ' 🗑️ 刪除 / 修改 - 學員資料', fg='#cb7575')
    search_delete_students_data.pack(fill='x', padx=(20, 20), pady=(50, 10))
    # search_delete_students_data_row1
    search_delete_students_data_row1 = frame_fun(search_delete_students_data)
    search_delete_students_data_row1.pack(fill='x', pady=(0, 10))
    
    # 顯示學員資料 - 查詢 / 修改 / 刪除 - 區域
    # 訓練班別
    label_fun(search_delete_students_data_row1, '訓練班別：').pack(side='left', padx=(20,0))
    class_type_code_var = ['1','2','3']
    combobox_fun(search_delete_students_data_row1, width=3, values=class_type_code_var).pack(side='left',pady=7)
    entry_fun(search_delete_students_data_row1, width=15).pack(side='left')
    
    # 考照類別
    label_fun(search_delete_students_data_row1, '考照類別：').pack(side='left', padx=(20,0))
    license_type_var = ['0','1','2','3','4','5','6','7']
    combobox_fun(search_delete_students_data_row1, values=license_type_var, width=3).pack(side='left')
    entry_fun(search_delete_students_data_row1, width=15).pack(side='left')
    
    # 性別
    label_fun(search_delete_students_data_row1, '性別：').pack(side='left', padx=(20,0))
    gender_var = ['男','女','無性別']
    combobox_fun(search_delete_students_data_row1, values=gender_var, width=3).pack(side='left')

    # 梯次
    label_fun(search_delete_students_data_row1, '梯次：').pack(side='left', padx=(20,0))
    text_batch_var = ['A','B']
    combobox_fun(search_delete_students_data_row1, values=text_batch_var, width=3).pack(side='left')
    
    # display_students_data_row3 #######################
    search_delete_students_data_row2 = frame_fun(search_delete_students_data)
    search_delete_students_data_row2.pack(fill='x',  pady=(0,10))
    
    # 學員姓名
    label_fun(search_delete_students_data_row2, '學員姓名：').pack(side='left', padx=(20,0))
    entry_fun(search_delete_students_data_row2, width=10).pack(side='left')
    
    # label 學員編號
    label_fun(search_delete_students_data_row2, '學員編號：').pack(side='left', padx=(20,0))
    entry_fun(search_delete_students_data_row2, width=5).pack(side='left')
    label_fun(search_delete_students_data_row2, '-').pack(side='left')
    entry_fun(search_delete_students_data_row2, width=5).pack(side='left')

    # 身分證字號
    label_fun(search_delete_students_data_row2, '身分證字號：').pack(side='left', padx=(20,0))
    entry_fun(search_delete_students_data_row2, width=10).pack(side='left')
    
    # 出生日期
    label_fun(search_delete_students_data_row2, '出生日期：').pack(side='left', padx=(20,0))
    entry_fun(search_delete_students_data_row2, width=10).pack(side='left')
    
    # display_students_data_row4 #######################
    search_delete_students_data_row3 = frame_fun(search_delete_students_data)
    search_delete_students_data_row3.pack(fill='x',  pady=(0,10))
    
    # 戶籍地址
    label_fun(search_delete_students_data_row3, '戶籍地址：').pack(side='left', padx=(20,0))
    registered_address_var = ['台北市','新北市','板橋區']
    combobox_fun(search_delete_students_data_row3, values=registered_address_var, width=5).pack(side='left')
    entry_fun(search_delete_students_data_row3, width=29).pack(side='left')
    
    # 信箱
    label_fun(search_delete_students_data_row3, '信箱：').pack(side='left', padx=(20,0))
    entry_fun(search_delete_students_data_row3, width=15).pack(side='left')
    
    # 行動電話
    label_fun(search_delete_students_data_row3, '行動電話：').pack(side='left', padx=(20,0))
    entry_fun(search_delete_students_data_row3, width=10).pack(side='left')
    
    search_delete_students_data_row4 = frame_fun(search_delete_students_data)
    search_delete_students_data_row4.pack(fill='x', pady=(0, 10))
    
    # 通訊地址
    label_fun(search_delete_students_data_row4, '通訊地址：').pack(side='left', padx=(20,0))
    address_var = ['台北市','新北市','板橋區']
    combobox_fun(search_delete_students_data_row4, values=address_var, width=5).pack(side='left')
    entry_fun(search_delete_students_data_row4, width=37).pack(side='left')
    
    # 室內電話
    label_fun(search_delete_students_data_row4, '室內電話：').pack(side='left', padx=(20,0), pady=7)
    entry_fun(search_delete_students_data_row4, width=10).pack(side='left', pady=7)
    
    # 學歷文憑
    label_fun(search_delete_students_data_row4, '學歷文憑：').pack(side='left', padx=(20,0))
    diploma_var = ['大學','碩士','博士']
    combobox_fun(search_delete_students_data_row4, values=diploma_var, width=5).pack(side='left', pady=7)
    
    # 指導教練
    label_fun(search_delete_students_data_row4, '指導教練：').pack(side='left', padx=(20,0))
    teacher_var = ['AAA','BBB','CCC']
    combobox_fun(search_delete_students_data_row4, values=teacher_var, width=9).pack(side='left')
    
    # 欠資料
    label_fun(search_delete_students_data_row4, '欠資料：').pack(side='left', padx=(20,0), pady=7)
    entry_fun(search_delete_students_data_row4, width=29).pack(side='left', pady=7)
    
    # search_delete_students_data_row5 #######################
    search_delete_students_data_row5 = frame_fun(search_delete_students_data)
    search_delete_students_data_row5.pack(fill='x',  pady=(0,10))
    
    # 水平線
    # hr_fun(search_delete_students_data_row5, height=2, bd=1, relief='sunken').pack(fill='x', padx=(20, 20), pady=(0, 10))
    
    # 按鈕 frame - 新增，修改，刪除
    button_fun(search_delete_students_data_row5, ' 📝 修改', width=8, height=3, fg='#cb7575').pack(side='left', padx=(20,0), pady=(20,20)) # 修改英文 amend
    button_fun(search_delete_students_data_row5, ' ❌ 刪除', width=8, height=3, fg='#cb7575').pack(side='left')

    


    
    # display_students_data_row6 = frame_fun(add_students_data)
    # display_students_data_row6.pack(fill='x', padx=(20, 20), pady=(0,10))
    #################################################
    # 學員資料查詢 Treeview 資料顯示列表
    # frame_data_list = frame_fun(frame_main)
    # frame_data_list.pack(fill='both', expand=True, padx=20, pady=10)
    
    # style = ttk.Style()
    # style.configure("Custom.Treeview", foreground="#626262", background="#F9F9F9")
    
    # students_data_list = ttk.Treeview(frame_data_list, columns=(
    #     "id","name","id_number","date_birth","gender","local_phone","mobile_phone","email","registered_address","mailing_address",
    # ),show="headings", style="Custom.Treeview")
    
    # students_data_list.heading("id", text="學員編號")
    # students_data_list.heading("name", text="學員姓名")
    # students_data_list.heading("id_number", text="身分證號")
    # students_data_list.heading("date_birth", text="出生日期")
    # students_data_list.heading("gender", text="性別")
    # students_data_list.heading("local_phone", text="室內電話")
    # students_data_list.heading("mobile_phone", text="行動電話")
    # students_data_list.heading("email", text="信箱")
    # students_data_list.heading("registered_address", text="戶籍地址")
    # students_data_list.heading("mailing_address", text="通訊地址")
    
    # students_data_list.column("id", width=100, anchor='w')
    # students_data_list.column("name", width=100, anchor='w')
    # students_data_list.column("id_number", width=100, anchor='w')
    # students_data_list.column("date_birth", width=100, anchor='w')
    # students_data_list.column("gender", width=100, anchor='w')
    # students_data_list.column("local_phone", width=100, anchor='w')
    # students_data_list.column("mobile_phone", width=100, anchor='w')
    # students_data_list.column("email", width=100, anchor='w')
    # students_data_list.column("registered_address", width=100, anchor='w')
    # students_data_list.column("mailing_address", width=100, anchor='w')
    
    # students_data_list.pack(side="left", fill="both", expand=True)
    
    # # 在 treeview 右邊垂直顯示Scrollbar滾動條
    # students_data_list_scroll = tk.Scrollbar(frame_data_list, command=students_data_list.yview)
    # students_data_list_scroll.pack(side="right", fill="y")
    # students_data_list.configure(yscrollcommand=students_data_list_scroll.set)
    
    # # 添加10條随机数据进行测试
    # for i in range(100):  # 生成100行数据来测试滚动条
    #     students_data_list.insert("", "end", values=(f"202{i % 10}", f"張{i}", f"A{i}", f"202{i % 10}-01-01", f"男", f"02{i % 10}", f"09{i % 10}", f"test{i}@gmail.com", f"台北市", f"台北市"))