# 開訓名冊
from utils.widget import *
from utils.config import *


# 開訓名冊建立後需要將資料顯示欄位的名冊號碼與學員資料綁定

def opening_training_roster(content):
    clear_frame(content)
    
    opening_training_roster = frame(content)
    opening_training_roster.columnconfigure(0, weight=1)
    opening_training_roster.columnconfigure(1, weight=1)
    opening_training_roster.columnconfigure(2, weight=1)
    opening_training_roster.columnconfigure(3, weight=1)
    opening_training_roster.place(relwidth=1, relheight=1)

    entry(opening_training_roster,  placeholder_text = "輸入學員編號").grid(row=0, column=0, columnspan=3, sticky='wen', padx=10, pady=(10,0))
    # 搜尋按鈕
    btn(opening_training_roster, text='搜尋學員信息', command=lambda: None).grid(row=0, column=3, sticky='wen', padx=(0,10), pady=(10,0))
    
    # 學員姓名
    label(opening_training_roster, text='學員姓名').grid(row=1, column=0, sticky='ws', padx=(10,0), pady=(50,0))
    display_entry_value(opening_training_roster).grid(row=2, column=0, sticky='wen', padx=(10,0))

    # 顯示學員身分證號碼
    label(opening_training_roster, text='身分證號').grid(row=1, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    display_entry_value(opening_training_roster).grid(row=2, column=1, sticky='wen', padx=(10,0))

    # 名冊號碼
    label(opening_training_roster, text='名冊號碼').grid(row=1, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    display_entry_value(opening_training_roster).grid(row=2, column=2, sticky='wen',padx=(10,0))

    # 性別
    label(opening_training_roster, text='性別').grid(row=1, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    display_entry_value(opening_training_roster).grid(row=2, column=3, sticky='wen',padx=10)
    
    # 出生日期
    label(opening_training_roster, text='出生日期').grid(row=3, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    display_entry_value(opening_training_roster).grid(row=4, column=0, sticky='wen',padx=(10,0))

    # 學照日期
    label(opening_training_roster, text='學照日期').grid(row=3, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    display_entry_value(opening_training_roster).grid(row=4, column=1, sticky='wen',padx=(10,0))

    # 梯次
    label(opening_training_roster, text='梯次').grid(row=3, column=2, sticky='ws', padx=10, pady=(10,0))
    display_entry_value(opening_training_roster).grid(row=4, column=2, columnspan=2, sticky='wen',padx=10)

    # 戶籍地址
    label(opening_training_roster, text='戶籍地址').grid(row=5, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    display_entry_value(opening_training_roster).grid(row=6, column=0, sticky='wen',padx=(10,0))
    display_entry_value(opening_training_roster).grid(row=6, column=1, sticky='wen',padx=(10,0))
    display_entry_value(opening_training_roster).grid(row=6, column=2, columnspan=2, sticky='wen',padx=10)
    
    # 訓練班別
    label(opening_training_roster, text='訓練班別').grid(row=7, column=0, sticky='ws', padx=(10,0), pady=(50,0))
    combobox(opening_training_roster, values=['1','2','3']).grid(row=8, column=0, sticky='wen',padx=(10,0))
    entry(opening_training_roster).grid(row=8, column=1, sticky='wen',padx=(10,0))

    # 名冊期別
    label(opening_training_roster, text='名冊期別').grid(row=7, column=2, sticky='ws', padx=(10,0))
    entry(opening_training_roster).grid(row=8, column=2, sticky='wen',padx=(10,0))

    # 梯次
    label(opening_training_roster, text='梯次：').grid(row=7, column=3, sticky='ws', padx=(10,0))
    combobox(opening_training_roster, values=['A', 'B']).grid(row=8, column=3, sticky='wen',padx=10)
    
    # 來源 下拉選單
    label(opening_training_roster, text='來源：').grid(row=9, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    combobox(opening_training_roster, values=['A', 'B']).grid(row=10, column=0, sticky='wen',padx=(10,0))

    # 手自排 下拉選單
    label(opening_training_roster, text='手自排：').grid(row=9, column=1, sticky='ws', padx=(10,0))
    combobox(opening_training_roster, values=['A', 'B']).grid(row=10, column=1, sticky='wen',padx=(10,0))

    # 教練 下拉選單
    label(opening_training_roster, text='教練：').grid(row=9, column=2, sticky='ws', padx=(10,0))
    combobox(opening_training_roster, values=['A', 'B']).grid(row=10, column=2, sticky='wen',padx=(10,0))
    entry(opening_training_roster).grid(row=10, column=3, sticky='wen',padx=10)

    # 按鈕
    btn(opening_training_roster, text='加入開訓名冊', command=lambda: None).grid(row=11, column=0,  columnspan=4,sticky='wen',padx=10, pady=20)

    # treeview
    data_list = ttk.Treeview(opening_training_roster, show='headings', column=['id', 'roster_number', 'batch', 'student_number', 'student_name', 'exam_source_type', 'transmission_type', 'instructor', 'gender', 'birth_date', 'national_id_no', 'zip_code', 'city_r_address', 'training_type'])
    
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
    
    data_list.grid(row=12, column=0, columnspan=4, sticky='wen', padx=10)
    
    for i in range(100):
        data_list.insert("", "end", values=(f"202{i % 10}", f"張{i}", f"A{i}", f"202{i % 10}-01-01", f"男", f"02{i % 10}", f"09{i % 10}", f"test{i}@gmail.com", f"台北市", f"台北市"))