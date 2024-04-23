 # 教練資料作業 新增 - 修改 - 刪除 - 查詢
from utils.widget import *
from utils.config import *


def instructor_all(content):
    clear_frame(content)

    instructor_all = frame(content)
    instructor_all.columnconfigure(0, weight=1)
    instructor_all.columnconfigure(1, weight=1)
    instructor_all.columnconfigure(2, weight=1)
    instructor_all.columnconfigure(3, weight=1)
    instructor_all.place(relwidth=1, relheight=1)


    # 教練編號
    label(instructor_all, text="教練編號").grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    entry(instructor_all).grid(row=1, column=0, sticky='wen', columnspan=2, padx=10)

    # 教練姓名
    label(instructor_all, text="教練姓名").grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    entry(instructor_all).grid(row=1, column=2, sticky='wen', columnspan=2, padx=10)

    # 身分證號碼
    label(instructor_all, text="身分證號碼").grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    entry(instructor_all).grid(row=3, column=0, sticky='wen', columnspan=2, padx=10)

    # 出生日期
    label(instructor_all, text="出生日期").grid(row=2, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    entry(instructor_all).grid(row=3, column=2, sticky='wen', columnspan=2, padx=10)

    # 市話
    label(instructor_all, text="市話").grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    entry(instructor_all).grid(row=5, column=0, sticky='wen', columnspan=2, padx=10)

    # 手機
    label(instructor_all, text="手機").grid(row=4, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    entry(instructor_all).grid(row=5, column=2, sticky='wen', columnspan=2, padx=10)

    # 電子郵件
    label(instructor_all, text="電子郵件").grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    entry(instructor_all).grid(row=7, column=0, sticky='wen', columnspan=2, padx=10)

    # 教練證號碼
    label(instructor_all, text="教練證號碼").grid(row=6, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    entry(instructor_all).grid(row=7, column=2, sticky='wen', columnspan=2, padx=10)

    # 駕照類別
    label(instructor_all, text="駕照類別").grid(row=8, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    combobox(instructor_all, values=['A','B']).grid(row=9, column=0, sticky='wen', columnspan=2, padx=10)

    # 駕照號碼
    label(instructor_all, text="駕照號碼").grid(row=8, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    entry(instructor_all).grid(row=9, column=2, sticky='wen', columnspan=2, padx=10)

    # 基本薪資
    label(instructor_all, text="基本薪資").grid(row=10, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    entry(instructor_all).grid(row=11, column=0, sticky='wen', columnspan=2, padx=10)

    # 入職日期
    label(instructor_all, text="入職日期").grid(row=10, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    entry(instructor_all).grid(row=11, column=2, sticky='wen', columnspan=2, padx=10)

    # 離職日期
    label(instructor_all, text="離職日期").grid(row=12, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    entry(instructor_all).grid(row=13, column=0, sticky='wen', columnspan=2, padx=10)

    # 備註
    label(instructor_all, text="備註").grid(row=12, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    entry(instructor_all).grid(row=13, column=2, sticky='wen', columnspan=2, padx=10)

    # 戶籍地址
    label(instructor_all, text="戶籍地址").grid(row=14, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    combobox(instructor_all, values=['231','116']).grid(row=15, column=0, sticky='wen', padx=10)
    combobox(instructor_all, values=['台北市','新北市']).grid(row=15, column=1, sticky='wen', padx=10)
    entry(instructor_all).grid(row=16, column=0, sticky='wen', columnspan=2, padx=10)

    # 通訊地址
    label(instructor_all, text="通訊地址").grid(row=14, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    combobox(instructor_all, values=['231','116']).grid(row=15, column=2, sticky='wen', padx=10)
    combobox(instructor_all, values=['台北市','新北市']).grid(row=15, column=3, sticky='wen', padx=10)
    entry(instructor_all).grid(row=16, column=2, sticky='wen', columnspan=2, padx=10)

    # 新增
    btn(instructor_all, text="新增", command=lambda: print("新增")).grid(row=17, column=0, sticky='wen', padx=10, pady=10)
    # 修改
    btn(instructor_all, text="修改", command=lambda: print("修改")).grid(row=17, column=2, sticky='wen', padx=10, pady=10)
    # 刪除
    btn(instructor_all, text="刪除", command=lambda: print("刪除")).grid(row=17, column=3, sticky='wen', padx=10, pady=10)

    # 資料顯示區
    data_list = ttk.Treeview(instructor_all, columns=('id', 'name', 'instructor_num', 'birth_date', 'city_phone', 'cell_phone', 'email', 'instructor_id', 'license_type', 'license_number', 'basic_salary', 'hire_date', 'leave_date', 'comment', 'home_address', 'communication_address'), show='headings')

    data_list.heading('id', text='編號')
    data_list.heading('name', text='姓名')
    data_list.heading('instructor_num', text='教練編號')
    data_list.heading('birth_date', text='出生日期')
    data_list.heading('city_phone', text='市話')
    data_list.heading('cell_phone', text='手機')
    data_list.heading('email', text='電子郵件')
    data_list.heading('instructor_id', text='教練證號碼')
    data_list.heading('license_type', text='駕照類別')
    data_list.heading('license_number', text='駕照號碼')
    data_list.heading('basic_salary', text='基本薪資')
    data_list.heading('hire_date', text='入職日期')
    data_list.heading('leave_date', text='離職日期')
    data_list.heading('comment', text='備註')
    data_list.heading('home_address', text='戶籍地址')
    data_list.heading('communication_address', text='通訊地址')

    data_list.column('#0', width=0, stretch=NO)
    data_list.column('id', width=50, anchor=CENTER)
    data_list.column('name', width=100, anchor=CENTER)
    data_list.column('instructor_num', width=100, anchor=CENTER)
    data_list.column('birth_date', width=100, anchor=CENTER)
    data_list.column('city_phone', width=100, anchor=CENTER)
    data_list.column('cell_phone', width=100, anchor=CENTER)
    data_list.column('email', width=100, anchor=CENTER)
    data_list.column('instructor_id', width=100, anchor=CENTER)
    data_list.column('license_type', width=100, anchor=CENTER)
    data_list.column('license_number', width=100, anchor=CENTER)
    data_list.column('basic_salary', width=100, anchor=CENTER)
    data_list.column('hire_date', width=100, anchor=CENTER)
    data_list.column('leave_date', width=100, anchor=CENTER)
    data_list.column('comment', width=100, anchor=CENTER)
    data_list.column('home_address', width=100, anchor=CENTER)
    data_list.column('communication_address', width=100, anchor=CENTER)

    data_list.grid(row=18, column=0, columnspan=4, sticky='wen', padx=10, pady=10)

    for i in range(100):
        data_list.insert("", "end", values=(f"202{i % 10}", f"張{i}", f"A{i}", f"202{i % 10}-01-01", f"男", f"02{i % 10}", f"09{i % 10}", f"test{i}@gmail.com", f"台北市", f"台北市"))