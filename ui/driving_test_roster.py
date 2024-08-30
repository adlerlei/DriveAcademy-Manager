# 路考清冊(場考)
from utils.widget import *
from utils.config import *
from models.test import *
import customtkinter as ctk
from tkinter import messagebox

# 檢測學員資料庫 id 欄位來判定是否修改或新增
current_student_id = None

def  driving_test_roster(content):
    clear_frame(content)
    
    # 添加列表變數來跟蹤 treeview 號碼流水號自動增加
    current_number = [0]

    driving_test_roster = frame(content)
    driving_test_roster.columnconfigure(0, weight=1)
    driving_test_roster.columnconfigure(1, weight=1)
    driving_test_roster.columnconfigure(2, weight=1)
    driving_test_roster.columnconfigure(3, weight=1)
    driving_test_roster.place(relwidth=1, relheight=1)

    # 學員編號
    label(driving_test_roster, text='學員編號').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    student_number = entry(driving_test_roster,  placeholder_text = "輸入學員編號")
    student_number.grid(row=1, column=0, sticky='wen', padx=(10,0))
    student_number.bind("<KeyRelease>", lambda event: populate_student_data('student_number', student_number.get()))
    
    # 學員姓名
    label(driving_test_roster, text='學員姓名').grid(row=0, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    student_name = display_entry_value(driving_test_roster)
    student_name.grid(row=1, column=1, sticky='wen', padx=(10,0))

    # 名冊號碼
    label(driving_test_roster, text='名冊號碼').grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    register_number = display_entry_value(driving_test_roster)
    register_number.grid(row=1, column=2, sticky='wen', padx=(10,0))

    # 身分證號碼
    label(driving_test_roster, text='身分證號碼').grid(row=0, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    national_id_no = display_entry_value(driving_test_roster)
    national_id_no.grid(row=1, column=3, sticky='wen',padx=10)

    # 出生日期
    label(driving_test_roster, text='出生日期').grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    birth_date = display_entry_value(driving_test_roster)
    birth_date.grid(row=3, column=0, sticky='wen',padx=(10,0))

    # 訓練班別
    label(driving_test_roster, text='訓練班別').grid(row=2, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    training_type_code = display_entry_value(driving_test_roster)
    training_type_code.grid(row=3, column=1, sticky='wen',padx=(10,0))
    training_type_name = display_entry_value(driving_test_roster)
    training_type_name.grid(row=3, column=2, sticky='wen',padx=(10,0))
    # combobox(driving_test_roster, values=['1']).grid(row=6, column=0, sticky='wen',padx=10)
    # combobox(driving_test_roster, values=['普通小型車班']).grid(row=6, column=1, sticky='wen',padx=10)
    
    # 期別
    label(driving_test_roster, text='期別').grid(row=2, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    register_term = display_entry_value(driving_test_roster)
    register_term.grid(row=3, column=3, sticky='wen',padx=10)

    # 梯次
    label(driving_test_roster, text='梯次').grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    batch = display_entry_value(driving_test_roster)
    batch.grid(row=5, column=0, sticky='wen',padx=(10,0))

    # 路試日期
    label(driving_test_roster, text='路試日期').grid(row=4, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    road_test_date = entry(driving_test_roster) 
    road_test_date.grid(row=5, column=1, sticky='wen',padx=(10,0))

    # 組別
    label(driving_test_roster, text='組別').grid(row=4, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    driving_test_group = entry(driving_test_roster)
    driving_test_group.grid(row=5, column=2, sticky='wen',padx=(10,0))

    # 路考項目
    label(driving_test_roster, text='路考項目').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    road_test_items_type = combobox(driving_test_roster, values=['1', '2', '3'])
    road_test_items_type.grid(row=7, column=0, sticky='wen',padx=(10,0))

    # 號碼
    label(driving_test_roster, text='號碼').grid(row=6, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    driving_test_number = display_entry_value(driving_test_roster)
    driving_test_number.grid(row=7, column=1, sticky='wen',padx=(10,0))

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
    data_list = ttk.Treeview(driving_test_roster, show='headings', column=columns)

    
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
    h_scrollbar = ttk.Scrollbar(driving_test_roster, orient="horizontal", command=data_list.xview)
    data_list.configure(xscrollcommand=h_scrollbar.set)

    # 創建垂直捲軸
    v_scrollbar = ttk.Scrollbar(driving_test_roster, orient="vertical", command=data_list.yview)
    data_list.configure(yscrollcommand=v_scrollbar.set)

    # 使用 grid 布局管理器來排列 Treeview 和捲軸
    h_scrollbar.grid(row=10, column=0, columnspan=4, sticky="ew", padx=10)
    v_scrollbar.grid(row=9, column=4, rowspan=2, sticky="ns", pady=10)

    # 配置行和列的權重，使其在窗口調整大小時自動調整
    driving_test_roster.grid_rowconfigure(14, weight=1)
    driving_test_roster.grid_columnconfigure(0, weight=1)
    driving_test_roster.grid_columnconfigure(1, weight=1)
    driving_test_roster.grid_columnconfigure(2, weight=1)
    driving_test_roster.grid_columnconfigure(3, weight=1)
    
    # 邏輯功能 - 搜尋學員資料並顯示在 entry 
    def populate_student_data(identifier, value):

        # 監聽學員編號輸入欄位如果為空，清除學員資料
        if identifier == 'student_number' and value == '':
            # 不保留任何欄位值，全部清除
            clear_entries_and_comboboxes(driving_test_roster)
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
                # 路試日期
                road_test_date.configure(state='normal')
                road_test_date.delete(0, ctk.END)
                if student_data[38] is not None:
                    road_test_date.insert(0, student_data[38])
                else:
                    road_test_date.insert(0, '')
                    # road_test_date.configure(state='readonly')
                # 組別
                driving_test_group.configure(state='normal')
                driving_test_group.delete(0, ctk.END)
                if student_data[39] is not None:
                    driving_test_group.insert(0, student_data[39])
                else:
                    driving_test_group.insert(0, '')
                # driving_test_group.configure(state='readonly')
                # 路考項目
                if student_data[40] is not None:
                    road_test_items_type.set(student_data[40])
                else:
                    road_test_items_type.set('')
                # 號碼
                driving_test_number.configure(state='normal')
                driving_test_number.delete(0, ctk.END)
                if student_data[42] is not None:
                    driving_test_number.insert(0, student_data[42])
                else:
                    driving_test_number.insert(0, '')
                driving_test_number.configure(state='readonly')
                                    

    # 獲取輸入欄位信息
    def save_student_data():
        uid = 1
        global current_student_id

        # 偵測號碼自動增加流水號
        current_number[0] += 1

        student_data = {
            # 'driving_test_number': driving_test_number.get(),
            # 使用 current_number 自動生成的號碼
            'driving_test_number': str(current_number[0]), # 號碼42
            'student_number': student_number.get(), # 學員編號
            'register_number': register_number.get(), # 名冊號碼34
            'batch': batch.get(), # 梯次
            'student_name': student_name.get(), # 學員姓名
            'birth_date': birth_date.get(), # 出生日期
            'national_id_no': national_id_no.get(), # 身分證號
            'road_test_date': road_test_date.get(), # 路試日期38
            'road_test_items_type': road_test_items_type.get(), # 路考項目40
            'driving_test_group': driving_test_group.get(), # 組別39
            'training_type_code': training_type_code.get(), # 訓練班別代號
            'id': current_student_id
        }

        if current_student_id is None:
            messagebox.showwarning('警告', '請先搜尋學員資料！')
            return
        
        update_student_data(student_data, uid=uid)
        clear_entries_and_comboboxes(driving_test_roster)

        # 讀取 save_student_data 的資料寫入 treeview
        data_list.insert('', 'end', values=(
            student_data['driving_test_number'], # 號碼
            student_data['student_number'], # 學員編號
            student_data['register_number'], # 名冊號碼
            student_data['batch'], # 梯次
            student_data['student_name'], # 學員姓名
            student_data['birth_date'], # 出生日期
            student_data['national_id_no'], # 身分證號
            student_data['road_test_date'], # 路試日期
            student_data['road_test_items_type'] # 路考項目
        ))

    # 新增按鈕
    add_btn(driving_test_roster, text='新增場考清冊', command=save_student_data).grid(row=8, column=1, sticky='wen', padx=(10,0), pady=(20,0))
    # 列印按鈕
    print_btn(driving_test_roster, text='列印場考清冊', command=lambda: None).grid(row=8, column=2, sticky='wen', padx=(10,0), pady=(20,0))
    # 匯出按鈕
    export_btn(driving_test_roster, text='匯出 場考清冊 文件', command=lambda: export_driving_test_data(database_path)).grid(row=8, column=3, sticky='wen', padx=10, pady=(20,0))
