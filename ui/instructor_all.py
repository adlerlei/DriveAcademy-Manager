 # 教練資料作業 新增 - 修改 - 刪除 - 查詢
from utils.widget import *
from utils.config import *
from models.instructor import *
import customtkinter as ctk
from tkinter import messagebox

is_editing = False
current_instructor_number = None

def instructor_all(content):
    clear_frame(content)

    instructor_all = frame(content)
    instructor_all.columnconfigure(0, weight=1)
    instructor_all.columnconfigure(1, weight=1)
    instructor_all.columnconfigure(2, weight=1)
    instructor_all.columnconfigure(3, weight=1)
    instructor_all.place(relwidth=1, relheight=1)


    # 教練編號0
    label(instructor_all, text="教練編號").grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    number = entry(instructor_all, placeholder_text='輸入教練編號查詢')
    number.grid(row=1, column=0, sticky='wen', padx=(10,0))
    number.bind("<KeyRelease>", lambda event: populate_instructor_data('number', number.get()))

    # 教練姓名1
    label(instructor_all, text="教練姓名").grid(row=0, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    name = entry(instructor_all)
    name.grid(row=1, column=1, sticky='wen', padx=(10,0))

    # 身分證號碼2
    label(instructor_all, text="身分證號碼").grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    national_id_no = entry(instructor_all)
    national_id_no.grid(row=1, column=2, sticky='wen', padx=(10,0))

    # 出生日期3
    label(instructor_all, text="出生日期").grid(row=0, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    birth_date = entry(instructor_all)
    birth_date.grid(row=1, column=3, sticky='wen', padx=10)

    # 市話0
    label(instructor_all, text="市話").grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    home_phone = entry(instructor_all)
    home_phone.grid(row=3, column=0, sticky='wen', padx=(10,0))

    # 手機1
    label(instructor_all, text="手機").grid(row=2, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    mobile_phone = entry(instructor_all)
    mobile_phone.grid(row=3, column=1, sticky='wen', padx=(10,0))

    # 電子郵件2
    label(instructor_all, text="電子郵件").grid(row=2, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    email = entry(instructor_all)
    email.grid(row=3, column=2, sticky='wen',padx=(10,0))

    # 教練證號碼3
    label(instructor_all, text="教練證號碼").grid(row=2, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    instructor_license_number = entry(instructor_all)
    instructor_license_number.grid(row=3, column=3, sticky='wen',padx=10)

    # 駕照類別0
    # license_type = ['自用小客車', '職業小客車', '自用大貨車', '職業大貨車', '自用大客車', '職業大客車', '自用聯結車', '職業聯結車']
    label(instructor_all, text="駕照類別").grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    driving_license_category = combobox(instructor_all, values = ['自用小客車', '職業小客車', '自用大貨車', '職業大貨車', '自用大客車', '職業大客車', '自用聯結車', '職業聯結車'])
    driving_license_category.grid(row=5, column=0, sticky='wen', padx=(10,0))
    driving_license_category.set("")

    # 駕照號碼1
    label(instructor_all, text="駕照號碼").grid(row=4, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    driving_license_number = entry(instructor_all)
    driving_license_number.grid(row=5, column=1, sticky='wen',padx=(10,0))

    # 基本薪資2
    label(instructor_all, text="基本薪資").grid(row=4, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    base_salary = entry(instructor_all)
    base_salary.grid(row=5, column=2, sticky='wen',padx=(10,0))

    # 入職日期3
    label(instructor_all, text="入職日期").grid(row=4, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    start_date = entry(instructor_all)
    start_date.grid(row=5, column=3, sticky='wen',padx=10)

    # 離職日期0
    label(instructor_all, text="離職日期").grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    end_date = entry(instructor_all)
    end_date.grid(row=7, column=0, sticky='wen',padx=(10,0))

    # 備註1
    label(instructor_all, text="備註").grid(row=6, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    remarks = entry(instructor_all)
    remarks.grid(row=7, column=1, sticky='wen', columnspan=3, padx=10)

    # 戶籍地址
    r_address_zip_code_lists, r_address_city_lists, r_address_dict = address_data()
    label(instructor_all, text='戶籍地址').grid(row=10, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    r_address_zip_code = combobox(instructor_all, values=r_address_zip_code_lists, command=lambda x: on_r_address_zip_change(x, r_address_city, r_address_dict))
    r_address_zip_code.grid(row=11, column=0, sticky='wen', padx=(10,0))
    r_address_city = combobox(instructor_all, values=r_address_city_lists, command=lambda x: on_r_address_city_change(x, r_address_zip_code, r_address_dict))
    r_address_city.grid(row=11, column=1, sticky='wen', padx=(10,0))
    r_address = entry(instructor_all)
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

    m_address_zip_code_lists, m_address_city_lists, m_address_dict = address_data()
    label(instructor_all, text='通訊地址').grid(row=10, column=2, sticky='ws', padx=(10,0), pady=(20,0))
    m_address_zip_code = combobox(instructor_all, values=m_address_zip_code_lists, command=lambda x: on_m_address_zip_change(x, m_address_city, m_address_dict))
    m_address_zip_code.grid(row=11, column=2, sticky='wen', padx=(10,0))
    m_address_city = combobox(instructor_all, values=m_address_city_lists, command=lambda x: on_m_address_city_change(x, m_address_zip_code, m_address_dict))
    m_address_city.grid(row=11, column=3, sticky='wen', padx=10)
    m_address = entry(instructor_all)
    m_address.grid(row=12, column=2, columnspan=2, sticky='wen', padx=10)
    m_address_zip_code.set('')
    m_address_city.set('')

    # 通訊地址監聽 zip code 改變時，自動更新 city 城市
    def on_m_address_zip_change(zip_code_list, m_address_city, address_dict):
        selected_zip_code = address_dict.get(zip_code_list, "")
        m_address_city.set(selected_zip_code)

    def on_m_address_city_change(select_city, m_address_number, address_dict):
        selected_number = next((number for number, city in address_dict.items() if city == select_city), "")
        m_address_number.set(selected_number)

    # 資料顯示區
    treeview_values = [
        'number',
        'name',
        'national_id_no',
        'birth_date',
        'home_phone',
        'mobile_phone',
        'email',
        'r_address_zip_code',
        'r_address_city',
        'r_address',
        'm_address_zip_code',
        'm_address_city',
        'm_address',
        'instructor_id',
        'license_type',
        'license_number',
        'basic_salary',
        'hire_date',
        'leave_date',
        'remarks',
        'creation_date'
    ]
    data_list = ttk.Treeview(instructor_all, columns=treeview_values, show='headings')

    data_list.heading('number', text='教練編號')
    data_list.heading('name', text='姓名')
    data_list.heading('national_id_no', text='身分證')
    data_list.heading('birth_date', text='出生日期')
    data_list.heading('home_phone', text='市話')
    data_list.heading('mobile_phone', text='手機')
    data_list.heading('email', text='電子郵件')
    data_list.heading('r_address_zip_code', text="戶籍區號")
    data_list.heading('r_address_city', text="戶籍縣市")
    data_list.heading('r_address', text="戶籍地址")
    data_list.heading('m_address_zip_code', text='通訊區號')
    data_list.heading('m_address_city', text='通訊縣市')
    data_list.heading('m_address', text='通訊地址')
    data_list.heading('instructor_id', text='教練證號碼')
    data_list.heading('license_type', text='駕照類別')
    data_list.heading('license_number', text='駕照號碼')
    data_list.heading('basic_salary', text='基本薪資')
    data_list.heading('hire_date', text='入職日期')
    data_list.heading('leave_date', text='離職日期')
    data_list.heading('remarks', text='備註')
    data_list.heading('creation_date', text='建檔日期')

    data_list.column('number', width=50, anchor=CENTER)
    data_list.column('name', width=70, anchor=CENTER)
    data_list.column('national_id_no', width=100, anchor=CENTER)
    data_list.column('birth_date', width=70, anchor=CENTER)
    data_list.column('home_phone', width=70, anchor=CENTER)
    data_list.column('mobile_phone', width=70, anchor=CENTER)
    data_list.column('email', width=100, anchor=CENTER)
    data_list.column('r_address_zip_code', width=50, anchor=CENTER)
    data_list.column('r_address_city', width=50, anchor=CENTER)
    data_list.column('r_address', width=150, anchor=CENTER)
    data_list.column('m_address_zip_code', width=50, anchor=CENTER)
    data_list.column('m_address_city', width=50, anchor=CENTER)
    data_list.column('m_address', width=150, anchor=CENTER)
    data_list.column('instructor_id', width=60, anchor=CENTER)
    data_list.column('license_type', width=70, anchor=CENTER)
    data_list.column('license_number', width=70, anchor=CENTER)
    data_list.column('basic_salary', width=50, anchor=CENTER)
    data_list.column('hire_date', width=50, anchor=CENTER)
    data_list.column('leave_date', width=50, anchor=CENTER)
    data_list.column('remarks', width=100, anchor=CENTER)
    data_list.column('creation_date', width=100, anchor=CENTER)

    data_list.grid(row=14, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)
    
    # 創建水平捲軸
    h_scrollbar = ttk.Scrollbar(instructor_all, orient="horizontal", command=data_list.xview)
    data_list.configure(xscrollcommand=h_scrollbar.set)

    # 創建垂直捲軸
    v_scrollbar = ttk.Scrollbar(instructor_all, orient="vertical", command=data_list.yview)
    data_list.configure(yscrollcommand=v_scrollbar.set)

    # 使用 grid 布局管理器來排列 Treeview 和捲軸
    h_scrollbar.grid(row=15, column=0, columnspan=4, sticky="ew", padx=10)
    v_scrollbar.grid(row=14, column=4, rowspan=2, sticky="ns", pady=10)

    # 配置行和列的權重，使其在窗口調整大小時自動調整
    instructor_all.grid_rowconfigure(14, weight=1)
    instructor_all.grid_columnconfigure(0, weight=1)
    instructor_all.grid_columnconfigure(1, weight=1)
    instructor_all.grid_columnconfigure(2, weight=1)
    instructor_all.grid_columnconfigure(3, weight=1)

    # 邏輯功能區
    def populate_instructor_data(identifier, value):
        global is_editing, current_instructor_number
        # 監聽教練編號輸入框，如果教練編號为空，则清空所有输入框
        if identifier == 'number' and value == '':
            clear_entries_and_comboboxes(instructor_all)
        else:
            instructor_data = get_instructor_data(identifier, value)
            if instructor_data:
                is_editing = True
                current_instructor_number = instructor_data[0]
                number.delete(0, ctk.END)
                number.insert(0, instructor_data[1])
                name.delete(0, ctk.END)
                name.insert(0, instructor_data[2])
                national_id_no.delete(0, ctk.END)
                national_id_no.insert(0, instructor_data[3])
                birth_date.delete(0, ctk.END)
                birth_date.insert(0, instructor_data[4])
                home_phone.delete(0, ctk.END)
                home_phone.insert(0, instructor_data[5])
                mobile_phone.delete(0, ctk.END)
                mobile_phone.insert(0, instructor_data[6])
                email.delete(0, ctk.END)
                email.insert(0, instructor_data[7])
                instructor_license_number.delete(0, ctk.END)
                instructor_license_number.insert(0, instructor_data[14])
                driving_license_category.set(str(instructor_data[15]) if instructor_data[15] is not None else "")
                driving_license_number.delete(0, ctk.END)
                driving_license_number.insert(0, instructor_data[16])
                base_salary.delete(0, ctk.END)
                base_salary.insert(0, instructor_data[17])
                start_date.delete(0, ctk.END)
                start_date.insert(0, instructor_data[18])
                end_date.delete(0, ctk.END)
                end_date.insert(0, instructor_data[19])
                remarks.delete(0, ctk.END)
                remarks.insert(0, instructor_data[20])
                r_address_zip_code.set(instructor_data[8])
                r_address_city.set(instructor_data[9])
                r_address.delete(0, ctk.END)
                r_address.insert(0, instructor_data[10])
                m_address_zip_code.set(instructor_data[11]) 
                m_address_city.set(instructor_data[12])  
                m_address.delete(0, ctk.END)
                m_address.insert(0, instructor_data[13])          
            else:
                is_editing = False
                current_instructor_number = None

    def save_instructor_data():
        global is_editing, current_instructor_number
        instructor_data = {
            'number': number.get(), # 教練編號1
            'name': name.get(), # 教練姓名2
            'national_id_no': national_id_no.get(), # 身分證號碼3
            'birth_date': birth_date.get(), # 出生日期4
            'home_phone': home_phone.get(), # 市內電話5
            'mobile_phone': mobile_phone.get(), # 手機6
            'email': email.get(), # 電子郵件7
            'instructor_license_number': instructor_license_number.get(), # 教練證號
            'driving_license_category': driving_license_category.get(), # 駕照類別
            'driving_license_number': driving_license_number.get(), # 駕照號碼
            'base_salary': base_salary.get(), # 基本薪資
            'start_date': start_date.get(), # 入職日期
            'end_date': end_date.get(), # 離職日期
            'remarks': remarks.get(), # 備註
            'r_address_zip_code': r_address_zip_code.get(), # 戶籍地址郵遞區號
            'r_address_city': r_address_city.get(), # 戶籍地址縣市區域
            'r_address': r_address.get(), # 戶籍地址
            'm_address_zip_code': m_address_zip_code.get(), # 通訊地址郵遞區號
            'm_address_city': m_address_city.get(), # 通訊地址縣市區域
            'm_address': m_address.get(), # 通訊地址
        }

        if is_editing:
            messagebox.showinfo('提示', '請使用 "修改" 功能來更新教練資料。')
            return

        insert_instructor_data(instructor_data)
        update_treeview()
        clear_entries_and_comboboxes(instructor_all)

    def update_instructor():
        global is_editing, current_instructor_number
        instructor_data = {
            'number': number.get(), # 教練編號1
            'name': name.get(), # 教練姓名2
            'national_id_no': national_id_no.get(), # 身分證號碼3
            'birth_date': birth_date.get(), # 出生日期4
            'home_phone': home_phone.get(), # 市內電話5
            'mobile_phone': mobile_phone.get(), # 手機6
            'email': email.get(), # 電子郵件7
            'instructor_license_number': instructor_license_number.get(), # 教練證號
            'driving_license_category': driving_license_category.get(), # 駕照類別
            'driving_license_number': driving_license_number.get(), # 駕照號碼
            'base_salary': base_salary.get(), # 基本薪資
            'start_date': start_date.get(), # 入職日期
            'end_date': end_date.get(), # 離職日期
            'remarks': remarks.get(), # 備註
            'r_address_zip_code': r_address_zip_code.get(), # 戶籍地址郵遞區號
            'r_address_city': r_address_city.get(), # 戶籍地址縣市區域
            'r_address': r_address.get(), # 戶籍地址
            'm_address_zip_code': m_address_zip_code.get(), # 通訊地址郵遞區號
            'm_address_city': m_address_city.get(), # 通訊地址縣市區域
            'm_address': m_address.get(), # 通訊地址
            'id': current_instructor_number
        }

        if current_instructor_number is None:
            messagebox.showwarning('提示', '請先搜尋需要修改的教練資料。')
            return
        else:
            update_instructor_data(instructor_data)
        # is_editing = False
        # current_instructor_number = None
        clear_entries_and_comboboxes(instructor_all)
        update_treeview()



    def delete_instructor():
        global is_editing, current_instructor_number
        if current_instructor_number:
            confirm = messagebox.askyesno('確認', '確定要刪除此教練資料嗎？此操作無法撤銷。')
            if confirm:
                delete_instructor_data(current_instructor_number)
                update_treeview()
                is_editing = False
                current_instructor_number = None
        else:
            messagebox.showwarning('提示', '請先搜尋需要刪除的教練資料。')
        clear_entries_and_comboboxes(instructor_all)


    def update_treeview():
        # 清空現有數據
        data_list.delete(*data_list.get_children())
        
        # 從資料庫獲取所有教練資料
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM instructor")
        instructors = cursor.fetchall()
        conn.close() 

        # 將教練資料插入 Treeview
        for instructor in instructors:
            data_list.insert("", "end", values=instructor[1:])  # 假设第一个字段是 id，我们不显示

    # 修改按钮配置
    add_btn(instructor_all, text="新增", command=save_instructor_data).grid(row=13, column=1, sticky='wen', padx=10, pady=10)
    modify_btn(instructor_all, text="修改", command=update_instructor).grid(row=13, column=2, sticky='wen', padx=10, pady=10)
    delete_btn(instructor_all, text="刪除", command=delete_instructor).grid(row=13, column=3, sticky='wen', padx=10, pady=10)

    # 初始化 Treeview
    update_treeview()