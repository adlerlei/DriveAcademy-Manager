# 開訓名冊
from utils.widget import *
from utils.config import *


# 開訓名冊建立後需要將資料顯示欄位的名冊號碼與學員資料綁定

def opening_training_roster(content):
    clear_frame(content)
    
    window_title = label_frame(content, '  開訓名冊資料作業  ')
    window_title.pack(fill='x', padx=(20,20), pady=(10,0))
    

    row1 = frame(window_title)
    row1.pack(fill='x', padx=(30, 0), pady=(30, 0))
    # 學員編號
    label(row1, text='學員編號：').pack(side='left', padx=(20, 0))
    entry(row1, width=10).pack(side='left')
    # 搜尋按鈕
    search_btn(row1, text='搜尋學員信息').pack(side='left', padx=(20, 0))
    
    
    # 學員信息資料顯示
    row5 = frame(window_title)
    row5.pack(fill='x', padx=(30, 0), pady=(30, 0))
    # 學員姓名
    label(row5, text='學員姓名：').pack(side='left', padx=(20,0))
    display_entry_value(row5, width=10).pack(side='left')
    # 顯示學員身分證號碼
    label(row5, text='身分證號：').pack(side='left', padx=(20, 0))
    display_entry_value(row5, width=10).pack(side='left')
    # 名冊號碼
    label(row5, text='名冊號碼：').pack(side='left', padx=(20, 0))
    display_entry_value(row5, width=10).pack(side='left')
    

    row6 = frame(window_title)
    row6.pack(fill='x', padx=(30, 0), pady=(20, 0))
    # 出生日期
    label(row6, text='出生日期：').pack(side='left', padx=(20, 0))
    display_entry_value(row6, width=8).pack(side='left')
    # 學照日期
    label(row6, text='學照日期：').pack(side='left', padx=(20, 0))
    display_entry_value(row6, width=8).pack(side='left')
    # 性別
    label(row6, text='性別：').pack(side='left', padx=(20, 0))
    display_entry_value(row6, width=8).pack(side='left')
    # 梯次
    label(row6, text='梯次：').pack(side='left', padx=(20, 0))
    display_entry_value(row6, width=8).pack(side='left')

    row7 = frame(window_title)
    row7.pack(fill='x', padx=(30, 0), pady=(20, 0))
    # 區號
    label(row7, text='區號：').pack(side='left', padx=(20, 0))
    display_entry_value(row7, width=8).pack(side='left')
    # 戶籍地址
    label(row7, text='戶籍地址：').pack(side='left', padx=(20, 0))
    display_entry_value(row7, width=45).pack(side='left')
    

    row5 = frame(window_title)
    row5.pack(fill='x', padx=(30, 0), pady=(30, 0))
    # 訓練班別（抓取資料庫呈現）
    label(row5, text='訓練班別：').pack(side='left', padx=(20,0))
    combobox(row5, width=3, values=['1','2','3']).pack(side='left')
    entry(row5, width=15).pack(side='left')
    # 名冊期別
    label(row5, text='名冊期別：').pack(side='left', padx=(20, 0))
    entry(row5, width=8).pack(side='left')
    # 梯次下拉選單
    label(row5, text='梯次：').pack(side='left', padx=(20, 0))
    combobox(row5, width=3, values=['A', 'B']).pack(side='left')
    


    row6 = frame(window_title)
    row6.pack(fill='x', padx=(30, 0), pady=(30, 0))
    # 來源 下拉選單
    label(row6, text='來源：').pack(side='left', padx=(20, 0))
    combobox(row6, width=3, values=['A', 'B']).pack(side='left')
    # 手自排 下拉選單
    label(row6, text='手自排：').pack(side='left', padx=(20, 0))
    combobox(row6, width=3, values=['A', 'B']).pack(side='left')
    # 教練 下拉選單
    label(row6, text='教練：').pack(side='left', padx=(20, 0))
    combobox(row6, width=3, values=['A', 'B']).pack(side='left')
    
    
    # 加入開訓名冊按鈕
    add_btn(row6, text='將該學員加入開訓名冊', command=lambda: None).pack(side='left', padx=(20, 0))
    
    
    # 第4行 frame 所有欄位顯示 treeview
    row8 = frame(window_title)
    row8.pack(fill='x', padx=(30, 0), pady=(20, 0))
    # treeview
    data_list = ttk.Treeview(row8, show='headings', column=['id', 'roster_number', 'batch', 'student_number', 'student_name', 'exam_source_type', 'transmission_type', 'instructor', 'gender', 'birth_date', 'national_id_no', 'zip_code', 'city_r_address', 'training_type'])
    
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
    
    data_list.pack(side="left", fill="both", expand=True, padx=(20,30), pady=(20,50))
    
    for i in range(100):  # 生成100行数据来测试滚动条
        data_list.insert("", "end", values=(f"202{i % 10}", f"張{i}", f"A{i}", f"202{i % 10}-01-01", f"男", f"02{i % 10}", f"09{i % 10}", f"test{i}@gmail.com", f"台北市", f"台北市"))