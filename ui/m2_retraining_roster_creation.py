# 監理站M2補訓名冊
from utils.widget import *
from utils.config import *


def  m2_retraining_roster_creation(content):
    clear_frame(content)
    
    m2_retraining_roster_creation = frame(content)
    m2_retraining_roster_creation.columnconfigure(0, weight=1)
    m2_retraining_roster_creation.columnconfigure(1, weight=1)
    m2_retraining_roster_creation.columnconfigure(2, weight=1)
    m2_retraining_roster_creation.columnconfigure(3, weight=1)
    m2_retraining_roster_creation.place(relwidth=1, relheight=1)

    entry(m2_retraining_roster_creation,  placeholder_text = "輸入學員編號").grid(row=0, column=0, columnspan=3, sticky='wen', padx=10, pady=(10,0))
    # 搜尋按鈕
    btn(m2_retraining_roster_creation, text='搜尋學員信息', command=lambda: None).grid(row=0, column=3, sticky='wen', padx=(0,10), pady=(10,0))
    
    # 學員姓名
    label(m2_retraining_roster_creation, text='學員姓名').grid(row=1, column=0, sticky='ws', padx=(10,0), pady=(50,0))
    display_entry_value(m2_retraining_roster_creation).grid(row=2, column=0, sticky='wen', padx=(10,0))

    # 顯示學員身分證號碼
    label(m2_retraining_roster_creation, text='身分證號').grid(row=1, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    display_entry_value(m2_retraining_roster_creation).grid(row=2, column=1, sticky='wen', padx=(10,0))

    # 名冊號碼
    label(m2_retraining_roster_creation, text='名冊號碼').grid(row=1, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    display_entry_value(m2_retraining_roster_creation).grid(row=2, column=2, sticky='wen',padx=(10,0))

    # 性別
    label(m2_retraining_roster_creation, text='性別').grid(row=1, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    display_entry_value(m2_retraining_roster_creation).grid(row=2, column=3, sticky='wen',padx=10)
    
    # 出生日期
    label(m2_retraining_roster_creation, text='出生日期').grid(row=3, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    display_entry_value(m2_retraining_roster_creation).grid(row=4, column=0, sticky='wen',padx=(10,0))

    # 學照日期
    label(m2_retraining_roster_creation, text='學照日期').grid(row=3, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    display_entry_value(m2_retraining_roster_creation).grid(row=4, column=1, sticky='wen',padx=(10,0))

    # 梯次
    label(m2_retraining_roster_creation, text='梯次').grid(row=3, column=2, sticky='ws', padx=10, pady=(10,0))
    display_entry_value(m2_retraining_roster_creation).grid(row=4, column=2, columnspan=2, sticky='wen',padx=10)

    # 戶籍地址
    label(m2_retraining_roster_creation, text='戶籍地址').grid(row=5, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    display_entry_value(m2_retraining_roster_creation).grid(row=6, column=0, sticky='wen',padx=(10,0))
    display_entry_value(m2_retraining_roster_creation).grid(row=6, column=1, sticky='wen',padx=(10,0))
    display_entry_value(m2_retraining_roster_creation).grid(row=6, column=2, columnspan=2, sticky='wen',padx=10)
    
    # 訓練班別
    label(m2_retraining_roster_creation, text='訓練班別').grid(row=7, column=0, sticky='ws', padx=(10,0), pady=(50,0))
    combobox(m2_retraining_roster_creation, values=['1','2','3']).grid(row=8, column=0, sticky='wen',padx=(10,0))
    entry(m2_retraining_roster_creation).grid(row=8, column=1, sticky='wen',padx=(10,0))

    # 名冊期別
    label(m2_retraining_roster_creation, text='名冊期別').grid(row=7, column=2, sticky='ws', padx=(10,0))
    entry(m2_retraining_roster_creation).grid(row=8, column=2, sticky='wen',padx=(10,0))

    # 梯次
    label(m2_retraining_roster_creation, text='梯次').grid(row=7, column=3, sticky='ws', padx=(10,0))
    combobox(m2_retraining_roster_creation, values=['A', 'B']).grid(row=8, column=3, sticky='wen',padx=10)
    
    # 來源 下拉選單
    label(m2_retraining_roster_creation, text='來源').grid(row=9, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    combobox(m2_retraining_roster_creation, values=['A', 'B']).grid(row=10, column=0, sticky='wen',padx=(10,0))

    # 手自排 下拉選單
    label(m2_retraining_roster_creation, text='手自排').grid(row=9, column=1, sticky='ws', padx=(10,0))
    combobox(m2_retraining_roster_creation, values=['A', 'B']).grid(row=10, column=1, sticky='wen',padx=(10,0))

    # 教練 下拉選單
    label(m2_retraining_roster_creation, text='教練').grid(row=9, column=2, sticky='ws', padx=(10,0))
    combobox(m2_retraining_roster_creation, values=['A', 'B']).grid(row=10, column=2, sticky='wen',padx=(10,0))
    entry(m2_retraining_roster_creation).grid(row=10, column=3, sticky='wen',padx=10)

    # 筆試路試
    label(m2_retraining_roster_creation, text='筆路').grid(row=11, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    combobox(m2_retraining_roster_creation, values=['補筆', '補路']).grid(row=12, column=0, columnspan=2, sticky='wen',padx=(10,0))

    # 資料選擇
    label(m2_retraining_roster_creation, text='資料選擇').grid(row=11, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    combobox(m2_retraining_roster_creation, values=['1.全部', '2.補筆', '3.補路']).grid(row=12, column=2, columnspan=2, sticky='wen', padx=10)

    # 按鈕
    btn(m2_retraining_roster_creation, text='加入補訓名冊', command=lambda: None).grid(row=13, column=0, columnspan=4, sticky='wen', padx=10, pady=20)

    # treeview
    data_list = ttk.Treeview(m2_retraining_roster_creation, show='headings', column=['id', 'roster_number', 'batch', 'student_number', 'student_name', 'exam_source_type', 'transmission_type', 'instructor', 'gender', 'birth_date', 'national_id_no', 'zip_code', 'city_r_address', 'training_type'])
    
    data_list.column('id', width=50, anchor='w')
    data_list.column('roster_number', width=50, anchor='w')
    data_list.column('batch', width=50, anchor='w')
    data_list.column('student_number', width=50, anchor='w')
    data_list.column('student_name', width=50, anchor='w')
    data_list.column('exam_source_type', width=50, anchor='w')
    data_list.column('transmission_type', width=50, anchor='w')
    data_list.column('instructor', width=50, anchor='w')
    data_list.column('gender', width=50, anchor='w')
    data_list.column('birth_date', width=50, anchor='w')
    data_list.column('national_id_no', width=60, anchor='w')
    data_list.column('training_type', width=50, anchor='w')
    data_list.column('zip_code', width=50, anchor='w')
    data_list.column('city_r_address', width=250, anchor='w')
    
    data_list.heading('id', text='ID')
    data_list.heading('roster_number', text='名冊號碼')
    data_list.heading('batch', text='梯次')
    data_list.heading('student_number', text='學員編號')
    data_list.heading('student_name', text='學員姓名')
    data_list.heading('exam_source_type', text='來源')
    data_list.heading('transmission_type', text='手自排')
    data_list.heading('instructor', text='教練')
    data_list.heading('gender', text='性別')
    data_list.heading('birth_date', text='出生日期')
    data_list.heading('national_id_no', text='身分證號')
    data_list.heading('training_type', text='訓練班別')
    data_list.heading('zip_code', text='區號')
    data_list.heading('city_r_address', text='戶籍地址')
    
    data_list.grid(row=14, column=0, columnspan=4, sticky='wen', padx=10)
    
    for i in range(100):
        data_list.insert("", "end", values=(f"202{i % 10}", f"張{i}", f"A{i}", f"202{i % 10}-01-01", f"男", f"02{i % 10}", f"09{i % 10}", f"test{i}@gmail.com", f"台北市", f"台北市"))