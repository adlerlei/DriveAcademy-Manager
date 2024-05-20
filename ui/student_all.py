# 學員新增 - 修改 - 刪除 - 查詢
from utils.widget import *
from utils.config import *
from models.student import get_instructor_data, address_data
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
    
    
    # 訓練班別 ######
    training_type_codes = ['1', '2', '3', '4', '5', '6', '7', '8']
    training_type_names = ['普通小型車班', '大貨車班', '大客車班', '聯結車班', '職業小型車班', '普通重機車班', '大型重機車班', '小型車逕升大客車班']
    training_type_dict = dict(zip(training_type_codes, training_type_names))
    label(student_all, text='訓練班別').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    training_type_code = combobox(student_all, values=training_type_codes, command=lambda x: on_training_type_code_changed(x, training_type_name, training_type_dict))
    training_type_code.grid(row=1, column=0, sticky='wen', padx=10)
    training_type_name = combobox(student_all, values=training_type_names)
    training_type_name.grid(row=1, column=1, sticky='wen', padx=10)

    # 監聽訓練班別第一個下拉選單的變化
    def on_training_type_code_changed(selected_code, training_type_name, training_type_dict):
        # 根據訓練班別代碼獲取訓練班別名稱
        selected_name = training_type_dict.get(selected_code, "")
        # 設置第二個下拉選單的值
        training_type_name.set(selected_name)
    #################

    # 考照類別 ######
    license_type_codes = ['0', '1', '2', '3', '4', '5', '6', '7']
    license_type_names = ['自用小客車', '職業小客車', '自用大貨車', '職業大貨車', '自用大客車', '職業大客車', '自用聯結車', '職業聯結車']
    license_type_dict = dict(zip(license_type_codes, license_type_names))
    label(student_all, text='考照類別').grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    license_type_code = combobox(student_all,  values=['0','1','2','3','4','5','6','7'], command=lambda x: on_license_type_code_changed(x, license_type_name, license_type_dict))
    license_type_code.grid(row=3, column=0, sticky='wen', padx=10)
    license_type_name = combobox(student_all, values=['自用小客車','職業小客車','自用大貨車','職業大貨車','自用大客車','職業大客車','自用聯結車','職業聯結車'])
    license_type_name.grid(row=3, column=1, sticky='wen', padx=(0,10))

    # 監聽考照類別第一個下拉選單的變化
    def on_license_type_code_changed(selected_code, license_type_name, license_type_dict):
        # 根據訓練班別代碼獲取訓練班別名稱
        selected_name = license_type_dict.get(selected_code, "")
        # 設置第二個下拉選單的值
        license_type_name.set(selected_name)
    #################


    # 學員編號
    label(student_all, text='學員編號').grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    student_number = entry(student_all)
    student_number.grid(row=5, column=0, sticky='wen', padx=10)
    
    
    # 梯次
    label(student_all, text='梯次').grid(row=4, column=1, sticky='ws', pady=(20,0))
    batch = combobox(student_all, values = ['A', 'B'])
    batch.grid(row=5, column=1, sticky='wen', padx=(0,10))
    batch.set('')

    # 學員姓名
    label(student_all, text='學員姓名').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(20,0 ))
    student_name = entry(student_all)
    student_name.grid(row=7, column=0, sticky='wen', padx=10)

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
    mobile_phone = entry(student_all)
    mobile_phone.grid(row=9, column=1, sticky='wen',padx=(0,10))
    

    # 抓取郵遞區號資料 #########
    r_address_zip_code_lists, r_address_city_lists, r_address_dict = address_data()
    # 戶籍地址 ######
    label(student_all, text='戶籍地址').grid(row=10, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    # 郵遞區號
    r_address_zip_code = combobox(student_all, values = r_address_zip_code_lists, command=lambda x: auto_event_r_address(x, r_address_city, r_address_dict))
    r_address_zip_code.grid(row=11, column=0, sticky='wen', padx=10)
    # 縣市區域
    r_address_city = combobox(student_all, values = r_address_city_lists)
    r_address_city.grid(row=11, column=1, sticky='wen', padx=(0,10))
    # 地址
    r_address = entry(student_all)
    r_address.grid(row=12, column=0, columnspan=2, sticky='wen', padx=10)
    r_address_zip_code.set('')
    r_address_city.set('')

    # 監聽第一個下拉選單的變化
    def auto_event_r_address(zip_code_list, r_address_city, address_dict):
        # 根據郵遞區號獲取城市
        selected_zip_code = address_dict.get(zip_code_list, "")
        # 設置第二個下拉選單的值
        r_address_city.set(selected_zip_code)
    #################


    # 家用電話
    label(student_all, text='市話').grid(row=0, column=2, sticky='ws', padx=(10,0))
    home_phone = entry(student_all)
    home_phone.grid(row=1, column=2, columnspan=2, sticky='wen', padx=10)

    # 性別
    label(student_all, text='性別').grid(row=2, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    gender = combobox(student_all, values=['男', '女'])
    gender.grid(row=3, column=2, sticky='wen', padx=10)
    gender.set('')

    # 學歷 
    label(student_all, text='學歷').grid(row=2, column=3, sticky='ws', pady=(20,0))
    education = combobox(student_all, values=['學前教育','國小','國中','高中','專科','大學','碩士','博士'])
    education.grid(row=3, column=3, sticky='wen', padx=(0,10))
    education.set('')

    # 獲取教練資料 ####
    instructor_numbers, instructor_names, instructor_dict = get_instructor_data()
    # 指導教練
    label(student_all, text='指導教練').grid(row=4, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    instructor_number = combobox(student_all, values=instructor_numbers, command=lambda x: on_instructor_number_changed(x, instructor_name, instructor_dict))
    instructor_number.grid(row=5, column=2, sticky='wen', padx=10)
    instructor_name = combobox(student_all, values=instructor_names)
    instructor_name.grid(row=5, column=3, sticky='wen', padx=(0,10))
    instructor_number.set('')
    instructor_name.set('')

    # 監聽第一個下拉選單的變化
    def on_instructor_number_changed(selected_number, instructor_name, instructor_dict):
        # 根據教練編號獲取教練名稱
        selected_name = instructor_dict.get(selected_number, "")
        # 設置第二個下拉選單的值
        instructor_name.set(selected_name)
    #################
    
    # 信箱
    label(student_all, text='信箱').grid(row=6, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    email = entry(student_all)
    email.grid(row=7, column=2, columnspan=2, sticky='wen', padx=10)

    # 備註
    label(student_all, text='備註').grid(row=8, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    remarks = entry(student_all)
    remarks.grid(row=9, column=2, columnspan=2, sticky='wen', padx=10)

    # 抓取郵遞區號資料 #########
    m_address_zip_code_lists, m_address_city_lists, m_address_dict = address_data()
    # 通訊地址 ######
    label(student_all, text='通訊地址').grid(row=10, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    # 郵遞區號
    m_address_zip_code_list = combobox(student_all,  values = m_address_zip_code_lists, command=lambda x: auto_event_m_address(x, m_address_city_list, m_address_dict))
    m_address_zip_code_list.grid(row=11, column=2, sticky='wen', padx=10)
    # 縣市區域
    m_address_city_list = combobox(student_all, values = m_address_city_lists)
    m_address_city_list.grid(row=11, column=3, sticky='wen', padx=(0,10))
    # 地址
    m_address = entry(student_all)
    m_address.grid(row=12, column=2, columnspan=2, sticky='wen', padx=10)
    m_address_zip_code_list.set('')
    m_address_city_list.set('')

    # 監聽第一個下拉選單的變化
    def auto_event_m_address(zip_code_list, m_address_city, address_dict):
        # 根據郵遞區號獲取城市
        selected_zip_code = address_dict.get(zip_code_list, "")
        # 設置第二個下拉選單的值
        m_address_city.set(selected_zip_code)
    #################
    

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

    
    # 獲取輸入欄位信息
    def get_data_and_insert():
        pass


    # 新增，修改，刪除，查詢 -- 按鈕
    add_btn(student_all, text='新增', command=lambda: None).grid(row=13, column=0, sticky='wen', padx=10, pady=20)
    search_btn(student_all, text='查詢', command=click_btn).grid(row=13, column=1, sticky='wen', padx=(0,10), pady=20)
    modify_btn(student_all, text='修改', command=lambda: None).grid(row=13, column=2, sticky='wen', padx=10, pady=20)
    delete_btn(student_all, text='刪除', command=lambda: None).grid(row=13, column=3, sticky='wen', padx=(0,10), pady=20)