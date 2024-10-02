# 道考清冊作業 介面
# 對應資料庫邏輯介面 models/test.py
# 該介面不需要匯出文件功能
from utils.widget import *
from utils.config import *
from models.test import *
import customtkinter as ctk
from tkinter import messagebox

# 檢測學員資料庫 id 欄位來判定是否修改或新增
current_student_id = None

def  road_test_roster(content):
    clear_frame(content)

    # 添加列表變數來跟蹤 treeview 號碼流水號自動增加
    current_number = [0]

    road_test_roster = frame(content)
    road_test_roster.columnconfigure(0, weight=1)
    road_test_roster.columnconfigure(1, weight=1)
    road_test_roster.columnconfigure(2, weight=1)
    road_test_roster.columnconfigure(3, weight=1)
    road_test_roster.place(relwidth=1, relheight=1)

    # 學員編號
    label(road_test_roster, text='學員編號').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    student_number = entry(road_test_roster,  placeholder_text = " 🔎")
    student_number.grid(row=1, column=0, sticky='wen', padx=(10,0))
    student_number.bind("<KeyRelease>", lambda event: populate_student_data('student_number', student_number.get()))
    
    # 學員姓名
    label(road_test_roster, text='學員姓名').grid(row=0, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    student_name = entry(road_test_roster, placeholder_text=" 🔎")
    student_name.grid(row=1, column=1, sticky='wen', padx=(10,0))
    student_name.bind("<KeyRelease>", lambda event: populate_student_data('student_name', student_name.get()))

    # 名冊號碼
    label(road_test_roster, text='名冊號碼').grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    register_number = entry(road_test_roster)
    register_number.grid(row=1, column=2, sticky='wen', padx=(10,0))

    # 身分證號碼
    label(road_test_roster, text='身分證號碼').grid(row=0, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    national_id_no = entry(road_test_roster, placeholder_text=" 🔎")
    national_id_no.grid(row=1, column=3, sticky='wen',padx=10)
    national_id_no.bind("<KeyRelease>", lambda event: populate_student_data('national_id_no', national_id_no.get()))

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
    
    # 期別
    label(road_test_roster, text='期別').grid(row=2, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    register_term = display_entry_value(road_test_roster)
    register_term.grid(row=3, column=3, sticky='wen',padx=10)

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

    # 號碼
    label(road_test_roster, text='號碼').grid(row=4, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    driving_test_number = display_entry_value(road_test_roster)
    driving_test_number.grid(row=5, column=3, sticky='wen',padx=(10,0))

    # 路考項目
    label(road_test_roster, text='路考項目').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    road_test_items_type = combobox(road_test_roster, values=['1', '2', '3'])
    road_test_items_type.grid(row=7, column=0, sticky='wen',padx=(10,0))

    # treeview
    columns = (
        'driving_test_number', # 考試號碼42
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
    
    data_list.column('driving_test_number', width=50, anchor='w')
    data_list.column('student_number', width=50, anchor='w')
    data_list.column('register_number', width=50, anchor='w')
    data_list.column('batch', width=50, anchor='w')
    data_list.column('student_name', width=50, anchor='w')
    data_list.column('birth_date', width=50, anchor='w')
    data_list.column('national_id_no', width=50, anchor='w')
    data_list.column('road_test_date', width=50, anchor='w')
    data_list.column('road_test_items_type', width=50, anchor='w')
    
    data_list.heading('driving_test_number', text='號碼')
    data_list.heading('student_number', text='學員編號')
    data_list.heading('register_number', text='名冊號碼')
    data_list.heading('batch', text='梯次')
    data_list.heading('student_name', text='學員姓名')
    data_list.heading('birth_date', text='出生日期')
    data_list.heading('national_id_no', text='身分證號碼')
    data_list.heading('road_test_date', text='路試日期')
    data_list.heading('road_test_items_type', text='路考項目')

    data_list.grid(row=9, column=0, columnspan=4, sticky='wen', padx=10, pady=(20,0))

    # 創建水平捲軸
    h_scrollbar = ttk.Scrollbar(road_test_roster, orient="horizontal", command=data_list.xview)
    data_list.configure(xscrollcommand=h_scrollbar.set)

    # 創建垂直捲軸
    v_scrollbar = ttk.Scrollbar(road_test_roster, orient="vertical", command=data_list.yview)
    data_list.configure(yscrollcommand=v_scrollbar.set)

    # 使用 grid 布局管理器來排列 Treeview 和捲軸
    h_scrollbar.grid(row=15, column=0, columnspan=4, sticky="ew", padx=10)
    v_scrollbar.grid(row=14, column=4, rowspan=2, sticky="ns", pady=10)

    # 配置行和列的權重，使其在窗口調整大小時自動調整
    road_test_roster.grid_rowconfigure(14, weight=1)
    road_test_roster.grid_columnconfigure(0, weight=1)
    road_test_roster.grid_columnconfigure(1, weight=1)
    road_test_roster.grid_columnconfigure(2, weight=1)
    road_test_roster.grid_columnconfigure(3, weight=1)
    
    # 邏輯功能 - 搜尋學員資料並顯示在 entry 
    def populate_student_data(identifier, value):

        # 監聽 學員編號 學員姓名 身份證 輸入欄位如果為空，清除學員資料
        if (identifier == 'student_number' and value == '') or \
           (identifier == 'national_id_no' and value == '') or \
           (identifier == 'student_name' and value ==''):
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
                # student_name.configure(state='readonly')
                # 名冊號碼
                register_number.configure(state='normal')
                register_number.delete(0, ctk.END)
                register_number.insert(0, student_data[34])
                #register_number.configure(state='readonly')
                # if student_data[34] is not None:
                #     register_number.delete(0, ctk.END)
                #     register_number.insert(0, student_data[34])
                # else:
                #     register_number.insert(0, '')
                # register_number.configure(state='readonly')
                # 身分證號碼
                national_id_no.configure(state='normal')
                national_id_no.delete(0, ctk.END)
                national_id_no.insert(0, student_data[10])
                # national_id_no.configure(state='readonly')
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
                # 路試日期
                road_test_date.configure(state='normal')
                road_test_date.delete(0, ctk.END)
                if student_data[37] is not None:
                    road_test_date.insert(0, student_data[37])
                else:
                    road_test_date.insert(0, '')
                # 組別
                driving_test_group.configure(state='normal')
                driving_test_group.delete(0, ctk.END)
                if student_data[38] is not None:
                    driving_test_group.insert(0, student_data[38])
                else:
                    driving_test_group.insert(0, '')
                # 路考項目
                if student_data[39] is not None:
                    road_test_items_type.set(student_data[39])
                else:
                    road_test_items_type.set('')
                # 號碼
                driving_test_number.configure(state='normal')
                driving_test_number.delete(0, ctk.END)
                if student_data[41] is not None:
                    driving_test_number.insert(0, student_data[41])
                else:
                    driving_test_number.insert(0, '')
                driving_test_number.configure(state='readonly')
                                    

    # 獲取輸入欄位信息
    def save_student_data():
        global current_student_id

        # 偵測號碼自動增加流水號
        current_number[0] += 1

        student_data = {
            # 'driving_test_number': driving_test_number.get(),
            # 使用 current_number 自動生成的號碼
            'driving_test_number': str(current_number[0]),
            'student_number': student_number.get(),
            'register_number': register_number.get(),
            'batch': batch.get(),
            'student_name': student_name.get(),
            'birth_date': birth_date.get(),
            'national_id_no': national_id_no.get(),
            'road_test_date': road_test_date.get(),
            'road_test_items_type': road_test_items_type.get(),
            'driving_test_group': driving_test_group.get(),
            'training_type_code': training_type_code.get(),
            'id': current_student_id
        }

        if current_student_id is None:
            messagebox.showwarning('警告', '請先搜尋學員資料！')
            return
        
        update_student_data(student_data, uid=1)
        clear_entries_and_comboboxes(road_test_roster)

        # 讀取 save_student_data 的資料寫入 treeview
        data_list.insert('', 'end', values=(
            student_data['driving_test_number'],
            student_data['student_number'],
            student_data['register_number'],
            student_data['batch'],
            student_data['student_name'],
            student_data['birth_date'],
            student_data['national_id_no'],
            student_data['road_test_date'],
            student_data['road_test_items_type']
        ))

    # 新增按鈕
    add_btn(road_test_roster, text='新增道考清冊', command=save_student_data).grid(row=7, column=2, sticky='wen', padx=(10,0))
    # 列印按鈕
    print_btn(road_test_roster, text='列印道考清冊', command=lambda: None).grid(row=7, column=3, sticky='wen', padx=(10,0))
