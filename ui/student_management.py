# 學員資料介面
import tkinter as tk
from tkinter import ttk
from utils.utility_functions import *


def create_student_window(frame_main):
    clear_frame(frame_main)
    
    # 視窗標題 frame - 學員資料作業標題文字
    frame_title = frame_function(frame_main, 'x')
    label_function(frame_title, '學員資料作業 / 新增 - 修改 - 刪除 - 查找', 'left', 20, 7)

    # 按鈕 frame - 新增，修改，刪除
    frame_btn = frame_function(frame_main, 'x')
    button_function(frame_btn, '新增', 8, 3, 'left', (20,0), 7)
    button_function(frame_btn, '修改', 8, 3, 'left', 0, 7) # 修改英文 amend
    button_function(frame_btn, '刪除', 8, 3, 'left', 0, 7)
    
    # 輸入欄位表單 frame row1#######################
    frame_form = frame_function(frame_main, 'x')
    label_function(frame_form, '✸ 訓練班別：', 'left', (20,0), 7)
    
    # 訓練班別代號下拉選單
    class_type_code_var = ['1','2','3']
    combobox_function(frame_form, 3, class_type_code_var, 'left', 0, 7)
    
    # 顯示訓練班別的值
    entry_function(frame_form, 15, 'left', 0, 7)
    
    # 考照類別
    label_function(frame_form, '✸ 考照類別：', 'left', (20, 0), 7)
    
    # 考照類別下拉選單
    license_type_var = ['0','1','2','3','4','5','6','7']
    combobox_function(frame_form, 3, license_type_var, 'left', 0, 7)
    
    # label 學員編號
    label_function(frame_form, '✸ 學員編號：', 'left', (20, 0), 7)
    entry_function(frame_form, 5, 'left', 0, 7)
    label_function(frame_form, '-', 'left', 0, 7)
    entry_function(frame_form, 5, 'left', 0, 7)

    # label 梯次
    label_function(frame_form, '✸ 梯次：', 'left', (20, 0), 7)

    # test_batch 梯次下拉選單
    text_batch_var = ['A','B']
    combobox_function(frame_form, 3, text_batch_var, 'left', 0, 7)
    
    # 學員姓名
    label_function(frame_form, '✸ 學員姓名：', 'left', (20, 0), 7)
    entry_function(frame_form, 10, 'left', 0, 7)
    # frame row1 END #########################
    
    # 輸入欄位表單 frame row2#######################
    frame_form_row2 = frame_function(frame_main, 'x')
    
    # 身分證字號
    label_function(frame_form_row2, '✸ 身分證字號：', 'left', (20, 0), 7)
    entry_function(frame_form_row2, 15, 'left', 0, 7)
    
    # 出生日期
    label_function(frame_form_row2, '✸ 出生日期：', 'left', (20, 0), 7)
    entry_function(frame_form_row2, 10, 'left', 0, 7)
    
    # email
    label_function(frame_form_row2, '✸ 信箱：', 'left', (20, 0), 7)
    entry_function(frame_form_row2, 15, 'left', 0, 7)
    
    # 性別
    label_function(frame_form_row2, '✸ 性別：', 'left', (20, 0), 7)
    #性別下拉選單
    gender_var = ['男','女','無性別']
    combobox_function(frame_form_row2, 3, gender_var, 'left', 0, 7)
    
    # 指導教練
    label_function(frame_form_row2, '✸ 指導教練：', 'left', (20, 0), 7)
    # 指導教練下拉選單
    teacher_var = ['AAA','BBB','CCC']
    combobox_function(frame_form_row2, 9, teacher_var, 'left', 0, 7)
    # frame row2 END #########################
    
    # 輸入欄位表單 row3 #########################
    frame_form_row3 = frame_function(frame_main, 'x')
    
    # 戶籍地址
    label_function(frame_form_row3, '✸ 戶籍地址：', 'left', (20, 0), 7)
    
    # registered_address 戶籍地址縣市下拉選單
    registered_address_var = ['台北市','新北市','板橋區']
    combobox_function(frame_form_row3, 5, registered_address_var, 'left', 0, 7)
    entry_function(frame_form_row3, 38, 'left', 0, 7)
    
    # 通訊地址
    label_function(frame_form_row3, '✸ 通訊地址：', 'left', (20, 0), 7)

    # 通訊地址縣市下拉選單
    address_var = ['台北市','新北市','板橋區']
    combobox_function(frame_form_row3, 5, address_var, 'left', 0, 7)

    # 通訊地址欄位
    entry_function(frame_form_row3, 37, 'left', 0, 7)
    # frame row3 END #########################

    # 輸入欄位表單 row4 #########################
    frame_form_row4 = frame_function(frame_main, 'x')
    
    # 室內電話
    label_function(frame_form_row4, '✸ 室內電話：', 'left', (20, 0), 7)
    entry_function(frame_form_row4, 10, 'left', 0, 7)
    
    # 行動電話
    label_function(frame_form_row4, '✸ 行動電話：', 'left', (20, 0), 7)
    entry_function(frame_form_row4, 10, 'left', 0, 7)
    
    # 學歷文憑
    label_function(frame_form_row4, '✸ 學歷文憑：', 'left', (20, 0), 7)
    #學歷下拉選單
    diploma_var = ['大學','碩士','博士']
    combobox_function(frame_form_row4, 5, diploma_var, 'left', 0, 7)
    
    # 欠資料
    label_function(frame_form_row4, '✸ 欠資料：', 'left', (20, 0), 7)
    entry_function(frame_form_row4, 47, 'left', 0, 7)
    
    # 水平分隔線 Frame
    hr_function(frame_main, 2, 1, 'x', (20,20), 7, relief='sunken')
    
    # frame 搜尋說明
    frame_search_explain = frame_function(frame_main, 'x')
    label_function(frame_search_explain, '📝 學員查詢專區，請依照以下三個欄位選擇一樣查詢即可。', 'left', (20, 0), 7)

    # frame 搜尋區域
    frame_search = frame_function(frame_main, 'x')
    
    # 使用學員姓名，手機，學員編號，身分證號來查詢學員
    label_function(frame_search, '🔎 學員姓名查詢：', 'left', (20, 0), 7)
    entry_function(frame_search, 15, 'left', 0, 7)
    label_function(frame_search, '🔎 學員手機查詢：', 'left', (20, 0), 7)    
    entry_function(frame_search, 15, 'left', 0, 7)
    label_function(frame_search, '🔎 學員身分證號查詢：', 'left', (20, 0), 7)
    entry_function(frame_search, 15, 'left', 0, 7)

    button_function(frame_search, '🔎 查詢', 8, 2, 'left', 10, 7)
    
    # hr_function(frame_main, 2, 1, 'x', (20, 20), 7, relief='sunken')
    
    # 學員資料查詢 Treeview 資料顯示列表
    frame_students_data_list = frame_function(frame_main, 'both', padx=(20,20), pady=20, expand=True)
    
    style = ttk.Style()
    style.configure("Custom.Treeview", foreground="#626262", background="#F9F9F9")
    
    students_data_list = ttk.Treeview(frame_students_data_list, columns=(
        "id","name","id_number","date_birth","gender","local_phone","mobile_phone","email","registered_address","mailing_address",
    ),show="headings", style="Custom.Treeview")
    
    students_data_list.heading("id", text="學員編號")
    students_data_list.heading("name", text="學員姓名")
    students_data_list.heading("id_number", text="身分證號")
    students_data_list.heading("date_birth", text="出生日期")
    students_data_list.heading("gender", text="性別")
    students_data_list.heading("local_phone", text="室內電話")
    students_data_list.heading("mobile_phone", text="行動電話")
    students_data_list.heading("email", text="信箱")
    students_data_list.heading("registered_address", text="戶籍地址")
    students_data_list.heading("mailing_address", text="通訊地址")
    
    students_data_list.column("id", width=100, anchor='w')
    students_data_list.column("name", width=100, anchor='w')
    students_data_list.column("id_number", width=100, anchor='w')
    students_data_list.column("date_birth", width=100, anchor='w')
    students_data_list.column("gender", width=100, anchor='w')
    students_data_list.column("local_phone", width=100, anchor='w')
    students_data_list.column("mobile_phone", width=100, anchor='w')
    students_data_list.column("email", width=100, anchor='w')
    students_data_list.column("registered_address", width=100, anchor='w')
    students_data_list.column("mailing_address", width=100, anchor='w')
    
    students_data_list.pack(side="left", fill="both", expand=True)
    
    # 在 treeview 右邊垂直顯示Scrollbar滾動條
    students_data_list_scroll = tk.Scrollbar(frame_students_data_list, command=students_data_list.yview)
    students_data_list_scroll.pack(side="right", fill="y")
    students_data_list.configure(yscrollcommand=students_data_list_scroll.set)
    
    # 添加10條随机数据进行测试
    for i in range(100):  # 生成100行数据来测试滚动条
        students_data_list.insert("", "end", values=(f"202{i % 10}", f"張{i}", f"A{i}", f"202{i % 10}-01-01", f"男", f"02{i % 10}", f"09{i % 10}", f"test{i}@gmail.com", f"台北市", f"台北市"))