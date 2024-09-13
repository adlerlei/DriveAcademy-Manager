# 學照統一送件（匯出 txt 文件）其餘皆為 csv 文件
from utils.widget import *
from utils.config import *
from models.license import *
import customtkinter as ctk
from tkinter import messagebox

# 檢測學員資料庫 id 欄位來判定是否修改或新增
current_student_id = None

def learner_license_submission(content):
    clear_frame(content)
    
    learner_license_submission = frame(content)
    learner_license_submission.columnconfigure(0, weight=1)
    learner_license_submission.columnconfigure(1, weight=1)
    learner_license_submission.columnconfigure(2, weight=1)
    learner_license_submission.columnconfigure(3, weight=1)
    learner_license_submission.place(relwidth=1, relheight=1)
    
    # 顯示 / 搜尋 學員編號
    label(learner_license_submission, text='學員編號').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    student_number = entry(learner_license_submission, placeholder_text='編號查詢')
    student_number.grid(row=1, column=0, sticky='wen', padx=(10,0))
    student_number.bind("<KeyRelease>", lambda event: populate_student_data('student_number', student_number.get()))

    # 顯示學員姓名
    label(learner_license_submission, text='學員姓名').grid(row=0, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    student_name = entry(learner_license_submission, placeholder_text='姓名查詢')
    student_name.grid(row=1, column=1, sticky='wen', padx=(10,0))
    student_name.bind("<KeyRelease>", lambda event: populate_student_data('student_name', student_name.get()))

    # 顯示學員身分證號碼
    label(learner_license_submission, text='身分證號').grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    national_id_no = entry(learner_license_submission, placeholder_text='身分證查詢')
    national_id_no.grid(row=1, column=2, sticky='wen', padx=(10,0))
    national_id_no.bind("<KeyRelease>", lambda event: populate_student_data('national_id_no', national_id_no.get()))

    # 顯示學員電話
    label(learner_license_submission, text='聯絡電話').grid(row=0, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    mobile_phone = entry(learner_license_submission, placeholder_text='手機查詢')
    mobile_phone.grid(row=1, column=3, sticky='wen', padx=10)
    mobile_phone.bind("<KeyRelease>", lambda event: populate_student_data('mobile_phone', mobile_phone.get()))

    # 顯示學員出生日期
    label(learner_license_submission, text='出生日期').grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    birth_date = display_entry_value(learner_license_submission)
    birth_date.grid(row=3, column=0, sticky='wen', padx=(10,0))

    # 學員信箱
    label(learner_license_submission, text='學員信箱').grid(row=2, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    email = display_entry_value(learner_license_submission)
    email.grid(row=3, column=1, sticky='wen', padx=(10,0))

    # 備註
    label(learner_license_submission, text='備註').grid(row=2, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    remarks = display_entry_value(learner_license_submission, width=55)
    remarks.grid(row=3, column=2, columnspan=2, sticky='wen', padx=10)

    # 顯示學員戶籍地址
    label(learner_license_submission, text='戶籍地址').grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    r_address_zip_code = display_entry_value(learner_license_submission)
    r_address_zip_code.grid(row=5, column=0, sticky='wen', padx=(10,0))
    r_address_city = display_entry_value(learner_license_submission)
    r_address_city.grid(row=5, column=1, sticky='wen', padx=(10,0))
    r_address = display_entry_value(learner_license_submission)
    r_address.grid(row=5, column=2, columnspan=2, sticky='wen', padx=10)
    
    # 送件日期
    label(learner_license_submission, text='送件日期').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(50,0))
    submission_date = entry(learner_license_submission)
    submission_date.grid(row=7, column=0, columnspan=2, sticky='wen', padx=(10,0))    

    # 使用 treeview 顯示學員資料
    global data_list
    columns = (
        'national_id_no',
        'birth_date',
        'student_name',
        'r_address_zip_code',
        'r_address_city',
        'r_address',
        'mobile_phone',
        'email'
    )
    data_list = ttk.Treeview(learner_license_submission, columns = columns, show='headings')

    data_list.heading('national_id_no', text='身分證號')
    data_list.heading('birth_date', text='出生日期')
    data_list.heading('student_name', text='學員姓名')
    data_list.heading('r_address_zip_code', text='區號')
    data_list.heading('r_address_city', text='縣市區')
    data_list.heading('r_address', text='戶籍地址')
    data_list.heading('mobile_phone', text='手機')
    data_list.heading('email', text='E-mail')
    
    data_list.column('national_id_no', width=50, anchor='center')
    data_list.column('birth_date', width=50, anchor='center')
    data_list.column('student_name', width=50, anchor='center')
    data_list.column('r_address_zip_code', width=50, anchor='center')
    data_list.column('r_address_city', width=50, anchor='center')
    data_list.column('r_address', width=60, anchor='center')
    data_list.column('mobile_phone', width=50, anchor='center')
    data_list.column('email', width=250, anchor='center')
    
    data_list.grid(row=8, column=0, columnspan=4, sticky='wen', padx=10, pady=(20,0))

    # 創建水平捲軸
    h_scrollbar = ttk.Scrollbar(learner_license_submission, orient="horizontal", command=data_list.xview)
    data_list.configure(xscrollcommand=h_scrollbar.set)

    # 創建垂直捲軸
    v_scrollbar = ttk.Scrollbar(learner_license_submission, orient="vertical", command=data_list.yview)
    data_list.configure(yscrollcommand=v_scrollbar.set)

    # 使用 grid 布局管理器來排列 Treeview 和捲軸
    h_scrollbar.grid(row=9, column=0, columnspan=4, sticky="ew", padx=10)
    v_scrollbar.grid(row=8, column=4, rowspan=2, sticky="ns", pady=10)

    # 配置行和列的權重，使其在窗口調整大小時自動調整
    learner_license_submission.grid_rowconfigure(14, weight=1)
    learner_license_submission.grid_columnconfigure(0, weight=1)
    learner_license_submission.grid_columnconfigure(1, weight=1)
    learner_license_submission.grid_columnconfigure(2, weight=1)
    learner_license_submission.grid_columnconfigure(3, weight=1)

    # 邏輯功能
    # 搜尋學員資料庫並且在 entry 顯示學員資料
    def populate_student_data(identifier, value):
        global current_student_id
        # 監聽學員編號輸入欄位如果為空，清除學員資料
        if value == '':
            clear_entries_and_comboboxes(learner_license_submission)
            current_student_id = None
        else:
            student_data = get_student_data(identifier, value)
            if student_data:
                current_student_id = student_data[0]
          
                # 保存当前触发搜索的字段值
                current_field_value = value
          
                # 填充数据
                student_number.delete(0, ctk.END)
                student_number.insert(0, student_data[5])
                student_name.delete(0, ctk.END)
                student_name.insert(0, student_data[6])
                national_id_no.delete(0, ctk.END)
                national_id_no.insert(0, student_data[10])
                mobile_phone.delete(0, ctk.END)
                mobile_phone.insert(0, student_data[11])
                birth_date.configure(state='normal')
                birth_date.delete(0, ctk.END)
                birth_date.insert(0, student_data[9])
                birth_date.configure(state='readonly')
                email.configure(state='normal')
                email.delete(0, ctk.END)
                email.insert(0, student_data[17])
                email.configure(state='readonly')
                remarks.configure(state='normal')
                remarks.delete(0, ctk.END)
                remarks.insert(0, student_data[18])
                remarks.configure(state='readonly')
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

                # 恢复当前触发搜索的字段值
                if identifier == 'student_number':
                    student_number.delete(0, ctk.END)
                    student_number.insert(0, current_field_value)
                elif identifier == 'student_name':
                    student_name.delete(0, ctk.END)
                    student_name.insert(0, current_field_value)
                elif identifier == 'national_id_no':
                    national_id_no.delete(0, ctk.END)
                    national_id_no.insert(0, current_field_value)
                elif identifier == 'mobile_phone':
                    mobile_phone.delete(0, ctk.END)
                    mobile_phone.insert(0, current_field_value)
            else:
                # 如果没有查询到学生资料,则重置 current_student_id
                current_student_id = None

 
    # 獲取輸入欄位信息
    def save_student_data():
        uid = 0
        global current_student_id
        student_data = {
            'id': current_student_id,
            'national_id_no': national_id_no.get(),
            'birth_date': birth_date.get(),
            'student_name': student_name.get(),
            'r_address_zip_code': r_address_zip_code.get(),
            'r_address_city': r_address_city.get(),
            'r_address': r_address.get(),
            'mobile_phone': mobile_phone.get(),
            'email': email.get(),
            'submission_date': submission_date.get()
        }

        # 驗證 送件日期 輸入欄位是否為空
        required_fields = [
            'submission_date'
        ]

        for field in required_fields:
            if not student_data[field]:
                messagebox.showwarning('提示', f'{validation_fields[field]} 欄位不能為空！')
                return
            
        if current_student_id is None:
            messagebox.showwarning('提示', '請先搜尋需要送件的學員')
            return
        
        update_student_data(student_data, uid = uid)

        # 需要保留的 entry 列表，clear_entries_and_comboboxes 函式中的參數之一 ###
        keep_entries = [submission_date]
        # 清空但保留特定 entry
        clear_entries_and_comboboxes(learner_license_submission, keep_entries)
        # clear_entries_and_comboboxes 函式結束 ################


        # 讀取 save_student_data 函式中的 key , 將新登錄的學員資料添加到 Treeview 中
        data_list.insert('', 'end', values = (
                student_data['national_id_no'],
                student_data['birth_date'],
                student_data['student_name'],
                student_data['r_address_zip_code'],
                student_data['r_address_city'],
                student_data['r_address'],
                student_data['mobile_phone'],
                student_data['email']
            ))
        
    # 學照資料送件
    btn(learner_license_submission, text='送件', command = save_student_data).grid(row=7, column=2, sticky='wen', padx=(10,0))
    export_btn(learner_license_submission, text='匯出文件', command=lambda: export_selected_data(data_list, submission_date)).grid(row=7, column=3, sticky='wen', padx=10)