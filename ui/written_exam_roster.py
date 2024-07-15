# 筆試清冊
from utils.widget import *
from utils.config import *
from models.test import *

def written_exam_roster(content):
    clear_frame(content)

    written_exam_roster = frame(content)
    written_exam_roster.columnconfigure(0, weight=1)
    written_exam_roster.columnconfigure(1, weight=1)
    written_exam_roster.columnconfigure(2, weight=1)
    written_exam_roster.columnconfigure(3, weight=1)
    written_exam_roster.place(relwidth=1, relheight=1)

    # 學員編號
    label(written_exam_roster, text='學員編號').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    student_number = entry(written_exam_roster,  placeholder_text = "輸入學員編號")
    student_number.grid(row=1, column=0, sticky='wen', padx=(10,0))
    # student_number.bind("<KeyRelease>", lambda event: populate_student_data('student_number', student_number.get()))
    
    # 學員姓名
    label(written_exam_roster, text='學員姓名').grid(row=0, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    student_name = display_entry_value(written_exam_roster)
    student_name.grid(row=1, column=1, sticky='wen', padx=(10,0))

    # 名冊號碼
    label(written_exam_roster, text='名冊號碼').grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    register_number = display_entry_value(written_exam_roster)
    register_number.grid(row=1, column=2, sticky='wen', padx=(10,0))

    # 身分證號碼
    label(written_exam_roster, text='身分證號碼').grid(row=0, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    national_id_no = display_entry_value(written_exam_roster)
    national_id_no.grid(row=1, column=3, sticky='wen',padx=(10,0))

    # 出生日期
    label(written_exam_roster, text='出生日期').grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    birth_date = display_entry_value(written_exam_roster)
    birth_date.grid(row=3, column=0, sticky='wen',padx=(10,0))

    # 訓練班別
    label(written_exam_roster, text='訓練班別').grid(row=2, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    training_type_code = display_entry_value(written_exam_roster)
    training_type_code.grid(row=3, column=1, sticky='wen',padx=(10,0))
    training_type_name = display_entry_value(written_exam_roster)
    training_type_name.grid(row=3, column=2, sticky='wen',padx=(10,0))
    # combobox(written_exam_roster, values=['1']).grid(row=6, column=0, sticky='wen',padx=10)
    # combobox(written_exam_roster, values=['普通小型車班']).grid(row=6, column=1, sticky='wen',padx=10)
    
    # 期別
    label(written_exam_roster, text='期別').grid(row=2, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    register_term = display_entry_value(written_exam_roster)
    register_term.grid(row=3, column=3, sticky='wen',padx=(10,0))

    # 梯次
    label(written_exam_roster, text='梯次').grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    batch = display_entry_value(written_exam_roster)
    batch.grid(row=5, column=0, sticky='wen',padx=(10,0))

    # 路試日期
    label(written_exam_roster, text='路試日期').grid(row=4, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    road_test_date = entry(written_exam_roster)
    road_test_date.grid(row=5, column=1, sticky='wen',padx=(10,0))

    # 組別
    label(written_exam_roster, text='組別').grid(row=4, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    driving_test_group = entry(written_exam_roster)
    driving_test_group.grid(row=5, column=2, sticky='wen',padx=(10,0))

    # 路考項目
    label(written_exam_roster, text='路考項目').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    road_test_items_type = combobox(written_exam_roster, values=['1', '2', '3'])
    road_test_items_type.grid(row=7, column=0, sticky='wen',padx=(10,0))

    # 號碼
    label(written_exam_roster, text='號碼').grid(row=6, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    driving_test_number = entry(written_exam_roster)
    driving_test_number.grid(row=7, column=1, sticky='wen',padx=(10,0))

    # 新增按鈕
    add_btn(written_exam_roster, text='新增道考清冊', command=lambda: None).grid(row=8, column=1, sticky='wen', padx=(10,0), pady=(20,0))

    # 列印按鈕
    print_btn(written_exam_roster, text='列印場考清冊', command=lambda: None).grid(row=8, column=2, sticky='wen', padx=(10,0), pady=(20,0))

    # 匯出按鈕
    export_btn(written_exam_roster, text='匯出文件', command=lambda: None).grid(row=8, column=3, sticky='wen', padx=10, pady=(20,0))

    # treeview
    data_list = ttk.Treeview(written_exam_roster, show='headings', column=['id', 'roster_number', 'batch', 'student_number', 'student_name', 'exam_source_type', 'transmission_type', 'instructor', 'gender', 'birth_date', 'national_id_no', 'zip_code', 'city_r_address', 'training_type'])
    
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
    
    data_list.grid(row=9, column=0, columnspan=4, sticky='wen', padx=10, pady=(20,0))
    
    for i in range(100):
        data_list.insert("", "end", values=(f"202{i % 10}", f"張{i}", f"A{i}", f"202{i % 10}-01-01", f"男", f"02{i % 10}", f"09{i % 10}", f"test{i}@gmail.com", f"台北市", f"台北市"))