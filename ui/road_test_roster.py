# 道考清冊
from utils.widget import *
from utils.config import *
from models.test import *
import customtkinter as ctk
from tkinter import messagebox

# 檢測學員資料庫 id 欄位來判定是否修改或新增
current_student_id = None

def  road_test_roster(content):
    clear_frame(content)

    road_test_roster = frame(content)
    road_test_roster.columnconfigure(0, weight=1)
    road_test_roster.columnconfigure(1, weight=1)
    road_test_roster.columnconfigure(2, weight=1)
    road_test_roster.columnconfigure(3, weight=1)
    road_test_roster.place(relwidth=1, relheight=1)

    # 學員編號
    label(road_test_roster, text='學員編號').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    student_number = entry(road_test_roster,  placeholder_text = "輸入學員編號")
    student_number.grid(row=1, column=0, sticky='wen', padx=(10,0))
    # student_number.bind("<KeyRelease>", lambda event: populate_student_data('student_number', student_number.get()))
    
    # 學員姓名
    label(road_test_roster, text='學員姓名').grid(row=0, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    student_name = display_entry_value(road_test_roster)
    student_name.grid(row=1, column=1, sticky='wen', padx=(10,0))

    # 名冊號碼
    label(road_test_roster, text='名冊號碼').grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    register_number = display_entry_value(road_test_roster)
    register_number.grid(row=1, column=2, sticky='wen', padx=(10,0))

    # 身分證號碼
    label(road_test_roster, text='身分證號碼').grid(row=0, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    national_id_no = display_entry_value(road_test_roster)
    national_id_no.grid(row=1, column=3, sticky='wen',padx=(10,0))

    # 出生日期
    label(road_test_roster, text='出生日期').grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    birth_date = display_entry_value(road_test_roster)
    birth_date.grid(row=3, column=0, sticky='wen',padx=(10,0))

    # 訓練班別
    label(road_test_roster, text='訓練班別').grid(row=2, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    training_type_code = display_entry_value(road_test_roster)
    training_type_code.grid(row=3, column=1, sticky='wen',padx=(10,0))
    training_type_name = display_entry_value(road_test_roster)
    training_type_name.grid(row=3, column=2, sticky='wen',padx=(10,0))
    # combobox(road_test_roster, values=['1']).grid(row=6, column=0, sticky='wen',padx=10)
    # combobox(road_test_roster, values=['普通小型車班']).grid(row=6, column=1, sticky='wen',padx=10)
    
    # 期別
    label(road_test_roster, text='期別').grid(row=2, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    register_term = display_entry_value(road_test_roster)
    register_term.grid(row=3, column=3, sticky='wen',padx=(10,0))

    # 梯次
    label(road_test_roster, text='梯次').grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    batch = display_entry_value(road_test_roster)
    batch.grid(row=5, column=0, sticky='wen',padx=(10,0))

    # 路試日期
    label(road_test_roster, text='路試日期').grid(row=4, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    road_test_date = entry(road_test_roster) 
    road_test_date.grid(row=5, column=1, sticky='wen',padx=(10,0))

    # 組別
    label(road_test_roster, text='組別').grid(row=4, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    driving_test_group = entry(road_test_roster)
    driving_test_group.grid(row=5, column=2, sticky='wen',padx=(10,0))

    # 路考項目
    label(road_test_roster, text='路考項目').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    road_test_items_type = combobox(road_test_roster, values=['1', '2', '3'])
    road_test_items_type.grid(row=7, column=0, sticky='wen',padx=(10,0))

    # 號碼
    label(road_test_roster, text='號碼').grid(row=6, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    driving_test_number = entry(road_test_roster)
    driving_test_number.grid(row=7, column=1, sticky='wen',padx=(10,0))

    # treeview
    columns = (
        'treeview_number', # 路號碼
        'student_number', # 學員編號
        'register_number', # 名冊號碼
        'batch', # 梯次
        'student_name', # 學員姓名
        'birth_date', # 出生日期
        'national_id_no', # 身分證號碼
        'road_test_date', # 路試日期
        'road_test_items_type', # 路考項目
    )
    data_list = ttk.Treeview(road_test_roster, show='headings', column=columns)
    
    data_list.column('treeview_number', width=50, anchor='w')
    data_list.column('student_number', width=50, anchor='w')
    data_list.column('register_number', width=50, anchor='w')
    data_list.column('batch', width=50, anchor='w')
    data_list.column('student_name', width=50, anchor='w')
    data_list.column('birth_date', width=50, anchor='w')
    data_list.column('national_id_no', width=50, anchor='w')
    data_list.column('road_test_date', width=50, anchor='w')
    data_list.column('road_test_items_type', width=50, anchor='w')
    
    data_list.heading('treeview_number', text='號碼')
    data_list.heading('student_number', text='學員編號')
    data_list.heading('register_number', text='名冊號碼')
    data_list.heading('batch', text='梯次')
    data_list.heading('student_name', text='學員姓名')
    data_list.heading('birth_date', text='出生日期')
    data_list.heading('national_id_no', text='身分證號碼')
    data_list.heading('road_test_date', text='路試日期')
    data_list.heading('road_test_items_type', text='路考項目')

    data_list.grid(row=9, column=0, columnspan=4, sticky='wen', padx=10, pady=(20,0))
    
    # 邏輯功能 - 搜尋學員資料並顯示在 entry 
    def populate_student_data(identifier, value):

        # 監聽學員編號輸入欄位如果為空，清除學員資料
        if identifier == 'student_number' and value == '':
            # 不保留任何欄位值，全部清除
            clear_entries_and_comboboxes(road_test_roster)
        else:
            global current_student_id
            student_data = get_student_data(identifier, value)
            if student_data:
                # 獲取學員資料庫 id 序列
                current_student_id = student_data[0]
                # 學員姓名
                student_name.configure(state='normal')
                student_name.delete(0, ctk.END)
                student_name.insert(0, student_data[6])
                student_name.configure(state='readonly')
                # 名冊號碼
                register_number.configure(state='readonly')
                register_number.configure(state='normal')
                register_number.delete(0, ctk.END)
                register_number.insert(0, student_data[34])
                register_number.configure(state='readonly')
                # 身分證號碼
                national_id_no.configure(state='normal')
                national_id_no.delete(0, ctk.END)
                national_id_no.insert(0, student_data[10])
                national_id_no.configure(state='readonly')
                # 出生日期
                birth_date.configure(state='normal')
                birth_date.delete(0, ctk.END)
                birth_date.insert(0, student_data[9])
                birth_date.configure(state='readonly')
                # 訓練班別代號
                training_type_code.configure(state='normal')
                training_type_code.delete(0, ctk.END)
                training_type_code.insert(0, student_data[3])
                training_type_code.configure(state='readonly')
                # 訓練班別名稱
                training_type_name.configure(state='normal')
                training_type_name.delete(0, ctk.END)
                training_type_name.insert(0, student_data[4])
                training_type_name.configure(state='readonly')
                # 期別
                register_term.configure(state='normal')
                register_term.delete(0, ctk.END)
                if student_data[35] is not None:
                    register_term.insert(0, student_data[35])
                else:
                    register_term.insert(0, '')
                register_number.configure(state='readonly')
                # 梯次
                batch.configure(state='normal')
                batch.delete(0, ctk.END)
                batch.insert(0, student_data[7])
                batch.configure(state='readonly')
                
                                    


    # 獲取輸入欄位信息
    def save_student_data():
        global current_student_id
        student_data = {
            # 獲取輸入欄位信息並呈現在 treeview
            'register_number': register_number.get(), # 名冊號碼
            'student_number': student_number.get(), # 學員編號
            'batch': batch.get(), # 梯次
            'student_name': student_name.get(), # 學員姓名
            'exam_code': exam_code.get(), # 來源代號
            'exam_name': exam_name.get(), # 來源名稱
            'exam_type_name': exam_type_name.get(), # 筆路
            'transmission_type_code': transmission_type_code.get(), # 手自排代號
            'transmission_type_name': transmission_type_name.get(), # 手自排名稱
            'instructor_number': instructor_number.get(), # 教練代號
            'national_id_no': national_id_no.get(), # 身分證
            'instructor_name': instructor_name.get(), # 教練名稱
            'learner_permit_data': learner_permit_date.get(), # 學照日期
            'gender': gender.get(), # 性別
            'birth_date': birth_date.get(), # 生日
            'register_term': register_term.get(), # 期別
            'r_address_zip_code': r_address_zip_code.get(), # 郵遞區號
            'r_address_city': r_address_city.get(), # 縣市區域
            'r_address': r_address.get(), # 戶籍地址
            'r_address_city_road': r_address_city.get() + r_address.get(), # 將縣市區域加上地址組合
            'training_type_code': training_type_code.get(), # 訓練班別代號
            'id': current_student_id
        }

        # 驗證 筆路 輸入欄位是否為空
        required_fields = [ 
            'exam_type_name',
        ]
        for field in required_fields:
            if not student_data[field]:
                messagebox.showwarning('提示', f'{validation_fields[field]} 欄位不能為空！')
                return

        if current_student_id is None:
            messagebox.showwarning('警告', '請先搜尋學員資料！')
            return
        
        update_student_data(student_data)
        clear_entries_and_comboboxes(m2_retraining_roster_creation)

        # 讀取 save_student_data 的資料寫入 treeview
        data_list.insert('', 'end', values = (
            student_data['register_number'],
            student_data['student_number'],
            student_data['batch'],
            student_data['student_name'],
            student_data['exam_code'],
            student_data['transmission_type_code'],
            student_data['instructor_number'],
            student_data['national_id_no'],
            student_data['learner_permit_data'],
            student_data['gender'],
            student_data['birth_date'],
            student_data['r_address_zip_code'],
            student_data['r_address_city_road'],
            student_data['training_type_code'] # 添加訓練班別代號
        ))

    # 新增按鈕
    add_btn(road_test_roster, text='新增道考清冊', command=lambda: None).grid(row=8, column=1, sticky='wen', padx=(10,0), pady=(20,0))

    # 列印按鈕
    print_btn(road_test_roster, text='列印場考清冊', command=lambda: None).grid(row=8, column=2, sticky='wen', padx=(10,0), pady=(20,0))

    # 匯出按鈕
    export_btn(road_test_roster, text='匯出文件', command=lambda: None).grid(row=8, column=3, sticky='wen', padx=10, pady=(20,0))