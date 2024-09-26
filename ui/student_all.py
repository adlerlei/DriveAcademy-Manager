# 學員資料作業 介面
# 對應介面 models/student.py
from utils.widget import *
from utils.config import *
from models.student import *
from tkinter import messagebox
import customtkinter as ctk

is_editing = False # 用來判斷用戶新增還是修改學員資料
current_student_id = None # 抓取 id 學員欄位

def student_all(content):
    global is_editing, current_student_id, is_adding_new, is_searching
    is_editing = False
    current_student_id = None
    is_adding_new = False  # 新增一个标志来表示是否正在添加新学员
    is_searching = False  # 新增一个标志来表示是否正在搜索
    
    clear_frame(content)

    student_all = frame(content)
    student_all.columnconfigure(0, weight=1)
    student_all.columnconfigure(1, weight=1)
    student_all.columnconfigure(2, weight=1)
    student_all.columnconfigure(3, weight=1)
    student_all.place(relwidth=1, relheight=1)

    # 訓練班別
    training_type_codes = ['1', '2', '3', '4', '5', '6', '7', '8']
    training_type_names = ['普通小型車班', '大貨車班', '大客車班', '聯結車班', '職業小型車班', '普通重機車班', '大型重機車班', '小型車逕升大客車班']
    training_type_dict_c = dict(zip(training_type_codes, training_type_names))
    training_type_dict_n = dict(zip(training_type_names, training_type_codes))
    training_type_dict = dict(zip(training_type_codes, training_type_names))
    label(student_all, text='訓練班別').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    training_type_code = combobox(student_all, values=training_type_codes, command=lambda x: on_training_type_code_changed(x, training_type_name, training_type_dict_c))
    training_type_code.grid(row=1, column=0, sticky='wen', padx=(10,0))
    training_type_name = combobox(student_all, values=training_type_names, command=lambda x: on_training_type_name_changed(x, training_type_code, training_type_dict_n))
    training_type_name.grid(row=1, column=1, sticky='wen', padx=(10,0))

    def on_training_type_code_changed(selected_code, training_type_name, training_type_dict):
        selected_name = training_type_dict.get(selected_code, "")
        training_type_name.set(selected_name)

    def on_training_type_name_changed(selected_name, training_type_code, training_type_dict):
        selected_code = training_type_dict.get(selected_name, "")
        training_type_code.set(selected_code)

    # 考照類別
    license_type_codes = ['0', '1', '2', '3', '4', '5', '6', '7']
    license_type_names = ['自用小客車', '職業小客車', '自用大貨車', '職業大貨車', '自用大客車', '職業大客車', '自用聯結車', '職業聯結車']
    license_type_dict_c = dict(zip(license_type_codes, license_type_names))
    license_type_dict_n = dict(zip(license_type_names, license_type_codes))
    label(student_all, text='考照類別').grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    license_type_code = combobox(student_all,  values=license_type_codes, command=lambda x: on_license_type_code_changed(x, license_type_name, license_type_dict_c))
    license_type_code.grid(row=3, column=0, sticky='wen', padx=(10,0))
    license_type_name = combobox(student_all, values=license_type_names, command=lambda x: on_license_type_name_changed(x, license_type_code, license_type_dict_n))
    license_type_name.grid(row=3, column=1, sticky='wen', padx=(10,0))

    # 考照類別下拉選單監聽 code 改變時，自動更新 name 名稱
    def on_license_type_code_changed(selected_code, license_type_name, license_type_dict):
        selected_name = license_type_dict.get(selected_code, "")
        license_type_name.set(selected_name)

    def on_license_type_name_changed(selected_name, license_type_code, license_type_dict):
        selected_code = license_type_dict.get(selected_name, "")
        license_type_code.set(selected_code)


    # 學員編號
    label(student_all, text='學員編號').grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    student_number = entry(student_all, placeholder_text='編號查詢')
    student_number.grid(row=5, column=0, sticky='wen', padx=(10,0))
    student_number.bind("<FocusOut>", lambda event: check_and_populate('student_number', student_number.get()))


    # 梯次
    label(student_all, text='梯次').grid(row=4, column=1, sticky='ws',padx=(10,0), pady=(20,0))
    batch = combobox(student_all, values=['A', 'B'])
    batch.grid(row=5, column=1, sticky='wen', padx=(10,0))
    batch.set('')


    # 學員姓名
    label(student_all, text='學員姓名').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    student_name = entry(student_all, placeholder_text='姓名查詢')
    student_name.grid(row=7, column=0, sticky='wen', padx=(10,0))
    student_name.bind("<FocusOut>", lambda event: check_and_populate('student_name', student_name.get()))

    # 身分證號碼
    label(student_all, text='身分證號碼').grid(row=6, column=1, sticky='ws', padx=(10,0), pady=(20,0))
    national_id_no = entry(student_all, placeholder_text='身分證號查詢')
    national_id_no.grid(row=7, column=1, sticky='wen', padx=(10,0))
    national_id_no.bind("<FocusOut>", lambda event: check_and_populate('national_id_no', national_id_no.get()))


    # 出生日期
    label(student_all, text='出生日期').grid(row=8, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    birth_date = entry(student_all)
    birth_date.grid(row=9, column=0, sticky='wen', padx=(10,0))


    # 行動電話
    label(student_all, text='手機').grid(row=8, column=1, sticky='ws', padx=(10,0), pady=(20,0))
    mobile_phone = entry(student_all, placeholder_text='手機查詢')
    mobile_phone.grid(row=9, column=1, sticky='wen', padx=(10,0))
    mobile_phone.bind("<FocusOut>", lambda event: check_and_populate('mobile_phone', mobile_phone.get()))


    # 戶籍地址
    r_address_zip_code_lists, r_address_city_lists, r_address_dict = address_data()
    label(student_all, text='戶籍地址').grid(row=10, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    r_address_zip_code = combobox(student_all, values=r_address_zip_code_lists, command=lambda x: on_r_address_zip_change(x, r_address_city, r_address_dict))
    r_address_zip_code.grid(row=11, column=0, sticky='wen', padx=(10,0))
    r_address_city = combobox(student_all, values=r_address_city_lists, command=lambda x: on_r_address_city_change(x, r_address_zip_code, r_address_dict))
    r_address_city.grid(row=11, column=1, sticky='wen', padx=(10,0))
    r_address = entry(student_all)
    r_address.grid(row=12, column=0, columnspan=2, sticky='wen', padx=(10,0))
    r_address_zip_code.set('')
    r_address_city.set('')

    # 戶籍地址監聽 zip code 改變時，自動更新 city 城市
    def on_r_address_zip_change(select_number, r_address_city, address_dict):
        selected_city = address_dict.get(select_number, "")
        r_address_city.set(selected_city)

    def on_r_address_city_change(select_city, r_address_number, address_dict):
        selected_number = next((number for number, city in address_dict.items() if city == select_city), "")
        r_address_number.set(selected_number)


    # 家用電話
    label(student_all, text='室內電話').grid(row=0, column=2, sticky='ws', padx=(10,0))
    home_phone = entry(student_all)
    home_phone.grid(row=1, column=2, columnspan=2, sticky='wen', padx=10)


    # 性別
    label(student_all, text='性別').grid(row=2, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    gender = combobox(student_all, values=['男', '女'])
    gender.grid(row=3, column=2, sticky='wen', padx=(10,0))
    gender.set('')


    # 學歷 
    label(student_all, text='學歷').grid(row=2, column=3, sticky='ws', pady=(20,0))
    education = combobox(student_all, values=['學前教育','國小','國中','高中','專科','大學','碩士','博士'])
    education.grid(row=3, column=3, sticky='wen', padx=10)
    education.set('')


    # 獲教練資料
    instructor_numbers, instructor_names, instructor_dict = get_instructor_data()
    label(student_all, text='指導教練').grid(row=4, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    instructor_number = combobox(student_all, values=instructor_numbers, command=lambda x: on_instructor_number_changed(x, instructor_name, instructor_dict))
    instructor_number.grid(row=5, column=2, sticky='wen', padx=(10,0))
    instructor_name = combobox(student_all, values=instructor_names, command=lambda x: on_instructor_name_changed(x, instructor_number, instructor_dict))
    instructor_name.grid(row=5, column=3, sticky='wen', padx=10)
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


    # 信箱
    label(student_all, text='電子郵件').grid(row=6, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    email = entry(student_all)
    email.grid(row=7, column=2, columnspan=2, sticky='wen', padx=10)

    # 備註
    label(student_all, text='備註').grid(row=8, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    remarks = entry(student_all)
    remarks.grid(row=9, column=2, columnspan=2, sticky='wen', padx=10)


    # 通訊地址
    m_address_zip_code_lists, m_address_city_lists, m_address_dict = address_data()
    label(student_all, text='通訊地址').grid(row=10, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    m_address_zip_code = combobox(student_all, values=m_address_zip_code_lists, command=lambda x: on_m_address_zip_change(x, m_address_city, m_address_dict))
    m_address_zip_code.grid(row=11, column=2, sticky='wen', padx=(10,0))
    m_address_city = combobox(student_all, values=m_address_city_lists, command=lambda x: on_m_address_city_change(x, m_address_zip_code, m_address_dict))
    m_address_city.grid(row=11, column=3, sticky='wen', padx=10)
    m_address = entry(student_all)
    m_address.grid(row=12, column=2, columnspan=2, sticky='wen', padx=10)
    m_address_zip_code.set('')
    m_address_city.set('')

    # 通訊地址監聽 zip code 改變時，自動更新 city 城市
    def on_m_address_zip_change(zip_code, m_address_city, address_dict):
        selected_city = address_dict.get(zip_code, "")
        m_address_city.set(selected_city)

    def on_m_address_city_change(select_city, m_address_zip_code, address_dict):
        selected_zip_code = next((zip_code for zip_code, city in address_dict.items() if city == select_city), "")
        m_address_zip_code.set(selected_zip_code)


    label(student_all, text='該學員是否退訓').grid(row=14, column=0, sticky='ws', padx=(10,0))
    dropout = display_entry_value(student_all)
    dropout.grid(row=15, column=0, sticky='wen', padx=(10,0))

    label(student_all, text='名冊號碼').grid(row=14, column=1, sticky='ws', padx=(10,0))
    register_number = display_entry_value(student_all)
    register_number.grid(row=15, column=1, sticky='wen', padx=(10,0))

    label(student_all, text='學照日期').grid(row=14, column=2, sticky='ws', padx=(10,0))
    learner_permit_date = display_entry_value(student_all)
    learner_permit_date.grid(row=15, column=2, sticky='wen', padx=(10,0))

    label(student_all, text='學照號碼').grid(row=14, column=3, sticky='ws', padx=(10,0))
    learner_permit_number = display_entry_value(student_all)
    learner_permit_number.grid(row=15, column=3, sticky='wen', padx=10)

    label(student_all, text='路試日期').grid(row=16, column=0, sticky='ws', padx=(10,0))
    road_test_date = display_entry_value(student_all)
    road_test_date.grid(row=17, column=0, sticky='wen', padx=(10,0))

    label(student_all, text='建檔日期').grid(row=16, column=1, sticky='ws', padx=(10,0))
    creation_date = display_entry_value(student_all)
    creation_date.grid(row=17, column=1, sticky='wen', padx=(10,0))


    # 學員資料顯示在輸入欄位�� 
    def check_and_populate(identifier, value):
        global is_searching
        if not is_adding_new and value and len(value) >= 1:  # 只有当输入至少3个字符时才搜索
            is_searching = True
            populate_student_data(identifier, value)
        elif not is_adding_new and not value:
            clear_all_fields()
        is_searching = False

    def clear_all_fields():
        global is_editing, current_student_id, is_adding_new
        if not is_adding_new:
            clear_entries_and_comboboxes(student_all)
            is_editing = False
            current_student_id = None

    def populate_student_data(identifier, value):
        global is_editing, current_student_id, is_searching
        if not is_searching:
            return
        
        student_data = get_student_data(identifier, value)
        
        if student_data is None:
            return
        
        is_editing = True
        current_student_id = student_data[0]
        
        # 填充所有字段
        training_type_code.set(student_data[3])
        training_type_name.set(student_data[4])
        license_type_code.set(student_data[1])
        license_type_name.set(student_data[2])
        student_number.delete(0, ctk.END)
        student_number.insert(0, student_data[5])
        batch.set(student_data[7])
        student_name.delete(0, ctk.END)
        student_name.insert(0, student_data[6])
        national_id_no.delete(0, ctk.END)
        national_id_no.insert(0, student_data[10])
        birth_date.delete(0, ctk.END)
        birth_date.insert(0, student_data[9])
        mobile_phone.delete(0, ctk.END)
        mobile_phone.insert(0, student_data[11])
        r_address_zip_code.set(student_data[19])
        r_address_city.set(student_data[20])
        r_address.delete(0, ctk.END)
        r_address.insert(0, student_data[21])
        home_phone.delete(0, ctk.END)
        home_phone.insert(0, student_data[12])
        gender.set(student_data[16])
        education.set(student_data[13])
        instructor_number.set(student_data[14])
        instructor_name.set(student_data[15])
        email.delete(0, ctk.END)
        email.insert(0, student_data[17])
        remarks.delete(0, ctk.END)
        remarks.insert(0, student_data[18])
        m_address_zip_code.set(student_data[22])
        m_address_city.set(student_data[23])
        m_address.delete(0, ctk.END)
        m_address.insert(0, student_data[24])

        # 学照日期
        learner_permit_date.configure(state='normal')
        learner_permit_date.delete(0, ctk.END)
        if student_data[26]:
            learner_permit_date.insert(0, student_data[26])
        else:
            learner_permit_date.insert(0, '')
        learner_permit_date.configure(state='readonly')

        # 学照号码
        learner_permit_number.configure(state='normal')
        learner_permit_number.delete(0, ctk.END)
        if student_data[27]:
            learner_permit_number.insert(0, student_data[27])
        else:
            learner_permit_number.insert(0, '')
        learner_permit_number.configure(state='readonly')

        # 是否退训
        dropout.configure(state='normal')
        dropout.delete(0, ctk.END)
        if student_data[33]:
            dropout.insert(0, student_data[33])
        else:
            dropout.insert(0, '')
        dropout.configure(state='readonly')
                
        # 名册号码
        register_number.configure(state='normal')
        register_number.delete(0, ctk.END)
        if student_data[34]:
            register_number.insert(0, student_data[34])
        register_number.configure(state='readonly')

        # 路试日期
        road_test_date.configure(state='normal')
        road_test_date.delete(0, ctk.END)
        if student_data[38]:
            road_test_date.insert(0, student_data[38])
        else:
            road_test_date.insert(0, '')
        road_test_date.configure(state='readonly')

        # 建档日期
        creation_date.configure(state='normal')
        creation_date.delete(0, ctk.END)
        if len(student_data) > 45 and student_data[45]:
            creation_date.insert(0, student_data[45])
        else:
            creation_date.insert(0, '')
        creation_date.configure(state='readonly')

    # 獲取輸入欄位信息
    def get_data_and_insert():
        global is_editing, current_student_id, is_adding_new
        is_adding_new = True  # 设置标志，表示正在添加新学员
        student_data = {
            'training_type_code': training_type_code.get(),
            'training_type_name': training_type_name.get(),
            'license_type_code': license_type_code.get(),
            'license_type_name': license_type_name.get(),
            'student_number': student_number.get(),
            'batch': batch.get(),
            'student_name': student_name.get(),
            'national_id_no': national_id_no.get(),
            'birth_date': birth_date.get(),
            'mobile_phone': mobile_phone.get(),
            'r_address_zip_code': r_address_zip_code.get(),
            'r_address_city': r_address_city.get(),
            'r_address': r_address.get(),
            'home_phone': home_phone.get(),
            'gender': gender.get(),
            'education': education.get(),
            'instructor_number': instructor_number.get(),
            'instructor_name': instructor_name.get(),
            'email': email.get(),
            'remarks': remarks.get(),
            'm_address_zip_code': m_address_zip_code.get(),
            'm_address_city': m_address_city.get(),
            'm_address': m_address.get(),
        }


        # 驗證必填欄位是否空
        required_fields = ['training_type_code', 'training_type_name', 'license_type_code', 'license_type_name', 
                        'student_number', 'student_name', 'batch', 'national_id_no', 'birth_date','r_address_zip_code', 'r_address_city', 'r_address','email']
        for field in required_fields:
            if not student_data[field]:
                messagebox.showwarning('提示', f'{validation_fields[field]} 欄位不能為空！')
                is_adding_new = False  # 重置标志
                return
        
        # 如果是編輯模式，提示使用者無法新增
        if is_editing:
            messagebox.showinfo('提示', '無法新增學員，請使用 "修改" 功能。')
            is_adding_new = False  # 重置标志
            return

        insert_student_data(student_data)

        # 清空字段，但保留某些字段
        keep_entries = [training_type_code, training_type_name, license_type_code, license_type_name]
        clear_entries_and_comboboxes(student_all, keep_entries)
        is_adding_new = False  # 重置标志

    # 修改按的事件處理函數
    def update_student():
        global is_editing, current_student_id
        
        if current_student_id is None:
            messagebox.showwarning('提示', '請先查詢並選擇要修改的學員資料。')
            return
        
        confirm = messagebox.askyesno('確定', '確定要修改此學員資料嗎？')
        if not confirm:
            return
        
        student_data = {
            'training_type_code': training_type_code.get(),
            'training_type_name': training_type_name.get(),
            'license_type_code': license_type_code.get(),
            'license_type_name': license_type_name.get(),
            'student_number': student_number.get(),
            'batch': batch.get(),
            'student_name': student_name.get(),
            'national_id_no': national_id_no.get(),
            'birth_date': birth_date.get(),
            'mobile_phone': mobile_phone.get(),
            'r_address_zip_code': r_address_zip_code.get(),
            'r_address_city': r_address_city.get(),
            'r_address': r_address.get(),
            'home_phone': home_phone.get(),
            'gender': gender.get(),
            'education': education.get(),
            'instructor_number': instructor_number.get(),
            'instructor_name': instructor_name.get(),
            'email': email.get(),
            'remarks': remarks.get(),
            'm_address_zip_code': m_address_zip_code.get(),
            'm_address_city': m_address_city.get(),
            'm_address': m_address.get(),
            'id': current_student_id
        }
        
        update_student_data(student_data)
        
        # 更新成功后，保持编辑状态
        # 清空字段，但保留某些字段
        keep_entries = [training_type_code, training_type_name, license_type_code, license_type_name]
        clear_entries_and_comboboxes(student_all, keep_entries)
        is_editing = True

    # 刪除按鈕的事件處理函數
    def delete_student():
        global is_editing, current_student_id
        if current_student_id:
            confirm = messagebox.askyesno('確認', '此動作無法原！確定要刪除此學員？')
            if confirm:
                delete_student_data(current_student_id)
                is_editing = False
                current_student_id = None

                # clear_entries_and_comboboxes(student_all)
                # 清空字段，但保留某些字段
                keep_entries = [training_type_code, training_type_name, license_type_code, license_type_name]
                clear_entries_and_comboboxes(student_all, keep_entries)

        else:
            messagebox.showwarning('提示', '請先輸入要刪除的學員資料！')

    # 修改按钮配置
    add_btn(student_all, text='新增', command=get_data_and_insert).grid(row=13, column=1, sticky='wen', padx=(10,0), pady=20)
    modify_btn(student_all, text='修改', command=update_student).grid(row=13, column=2, sticky='wen', padx=(10,0), pady=20)
    delete_btn(student_all, text='刪除', command=delete_student).grid(row=13, column=3, sticky='wen', padx=10, pady=20)