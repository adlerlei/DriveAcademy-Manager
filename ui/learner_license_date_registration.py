# 學習駕照日期登錄
from utils.widget import *
from utils.config import * 
from models.license import *
import customtkinter as ctk
from tkinter import messagebox


def learner_license_date_registration(content):
    clear_frame(content)
        
    learner_license_date_registration = frame(content)
    learner_license_date_registration.columnconfigure(0, weight=1)
    learner_license_date_registration.columnconfigure(1, weight=1)
    learner_license_date_registration.columnconfigure(2, weight=1)
    learner_license_date_registration.columnconfigure(3, weight=1)
    learner_license_date_registration.place(relwidth=1, relheight=1)

    # 輸入學號
    select_student_number = entry(learner_license_date_registration, placeholder_text = "輸入學員編號")
    select_student_number.grid(row=0, column=0, columnspan=3, sticky='wen', padx=10, pady=(10,0))

    # # 搜尋按鈕
    # search_btn(learner_license_date_registration, text='搜尋學員信息', command=lambda: search_student_info(
    #     select_student_number.get(), student_number, student_name, national_id_no, birth_date, mobile_phone, license_type_code, license_type_name, remarks, r_address_zip_code, r_address_city, r_address
    # )).grid(row=0, column=3, sticky='wen', padx=(0,10), pady=(10,0))

    # 顯示學員編號
    label(learner_license_date_registration, text='學員編號').grid(row=1, column=0, sticky='ws', padx=(10,0), pady=(50,0))
    student_number = display_entry_value(learner_license_date_registration)
    student_number.grid(row=2, column=0, sticky='wen', padx=10)

    # 顯示學員姓名
    label(learner_license_date_registration, text='學員姓名').grid(row=1, column=1, sticky='ws', pady=(10,0))
    student_name = display_entry_value(learner_license_date_registration)
    student_name.grid(row=2, column=1, sticky='wen', padx=(0,10))

    # 顯示學員身分證號碼
    label(learner_license_date_registration, text='身分證號').grid(row=1, column=2, sticky='ws',pady=(10,0))
    national_id_no = display_entry_value(learner_license_date_registration)
    national_id_no.grid(row=2, column=2, sticky='wen', padx=(0,10))

    # 顯示學員電話
    label(learner_license_date_registration, text='聯絡手機').grid(row=1, column=3, sticky='ws', pady=(10,0))
    mobile_phone = display_entry_value(learner_license_date_registration)
    mobile_phone.grid(row=2, column=3, sticky='wen', padx=(0,10))

    # 顯示學員出生日期
    label(learner_license_date_registration, text='出生日期').grid(row=3, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    birth_date = display_entry_value(learner_license_date_registration)
    birth_date.grid(row=4, column=0, sticky='wen', padx=10)

    # 顯示考照類別
    label(learner_license_date_registration, text='考照類別').grid(row=3, column=1, sticky='ws', pady=(10,0))
    license_type_code = display_entry_value(learner_license_date_registration)
    license_type_code.grid(row=4, column=1, sticky='wen', padx=(0,10))
    license_type_name = display_entry_value(learner_license_date_registration)
    license_type_name.grid(row=4, column=2, sticky='wen', padx=(0,10))

    # 備註
    label(learner_license_date_registration, text='備註').grid(row=3, column=3, sticky='ws',pady=(10,0))
    remarks = display_entry_value(learner_license_date_registration)
    remarks.grid(row=4, column=3, sticky='wen', padx=(0,10))

    # 戶籍地址
    label(learner_license_date_registration, text='戶籍地址').grid(row=5, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    r_address_zip_code = display_entry_value(learner_license_date_registration)
    r_address_zip_code.grid(row=6, column=0, sticky='wen', padx=10)
    r_address_city = display_entry_value(learner_license_date_registration)
    r_address_city.grid(row=6, column=1, sticky='wen', padx=(0,10))
    r_address = display_entry_value(learner_license_date_registration)
    r_address.grid(row=6, column=2, columnspan=2, sticky='wen', padx=(0,10))
    
    # 登錄日期
    label(learner_license_date_registration, text='登錄日期：').grid(row=7, column=0, sticky='ws', padx=(10,0), pady=(50,0))
    learner_permit_login_data = entry(learner_license_date_registration)
    learner_permit_login_data.grid(row=8, column=0, sticky='wen', padx=10)


    # 學照日期
    label(learner_license_date_registration, text='學照日期：').grid(row=7, column=1, sticky='ws', pady=(10,0))
    learner_permit_date = entry(learner_license_date_registration)
    learner_permit_date.grid(row=8, column=1, sticky='wen', padx=(0,10))

    # 學照號碼
    label(learner_license_date_registration, text='學照號碼：').grid(row=7, column=2, sticky='ws', pady=(10,0))
    learner_permit_number = entry(learner_license_date_registration)
    learner_permit_number.grid(row=8, column=2, sticky='wen', padx=(0,10))


    # 搜尋按鈕
    search_btn(learner_license_date_registration, text='搜尋學員信息', command=lambda: search_student_info(
        select_student_number.get(), student_number, student_name, national_id_no, birth_date, mobile_phone, license_type_code, license_type_name, remarks, r_address_zip_code, r_address_city, r_address
    )).grid(row=0, column=3, sticky='wen', padx=(0,10), pady=(10,0))


    # 定義按鈕點擊事件
    def add_btn_click():
        learner_permit_login_data_val = learner_permit_login_data.get()
        learner_permit_date_val = learner_permit_date.get()
        learner_permit_number_val = learner_permit_number.get()

        # 檢查欄位是否為空
        if not all([learner_permit_login_data_val, learner_permit_date_val, learner_permit_number_val]):
            messagebox.showerror('錯誤', '登錄日期、學照日期、學照號碼 - 欄位不可為空')
            return
        else:
            student_name_val = student_name.get()
            national_id_val = national_id_no.get()
            birth_date_val = birth_date.get()
            mobile_phone_val = mobile_phone.get()
            
            license_update_student_data(id, student_name_val, national_id_val, birth_date_val, mobile_phone_val)
            select_student_number.delete(0, ctk.END)
            student_number.delete(0, ctk.END)
            student_name.delete(0, ctk.END)
            national_id_no.delete(0, ctk.END)
            mobile_phone.delete(0, ctk.END)
            birth_date.delete(0, ctk.END)
            license_type_code.delete(0, ctk.END)
            license_type_name.delete(0, ctk.END)
            remarks.delete(0, ctk.END)
            r_address_zip_code.delete(0, ctk.END)
            r_address_city.delete(0, ctk.END)
            r_address.delete(0, ctk.END)
            learner_permit_login_data.delete(0, ctk.END)
            learner_permit_date.delete(0, ctk.END)
            learner_permit_number.delete(0, ctk.END)
            messagebox.showinfo('成功', '學照日期登錄成功')

            # 在 Treeview 中顯示更新後的資料
            for i in data_list.get_children():
                data_list.delete(i)
            load_data_into_treeview(data_list)


    # 學照資料登錄按鈕
    btn(learner_license_date_registration, text='登錄', command = add_btn_click).grid(row=8, column=3, sticky='wen', padx=(0,10))
    
    
    # 登錄後顯示信息列表
    data_list = ttk.Treeview(learner_license_date_registration, show='headings', columns=(
        'id', 'learner_license_date', 'learner_license_number', 'learner_license_type', 
        'student_number', 'student_name','birth_date', 'national_id_no', 'phone',
        'r_address_zip_code', 'r_address_city', 'r_address'))
    
    data_list.column('id', width=50, anchor='w')
    data_list.column('learner_license_date', width=50, anchor='w')
    data_list.column('learner_license_number', width=50, anchor='w')
    data_list.column('learner_license_type', width=50, anchor='w')
    data_list.column('student_number', width=50, anchor='w')
    data_list.column('student_name', width=50, anchor='w')
    data_list.column('birth_date', width=50, anchor='w')
    data_list.column('national_id_no', width=60, anchor='w')
    data_list.column('phone', width=50, anchor='w')
    data_list.column('r_address_zip_code', width=50, anchor='w')
    data_list.column('r_address_city', width=50, anchor='w')
    data_list.column('r_address', width=250, anchor='w')
    
    data_list.heading('id', text='ID')
    data_list.heading('learner_license_date', text='學照日期')
    data_list.heading('learner_license_number', text='學照號碼')
    data_list.heading('learner_license_type', text='考照類別')
    data_list.heading('student_number', text='學員編號')
    data_list.heading('student_name', text='學員姓名')
    data_list.heading('birth_date', text='出生日期')
    data_list.heading('national_id_no', text='身分證號')
    data_list.heading('phone', text='聯絡手機')
    data_list.heading('r_address_zip_code', text='區號')
    data_list.heading('r_address_city', text='縣市')
    data_list.heading('r_address', text='地址')
    
    data_list.grid(row=9, column=0, columnspan=4, sticky='wen', padx=10, pady=(20,0))
    
    # def load_data_into_treeview(treeview):
    #     conn = sqlite3.connect('database.db')
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT * FROM student")
    #     rows = cursor.fetchall()
    #     for row in rows:
    #         treeview.insert("", "end", values=row)
    #     conn.close()
    
    load_data_into_treeview(data_list)