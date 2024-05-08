# 學員新增 - 修改 - 刪除 - 查詢
from utils.widget import *
from utils.config import *
from models.student import get_instructors, on_instructor_selected
from tkinter import messagebox
import customtkinter as ctk


def student_all(content):
    # 驗證控件是否存在
    global checkbox_added
    clear_frame(content)
    checkbox_added = False 
    
    student_all = frame(content)
    student_all.columnconfigure(0, weight=1)
    student_all.columnconfigure(1, weight=1)
    student_all.columnconfigure(2, weight=1)
    student_all.columnconfigure(3, weight=1)
    student_all.place(relwidth=1, relheight=1)


    # 訓練班別下拉選單training_type_code監聽變化
    def training_type_combobox(event): 
        # 獲取第一個下拉選單的當前選擇
        selected_training_code = training_type_code.get()
        # 根據選擇更新第二個下拉選單的值
        match selected_training_code:
            case '1':
                training_type_name.set('普通小型車班')
            case '2':
                training_type_name.set('大貨車班')
            case '3':
                training_type_name.set('大客車班')
            case '4':
                training_type_name.set('聯結車班')
            case '5':
                training_type_name.set('職業小型車班')
            case '6':
                training_type_name.set('普通重機車班')
            case '7':
                training_type_name.set('大型重機車班')
            case '8':
                training_type_name.set('小型車逕升大客車班')

    # 訓練班別下拉選單training_type_code監聽變化
    def license_type_combobox(event): 
        # 獲取第一個下拉選單的當前選擇
        selected_license_code = license_type_code.get()
        # 根據選擇更新第二個下拉選單的值
        match selected_license_code:
            case '0':
                license_type_name.set('自用小客車')
            case '1':
                license_type_name.set('職業小客車')
            case '2':
                license_type_name.set('自用大貨車')
            case '3':
                license_type_name.set('職業大貨車')
            case '4':
                license_type_name.set('自用大客車')
            case '5':
                license_type_name.set('職業大客車')
            case '6':
                license_type_name.set('自用聯結車')
            case '7':
                license_type_name.set('職業聯結車')
    
    
    # 訓練班別
    label(student_all, text='訓練班別').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    training_type_code = combobox(student_all,  values=['1','2','3','4','5','6','7','8'], command=training_type_combobox)
    training_type_code.grid(row=1, column=0, sticky='wen', padx=10)
    training_type_name = combobox(student_all, values=['普通小型車班','大貨車班','大客車班','聯結車班','職業小型車班','普通重機車班','大型重機車班','小型車逕升大客車班'])
    training_type_name.grid(row=1, column=1, sticky='wen', padx=10)

    # 綁定函數到第一個下拉選單的選擇變化事件
    training_type_code.bind("<<ComboboxSelected>>", training_type_combobox)

    # 考照類別
    label(student_all, text='考照類別').grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    license_type_code = combobox(student_all,  values=['0','1','2','3','4','5','6','7'], command=license_type_combobox)
    license_type_code.grid(row=3, column=0, sticky='wen', padx=10)
    license_type_name = combobox(student_all, values=['自用小客車','職業小客車','自用大貨車','職業大貨車','自用大客車','職業大客車','自用聯結車','職業聯結車'])
    license_type_name.grid(row=3, column=1, sticky='wen', padx=(0,10))

    # 綁定函數到第二個下拉選單的選擇變化事件
    license_type_code.bind("<<ComboboxSelected>>", license_type_combobox)

    #學員編號
    label(student_all, text='學員編號').grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    number = entry(student_all)
    number.grid(row=5, column=0, sticky='wen', padx=10)
    
    
    # 梯次（抓取資料庫呈現）
    label(student_all, text='梯次').grid(row=4, column=1, sticky='ws', pady=(20,0))
    combobox(student_all, values=['A','B']).grid(row=5, column=1, sticky='wen', padx=(0,10))

    # 學員姓名
    label(student_all, text='學員姓名').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(20,0 ))
    name = entry(student_all)
    name.grid(row=7, column=0, sticky='wen', padx=10)

    # 身分證號碼
    label(student_all, text='身分證號碼').grid(row=6, column=1, sticky='ws', pady=(20,0))
    national_id_no = entry(student_all)
    national_id_no.grid(row=7, column=1, sticky='wen', padx=(0,10))

    # 出生日期
    label(student_all, text='出生日期').grid(row=8, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    birth_date = entry(student_all)
    birth_date.grid(row=9, column=0, sticky='wen', padx=10)

    # 行動電話
    label(student_all, text='手機').grid(row=8, column=1, sticky='ws', pady=(20,0))
    entry(student_all).grid(row=9, column=1, sticky='wen',padx=(0,10))
    
    # 戶籍地址 ######
    label(student_all, text='戶籍地址').grid(row=10, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    # 郵遞區號
    combobox(student_all, values=['231', '116']).grid(row=11, column=0, sticky='wen', padx=10)
    # 區域別
    combobox(student_all, values=['台北市中山區', '新北市新店區']).grid(row=11, column=1, sticky='wen', padx=(0,10))
    # 地址
    r_address = entry(student_all)
    r_address.grid(row=12, column=0, columnspan=2, sticky='wen', padx=10)



    # 家用電話
    label(student_all, text='市話').grid(row=0, column=2, sticky='ws', padx=(10,0))
    entry(student_all).grid(row=1, column=2, columnspan=2, sticky='wen', padx=10)

    # 性別
    label(student_all, text='性別').grid(row=2, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    combobox(student_all, values=['男', '女']).grid(row=3, column=2, sticky='wen', padx=10)

    # 學歷 
    label(student_all, text='學歷').grid(row=2, column=3, sticky='ws', pady=(20,0))
    combobox(student_all, values=['國中', '高中', '大學']).grid(row=3, column=3, sticky='wen', padx=(0,10))

    instructor_numbers, instructor_names = get_instructors()
    #指導教練
    label(student_all, text='指導教練').grid(row=4, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    instructor_number = combobox(student_all, values=instructor_numbers)
    instructor_number.grid(row=5, column=2, sticky='wen', padx=10)
    instructor_name = entry(student_all)
    instructor_name.grid(row=5, column=3, sticky='wen', padx=(0,10))
    instructor_number.bind("<<ComboboxSelected>>", lambda event: on_instructor_selected(instructor_number, instructor_names, instructor_name, event))

    # 信箱
    label(student_all, text='信箱').grid(row=6, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    email = entry(student_all)
    email.grid(row=7, column=2, columnspan=2, sticky='wen', padx=10)

    # 備註
    label(student_all, text='備註').grid(row=8, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    remarks = entry(student_all)
    remarks.grid(row=9, column=2, columnspan=2, sticky='wen', padx=10)

    # 通訊地址 ####
    label(student_all, text='通訊地址').grid(row=10, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    # 郵遞區號
    combobox(student_all,  values=['231', '116']).grid(row=11, column=2, sticky='wen', padx=10)
    # 縣市區域
    combobox(student_all, values=['台北市中山區', '新北市新店區']).grid(row=11, column=3, sticky='wen', padx=(0,10))
    # 地址
    m_address = entry(student_all)
    m_address.grid(row=12, column=2, columnspan=2, sticky='wen', padx=10)
    

    # 點擊按鈕觸發事件，並顯示隱藏的控件顯示學員資料
    def click_btn():
        global checkbox_added
        if not checkbox_added:
        # 讀取資料（暫時留空）

            
            # 顯示是否退訓
            label(student_all, text='該學員是否退訓').grid(row=14, column=0, sticky='ws', padx=(10,0))
            display_entry_value(student_all, width=5).grid(row=15, column=0, sticky='wen', padx=10)
            
            # 顯示名冊號碼 opening_closing_register 關聯資料庫欄位
            label(student_all, text='名冊號碼').grid(row=14, column=1, sticky='ws')
            display_entry_value(student_all, width=7).grid(row=15, column=1, sticky='wen', padx=(0,10))

            # 顯示學照日期
            label(student_all, text='學照日期').grid(row=14, column=2, sticky='ws', padx=(10,0))
            display_entry_value(student_all, width=7).grid(row=15, column=2, sticky='wen', padx=10)

            # 顯示學照號碼
            label(student_all, text='學照號碼').grid(row=14, column=3, sticky='ws')
            display_entry_value(student_all, width=7).grid(row=15, column=3, sticky='wen', padx=(0,10))

            # 顯示路試日期
            label(student_all, text='路試日期').grid(row=16, column=0, sticky='ws', padx=(10,0))
            display_entry_value(student_all, width=7).grid(row=17, column=0, sticky='wen', padx=10)
            # 顯示建檔日期
            label(student_all, text='建檔日期').grid(row=16, column=1, sticky='ws')
            display_entry_value(student_all, width=7).grid(row=17, column=1, sticky='wen')

            checkbox_added = True


    # 新增，修改，刪除，查詢 -- 按鈕
    btn(student_all, text='新增', command=lambda: None).grid(row=13, column=0, sticky='wen', padx=10, pady=20)
    btn(student_all, text='查詢', command=click_btn).grid(row=13, column=1, sticky='wen', padx=(0,10), pady=20)
    btn(student_all, text='修改', command=lambda: None).grid(row=13, column=2, sticky='wen', padx=10, pady=20)
    btn(student_all, text='刪除', command=lambda: None).grid(row=13, column=3, sticky='wen', padx=(0,10), pady=20)