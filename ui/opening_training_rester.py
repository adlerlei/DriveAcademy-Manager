# 開訓名冊
from utils.widget import *
from utils.config import * 
from models.training import *
import customtkinter as ctk
from tkinter import messagebox


# 開訓名冊建立後需要將資料顯示欄位的名冊號碼與學員資料綁定

def opening_training_roster(content):
    clear_frame(content)
    
    opening_training_roster = frame(content)
    opening_training_roster.columnconfigure(0, weight=1)
    opening_training_roster.columnconfigure(1, weight=1)
    opening_training_roster.columnconfigure(2, weight=1)
    opening_training_roster.columnconfigure(3, weight=1)
    opening_training_roster.place(relwidth=1, relheight=1)

    # 顯示 / 搜尋 學員編號
    label(opening_training_roster, text='學員編號').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    student_number = entry(opening_training_roster,  placeholder_text = "輸入學員編號查詢")
    student_number.grid(row=1, column=0, sticky='wen', padx=(10,0))

    # 學員姓名
    label(opening_training_roster, text='學員姓名').grid(row=0, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    student_name = display_entry_value(opening_training_roster)
    student_name.grid(row=1, column=1, sticky='wen', padx=(10,0))

    # 學員身分證號碼
    label(opening_training_roster, text='身分證號').grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    national_id_no = display_entry_value(opening_training_roster)
    national_id_no.grid(row=1, column=2, sticky='wen', padx=(10,0))

    # 出生日期
    label(opening_training_roster, text='出生日期').grid(row=0, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    birth_date = display_entry_value(opening_training_roster)
    birth_date.grid(row=1, column=3, sticky='wen', padx=10)

    # 學照日期
    label(opening_training_roster, text='學照日期').grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    learner_permit_date = display_entry_value(opening_training_roster)
    learner_permit_date.grid(row=3, column=0, sticky='wen',padx=(10,0))

    # 名冊號碼
    label(opening_training_roster, text='名冊號碼').grid(row=2, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    register_number = display_entry_value(opening_training_roster)
    register_number.grid(row=3, column=1, sticky='wen',padx=(10,0))

    # 名冊期別 ( 抓取年度計畫期別新增 "期別" 使用下拉選單呈現選擇)
    label(opening_training_roster, text='名冊期別').grid(row=2, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    register_term = combobox(opening_training_roster, values=['A','B'])
    register_term.grid(row=3, column=2, sticky='wen',padx=(10,0))

    # 性別
    label(opening_training_roster, text='性別').grid(row=2, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    gender = display_entry_value(opening_training_roster)
    gender.grid(row=3, column=3, sticky='wen',padx=10)

    # 梯次
    label(opening_training_roster, text='梯次').grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    batch = display_entry_value(opening_training_roster)
    batch.grid(row=5, column=0, sticky='wen', padx=(10,0))

    # 名冊梯次 將梯次的值直接帶過來即可
    label(opening_training_roster, text='梯次').grid(row=4, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    register_batch = combobox(opening_training_roster, values=['A', 'B'])
    register_batch.grid(row=5, column=1, sticky='wen', padx=(10,0))

    # 訓練班別
    label(opening_training_roster, text='訓練班別').grid(row=4, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    training_type_code = combobox(opening_training_roster, values=['1','2','3'])
    training_type_code.grid(row=5, column=2, sticky='wen',padx=(10,0))
    training_type_name = entry(opening_training_roster)
    training_type_name.grid(row=5, column=3, sticky='wen',padx=10)

    # 戶籍地址
    label(opening_training_roster, text='戶籍地址').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    r_address_zip_code =  display_entry_value(opening_training_roster)
    r_address_zip_code.grid(row=7, column=0, sticky='wen',padx=(10,0))
    r_address_city = display_entry_value(opening_training_roster)
    r_address_city.grid(row=7, column=1, sticky='wen',padx=(10,0))
    r_address = display_entry_value(opening_training_roster)
    r_address.grid(row=7, column=2, columnspan=2, sticky='wen',padx=10)
    
    # 來源 下拉選單
    label(opening_training_roster, text='來源').grid(row=8, column=0, sticky='ws', padx=(10,0), pady=(50,0))
    exam_code = combobox(opening_training_roster, values=['A','B','C','G','Z'])
    exam_code.grid(row=9, column=0, sticky='wen', padx=(10,0))
    exam_name = combobox(opening_training_roster, values=['新考','晉考','換考','吊扣註銷重考','臨時駕駛執照'])
    exam_name.grid(row=9, column=1, sticky='wen', padx=(10,0))

    # 手自排 下拉選單
    label(opening_training_roster, text='手自排').grid(row=8, column=2, sticky='ws', padx=(10,0), pady=(50,0))
    transmission_type_code = combobox(opening_training_roster, values=['M','A','S'])
    transmission_type_code.grid(row=9, column=2, sticky='wen', padx=(10,0))
    transmission_type_name = combobox(opening_training_roster, values=['手排','自排','特製車'])
    transmission_type_name.grid(row=9, column=3, sticky='wen', padx=10)

    # 教練 下拉選單
    label(opening_training_roster, text='教練').grid(row=10, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    instructor_number = combobox(opening_training_roster, values=['A', 'B'])
    instructor_number.grid(row=11, column=0, sticky='wen', padx=(10,0))
    instructor_name = entry(opening_training_roster)
    instructor_name.grid(row=11, column=1, sticky='wen', padx=(10,0))

    # 按鈕
    btn(opening_training_roster, text='加入開訓名冊', command=lambda: None).grid(row=11, column=2, columnspan=2, sticky='wen', padx=10)

    # treeview
    data_list = ttk.Treeview(opening_training_roster, show='headings', column=['id', 'roster_number', 'batch', 'student_number', 'student_name', 'exam_source_type', 'transmission_type', 'instructor', 'gender', 'birth_date', 'national_id_no', 'zip_code', 'city_r_address', 'training_type'])
    
    data_list.column('id', width=50, anchor='w')
    data_list.column('roster_number', width=50, anchor='w')
    data_list.column('batch', width=50, anchor='w')
    data_list.column('student_number', width=50, anchor='w')
    data_list.column('student_name', width=50, anchor='w')
    data_list.column('exam_source_type', width=50, anchor='w')
    data_list.column('transmission_type', width=50, anchor='w')
    data_list.column('instructor', width=50, anchor='w')
    data_list.column('gender', width=50, anchor='w')
    data_list.column('birth_date', width=50, anchor='w')
    data_list.column('national_id_no', width=60, anchor='w')
    data_list.column('training_type', width=50, anchor='w')
    data_list.column('zip_code', width=50, anchor='w')
    data_list.column('city_r_address', width=250, anchor='w')
    
    data_list.heading('id', text='ID')
    data_list.heading('roster_number', text='名冊號碼')
    data_list.heading('batch', text='梯次')
    data_list.heading('student_number', text='學員編號')
    data_list.heading('student_name', text='學員姓名')
    data_list.heading('exam_source_type', text='來源')
    data_list.heading('transmission_type', text='手自排')
    data_list.heading('instructor', text='教練')
    data_list.heading('gender', text='性別')
    data_list.heading('birth_date', text='出生日期')
    data_list.heading('national_id_no', text='身分證號')
    data_list.heading('training_type', text='訓練班別')
    data_list.heading('zip_code', text='區號')
    data_list.heading('city_r_address', text='戶籍地址')
    
    data_list.grid(row=12, column=0, columnspan=4, sticky='wen', padx=10, pady=(20,0))
    
    for i in range(100):
        data_list.insert("", "end", values=(f"202{i % 10}", f"張{i}", f"A{i}", f"202{i % 10}-01-01", f"男", f"02{i % 10}", f"09{i % 10}", f"test{i}@gmail.com", f"台北市", f"台北市"))