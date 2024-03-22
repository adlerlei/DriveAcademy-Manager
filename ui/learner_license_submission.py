# 學習駕照統一送件
from utils.widget import *
from utils.config import *

def learner_license_submission(content):
    clear_frame(content)
    
    clear_frame(content)
    
    window_title = label_frame(content, "  學習駕照統一送件  ", fg=font_color['學習駕照'])
    window_title.pack(fill='x', padx=(20,20), pady=(10,0))
    
    row1 = frame(window_title)
    row1.pack(fill='x', padx=(30, 0), pady=(30, 0))
    # 輸入學號
    label(row1, text='輸入學號：', fg=font_color['label_font']).pack(side='left', padx=(20, 0))
    entry(row1, width=10).pack(side='left')
    # 搜尋按鈕
    search_btn(row1, text='搜尋學員信息').pack(side='left', padx=(20, 0))
    
    # 顯示學員資料說明文字
    # display_student_info_title= frame(window_title)
    # display_student_info_title.pack(fill='x', padx=(30, 20), pady=(40, 0))
    # display_info_label(display_student_info_title, text='學員資料顯示區').pack(side='left', padx=(20, 0))
    
    row2 = frame(window_title)
    row2.pack(fill='x', padx=(30, 0), pady=(30, 0))
    # 顯示學員編號
    label(row2, text='學員編號：').pack(side='left', padx=(20, 0))
    display_entry_value(row2, width=10).pack(side='left')
    # 顯示學員姓名
    label(row2, text='學員姓名：').pack(side='left', padx=(20, 0))
    display_entry_value(row2, width=10).pack(side='left')
    # 顯示學員出生日期
    label(row2, text='出生日期：').pack(side='left', padx=(20, 0))
    display_entry_value(row2, width=10).pack(side='left')
    
    row3 = frame(window_title)
    row3.pack(fill='x', padx=(30, 0), pady=(20, 0))
    # 顯示考照類別
    label(row3, text='學員信箱：').pack(side='left', padx=(20, 0))
    display_entry_value(row3, width=10).pack(side='left')
    # 顯示學員身分證號碼
    label(row3, text='身分證號：').pack(side='left', padx=(20, 0))
    display_entry_value(row3, width=10).pack(side='left')
    # 顯示學員電話
    label(row3, text='聯絡電話：').pack(side='left', padx=(20, 0))
    display_entry_value(row3, width=10).pack(side='left')
    
    row4 = frame(window_title)
    row4.pack(fill='x', padx=(30, 0), pady=(20, 0))
    # 顯示學員戶籍地址
    label(row4, text='戶籍地址：').pack(side='left', padx=(20, 0))
    display_entry_value(row4, width=3).pack(side='left')
    display_entry_value(row4, width=15).pack(side='left')
    display_entry_value(row4, width=32).pack(side='left')
    

    row5= frame(window_title)
    row5.pack(fill='x', padx=(30, 20), pady=(20, 0))
    # 備註
    label(row5, text='備註：').pack(side='left', padx=(20, 0))
    display_entry_value(row5, width=55).pack(side='left')
    
    # 說明文字
    # display_input_info_title= frame(window_title)
    # display_input_info_title.pack(fill='x', padx=(30, 20), pady=(40, 0))
    # display_info_label(display_input_info_title, text='輸入資料區').pack(side='left', padx=(20, 0))
    
    
    row6 = frame(window_title)
    row6.pack(fill='x', padx=(30,0), pady=(30,0))
    # 送件日期
    label(row6, text='登入日期：').pack(side='left', padx=(20, 0))
    entry(row6, width=10).pack(side='left')
    # 學照資料登錄
    add_btn(row6, text='學照送件加入', command=lambda: None).pack(side='left', padx=(20, 0))
    
    
    row7 = frame(window_title)
    row7.pack(fill='x', padx=(30, 0), pady=(20, 0))
    # 登錄後顯示信息列表
    data_list = ttk.Treeview(row7, show='headings', columns=('id', 'learner_license_date', 'learner_license_number', 'learner_license_type', 'students_number', 'students_name','birth_date', 'national_id_no', 'phone','address'))
    
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
    
    data_list.pack(side="left", fill="both", expand=True, padx=(20,30), pady=(20,50))
    
    for i in range(100):  # 生成100行数据来测试滚动条
        data_list.insert("", "end", values=(f"202{i % 10}", f"張{i}", f"A{i}", f"202{i % 10}-01-01", f"男", f"02{i % 10}", f"09{i % 10}", f"test{i}@gmail.com", f"台北市", f"台北市"))