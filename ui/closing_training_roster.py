# 結訓名冊作業 介面
# 對應資料庫邏輯介面 models/training.py
from utils.widget import *
from utils.config import * 
from models.training import *
from models.annual_plan import annual_plan_data
import customtkinter as ctk
from tkinter import messagebox
import webbrowser
import pyautogui
import time
import os
from jinja2 import Environment, FileSystemLoader
import webbrowser
import time

# 檢測學員資料庫 id 欄位來判定是否修改或新增
current_student_id = None

counter = 1
current_choice = None

def closing_training_roster(content):
    clear_frame(content)
    
    closing_training_roster = frame(content)
    closing_training_roster.columnconfigure(0, weight=1)
    closing_training_roster.columnconfigure(1, weight=1)
    closing_training_roster.columnconfigure(2, weight=1)
    closing_training_roster.columnconfigure(3, weight=1)
    closing_training_roster.place(relwidth=1, relheight=1)

    # 監聽 名冊號碼 register_number 輸入值
    # def register_number_data_changed(choice):
    #     global counter, current_choice  # 使用全域變數
        
    #     # 檢查當前選擇的值是否改變
    #     if current_choice != choice:
    #         current_choice = choice
    #         counter = 1  # 重置計數器
        
    #     batch_value = batch.get()
    #     value = '0' + choice + batch_value + f'{counter:03d}'  # 格式化數字為三位數
    #     register_number.delete(0, ctk.END)
    #     register_number.insert(0, value)
    #     counter += 1  # 計數器遞增

    # 顯示 / 搜尋 學員編號
    label(closing_training_roster, text='學員編號').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    student_number = entry(closing_training_roster,  placeholder_text = " 🔎")
    student_number.grid(row=1, column=0, sticky='wen', padx=(10,0))
    student_number.bind("<KeyRelease>", lambda event: check_and_populate('student_number', student_number.get()))

    # 顯示 / 搜尋 學員姓名
    label(closing_training_roster, text='學員姓名').grid(row=0, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    student_name = entry(closing_training_roster, placeholder_text=" 🔎")
    student_name.grid(row=1, column=1, sticky='wen', padx=(10,0))
    student_name.bind("<KeyRelease>", lambda event: check_and_populate('student_name', student_name.get()))

    # 顯示 / 搜尋 學員身分證號碼
    label(closing_training_roster, text='身分證號').grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    national_id_no = entry(closing_training_roster, placeholder_text=" 🔎")
    national_id_no.grid(row=1, column=2, sticky='wen', padx=(10,0))
    national_id_no.bind("<KeyRelease>", lambda event: check_and_populate('national_id_no', national_id_no.get()))

    # 出生日期
    label(closing_training_roster, text='出生日期').grid(row=0, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    birth_date = display_entry_value(closing_training_roster)
    birth_date.grid(row=1, column=3, sticky='wen', padx=10)

    # 學照日期
    label(closing_training_roster, text='學照日期').grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    learner_permit_date = entry(closing_training_roster)
    learner_permit_date.grid(row=3, column=0, sticky='wen',padx=(10,0))

    # 名冊號碼
    label(closing_training_roster, text='名冊號碼').grid(row=2, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    register_number = entry(closing_training_roster, placeholder_text='此欄位自動生成，無須輸入')
    register_number.grid(row=3, column=1, sticky='wen',padx=(10,0))

    # 期別 ( 抓取年度計畫期別新增 "期別" 使用下拉選單呈現選擇) 不需要從資料庫讀取，但需要寫入資料庫
    # term_data = get_term_data()
    # label(closing_training_roster, text='期別').grid(row=2, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    # register_term = combobox(closing_training_roster, values=term_data, command=register_number_data_changed)
    # register_term.grid(row=3, column=2, sticky='wen',padx=(10,0))
    # register_term.set('')  # 初始值設為空
    label(closing_training_roster, text='期別').grid(row=2, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    register_term = entry(closing_training_roster)
    register_term.grid(row=3, column=2, sticky='wen',padx=(10,0))

    # 性別
    label(closing_training_roster, text='性別').grid(row=2, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    gender = display_entry_value(closing_training_roster)
    gender.grid(row=3, column=3, sticky='wen',padx=10)

    # 梯次
    label(closing_training_roster, text='梯次').grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    batch = display_entry_value(closing_training_roster)
    batch.grid(row=5, column=0, sticky='wen', padx=(10,0))

    # 名冊梯次 將梯次的值直接帶過來即可，不需要從資料庫讀取，但需要寫入資料庫
    label(closing_training_roster, text='名冊梯次').grid(row=4, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    register_batch = display_entry_value(closing_training_roster)
    register_batch.grid(row=5, column=1, sticky='wen', padx=(10,0))

    # 訓練班別
    label(closing_training_roster, text='訓練班別').grid(row=4, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    training_type_code = display_entry_value(closing_training_roster)
    training_type_code.grid(row=5, column=2, sticky='wen',padx=(10,0))
    training_type_name = display_entry_value(closing_training_roster)
    training_type_name.grid(row=5, column=3, sticky='wen',padx=10)

    # 戶籍地址
    label(closing_training_roster, text='戶籍地址').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    r_address_zip_code =  display_entry_value(closing_training_roster)
    r_address_zip_code.grid(row=7, column=0, sticky='wen',padx=(10,0))
    r_address_city = display_entry_value(closing_training_roster)
    r_address_city.grid(row=7, column=1, sticky='wen',padx=(10,0))
    r_address = display_entry_value(closing_training_roster)
    r_address.grid(row=7, column=2, columnspan=2, sticky='wen',padx=10)

    # 獲得教練資料庫資料
    instructor_numbers, instructor_names, instructor_dict = get_instructor_data()
    label(closing_training_roster, text='指導教練').grid(row=8, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    instructor_number = combobox(closing_training_roster, values=instructor_numbers, command=lambda x: on_instructor_number_changed(x, instructor_name, instructor_dict))
    instructor_number.grid(row=9, column=0, sticky='wen', padx=(10,0))
    instructor_name = combobox(closing_training_roster, values=instructor_names, command=lambda x: on_instructor_name_changed(x, instructor_number, instructor_dict))
    instructor_name.grid(row=9, column=1, sticky='wen', padx=(10,0))
    instructor_number.set('')
    instructor_name.set('')

    # 指導教練下拉選單監聽 number 改變時，自動更新 name 名稱
    def on_instructor_number_changed(selected_number, instructor_name, instructor_dict):
        selected_name = instructor_dict.get(selected_number, "")
        instructor_name.set(selected_name)

    # 指導教練下拉選單監聽 name 改變時，自動更新 number 編號 
    def on_instructor_name_changed(selected_name, instructor_number, instructor_dict):
        selected_number = next((number for number, name in instructor_dict.items() if name == selected_name), "")
        instructor_number.set(selected_number)

    # 手自排 下拉選單
    transmission_type_codes = ['M','A','S']
    transmission_type_names = ['手排','自排','特製車']
    transmission_type_dict_c = dict(zip(transmission_type_codes, transmission_type_names))
    transmission_type_dict_n = dict(zip(transmission_type_names, transmission_type_codes))
    label(closing_training_roster, text='手自排').grid(row=8, column=2, sticky='ws', padx=(10,0), pady=(50,0))
    transmission_type_code = combobox(closing_training_roster, values=transmission_type_codes, command=lambda x:on_transmission_type_code_changed(x, transmission_type_name, transmission_type_dict_c))
    transmission_type_code.grid(row=9, column=2, sticky='wen', padx=(10,0))
    transmission_type_name = combobox(closing_training_roster, values=transmission_type_names, command=lambda x:on_transmission_type_name_changes(x, transmission_type_code, transmission_type_dict_n))
    transmission_type_name.grid(row=9, column=3, sticky='wen', padx=10)
    transmission_type_code.set('')
    transmission_type_name.set('')

    def on_transmission_type_code_changed(select_code, transmission_type_name, transmission_type_dict):
        select_name = transmission_type_dict.get(select_code, "")
        transmission_type_name.set(select_name)

    def on_transmission_type_name_changes(select_name, transmission_type_code, transmission_type_dict):
        select_code = transmission_type_dict.get(select_name, "")
        transmission_type_code.set(select_code)

    # 退訓
    label(closing_training_roster, text='退訓').grid(row=9, column=0, sticky='ws', padx=(10,0), pady=(50,0))
    dropout = combobox(closing_training_roster, values=['是','否'], command=None)
    dropout.grid(row=10, column=0, sticky='wen', padx=(10,0))
    dropout.set('')

    # treeview
    global data_list
    columns = (
        'register_number', # 名冊號碼
        'batch', # 梯次
        'student_number', # 學員編號
        'student_name', # 學員姓名
        'dropout', # 退訓
        'transmission_type_code', # 手自排 編號
        'instructor_number', # 指導教練 編號
        'gender', # 學員性別
        'birth_date', # 出生日期
        'national_id_no', # 學員 身分證號碼
        'r_address_zip_code', # 戶籍地址區號
        'r_address_city_road', # 戶籍地址 ( 前面增加縣市區域，但不需要顯示 treeview )
        'learner_permit_date', # 學照日期
    )
    data_list = ttk.Treeview(closing_training_roster, show='headings', column = columns)
    
    data_list.heading('register_number', text='名冊號碼', anchor='center')
    data_list.heading('batch', text='梯次', anchor='center')
    data_list.heading('student_number', text='學員編號', anchor='center')
    data_list.heading('student_name', text='學員姓名', anchor='center')
    data_list.heading('dropout', text='退訓', anchor='center')
    data_list.heading('transmission_type_code', text='手自排', anchor='center')
    data_list.heading('instructor_number', text='教練', anchor='center')
    data_list.heading('gender', text='性別', anchor='center')
    data_list.heading('birth_date', text='出生日期', anchor='center')
    data_list.heading('national_id_no', text='身分證號', anchor='center')
    data_list.heading('r_address_zip_code', text='區號', anchor='center')
    data_list.heading('r_address_city_road', text='戶籍地址', anchor='center')
    data_list.heading('learner_permit_date', text='學照日期', anchor='center')

    data_list.column('register_number', width=50, anchor='center')
    data_list.column('batch', width=50, anchor='center')
    data_list.column('student_number', width=50, anchor='center')
    data_list.column('student_name', width=50, anchor='center')
    data_list.column('dropout', width=50, anchor='center')
    data_list.column('transmission_type_code', width=50, anchor='center')
    data_list.column('instructor_number', width=50, anchor='center')
    data_list.column('gender', width=50, anchor='center')
    data_list.column('birth_date', width=50, anchor='center')
    data_list.column('national_id_no', width=60, anchor='center')
    data_list.column('r_address_zip_code', width=50, anchor='center')
    data_list.column('r_address_city_road', width=250, anchor='center')
    data_list.column('learner_permit_date', width=50, anchor='center')
    
    data_list.grid(row=12, column=0, columnspan=4, sticky='wens', padx=10)

    # 創建水平捲軸
    h_scrollbar = ttk.Scrollbar(closing_training_roster, orient="horizontal", command=data_list.xview)
    data_list.configure(xscrollcommand=h_scrollbar.set)

    # 創建垂直捲軸
    v_scrollbar = ttk.Scrollbar(closing_training_roster, orient="vertical", command=data_list.yview)
    data_list.configure(yscrollcommand=v_scrollbar.set)

    # 使用 grid 布局管理器來排列 Treeview 和捲軸
    h_scrollbar.grid(row=13, column=0, columnspan=4, sticky="ew", padx=10)
    v_scrollbar.grid(row=12, column=4, rowspan=2, sticky="ns", pady=10)

    # 配置行和列的權重，使其在窗口調整大小時自動調整
    closing_training_roster.grid_rowconfigure(12, weight=1)
    closing_training_roster.grid_columnconfigure(0, weight=1)
    closing_training_roster.grid_columnconfigure(1, weight=1)
    closing_training_roster.grid_columnconfigure(2, weight=1)
    closing_training_roster.grid_columnconfigure(3, weight=1)
    
    # 邏輯功能 - 搜尋學員資料並顯示在 entry 
    def check_and_populate(identifier, value):
        if value == '':
            clear_all_fields()
        else:
            populate_student_data(identifier, value)

    def clear_all_fields():
        global current_student_id
        clear_entries_and_comboboxes(closing_training_roster, [register_term])
        current_student_id = None

    def populate_student_data(identifier, value):
        global current_student_id
        student_data = get_student_data(identifier, value)
        if student_data:
            # 獲取學員資料庫 id 序列
            current_student_id = student_data[0]
            # 學員編號
            student_number.delete(0, ctk.END)
            student_number.insert(0, student_data[5])
            # 學員姓名
            student_name.delete(0, ctk.END)
            student_name.insert(0, student_data[6])
            # 身分證號
            national_id_no.delete(0, ctk.END)
            national_id_no.insert(0, student_data[10])
            # 出生日期
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
            # 名冊號碼
            if student_data[34] is not None:
                register_number.delete(0, ctk.END)
                register_number.insert(0, student_data[34])
                # messagebox.showinfo('提示', '該學員已經存在名冊號碼')
            else:
                register_number.delete(0, ctk.END)
            # 期別
            if student_data[35] is not None:
                register_term.delete(0, ctk.END)
                register_term.insert(0, student_data[35])
            else:
                register_term.delete(0, ctk.END)
            # if student_data[35] is not None:
            #     register_term.set(student_data[35])
            # else:
            #     register_term.set('')
            # 退訓
            if student_data[33] is not None:
                dropout.set(student_data[33])
            else:
                dropout.set('')
            # 手自排
            if student_data[31] is not None:
                transmission_type_code.set(student_data[31])
            else:
                transmission_type_code.set('')
            # 手自排名稱
            if student_data[32] is not None:
                transmission_type_name.set(student_data[32])
            else:
                transmission_type_name.set('')
            # 指導教練編號
            if student_data[14] is not None:
                instructor_number.set(student_data[14])
            else:
                instructor_number.set('')
            # 指導教練名稱
            if student_data[15] is not None:
                instructor_name.set(student_data[15])
            else:
                instructor_name.set('')
            # 性別
            gender.configure(state='normal')
            gender.delete(0, ctk.END)
            gender.insert(0, student_data[16])
            gender.configure(state='readonly')
            # 梯次
            batch.configure(state='normal')
            batch.delete(0, ctk.END)
            batch.insert(0, student_data[7])
            batch.configure(state='readonly')
            # 名冊梯次
            register_batch.configure(state='normal')
            register_batch.delete(0, ctk.END)
            register_batch.insert(0, student_data[7])
            register_batch.configure(state='readonly')
            # 訓練班別代號
            training_type_code.configure(state='normal')
            training_type_code.delete(0, ctk.END)
            training_type_code.insert(0, student_data[3])
            training_type_code.configure(state='readonly')
            # 訓練班別名稱
            training_type_name.configure(state='normal')
            training_type_name.delete(0, ctk.END)
            training_type_name.insert(0, student_data[4])
            training_type_name.configure(state='readonly')
            # 戶籍地址 郵遞區號
            r_address_zip_code.configure(state='normal')
            r_address_zip_code.delete(0, ctk.END)
            r_address_zip_code.insert(0, student_data[19])
            r_address_zip_code.configure(state='readonly')
            # 戶籍地址 縣市區域
            r_address_city.configure(state='normal')
            r_address_city.delete(0, ctk.END)
            r_address_city.insert(0, student_data[20])
            r_address_city.configure(state='readonly')
            # 戶籍地址 地址
            r_address.configure(state='normal')
            r_address.delete(0, ctk.END)
            r_address.insert(0, student_data[21])
            r_address.configure(state='readonly')

    # 獲取輸入欄位信息
    def save_student_data():
        uid = 0
        global current_student_id
        student_data = {
            # 獲取輸入欄位呈現資料列表 treeview
            'register_number': register_number.get(), # 名冊號碼
            'batch': batch.get(), # 梯次
            'register_batch': register_batch.get(), # 名冊梯次
            'student_number': student_number.get(), # 學員編號
            'student_name': student_name.get(), # 姓名
            'gender': gender.get(), # 性別
            'birth_date': birth_date.get(), # 生日
            'national_id_no': national_id_no.get(), # 身分證字號
            'r_address_zip_code': r_address_zip_code.get(), # 戶籍地址 郵遞區號
            'r_address_city': r_address_city.get(), # 戶籍地址 縣市區域
            'r_address': r_address.get(), # 戶籍地址 地址
            'learner_permit_date': learner_permit_date.get(), # 學照日期
            'dropout': dropout.get(), # 退訓
            'register_term': register_term.get(), # 期別
            'transmission_type_code': transmission_type_code.get(), # 手自排
            'transmission_type_name': transmission_type_name.get(), # 手自排
            'instructor_number': instructor_number.get(), # 指導教練編號
            'instructor_name': instructor_name.get(), # 教練名稱
            'r_address_city_road': r_address_city.get() + r_address.get(), # 將縣市區域加上地址組合
            'id': current_student_id
        }

        # 格式化 learner_permit_date 日期
        formatted_learner_permit_date = student_data['learner_permit_date']
        if formatted_learner_permit_date and len(formatted_learner_permit_date) >= 6:
            year = formatted_learner_permit_date[:-4]
            month = formatted_learner_permit_date[-4:-2]
            day = formatted_learner_permit_date[-2:]
            formatted_learner_permit_date = f"{year} / {month} / {day}"

        # 驗證 名冊期別，來源，手自排，教練 輸入欄位是否為空
        required_fields = [
            'dropout',
            'register_term',
            'transmission_type_code',
            'transmission_type_name',
            'instructor_number',
            'instructor_name',
            'register_number'
        ]
        for field in required_fields:
            if not student_data[field]:
                messagebox.showwarning('提示', f'{validation_fields[field]} 欄位不能為空！')
                return
            
        if current_student_id is None:
            messagebox.showwarning('提示', '請先搜尋學員資料！')
            return

        update_student_data(student_data, uid=uid)
        clear_entries_and_comboboxes(closing_training_roster)
 
        # 讀取 save_student_data 的資料寫入 treeview
        data_list.insert('', 'end', values = (
            student_data['register_number'],
            student_data['batch'],
            student_data['student_number'],
            student_data['student_name'],
            student_data['dropout'], 
            student_data['transmission_type_code'],
            student_data['instructor_number'],
            student_data['gender'],
            student_data['birth_date'],
            student_data['national_id_no'],
            student_data['r_address_zip_code'],
            student_data['r_address_city_road'],
            # student_data['learner_permit_date'],
            formatted_learner_permit_date  # 使用格式化後的日期
        ))

    # 獲取輸入欄位中需要顯示在列印頁面上的信息:
    def get_treeview_data():
        data = []
        for item in data_list.get_children():
            values = data_list.item(item)['values']
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
                'gender': values[7], # 性別
                'birth_year': year, # 生日-年
                'birth_month': month, # 生日-月
                'birth_day': day, # 生日-日
                'national_id_no': values[9], # 身分證字號
                'r_address_city_road': values[11], # 地址
                'learner_permit_date': values[12], # 學照登錄日期
            })
        return data

    # 列印函式
    def print_html_report(for_dmv=True):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir = os.path.join(base_dir, "print")
        env = Environment(loader=FileSystemLoader(template_dir))

        # 根據 for_dmv 的值選擇不的列印模板
        if for_dmv:
            template = env.get_template("closing_training_roster.html")
        else:
            template = env.get_template("closing_training_roster_駕訓班公告.html")

        data = get_treeview_data()
        if not data:
            messagebox.showwarning("警告", "沒有數據可以打印")
            return
        elif not for_dmv:
            for item in data:
                item['national_id_no'] = '0000'

        # 讀取年度計畫表資料信息
        results = annual_plan_data()

        # 獲取 annual_plan 資料表的 training_type_name, term, batch, start_date, end_date 數據
        class_name = "佑名駕訓班"  # 请替换为实际的班名
        training_type_name = results[0][6] # 訓練班別名稱
        term = results[0][2] # 期別
        batch = results[0][4] # 梯次
        start_date = results[0][7] # 開訓日期
        end_date = results[0][8] # 結訓日期

        # 將開訓日期的值拆分成年月日
        if start_date and len(start_date) >= 6:
            start_year = start_date[:-4]
            start_month = start_date[-4:-2]
            start_day = start_date[-2:]
            start_date = f"{start_year} 年 {start_month} 月 {start_day} 日"

        # 將結訓日期的值拆分成年月日
        if end_date and len(end_date) >= 6:
            end_year = end_date[:-4]
            end_month = end_date[-4:-2]
            end_day = end_date[-2:]
            end_date = f"{end_year} 年 {end_month} 月 {end_day} 日"


        html_content = template.render(
            students=data,
            class_name=class_name,
            training_type_name=training_type_name,
            term=term,
            batch=batch,
            start_date=start_date,
            end_date=end_date,
            learner_permit_date=learner_permit_date
        )


        temp_html_path = os.path.join(base_dir, "print", "temp_closing_training_roster.html")
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

    # 按鈕
    btn(closing_training_roster, text='加入結訓名冊', command=save_student_data).grid(row=11, column=0, sticky='wen', padx=(10, 0), pady=10)
    export_btn(closing_training_roster, text='匯出文件', command=lambda: export_selected_data(data_list)).grid(row=11, column=1, sticky='wen', padx=(10, 0), pady=10)
    print_btn(closing_training_roster, text='列印結訓名冊(監理所用)', command=lambda: print_html_report(for_dmv=True)).grid(row=11, column=2, sticky='wen', padx=(10, 0), pady=10)
    print_btn(closing_training_roster, text='列印結訓名冊(駕訓班用)', command=lambda: print_html_report(for_dmv=False)).grid(row=11, column=3, sticky='wen', padx=10, pady=10)