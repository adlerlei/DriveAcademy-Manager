# M2補訓名冊 介面 
# 該介面不需要匯出文件功能
# 對應介面 models/m2retraining.py
from utils.widget import *
from utils.config import *
from models.m2retraining import * 
import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk

# 檢測學員資料庫 id 欄位來判定是否修改或新增
current_student_id = None

# 在文件顶部添加全局变量声明
global data_list

def m2_retraining_roster_creation(content):
    global data_list  # 在函数开始处添加这行
    
    m2_retraining_roster_creation = frame(content)
    m2_retraining_roster_creation.columnconfigure(0, weight=1)
    m2_retraining_roster_creation.columnconfigure(1, weight=1)
    m2_retraining_roster_creation.columnconfigure(2, weight=1)
    m2_retraining_roster_creation.columnconfigure(3, weight=1)
    m2_retraining_roster_creation.place(relwidth=1, relheight=1)

    # 顯示 / 搜尋 學員編號
    label(m2_retraining_roster_creation, text='學員編號').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    student_number = entry(m2_retraining_roster_creation,  placeholder_text = " 🔎")
    student_number.grid(row=1, column=0, sticky='wen', padx=(10,0))
    student_number.bind("<KeyRelease>", lambda event: check_and_populate('student_number', student_number.get()))
    
    # 顯示 / 搜尋 學員姓名
    label(m2_retraining_roster_creation, text='學員姓名').grid(row=0, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    student_name = entry(m2_retraining_roster_creation, placeholder_text=" 🔎")
    student_name.grid(row=1, column=1, sticky='wen', padx=(10,0))
    student_name.bind("<KeyRelease>", lambda event: check_and_populate('student_name', student_name.get()))

    # 顯示 / 搜尋 身分證號碼
    label(m2_retraining_roster_creation, text='身分證號').grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    national_id_no = entry(m2_retraining_roster_creation, placeholder_text=" 🔎")
    national_id_no.grid(row=1, column=2, sticky='wen', padx=(10,0))
    national_id_no.bind("<KeyRelease>", lambda event: check_and_populate('national_id_no', national_id_no.get()))

    # 出生日期
    label(m2_retraining_roster_creation, text='出生日期').grid(row=0, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    birth_date = display_entry_value(m2_retraining_roster_creation)
    birth_date.grid(row=1, column=3, sticky='wen',padx=10)

    # 學照日期
    label(m2_retraining_roster_creation, text='學照日期').grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    learner_permit_date = display_entry_value(m2_retraining_roster_creation)
    learner_permit_date.grid(row=3, column=0, sticky='wen',padx=(10,0))

    # 名冊號碼
    label(m2_retraining_roster_creation, text='名冊號碼').grid(row=2, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    register_number = display_entry_value(m2_retraining_roster_creation)
    register_number.grid(row=3, column=1, sticky='wen',padx=(10,0))

    # 期別
    label(m2_retraining_roster_creation, text='期別').grid(row=2, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    register_term = display_entry_value(m2_retraining_roster_creation)
    register_term.grid(row=3, column=2, sticky='wen',padx=(10,0))

    # 性別
    label(m2_retraining_roster_creation, text='性別').grid(row=2, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    gender = display_entry_value(m2_retraining_roster_creation)
    gender.grid(row=3, column=3, sticky='wen',padx=10)

    # 梯次
    label(m2_retraining_roster_creation, text='梯次').grid(row=4, column=0, sticky='ws', padx=10, pady=(10,0))
    batch = display_entry_value(m2_retraining_roster_creation)
    batch.grid(row=5, column=0, sticky='wen',padx=(10,0))

    # 訓練班別
    label(m2_retraining_roster_creation, text='訓練班別').grid(row=4, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    training_type_code = display_entry_value(m2_retraining_roster_creation)
    training_type_code.grid(row=5, column=1, sticky='wen',padx=(10,0))
    training_type_name = display_entry_value(m2_retraining_roster_creation)
    training_type_name.grid(row=5, column=2, sticky='wen',padx=(10,0))

    # 戶籍地址
    label(m2_retraining_roster_creation, text='戶籍地址').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    r_address_zip_code = display_entry_value(m2_retraining_roster_creation)
    r_address_zip_code.grid(row=7, column=0, sticky='wen',padx=(10,0))
    r_address_city = display_entry_value(m2_retraining_roster_creation)
    r_address_city.grid(row=7, column=1, sticky='wen',padx=(10,0))
    r_address = display_entry_value(m2_retraining_roster_creation)
    r_address.grid(row=7, column=2, columnspan=2, sticky='wen',padx=10)
    
    # 來源
    exam_codes = ['A','B','C','G','Z']
    exam_names = ['新考','晉考','換考','吊扣註銷重考','臨時駕駛執照']
    exam_dict_c = dict(zip(exam_codes, exam_names))
    exam_dict_n = dict(zip(exam_names, exam_codes))

    label(m2_retraining_roster_creation, text='來源').grid(row=8, column=0, sticky='ws', padx=(10,0), pady=(50,0))
    exam_code = combobox(m2_retraining_roster_creation, values=exam_codes, command=lambda x: on_exam_code_changed(x, exam_name, exam_dict_c))
    exam_code.grid(row=9, column=0, sticky='wen', padx=(10,0))
    exam_name = combobox(m2_retraining_roster_creation, values=exam_names, command=lambda x: on_exam_name_changed(x, exam_code, exam_dict_n))
    exam_name.grid(row=9, column=1, sticky='wen', padx=(10,0))
    exam_code.set('')
    exam_name.set('')

    def on_exam_code_changed(select_code, exam_name, exam_dict):
        select_name = exam_dict.get(select_code, "")
        exam_name.set(select_name)

    def on_exam_name_changed(select_name, exam_code, exam_dict):
        select_code = exam_dict.get(select_name, "")
        exam_code.set(select_code)

    # 手自排 下拉選單
    transmission_type_codes = ['M','A','S']
    transmission_type_names = ['手排','自排','特製車']
    transmission_type_dict_c = dict(zip(transmission_type_codes, transmission_type_names))
    transmission_type_dict_n = dict(zip(transmission_type_names, transmission_type_codes))
    label(m2_retraining_roster_creation, text='手自排').grid(row=8, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    transmission_type_code = combobox(m2_retraining_roster_creation, values=transmission_type_codes, command=lambda x:on_transmission_type_code_changed(x, transmission_type_name, transmission_type_dict_c))
    transmission_type_code.grid(row=9, column=2, sticky='wen', padx=(10,0))
    transmission_type_name = combobox(m2_retraining_roster_creation, values=transmission_type_names, command=lambda x:on_transmission_type_name_changes(x, transmission_type_code, transmission_type_dict_n))
    transmission_type_name.grid(row=9, column=3, sticky='wen', padx=10)
    transmission_type_code.set('')
    transmission_type_name.set('')

    def on_transmission_type_code_changed(select_code, transmission_type_name, transmission_type_dict):
        select_name = transmission_type_dict.get(select_code, "")
        transmission_type_name.set(select_name)

    def on_transmission_type_name_changes(select_name, transmission_type_code, transmission_type_dict):
        select_code = transmission_type_dict.get(select_name, "")
        transmission_type_code.set(select_code)

    # 教練 下拉選單
    instructor_numbers, instructor_names, instructor_dict = get_instructor_data()
    label(m2_retraining_roster_creation, text='指導教練').grid(row=10, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    instructor_number = combobox(m2_retraining_roster_creation, values=instructor_numbers, command=lambda x: on_instructor_number_changed(x, instructor_name, instructor_dict))
    instructor_number.grid(row=11, column=0, sticky='wen', padx=(10,0))
    instructor_name = combobox(m2_retraining_roster_creation, values=instructor_names, command=lambda x: on_instructor_name_changed(x, instructor_number, instructor_dict))
    instructor_name.grid(row=11, column=1, sticky='wen', padx=(10,0))
    instructor_number.set('')
    instructor_name.set('')

    def on_instructor_number_changed(selected_number, instructor_name, instructor_dict):
        selected_name = instructor_dict.get(selected_number, "")
        instructor_name.set(selected_name)

    def on_instructor_name_changed(selected_name, instructor_number, instructor_dict):
        selected_number = next((number for number, name in instructor_dict.items() if name == selected_name), "")
        instructor_number.set(selected_number)

    # 筆試路試
    label(m2_retraining_roster_creation, text='筆路').grid(row=10, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    exam_type_name = combobox(m2_retraining_roster_creation, values=['1 . 補筆', '2 . 補路'])
    exam_type_name.grid(row=11, column=2, sticky='wen',padx=(10,0))
    exam_type_name.set('')

    # treeview
    columns = (
        'register_number', # 名冊號碼
        'student_number', # 學員編號
        'batch', # 梯次
        'student_name', # 學員姓名
        'exam_code', # 來源 編號
        'transmission_type_code', # 手自排 編號
        'instructor_number', # 教練 編號
        'national_id_no', # 學員 身分證號碼
        'learner_permit_date', # 學照日期
        'gender', # 學員性別
        'birth_date', # 出生日期
        'r_address_zip_code', # 戶籍地址區號
        'r_address_city_road', # 戶籍地址 ( 前面增加縣市區域，但不需要顯示 treeview )
        'training_type_code' # 訓練班別代號 (隱藏列)
    )
    data_list = ttk.Treeview(m2_retraining_roster_creation, show='headings', column = columns)

    data_list.heading('register_number', text='名冊號碼')
    data_list.heading('student_number', text='學員編號')
    data_list.heading('batch', text='梯次')
    data_list.heading('student_name', text='學員姓名')
    data_list.heading('exam_code', text='來源')
    data_list.heading('transmission_type_code', text='手自排')
    data_list.heading('instructor_number', text='教練')
    data_list.heading('national_id_no', text='身分證號')
    data_list.heading('learner_permit_date', text='學照日期')
    data_list.heading('gender', text='性別')
    data_list.heading('birth_date', text='出生日期')
    data_list.heading('r_address_zip_code', text='區號')
    data_list.heading('r_address_city_road', text='戶籍地址')
    
    data_list.column('register_number', width=50, anchor='w')
    data_list.column('student_number', width=50, anchor='w')
    data_list.column('batch', width=20, anchor='w')
    data_list.column('student_name', width=50, anchor='w')
    data_list.column('exam_code', width=20, anchor='w')
    data_list.column('transmission_type_code', width=20, anchor='w')
    data_list.column('instructor_number', width=20, anchor='w')
    data_list.column('national_id_no', width=50, anchor='w')
    data_list.column('learner_permit_date', width=50, anchor='w')
    data_list.column('gender', width=20, anchor='w')
    data_list.column('birth_date', width=50, anchor='w')
    data_list.column('r_address_zip_code', width=20, anchor='w')
    data_list.column('r_address_city_road', width=100, anchor='w')
    
    data_list.grid(row=13, column=0, columnspan=4, sticky='nsew', padx=10, pady=(10,0))

    # 邏輯功能
    def check_and_populate(identifier, value):
        if value == '':
            clear_all_fields()
        else:
            populate_student_data(identifier, value)

    def clear_all_fields():
        global current_student_id
        clear_entries_and_comboboxes(m2_retraining_roster_creation)
        current_student_id = None

    # 搜尋學員資料庫並且在 entry 顯示學員資料
    def populate_student_data(identifier, value):
        global current_student_id
        student_data = get_student_data(identifier, value)
        if student_data:
            current_student_id = student_data[0]
            student_number.delete(0, ctk.END)
            student_number.insert(0, student_data[5])
            student_name.delete(0, ctk.END)
            student_name.insert(0, student_data[6])
            national_id_no.delete(0, ctk.END)
            national_id_no.insert(0, student_data[10])
            birth_date.configure(state='normal')
            birth_date.delete(0, ctk.END)
            birth_date.insert(0, student_data[9])
            birth_date.configure(state='readonly')

            # 學照日期
            if student_data[26] is not None:
                learner_permit_date.delete(0, ctk.END)
                learner_permit_date.insert(0, student_data[26])
            else:
                learner_permit_date.delete(0, ctk.END)
                learner_permit_date.insert(0, '')

            # register_number.configure(state='normal')
            # register_number.delete(0, ctk.END)
            # register_number.insert(0, student_data[34])
            # register_number.configure(state='readonly')
            if student_data[34] is not None:
                register_number.delete(0, ctk.END)
                register_number.insert(0, student_data[34])
            else:
                register_number.delete(0, ctk.END)
                register_number.insert(0, '')

            # register_term.configure(state='normal')
            # register_term.delete(0, ctk.END)
            # register_term.insert(0, student_data[35])
            # register_term.configure(state='readonly')
            if student_data[35] is not None:
                register_term.delete(0, ctk.END)
                register_term.insert(0, student_data[35])
            else:
                register_term.delete(0, ctk.END)
                register_term.insert(0, '')


            gender.configure(state='normal')
            gender.delete(0, ctk.END)
            gender.insert(0, student_data[16])
            gender.configure(state='readonly')
            batch.configure(state='normal')
            batch.delete(0, ctk.END)
            batch.insert(0, student_data[7])
            batch.configure(state='readonly')
            training_type_code.configure(state='normal')
            training_type_code.delete(0, ctk.END)
            training_type_code.insert(0, student_data[3])
            training_type_code.configure(state='readonly')
            training_type_name.configure(state='normal')
            training_type_name.delete(0, ctk.END)
            training_type_name.insert(0, student_data[4])
            training_type_name.configure(state='readonly')
            r_address_zip_code.configure(state='normal')
            r_address_zip_code.delete(0, ctk.END)
            r_address_zip_code.insert(0, student_data[19])
            r_address_zip_code.configure(state='readonly')
            r_address_city.configure(state='normal')
            r_address_city.delete(0, ctk.END)
            r_address_city.insert(0, student_data[20])
            r_address_city.configure(state='readonly')
            r_address.configure(state='normal')
            r_address.delete(0, ctk.END)
            r_address.insert(0, student_data[21])
            r_address.configure(state='readonly')
            
            # 來源
            if student_data[29] is not None:
                exam_code.set(student_data[29])
            else:
                exam_code.set('')
            # 來源名稱
            if student_data[30] is not None:
                exam_name.set(student_data[30])
            else:
                exam_name.set('')
            
            # 設置其他字段的值（如來源、手自排、教練等）
            if student_data[31] is not None:
                transmission_type_code.set(student_data[31])
            if student_data[32] is not None:
                transmission_type_name.set(student_data[32])
            if student_data[14] is not None:
                instructor_number.set(student_data[14])
            if student_data[15] is not None:
                instructor_name.set(student_data[15])
            if len(student_data) > 43:
                if student_data[43] is not None:
                    exam_type_name.set(student_data[43])
                else:
                    exam_type_name.set('')
            else:
                exam_type_name.set('')  # 如果没有这个字段，设置为空字符串

    # 獲取入欄位信息
    def save_student_data():
        global data_list  # 在函数开始处添加这行
        uid = 0
        global current_student_id
        student_data = {
            'register_number': register_number.get(),
            'student_number': student_number.get(),
            'batch': batch.get(),
            'student_name': student_name.get(),
            'exam_code': exam_code.get(),
            'exam_name': exam_name.get(),
            'exam_type_name': exam_type_name.get(),
            'transmission_type_code': transmission_type_code.get(),
            'transmission_type_name': transmission_type_name.get(),
            'instructor_number': instructor_number.get(),
            'national_id_no': national_id_no.get(),
            'instructor_name': instructor_name.get(),
            'learner_permit_date': learner_permit_date.get(),
            'gender': gender.get(),
            'birth_date': birth_date.get(),
            'register_term': register_term.get(),
            'r_address_zip_code': r_address_zip_code.get(),
            'r_address_city': r_address_city.get(),
            'r_address': r_address.get(),
            'r_address_city_road': r_address_city.get() + r_address.get(),
            'training_type_code': training_type_code.get(),
            'id': current_student_id
        }

        # 驗證 筆路 輸入欄位是否為空
        required_fields = [ 
            'exam_type_name',
        ]
        for field in required_fields:
            if not student_data[field]:
                messagebox.showwarning('提示', f'{validation_fields[field]} 欄位不能為空！')
                return

        if current_student_id is None:
            messagebox.showwarning('警告', '請先搜尋學員資料！')
            return
        
        update_student_data(student_data)
        clear_entries_and_comboboxes(m2_retraining_roster_creation)

        # 讀取 save_student_data 的資料寫入 treeview
        data_list.insert('', 'end', values = (
            student_data['register_number'],
            student_data['student_number'],
            student_data['batch'],
            student_data['student_name'],
            student_data['exam_code'],
            student_data['transmission_type_code'],
            student_data['instructor_number'],
            student_data['national_id_no'],
            student_data['learner_permit_date'],
            student_data['gender'],
            student_data['birth_date'],
            student_data['r_address_zip_code'],
            student_data['r_address_city_road'],
            student_data['training_type_code']
        ))

    # 按鈕
    add_btn(m2_retraining_roster_creation, text='加入M2補訓', command=save_student_data).grid(row=12, column=2, sticky='wen', padx=(10, 0), pady=(20, 0))
    print_btn(m2_retraining_roster_creation, text='列印M2補訓名冊', command=None).grid(row=12, column=3, sticky='wen', padx=10, pady=(20, 0))