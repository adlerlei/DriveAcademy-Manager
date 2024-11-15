# 開訓名冊作業 介面
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

def opening_training_roster(content):
    clear_frame(content)
    
    opening_training_roster = frame(content)
    opening_training_roster.columnconfigure(0, weight=1)
    opening_training_roster.columnconfigure(1, weight=1)
    opening_training_roster.columnconfigure(2, weight=1)
    opening_training_roster.columnconfigure(3, weight=1)
    opening_training_roster.place(relwidth=1, relheight=1)

    # 監聽 名冊號碼 register_number 輸入值
    def register_number_data_changed(choice):
        global counter, current_choice  # 使用全域變數
        
        # 檢查當前選擇的值是否改變
        if current_choice != choice:
            current_choice = choice
            counter = 1  # 重置計數器
        
        batch_value = batch.get()
        value = '0' + choice + batch_value + f'{counter:03d}'  # 格式化數字為位數
        register_number.delete(0, ctk.END)
        register_number.insert(0, value)
        counter += 1  # 計數器遞增

    # 顯示 / 搜尋 學員編號
    label(opening_training_roster, text='學員編號').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    student_number = entry(opening_training_roster,  placeholder_text = " 🔎")
    student_number.grid(row=1, column=0, sticky='wen', padx=(10,0))
    student_number.bind("<KeyRelease>", lambda event: check_and_populate('student_number', student_number.get()))

    # 顯示 / 搜尋 學員姓名
    label(opening_training_roster, text='學員姓名').grid(row=0, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    student_name = entry(opening_training_roster, placeholder_text=" 🔎")
    student_name.grid(row=1, column=1, sticky='wen', padx=(10,0))
    student_name.bind("<KeyRelease>", lambda event: check_and_populate('student_name', student_name.get()))

    # 顯示 / 搜尋 學員身分證號碼
    label(opening_training_roster, text='身分證號').grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    national_id_no = entry(opening_training_roster, placeholder_text=" 🔎")
    national_id_no.grid(row=1, column=2, sticky='wen', padx=(10,0))
    national_id_no.bind("<KeyRelease>", lambda event: check_and_populate('national_id_no', national_id_no.get()))

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
    register_number = entry(opening_training_roster, placeholder_text='此欄位自動生成，無須輸入')
    register_number.grid(row=3, column=1, sticky='wen',padx=(10,0))

    # 期別 ( 抓取年度計畫期別新增 "期別" 使用下拉選單呈現選擇) 不需要從資料庫讀取，但需要寫入資料庫
    term_data = get_term_data()
    label(opening_training_roster, text='期別').grid(row=2, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    register_term = combobox(opening_training_roster, values=term_data, command=register_number_data_changed)
    register_term.grid(row=3, column=2, sticky='wen',padx=(10,0))
    register_term.set('')  # 初始值設為空

    # 性別
    label(opening_training_roster, text='性別').grid(row=2, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    gender = display_entry_value(opening_training_roster)
    gender.grid(row=3, column=3, sticky='wen',padx=10)

    # 梯次
    label(opening_training_roster, text='梯次').grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    batch = display_entry_value(opening_training_roster)
    batch.grid(row=5, column=0, sticky='wen', padx=(10,0))

    # 名冊梯次 將梯次的值直接帶過來即可，不需要從資料庫讀取，但需要寫入資料庫
    label(opening_training_roster, text='名冊梯次').grid(row=4, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    register_batch = display_entry_value(opening_training_roster)
    register_batch.grid(row=5, column=1, sticky='wen', padx=(10,0))

    # 訓練班別
    label(opening_training_roster, text='訓練班別').grid(row=4, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    training_type_code = display_entry_value(opening_training_roster)
    training_type_code.grid(row=5, column=2, sticky='wen',padx=(10,0))
    training_type_name = display_entry_value(opening_training_roster)
    training_type_name.grid(row=5, column=3, sticky='wen',padx=10)

    # 戶籍地址
    label(opening_training_roster, text='戶籍地址').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    r_address_zip_code =  display_entry_value(opening_training_roster)
    r_address_zip_code.grid(row=7, column=0, sticky='wen',padx=(10,0))
    r_address_city = display_entry_value(opening_training_roster)
    r_address_city.grid(row=7, column=1, sticky='wen',padx=(10,0))
    r_address = display_entry_value(opening_training_roster)
    r_address.grid(row=7, column=2, columnspan=2, sticky='wen',padx=10)
    
    # 來源 下拉選單 ################################################
    exam_codes = ['A','B','C','G','Z']
    exam_names = ['新考','晉考','換考','吊扣註銷重考','臨時駕駛執照']
    # 使用 zip 函數生成字典來填充 exam_code
    exam_dict_c = dict(zip(exam_codes, exam_names))
    # 使用 zip 函數生成字典來填充 exam_name
    exam_dict_n = dict(zip(exam_names, exam_codes))

    label(opening_training_roster, text='來源').grid(row=8, column=0, sticky='ws', padx=(10,0), pady=(50,0))
    exam_code = combobox(opening_training_roster, values=exam_codes, command=lambda x: on_exam_code_changed(x, exam_name, exam_dict_c))
    exam_code.grid(row=9, column=0, sticky='wen', padx=(10,0))
    exam_name = combobox(opening_training_roster, values=exam_names, command=lambda x: on_exam_name_changed(x, exam_code, exam_dict_n))
    exam_name.grid(row=9, column=1, sticky='wen', padx=(10,0))
    exam_code.set('')
    exam_name.set('')

    # 來源拉選單監聽 code 改變時，自動更新 name 名稱
    def on_exam_code_changed(select_code, exam_name, exam_dict):
        select_name = exam_dict.get(select_code, "")
        exam_name.set(select_name)

    # 來源下拉選單監聽 name 改變時，自動更新 code 名稱
    def on_exam_name_changed(select_name, exam_code, exam_dict):
        select_code = exam_dict.get(select_name, "")
        exam_code.set(select_code)
    # 來源 下拉選單 END ##############################################

    # 手自排 下拉選單
    transmission_type_codes = ['M','A','S']
    transmission_type_names = ['手排','自排','特製車']
    transmission_type_dict_c = dict(zip(transmission_type_codes, transmission_type_names))
    transmission_type_dict_n = dict(zip(transmission_type_names, transmission_type_codes))
    label(opening_training_roster, text='手自排').grid(row=8, column=2, sticky='ws', padx=(10,0), pady=(50,0))
    transmission_type_code = combobox(opening_training_roster, values=transmission_type_codes, command=lambda x:on_transmission_type_code_changed(x, transmission_type_name, transmission_type_dict_c))
    transmission_type_code.grid(row=9, column=2, sticky='wen', padx=(10,0))
    transmission_type_name = combobox(opening_training_roster, values=transmission_type_names, command=lambda x:on_transmission_type_name_changes(x, transmission_type_code, transmission_type_dict_n))
    transmission_type_name.grid(row=9, column=3, sticky='wen', padx=10)
    transmission_type_code.set('')
    transmission_type_name.set('')

    def on_transmission_type_code_changed(select_code, transmission_type_name, transmission_type_dict):
        select_name = transmission_type_dict.get(select_code, "")
        transmission_type_name.set(select_name)

    def on_transmission_type_name_changes(select_name, transmission_type_code, transmission_type_dict):
        select_code = transmission_type_dict.get(select_name, "")
        transmission_type_code.set(select_code)


    # 教練 下拉選單 #################################################
    # 獲得教練資料庫資料
    instructor_numbers, instructor_names, instructor_dict = get_instructor_data()
    label(opening_training_roster, text='指導教練').grid(row=10, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    instructor_number = combobox(opening_training_roster, values=instructor_numbers, command=lambda x: on_instructor_number_changed(x, instructor_name, instructor_dict))
    instructor_number.grid(row=11, column=0, sticky='wen', padx=(10,0))
    instructor_name = combobox(opening_training_roster, values=instructor_names, command=lambda x: on_instructor_name_changed(x, instructor_number, instructor_dict))
    instructor_name.grid(row=11, column=1, sticky='wen', padx=(10,0))
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

    # 教練 下拉選單 END #################################################


    # treeview
    global data_list
    columns = (
        'register_number', # 名冊號碼
        'batch', # 梯次
        'student_number', # 學員編號
        'student_name', # 學員姓名
        'exam_code', # 來源 編號
        'transmission_type_code', # 手自排 編號
        'instructor_number', # 指導教練 編號
        'gender', # 學員性別
        'birth_date', # 出生日期
        'national_id_no', # 學員 身分證號碼
        'r_address_zip_code', # 戶籍地址區號
        'r_address_city_road', # 戶籍地址 ( 前面增加縣市區域，但不需要顯示 treeview )
        'learner_permit_date', # 學照日期
        'training_type_code' # 訓練班別代號 (隱藏列)
    )
    data_list = ttk.Treeview(opening_training_roster, show='headings', column = columns)
    
    data_list.heading('register_number', text='名冊號碼', anchor='center')
    data_list.heading('batch', text='梯次', anchor='center')
    data_list.heading('student_number', text='學員編號', anchor='center')
    data_list.heading('student_name', text='學員姓名', anchor='center')
    data_list.heading('exam_code', text='來源', anchor='center') 
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
    data_list.column('exam_code', width=50, anchor='center')
    data_list.column('transmission_type_code', width=50, anchor='center')
    data_list.column('instructor_number', width=50, anchor='center')
    data_list.column('gender', width=50, anchor='center')
    data_list.column('birth_date', width=50, anchor='center')
    data_list.column('national_id_no', width=60, anchor='center')
    data_list.column('r_address_zip_code', width=50, anchor='center')
    data_list.column('r_address_city_road', width=250, anchor='center')
    data_list.column('learner_permit_date', width=50, anchor='center')
    data_list.column('training_type_code', width=0, stretch=0)
    
    data_list.grid(row=13, column=0, columnspan=4, sticky='wens', padx=10, pady=10)

    # 創建水平捲軸
    h_scrollbar = ttk.Scrollbar(opening_training_roster, orient="horizontal", command=data_list.xview)
    data_list.configure(xscrollcommand=h_scrollbar.set)

    # 創建垂直捲軸
    v_scrollbar = ttk.Scrollbar(opening_training_roster, orient="vertical", command=data_list.yview)
    data_list.configure(yscrollcommand=v_scrollbar.set)

    # 使用 grid 布局管理器來排列 Treeview 和捲軸
    h_scrollbar.grid(row=14, column=0, columnspan=4, sticky="ew", padx=10)
    v_scrollbar.grid(row=13, column=4, rowspan=2, sticky="ns", pady=10)

    # 配置行和列的權重，使其在窗口調整大小時自動調整
    opening_training_roster.grid_rowconfigure(13, weight=1)
    opening_training_roster.grid_columnconfigure(0, weight=1)
    opening_training_roster.grid_columnconfigure(1, weight=1)
    opening_training_roster.grid_columnconfigure(2, weight=1)
    opening_training_roster.grid_columnconfigure(3, weight=1)
    
    # 邏輯功能 - 搜尋學員資料並顯示在 entry 
    def check_and_populate(identifier, value):
        if value == '':
            clear_all_fields()
        else:
            populate_student_data(identifier, value)

    def clear_all_fields():
        global current_student_id
        clear_entries_and_comboboxes(opening_training_roster, [register_term])
        current_student_id = None

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
            learner_permit_date.configure(state='normal')
            learner_permit_date.delete(0, ctk.END)

            if student_data[26] is not None:
                learner_permit_date.insert(0, student_data[26])
            else:
                learner_permit_date.insert(0, '')

            if student_data[34] is not None:
                register_number.insert(0, student_data[34])
                # messagebox.showinfo('提示用戶', '該學員已經存在名冊號碼')
            else:
                register_number.insert(0, '')

            if student_data[35] is not None:
                register_term.set(student_data[35])
            else:
                register_term.set('')

            if student_data[29] is not None:
                exam_code.set(student_data[29])
            else:
                exam_code.set('')

            if student_data[30] is not None:
                exam_name.set(student_data[30])
            else:
                exam_name.set('')

            if student_data[31] is not None:
                transmission_type_code.set(student_data[31])
            else:
                transmission_type_code.set('')

            if student_data[32] is not None:
                transmission_type_name.set(student_data[32])
            else:
                transmission_type_name.set('')

            if student_data[14] is not None:
                instructor_number.set(student_data[14])
            else:
                instructor_number.set('')

            if student_data[15] is not None:
                instructor_name.set(student_data[15])
            else:
                instructor_name.set('')

            gender.configure(state='normal')
            gender.delete(0, ctk.END)
            gender.insert(0, student_data[16])
            gender.configure(state='readonly')

            batch.configure(state='normal')
            batch.delete(0, ctk.END)
            batch.insert(0, student_data[7])
            batch.configure(state='readonly')

            register_batch.configure(state='normal')
            register_batch.delete(0, ctk.END)

            if student_data[8] is not None:
                register_batch.insert(0, student_data[8])
            else:
                register_batch.insert(0, '')
            register_batch.configure(state='readonly')

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


    # 獲取輸入欄位信息
    def save_student_data():
        uid = 1
        global current_student_id
        student_data = {
            'register_number': register_number.get(),
            'batch': batch.get(),
            'register_batch': register_batch.get(),
            'student_number': student_number.get(),
            'student_name': student_name.get(),
            'gender': gender.get(),
            'birth_date': birth_date.get(),
            'national_id_no': national_id_no.get(),
            'r_address_zip_code': r_address_zip_code.get(),
            'r_address_city': r_address_city.get(),
            'r_address': r_address.get(),
            'learner_permit_date': learner_permit_date.get(),
            'exam_code': exam_code.get(),
            'exam_name': exam_name.get(),
            'register_term': register_term.get(),
            'transmission_type_code': transmission_type_code.get(),
            'transmission_type_name': transmission_type_name.get(),
            'instructor_number': instructor_number.get(),
            'instructor_name': instructor_name.get(),
            'r_address_city_road': r_address_city.get() + r_address.get(),
            'training_type_code': training_type_code.get(),
            'id': current_student_id
        }


        required_fields = [ 
            'exam_code',
            'exam_name',
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
        clear_entries_and_comboboxes(opening_training_roster)

        data_list.insert('', 'end', values = (
            student_data['register_number'],
            student_data['batch'],
            student_data['student_number'],
            student_data['student_name'],
            student_data['exam_code'],
            student_data['transmission_type_code'],
            student_data['instructor_number'],
            student_data['gender'],
            student_data['birth_date'],
            student_data['national_id_no'],
            student_data['r_address_zip_code'],
            student_data['r_address_city_road'],
            student_data['learner_permit_date'],
            student_data['training_type_code']
        ))

    # 新增函示以獲取所有新增到 treeview 的學員 ID
    def get_all_added_student_ids():
        all_ids = []  # 用於存儲所有新增學員的 ID
        for item in data_list.get_children():  # 獲取所有項目
            all_ids.append(data_list.item(item)['values'][0])  # 假設學員 ID 在第一列
        return all_ids
    
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
                    print(f"轉換後的日期: {year}年{month}月{day}日")  # 調試輸出
                else:
                    year, month, day = '-', '-', '-'
                    print("無效的月份或日期")
            else:
                year, month, day = '-', '-', '-'
                print("日期格式不符合要求")
            
            data.append({
                'student_number': values[2],
                'student_name': values[3],
                'gender': values[7],
                'birth_year': year,
                'birth_month': month,
                'birth_day': day,
                'national_id_no': values[9],
                'r_address_city_road': values[11],
                'register_number': values[0],
            })
        return data
    
    # 列印函式
    def print_html_report(for_dmv=True):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir = os.path.join(base_dir, "print")
        env = Environment(loader=FileSystemLoader(template_dir))

        # 根據 for_dmv 的值選擇不同的列印模板
        if for_dmv:
            template = env.get_template("opening_training_rester.html")
        else:
            template = env.get_template("opening_training_rester_駕訓班公告.html")

        data = get_treeview_data()
        if not data:
            messagebox.showwarning("警告", "沒有數據可以打印")
            return
        elif not for_dmv:
            for item in data:
                item['national_id_no'] = '0000'

        # 讀取年度計畫表資
        results = annual_plan_data()

        # 獲取 annual_plan 資料表的 training_type_name, term, batch, start_date, end_date 數據
        class_name = "佑名駕訓班"  # 请替换为实际的班名
        training_type_name = results[0][6] 
        term = results[0][2]
        batch = results[0][4]
        start_date = results[0][7]
        end_date = results[0][8]
        

        html_content = template.render(
            students=data,
            class_name=class_name,
            training_type_name=training_type_name,
            term=term,
            batch=batch,
            start_date=start_date,
            end_date=end_date
        )

        temp_html_path = os.path.join(base_dir, "print", "temp_opening_training_rester.html")
        with open(temp_html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        webbrowser.open_new_tab(f'file://{temp_html_path}')

        # 等待瀏覽器加載
        time.sleep(3) 
        # 模擬鍵盤操作觸發打印 (Ctrl+P)
        # 每個按鍵之間延遲0.1秒
        pyautogui.hotkey('ctrl', 'p', interval=0.1)
        # 每個按鍵之間延遲0.1秒
        # pyautogui.hotkey('command', 'p', interval=0.1)
        # 等待打印窗口出現
        time.sleep(2)
        # 模擬鍵盤操作確認打印 (Enter)
        # pyautogui.press('enter')

        # 删除临时文件
        time.sleep(1)  # 等待打印完成
        os.remove(temp_html_path)



        

    # 按鈕
    btn(opening_training_roster, text='加入開訓名冊', command=save_student_data).grid(row=11, column=2, sticky='wen', padx=(10, 0))
    print_btn(opening_training_roster, text='列印開訓名冊(駕訓班用)', command=lambda: print_html_report(for_dmv=False)).grid(row=12, column=0, columnspan=2, sticky='wen', padx=(10,0), pady=10)
    print_btn(opening_training_roster, text='列印開訓名冊(監理站用)', command=lambda: print_html_report(for_dmv=True)).grid(row=12, column=2, columnspan=2, sticky='wen', padx=10, pady=10)
    export_btn(opening_training_roster, text='匯出文件', command=lambda: export_selected_data(data_list)).grid(row=11, column=3, sticky='wen', padx=10)