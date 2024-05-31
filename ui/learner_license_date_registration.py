# 學照登錄介面
from utils.widget import *
from utils.config import * 
from models.license import *
import customtkinter as ctk
from tkinter import messagebox

# 檢測學員資料庫 id 欄位來判定是否修改或新增
current_student_id = None

def learner_license_date_registration(content):
    clear_frame(content)
        
    learner_license_date_registration = frame(content)
    learner_license_date_registration.columnconfigure(0, weight=1)
    learner_license_date_registration.columnconfigure(1, weight=1)
    learner_license_date_registration.columnconfigure(2, weight=1)
    learner_license_date_registration.columnconfigure(3, weight=1)
    learner_license_date_registration.place(relwidth=1, relheight=1)

    # 顯示學員編號
    label(learner_license_date_registration, text='學員編號').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    student_number = entry(learner_license_date_registration, placeholder_text="輸入學員編號查詢")
    student_number.grid(row=1, column=0, sticky='wen', padx=10)
    student_number.bind("<KeyRelease>", lambda event: populate_student_data('student_number', student_number.get()))

    # 顯示學員姓名
    label(learner_license_date_registration, text='學員姓名').grid(row=0, column=1, sticky='ws', pady=(10,0))
    student_name = display_entry_value(learner_license_date_registration)
    student_name.grid(row=1, column=1, sticky='wen', padx=(0,10))

    # 顯示學員身分證號碼
    label(learner_license_date_registration, text='身分證號').grid(row=0, column=2, sticky='ws',pady=(10,0))
    national_id_no = display_entry_value(learner_license_date_registration)
    national_id_no.grid(row=1, column=2, sticky='wen', padx=(0,10))

    # 顯示學員電話
    label(learner_license_date_registration, text='聯絡手機').grid(row=0, column=3, sticky='ws', pady=(10,0))
    mobile_phone = display_entry_value(learner_license_date_registration)
    mobile_phone.grid(row=1, column=3, sticky='wen', padx=(0,10))

    # 顯示學員出生日期
    label(learner_license_date_registration, text='出生日期').grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    birth_date = display_entry_value(learner_license_date_registration)
    birth_date.grid(row=3, column=0, sticky='wen', padx=10)

    # 顯示考照類別
    label(learner_license_date_registration, text='考照類別').grid(row=2, column=1, sticky='ws', pady=(10,0))
    license_type_code = display_entry_value(learner_license_date_registration)
    license_type_code.grid(row=3, column=1, sticky='wen', padx=(0,10))
    license_type_name = display_entry_value(learner_license_date_registration)
    license_type_name.grid(row=3, column=2, sticky='wen', padx=(0,10))

    # 顯示備註
    label(learner_license_date_registration, text='備註').grid(row=2, column=3, sticky='ws',pady=(10,0))
    remarks = display_entry_value(learner_license_date_registration)
    remarks.grid(row=3, column=3, sticky='wen', padx=(0,10))

    # 顯示戶籍地址
    label(learner_license_date_registration, text='戶籍地址').grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    r_address_zip_code = display_entry_value(learner_license_date_registration)
    r_address_zip_code.grid(row=5, column=0, sticky='wen', padx=10)
    r_address_city = display_entry_value(learner_license_date_registration)
    r_address_city.grid(row=5, column=1, sticky='wen', padx=(0,10))
    r_address = display_entry_value(learner_license_date_registration)
    r_address.grid(row=5, column=2, columnspan=2, sticky='wen', padx=(0,10))
    
    # 輸入登錄日期
    label(learner_license_date_registration, text='登錄日期：').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(50,0))
    learner_permit_login_data = entry(learner_license_date_registration)
    learner_permit_login_data.grid(row=7, column=0, sticky='wen', padx=10)

    # 輸入學照日期
    label(learner_license_date_registration, text='學照日期：').grid(row=6, column=1, sticky='ws', pady=(10,0))
    learner_permit_date = entry(learner_license_date_registration)
    learner_permit_date.grid(row=7, column=1, sticky='wen', padx=(0,10))

    # 輸入學照號碼
    label(learner_license_date_registration, text='學照號碼：').grid(row=6, column=2, sticky='ws', pady=(10,0))
    learner_permit_number = entry(learner_license_date_registration)
    learner_permit_number.grid(row=7, column=2, sticky='wen', padx=(0,10))
    
    # 使用 treeview 顯示學員資料
    global data_list
    columns = (
        'learner_permit_date', 
        'learner_permit_number', 
        'license_type_code',
        'student_number',
        'student_name', 
        'birth_date', 
        'national_id_no',
        'mobile_phone', 
        'r_address_zip_code', 
        'r_address'
    )
    data_list = ttk.Treeview(learner_license_date_registration, columns=columns, show='headings')

    data_list.heading('learner_permit_date', text='學照日期')  
    data_list.heading('learner_permit_number', text='學照號碼')  
    data_list.heading('license_type_code', text='考照類別')  
    data_list.heading('student_number', text='學員編號')  
    data_list.heading('student_name', text='學員姓名')  
    data_list.heading('birth_date', text='出生日期')  
    data_list.heading('national_id_no', text='身分證號')  
    data_list.heading('mobile_phone', text='手機')  
    data_list.heading('r_address_zip_code', text='區號')  
    data_list.heading('r_address', text='地址')  

    data_list.column('learner_permit_date', width=50, anchor='center')  
    data_list.column('learner_permit_number', width=50, anchor='center')  
    data_list.column('license_type_code', width=50, anchor='center')  
    data_list.column('student_number', width=50, anchor='center')  
    data_list.column('student_name', width=50, anchor='center')  
    data_list.column('birth_date', width=50, anchor='center')  
    data_list.column('national_id_no', width=60, anchor='center')  
    data_list.column('mobile_phone', width=50, anchor='center')  
    data_list.column('r_address_zip_code', width=50, anchor='center')  
    data_list.column('r_address', width=250, anchor='center')  

    data_list.grid(row=8, column=0, columnspan=4, sticky='wen', padx=10, pady=(20,0))

    # 邏輯功能
    # 搜尋學員資料庫並且在 entry 顯示學員資料
    def populate_student_data(identifier, value):
        global current_student_id
        student_data = get_student_data(identifier, value)
        if student_data:
            # 獲取學員資料庫 id 序列
            current_student_id = student_data[0]
            # 學員編號
            student_number.configure(state='normal')
            student_number.delete(0, ctk.END)
            student_number.insert(0, student_data[5])
            # 學員姓名
            student_name.configure(state='normal')
            student_name.delete(0, ctk.END)
            student_name.insert(0, student_data[6])
            student_name.configure(state='readonly')
            # 身分證號
            national_id_no.configure(state='normal')
            national_id_no.delete(0, ctk.END)
            national_id_no.insert(0, student_data[9])
            national_id_no.configure(state='readonly')
            # 聯絡手機
            mobile_phone.configure(state='normal')
            mobile_phone.delete(0, ctk.END)
            mobile_phone.insert(0, student_data[10])
            mobile_phone.configure(state='readonly')
            # 出生日期
            birth_date.configure(state='normal')
            birth_date.delete(0, ctk.END)
            birth_date.insert(0, student_data[8])
            birth_date.configure(state='readonly')
            # 考照類別 代號
            license_type_code.configure(state='normal')
            license_type_code.delete(0, ctk.END)
            license_type_code.insert(0, student_data[3])
            license_type_code.configure(state='readonly')
            # 考照類別 名稱
            license_type_name.configure(state='normal')
            license_type_name.delete(0, ctk.END)
            license_type_name.insert(0, student_data[4])
            license_type_name.configure(state='readonly')
            # 備註
            remarks.configure(state='normal')
            remarks.delete(0, ctk.END)
            remarks.insert(0, student_data[17])
            remarks.configure(state='readonly')
            # 戶籍地址 郵遞區號
            r_address_zip_code.configure(state='normal')
            r_address_zip_code.delete(0, ctk.END)
            r_address_zip_code.insert(0, student_data[18])
            r_address_zip_code.configure(state='readonly')
            # 戶籍地址 縣市區域
            r_address_city.configure(state='normal')
            r_address_city.delete(0, ctk.END)
            r_address_city.insert(0, student_data[19])
            r_address_city.configure(state='readonly')
            # 戶籍地址 地址
            r_address.configure(state='normal')
            r_address.delete(0, ctk.END)
            r_address.insert(0, student_data[20])
            r_address.configure(state='readonly')


    # 獲取輸入欄位信息
    def save_student_data():
        uid = 1
        global current_student_id
        student_data = {
            'learner_permit_login_data': learner_permit_login_data.get(),
            'learner_permit_date': learner_permit_date.get(),
            'learner_permit_number': learner_permit_number.get(),
            'license_type_name': license_type_name.get(),
            'student_number': student_number.get(),
            'student_name': student_name.get(),
            'birth_date': birth_date.get(),
            'national_id_no': national_id_no.get(),
            'mobile_phone': mobile_phone.get(),
            'r_address_zip_code': r_address_zip_code.get(),
            'r_address': r_address.get(),
            'id': current_student_id
        }

        # 驗證 登錄日期，學照日期，學照號碼，輸入欄位是否為空
        required_fields = [
            'learner_permit_login_data',
            'learner_permit_date',
            'learner_permit_number'
        ]
        
        for field in required_fields:
            if not student_data[field]:
                messagebox.showwarning('提示', f'{validation_fields[field]} 欄位不能為空！')
                return

        if current_student_id is None:
            messagebox.showwarning('提示', '請先搜尋需要登錄的學員')
            return

        update_student_data(student_data, uid = 1)
        clear_entries_and_comboboxes(learner_license_date_registration)

        # 讀取 save_student_data 函式中的 key , 將新登錄的學員資料添加到 Treeview 中
        data_list.insert('', 'end', values = (
            student_data['learner_permit_date'],
            student_data['learner_permit_number'],
            student_data['license_type_name'],
            student_data['student_number'],
            student_data['student_name'],
            student_data['birth_date'],
            student_data['national_id_no'],
            student_data['mobile_phone'],
            student_data['r_address_zip_code'],
            student_data['r_address']
        ))

    # 學照資料登錄按鈕
    btn(learner_license_date_registration, text='登錄', command = save_student_data).grid(row=7, column=3, sticky='wen', padx=(0,10))