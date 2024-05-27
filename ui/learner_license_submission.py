# 學照統一送件（匯出 txt 文件）其餘皆為 csv 文件
from utils.widget import *
from utils.config import *

def learner_license_submission(content):
    clear_frame(content)
    
    learner_license_submission = frame(content)
    learner_license_submission.columnconfigure(0, weight=1)
    learner_license_submission.columnconfigure(1, weight=1)
    learner_license_submission.columnconfigure(2, weight=1)
    learner_license_submission.columnconfigure(3, weight=1)
    learner_license_submission.place(relwidth=1, relheight=1)

    # # 輸入學號
    entry(learner_license_submission, placeholder_text = "輸入學號").grid(row=0, column=0, columnspan=3, sticky='wen', padx=10, pady=(10,0))

    # 搜尋按鈕
    btn(learner_license_submission, text='搜尋學員信息', command=lambda: None).grid(row=0, column=3, sticky='wen', padx=(0,10), pady=(10,0))
    
    # 顯示學員編號
    label(learner_license_submission, text='學員編號').grid(row=1, column=0, sticky='ws', padx=(10,0), pady=(50,0))
    display_entry_value(learner_license_submission).grid(row=2, column=0, sticky='wen', padx=10)

    # 顯示學員姓名
    label(learner_license_submission, text='學員姓名').grid(row=1, column=1, sticky='ws', pady=(10,0))
    display_entry_value(learner_license_submission).grid(row=2, column=1, sticky='wen', padx=(0,10))

    # 顯示學員身分證號碼
    label(learner_license_submission, text='身分證號').grid(row=1, column=2, sticky='ws',pady=(10,0))
    display_entry_value(learner_license_submission).grid(row=2, column=2, sticky='wen', padx=(0,10))

    # 顯示學員電話
    label(learner_license_submission, text='聯絡電話').grid(row=1, column=3, sticky='ws', pady=(10,0))
    display_entry_value(learner_license_submission).grid(row=2, column=3, sticky='wen', padx=(0,10))

    # 顯示學員出生日期
    label(learner_license_submission, text='出生日期').grid(row=3, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    display_entry_value(learner_license_submission).grid(row=4, column=0, sticky='wen', padx=10)

    # 學員信箱
    label(learner_license_submission, text='學員信箱').grid(row=3, column=1, sticky='ws', pady=(10,0))
    display_entry_value(learner_license_submission).grid(row=4, column=1, sticky='wen', padx=(0,10))

    # 備註
    label(learner_license_submission, text='備註').grid(row=3, column=2, sticky='ws',pady=(10,0))
    display_entry_value(learner_license_submission, width=55).grid(row=4, column=2, columnspan=2, sticky='wen', padx=(0,10))

    # 顯示學員戶籍地址
    label(learner_license_submission, text='戶籍地址').grid(row=5, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    display_entry_value(learner_license_submission).grid(row=6, column=0, sticky='wen', padx=10)
    display_entry_value(learner_license_submission).grid(row=6, column=1, sticky='wen', padx=(0,10))
    display_entry_value(learner_license_submission).grid(row=6, column=2, columnspan=2, sticky='wen', padx=(0,10))
    
    # 送件日期
    label(learner_license_submission, text='送件日期').grid(row=7, column=0, sticky='ws', padx=(10,0), pady=(50,0))
    entry(learner_license_submission).grid(row=8, column=0, columnspan=2, sticky='wen', padx=10)

    # 學照資料送件
    btn(learner_license_submission, text='送件', command=lambda: None).grid(row=8, column=2, sticky='wen', padx=(0,10))
    export_btn(learner_license_submission, text='匯出文件', command=lambda: None).grid(row=8, column=3, sticky='wen', padx=(0,10))
    
    

    # 登錄後顯示信息列表
    data_list = ttk.Treeview(learner_license_submission, show='headings', columns=('id', 'learner_license_date', 'learner_license_number', 'learner_license_type', 'students_number', 'students_name','birth_date', 'national_id_no', 'phone','address'))
    
    data_list.column('id', width=50, anchor='w')
    data_list.column('learner_license_date', width=50, anchor='w')
    data_list.column('learner_license_number', width=50, anchor='w')
    data_list.column('learner_license_type', width=50, anchor='w')
    data_list.column('students_number', width=50, anchor='w')
    data_list.column('students_name', width=50, anchor='w')
    data_list.column('birth_date', width=50, anchor='w')
    data_list.column('national_id_no', width=60, anchor='w')
    data_list.column('phone', width=50, anchor='w')
    data_list.column('address', width=250, anchor='w')
    
    data_list.heading('id', text='ID')
    data_list.heading('learner_license_date', text='學照日期')
    data_list.heading('learner_license_number', text='學照號碼')
    data_list.heading('learner_license_type', text='考照類別')
    data_list.heading('students_number', text='學員編號')
    data_list.heading('students_name', text='學員姓名')
    data_list.heading('birth_date', text='出生日期')
    data_list.heading('national_id_no', text='身分證號')
    data_list.heading('phone', text='聯絡電話')
    data_list.heading('address', text='戶籍地址')
    
    data_list.grid(row=9, column=0, columnspan=4, sticky='wen', padx=10, pady=(20,0))
    
    for i in range(100):  # 生成100行数据来测试滚动条
        data_list.insert("", "end", values=(f"202{i % 10}", f"張{i}", f"A{i}", f"202{i % 10}-01-01", f"男", f"02{i % 10}", f"09{i % 10}", f"test{i}@gmail.com", f"台北市", f"台北市"))