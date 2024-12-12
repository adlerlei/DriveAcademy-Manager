# M2補訓名冊 介面 
# 該介面不需要匯出文件功能
# 對應介面 models/m2retraining.py
from utils.widget import *
from utils.config import *
from models.m2retraining import * 
import customtkinter as ctk
from tkinter import messagebox
from models.annual_plan import annual_plan_data
from tkinter import ttk
import webbrowser
import pyautogui
import time
import os
from jinja2 import Environment, FileSystemLoader
import webbrowser
import time

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
    learner_permit_date = entry(m2_retraining_roster_creation)
    learner_permit_date.grid(row=3, column=0, sticky='wen',padx=(10,0))

    # 名冊號碼
    label(m2_retraining_roster_creation, text='名冊號碼').grid(row=2, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    register_number = entry(m2_retraining_roster_creation)
    register_number.grid(row=3, column=1, sticky='wen',padx=(10,0))

    # 期別
    label(m2_retraining_roster_creation, text='期別').grid(row=2, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    register_term = entry(m2_retraining_roster_creation)
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
    exam_type_name = combobox(m2_retraining_roster_creation, values=['補筆試', '補路試'])
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

    data_list.heading('register_number', text='名冊號碼', anchor='center')
    data_list.heading('student_number', text='學員編號', anchor='center')
    data_list.heading('batch', text='梯次', anchor='center')
    data_list.heading('student_name', text='學員姓名', anchor='center')
    data_list.heading('exam_code', text='來源', anchor='center')
    data_list.heading('transmission_type_code', text='手自排', anchor='center')
    data_list.heading('instructor_number', text='教練', anchor='center')
    data_list.heading('national_id_no', text='身分證號', anchor='center')
    data_list.heading('learner_permit_date', text='學照日期', anchor='center')
    data_list.heading('gender', text='性別', anchor='center')
    data_list.heading('birth_date', text='出生日期', anchor='center')
    data_list.heading('r_address_zip_code', text='區號', anchor='center')
    data_list.heading('r_address_city_road', text='戶籍地址', anchor='center')
    
    data_list.column('register_number', width=50, anchor='center')
    data_list.column('student_number', width=50, anchor='center')
    data_list.column('batch', width=20, anchor='center')
    data_list.column('student_name', width=50, anchor='center')
    data_list.column('exam_code', width=20, anchor='center')
    data_list.column('transmission_type_code', width=20, anchor='center')
    data_list.column('instructor_number', width=20, anchor='center')
    data_list.column('national_id_no', width=50, anchor='center')
    data_list.column('learner_permit_date', width=50, anchor='center')
    data_list.column('gender', width=20, anchor='center')
    data_list.column('birth_date', width=50, anchor='center')
    data_list.column('r_address_zip_code', width=20, anchor='center')
    data_list.column('r_address_city_road', width=100, anchor='center')
    
    data_list.grid(row=13, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)

    # 創建水平捲軸
    h_scrollbar = ttk.Scrollbar(m2_retraining_roster_creation, orient="horizontal", command=data_list.xview)
    data_list.configure(xscrollcommand=h_scrollbar.set)

    # 創建垂直捲軸
    v_scrollbar = ttk.Scrollbar(m2_retraining_roster_creation, orient="vertical", command=data_list.yview)
    data_list.configure(yscrollcommand=v_scrollbar.set)

    # 使用 grid 布局管理器來排列 Treeview 和捲軸
    h_scrollbar.grid(row=14, column=0, columnspan=4, sticky="ew", padx=10)
    v_scrollbar.grid(row=13, column=4, rowspan=2, sticky="ns", pady=10)

    # 配置行和列的權重，使其在窗口調整大小時自動調整
    m2_retraining_roster_creation.grid_rowconfigure(13, weight=1)
    m2_retraining_roster_creation.grid_columnconfigure(0, weight=1)
    m2_retraining_roster_creation.grid_columnconfigure(1, weight=1)
    m2_retraining_roster_creation.grid_columnconfigure(2, weight=1)
    m2_retraining_roster_creation.grid_columnconfigure(3, weight=1)

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
        # 如果没有找到数据，直接返回
        if not student_data:
            return
        
        if student_data:
            current_student_id = student_data[0]

            # 學員編號
            student_number.delete(0, ctk.END)
            student_number.insert(0, str(student_data[5]) if student_data[5] else '')

            # 學員姓名
            student_name.delete(0, ctk.END)
            student_name.insert(0, str(student_data[6]) if student_data[6] else '')

            # 身分證號
            national_id_no.delete(0, ctk.END)
            national_id_no.insert(0, str(student_data[10]) if student_data[10] else '')

            # 出生日期
            birth_date.configure(state='normal')
            birth_date.delete(0, ctk.END)
            birth_date.insert(0, str(student_data[9]) if student_data[9] else '')
            birth_date.configure(state='readonly')

            # 學照日期
            learner_permit_date.delete(0, ctk.END)
            learner_permit_date.insert(0, str(student_data[26]) if student_data[26] is not None else '')

            # 名冊號碼
            register_number.delete(0, ctk.END)
            register_number.insert(0, str(student_data[34]) if student_data[34] is not None else '')

            # 期別
            register_term.delete(0, ctk.END)
            register_term.insert(0, str(student_data[35]) if student_data[35] is not None else '')

            # 性別
            gender.configure(state='normal')
            gender.delete(0, ctk.END)
            gender.insert(0, str(student_data[16]) if student_data[16] else '')
            gender.configure(state='readonly')

            # 梯次
            batch.configure(state='normal')
            batch.delete(0, ctk.END)
            batch.insert(0, str(student_data[7]) if student_data[7] else '')
            batch.configure(state='readonly')

            # 訓練班別代號
            training_type_code.configure(state='normal')
            training_type_code.delete(0, ctk.END)
            training_type_code.insert(0, str(student_data[3]) if student_data[3] else '')
            training_type_code.configure(state='readonly')

            # 訓練班別名稱
            training_type_name.configure(state='normal')
            training_type_name.delete(0, ctk.END)
            training_type_name.insert(0, str(student_data[4]) if student_data[4] else '')
            training_type_name.configure(state='readonly')

            # 戶籍地址 郵遞區號
            r_address_zip_code.configure(state='normal')
            r_address_zip_code.delete(0, ctk.END)
            r_address_zip_code.insert(0, str(student_data[19]) if student_data[19] else '')
            r_address_zip_code.configure(state='readonly')

            # 戶籍地址 縣市區域
            r_address_city.configure(state='normal')
            r_address_city.delete(0, ctk.END)
            r_address_city.insert(0, str(student_data[20]) if student_data[20] else '')
            r_address_city.configure(state='readonly')

            # 戶籍地址 地址
            r_address.configure(state='normal')
            r_address.delete(0, ctk.END)
            r_address.insert(0, str(student_data[21]) if student_data[21] else '')
            r_address.configure(state='readonly')

            # 來源
            exam_code.set(str(student_data[29]) if student_data[29] is not None else '')

            # 來源名稱
            exam_name.set(str(student_data[30]) if student_data[30] is not None else '')

            # 設置其他字段的值
            transmission_type_code.set(str(student_data[31]) if student_data[31] is not None else '')
            transmission_type_name.set(str(student_data[32]) if student_data[32] is not None else '')
            instructor_number.set(str(student_data[14]) if student_data[14] is not None else '')
            instructor_name.set(str(student_data[15]) if student_data[15] is not None else '')

            # 考試類型名稱
            if len(student_data) > 43:
                exam_type_name.set(str(student_data[40]) if student_data[40] is not None else '')
            else:
                exam_type_name.set('')  # 如果没有这个字段，设置为空字符串


    # 獲取輸入欄位信息
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

        # 格式化 learner_permit_date 日期
        formatted_learner_permit_date = student_data['learner_permit_date']
        if formatted_learner_permit_date and len(formatted_learner_permit_date) >= 6:
            year = formatted_learner_permit_date[:-4]
            month = formatted_learner_permit_date[-4:-2]
            day = formatted_learner_permit_date[-2:]
            formatted_learner_permit_date = f"{year} / {month} / {day}"

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
            student_data['exam_type_name']
            # student_data['training_type_code']
        ))

    ## 列印功能 ##########
    # 獲取輸入欄位中需要顯示在列印頁面上的信息:
    def get_treeview_data():
        data = []
        for item in data_list.get_children():
            values = data_list.item(item)['values']
            print(values)
            # 獲取原始日期字符串
            birth_date = str(values[8]) if values[8] is not None else ''
      
            # 轉換日期格式
            if birth_date and len(birth_date) >= 6:  # 允許年份位數變化
                # 從後往前取值，因為月日固定是最後4位
                day = birth_date[-2:]  # 最後2位是日
                month = birth_date[-4:-2]  # 倒數第3-4位是月
                year = birth_date[:-4]  # 剩下的都是年
                
                # 驗證月份和日期的有效性
                if month.isdigit() and day.isdigit() and 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                    # 正確的日期格式，不需要輸出
                    pass
                else:
                    year, month, day = '-', '-', '-'
            else:
                year, month, day = '-', '-', '-'
 

            data.append({
                # 'student_number': values[2], # 學員編號
                'register_number': values[0], # 名冊號碼
                'student_name': values[3], # 學員姓名
                'gender': values[9], # 性別
                'birth_year': year, # 生日-年
                'birth_month': month, # 生日-月
                'birth_day': day, # 生日-日
                'national_id_no': values[7], # 身分證字號
                'r_address_city_road': values[12], # 地址
                'learner_permit_date': values[8], # 學照登錄日期
                'exam_type_name': values[13], # 筆路
            })
        return data
    

    # 獲取性別為男的資料總數
    def get_male_student_count():
        male_count = 0
        for item in data_list.get_children():
            values = data_list.item(item)['values']
            if values[9] == '男':  # 假設性別欄位在第10列
                male_count += 1
        return male_count
    
    # 獲取性別為女的資料總數
    def get_female_student_count():
        female_count = 0
        for item in data_list.get_children():
            values = data_list.item(item)['values']
            if values[9] == '女':  # 假設性別欄位在第10列
                female_count += 1
        return female_count


    # 列印函式中添加 male_count 變量
    def print_html_report(for_dmv=True):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir = os.path.join(base_dir, "print")
        env = Environment(loader=FileSystemLoader(template_dir))

        if for_dmv:
            template = env.get_template("m2.html")
        else:
            template = env.get_template("m2_駕訓班公告.html")

        data = get_treeview_data()
        if not data:
            messagebox.showwarning("警告", "沒有數據可以打印")
            return
        elif not for_dmv:
            for item in data:
                item['national_id_no'] = '0000'

        results = annual_plan_data()

        class_name = "佑名駕訓班"
        training_type_name = results[0][6]
        term = results[0][2]
        batch = results[0][4]
        start_date = results[0][7]
        end_date = results[0][8]

        if start_date and len(start_date) >= 6:
            start_year = start_date[:-4]
            start_month = start_date[-4:-2]
            start_day = start_date[-2:]
            start_date = f"{start_year} 年 {start_month} 月 {start_day} 日"

        if end_date and len(end_date) >= 6:
            end_year = end_date[:-4]
            end_month = end_date[-4:-2]
            end_day = end_date[-2:]
            end_date = f"{end_year} 年 {end_month} 月 {end_day} 日"

        male_count_boy = get_male_student_count()
        male_count_girl = get_female_student_count()

        html_content = template.render(
            students=data,
            class_name=class_name,
            training_type_name=training_type_name,
            term=term,
            batch=batch,
            start_date=start_date,
            end_date=end_date,
            learner_permit_date=learner_permit_date,
            male_count_boy=male_count_boy,
            male_count_girl=male_count_girl,
            male_count_people=male_count_boy+male_count_girl
        )

        temp_html_path = os.path.join(base_dir, "print", "temp_m2.html")
        with open(temp_html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        webbrowser.open_new_tab(f'file://{temp_html_path}')

        # 等待瀏覽器加載
        time.sleep(3) 
        # 每個按鍵之間延遲0.1秒
        pyautogui.hotkey('ctrl', 'p', interval=0.1)
        # 等待打印窗口出現
        time.sleep(2)
        # 模擬鍵盤操作確認打印 (Enter)
        pyautogui.press('enter')

        # 删除临时文件
        time.sleep(1)  # 等待打印完成
        os.remove(temp_html_path)
        
        # pyautogui.hotkey('ctrl', 'shift', 'p', interval=0.1)  # 打开打印设置
        # time.sleep(2)
        # pyautogui.press('tab', presses=2, interval=0.1)  # 移动到纸张大小选项
        # pyautogui.press('down', presses=1, interval=0.1)  # 选择A4纸张
        # pyautogui.press('tab', presses=2, interval=0.1)  # 移动到方向选项
        # pyautogui.press('down', presses=1, interval=0.1)  # 选择横向
        # pyautogui.press('enter')  # 确认设置
        # pyautogui.press('enter')



    # 列印函式
    # def print_html_report(for_dmv=True):
    #     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #     template_dir = os.path.join(base_dir, "print")
    #     env = Environment(loader=FileSystemLoader(template_dir))

    #     # 根據 for_dmv 的值選擇不的列印模板
    #     if for_dmv:
    #         template = env.get_template("m2.html")
    #     else:
    #         template = env.get_template("m2_駕訓班公告.html")

    #     data = get_treeview_data()
    #     if not data:
    #         messagebox.showwarning("警告", "沒有數據可以打印")
    #         return
    #     elif not for_dmv:
    #         for item in data:
    #             item['national_id_no'] = '0000'

    #     # 讀取年度計畫表資料信息
    #     results = annual_plan_data()

    #     # 獲取 annual_plan 資料表的 training_type_name, term, batch, start_date, end_date 數據
    #     class_name = "佑名駕訓班"  # 请替换为实际的班名
    #     training_type_name = results[0][6] # 訓練班別名稱
    #     term = results[0][2] # 期別
    #     batch = results[0][4] # 梯次
    #     start_date = results[0][7] # 開訓日期
    #     end_date = results[0][8] # 結訓日期

    #     # 將開訓日期的值拆分成年月日
    #     if start_date and len(start_date) >= 6:
    #         start_year = start_date[:-4]
    #         start_month = start_date[-4:-2]
    #         start_day = start_date[-2:]
    #         start_date = f"{start_year} 年 {start_month} 月 {start_day} 日"

    #     # 將結訓日期的值拆分成年月日
    #     if end_date and len(end_date) >= 6:
    #         end_year = end_date[:-4]
    #         end_month = end_date[-4:-2]
    #         end_day = end_date[-2:]
    #         end_date = f"{end_year} 年 {end_month} 月 {end_day} 日"


    #     html_content = template.render(
    #         students=data,
    #         class_name=class_name,
    #         training_type_name=training_type_name,
    #         term=term,
    #         batch=batch,
    #         start_date=start_date,
    #         end_date=end_date,
    #         learner_permit_date=learner_permit_date
    #     )


    #     temp_html_path = os.path.join(base_dir, "print", "temp_m2.html")
    #     with open(temp_html_path, 'w', encoding='utf-8') as f:
    #         f.write(html_content)

    #     webbrowser.open_new_tab(f'file://{temp_html_path}')

    #     # 等待瀏覽器加載
    #     time.sleep(3) 
    #     # 每個按鍵之間延遲0.1秒
    #     pyautogui.hotkey('ctrl', 'p', interval=0.1)
    #     # 等待打印窗口出現
    #     time.sleep(2)
    #     # 模擬鍵盤操作確認打印 (Enter)
    #     pyautogui.press('enter')

    #     # 删除临时文件
    #     time.sleep(1)  # 等待打印完成
    #     os.remove(temp_html_path)

    # 按鈕
    add_btn(m2_retraining_roster_creation, text='加入M2補訓', command=save_student_data).grid(row=12, column=1, sticky='wen', padx=(10, 0), pady=(20, 0))
    print_btn(m2_retraining_roster_creation, text='列印M2補訓(駕訓班用)', command=lambda: print_html_report(for_dmv=False)).grid(row=12, column=2, sticky='wen', padx=(10, 0), pady=(20, 0))
    print_btn(m2_retraining_roster_creation, text='列印M2補訓(監理站用)', command=lambda: print_html_report(for_dmv=True)).grid(row=12, column=3, sticky='wen', padx=10, pady=(20, 0))