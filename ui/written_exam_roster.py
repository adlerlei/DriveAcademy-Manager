# 筆試清冊作業 介面
# 對應資料庫邏輯介面 models/test.py
from utils.widget import *
from utils.config import *
from models.test import *
import customtkinter as ctk
from tkinter import messagebox
import webbrowser
import pyautogui
import time
import os
from jinja2 import Environment, FileSystemLoader


current_student_id = None # 檢測學員資料庫 id 欄位來判定是否修改或新增
current_driving_test_number = 0 # 考試號碼監聽
is_adding_new = False  # 監聽是否新增學員
is_searching = False  

def written_exam_roster(content):
    global current_driving_test_number, is_adding_new, is_searching
    current_driving_test_number = 0 # 每次載入介面時，考試號碼歸零
    clear_frame(content)

    # # 添加列表變數來跟蹤 treeview 號碼流水號自動增加
    # current_number = [0]

    written_exam_roster = frame(content)
    written_exam_roster.columnconfigure(0, weight=1)
    written_exam_roster.columnconfigure(1, weight=1)
    written_exam_roster.columnconfigure(2, weight=1)
    written_exam_roster.columnconfigure(3, weight=1)
    written_exam_roster.place(relwidth=1, relheight=1)

    # 學員編號
    label(written_exam_roster, text='學員編號').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    student_number = entry(written_exam_roster, placeholder_text=" 🔎")
    student_number.grid(row=1, column=0, sticky='wen', padx=(10,0))
    student_number.bind("<KeyRelease>", lambda event: check_and_populate('student_number', student_number.get()))
    
    # 學員姓名
    label(written_exam_roster, text='學員姓名').grid(row=0, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    student_name = entry(written_exam_roster, placeholder_text=" 🔎")
    student_name.grid(row=1, column=1, sticky='wen', padx=(10,0))
    student_name.bind("<KeyRelease>", lambda event: check_and_populate('student_name', student_name.get()))

    # 名冊號碼
    label(written_exam_roster, text='名冊號碼').grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    register_number = entry(written_exam_roster)
    register_number.grid(row=1, column=2, sticky='wen', padx=(10,0))

    # 身分證號碼
    label(written_exam_roster, text='身分證號碼').grid(row=0, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    national_id_no = entry(written_exam_roster, placeholder_text=" 🔎")
    national_id_no.grid(row=1, column=3, sticky='wen', padx=10)
    national_id_no.bind("<KeyRelease>", lambda event: check_and_populate('national_id_no', national_id_no.get()))

    # 出生日期
    label(written_exam_roster, text='出生日期').grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    birth_date = display_entry_value(written_exam_roster)
    birth_date.grid(row=3, column=0, sticky='wen', padx=(10,0))

    # 訓練班別
    label(written_exam_roster, text='訓練班別').grid(row=2, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    training_type_code = display_entry_value(written_exam_roster)
    training_type_code.grid(row=3, column=1, sticky='wen', padx=(10,0))
    training_type_name = display_entry_value(written_exam_roster)
    training_type_name.grid(row=3, column=2, sticky='wen', padx=(10,0))
    
    # 期別
    label(written_exam_roster, text='期別').grid(row=2, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    register_term = entry(written_exam_roster)
    register_term.grid(row=3, column=3, sticky='wen', padx=10)

    # 梯次
    label(written_exam_roster, text='梯次').grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    batch = display_entry_value(written_exam_roster)
    batch.grid(row=5, column=0, sticky='wen', padx=(10,0))

    # 筆試日期
    label(written_exam_roster, text='筆試日期').grid(row=4, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    written_exam_date = entry(written_exam_roster)
    written_exam_date.grid(row=5, column=1, sticky='wen', padx=(10,0))

    # 場次
    label(written_exam_roster, text='場次').grid(row=4, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    driving_test_session = entry(written_exam_roster)
    driving_test_session.grid(row=5, column=2, sticky='wen', padx=(10,0))

    # 號碼
    label(written_exam_roster, text='號碼').grid(row=4, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    driving_test_number = entry(written_exam_roster, placeholder_text='此欄位自動生成，無須輸入')
    driving_test_number.grid(row=5, column=3, sticky='wen', padx=(10,0))

    # 代碼
    label(written_exam_roster, text='代碼').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    driving_test_code = entry(written_exam_roster)
    driving_test_code.grid(row=7, column=0, sticky='wen',padx=(10,0))

    # treeview
    columns = (
        'driving_test_number', # 號碼
        'register_number', # 名冊號碼
        'batch', # 梯次
        'student_number', # 學員編號
        'student_name', # 學員姓名
        'national_id_no', # 身分證號碼
        'birth_date', # 出生日期
        'driving_test_session', # 場次
        'written_exam_date', # 筆試日期
        'driving_test_code', # 代碼
    )
    data_list = ttk.Treeview(written_exam_roster, show='headings', column=columns)
    
    data_list.column('driving_test_number', width=50, anchor='w')
    data_list.column('register_number', width=50, anchor='w')
    data_list.column('batch', width=50, anchor='w')
    data_list.column('student_number', width=50, anchor='w')
    data_list.column('student_name', width=50, anchor='w')
    data_list.column('national_id_no', width=50, anchor='w')
    data_list.column('birth_date', width=50, anchor='w')
    data_list.column('written_exam_date', width=50, anchor='w')
    data_list.column('driving_test_session', width=50, anchor='w')
    data_list.column('driving_test_code', width=50, anchor='w')
    
    data_list.heading('driving_test_number', text='號碼')
    data_list.heading('register_number', text='名冊號碼')
    data_list.heading('batch', text='梯次')
    data_list.heading('student_number', text='學員編號')
    data_list.heading('student_name', text='學員姓名')
    data_list.heading('national_id_no', text='身分證號碼')
    data_list.heading('birth_date', text='出生日期')
    data_list.heading('written_exam_date', text='筆試日期')
    data_list.heading('driving_test_session', text='場次')
    data_list.heading('driving_test_code', text='代碼')

    data_list.grid(row=9, column=0, columnspan=4, sticky='wen', padx=10, pady=(20,0))

    # 創建水平捲軸
    h_scrollbar = ttk.Scrollbar(written_exam_roster, orient="horizontal", command=data_list.xview)
    data_list.configure(xscrollcommand=h_scrollbar.set)

    # 創建垂直捲軸
    v_scrollbar = ttk.Scrollbar(written_exam_roster, orient="vertical", command=data_list.yview)
    data_list.configure(yscrollcommand=v_scrollbar.set)

    # 使用 grid 布局管理器來排列 Treeview 和捲軸
    h_scrollbar.grid(row=10, column=0, columnspan=4, sticky="ew", padx=10)
    v_scrollbar.grid(row=9, column=4, rowspan=2, sticky="ns", pady=10)

    # 配置行和列的權重，使其在窗口調整大小時自動調整
    written_exam_roster.grid_rowconfigure(14, weight=1)
    written_exam_roster.grid_columnconfigure(0, weight=1)
    written_exam_roster.grid_columnconfigure(1, weight=1)
    written_exam_roster.grid_columnconfigure(2, weight=1)
    written_exam_roster.grid_columnconfigure(3, weight=1)

    # 邏輯功能
    def check_and_populate(identifier, value):
        global is_searching, is_adding_new
        if not is_adding_new and value and len(value) >= 3: # 監聽至少輸入3個字符串才搜尋
            is_searching = True
            populate_student_data(identifier, value)
        elif not is_adding_new and not value:
            clear_all_fields()
        is_searching = False

    def clear_all_fields():
        global current_student_id
        clear_entries_and_comboboxes(written_exam_roster)
        current_student_id = None

    # 邏輯功能 - 搜尋學員資料並顯示在 entry
    def populate_student_data(identifier, value):
        global current_student_id, is_searching
        if not is_searching:
            return
        student_data = get_student_data(identifier, value)
        if student_data:
            # 獲取學員資料庫 id 序列
            current_student_id = student_data[0]
            # 學員編號
            student_number.delete(0, ctk.END)
            student_number.insert(0, student_data[5])
            # 學員姓名
            student_name.delete(0, ctk.END)
            student_name.insert(0, student_data[6])
            # 名冊號碼
            if student_data[34] is not None:
                register_number.delete(0, ctk.END)
                register_number.insert(0, student_data[34])
            else:
                register_number.delete(0, ctk.END)
                register_number.insert(0, '')
            # 身分證號碼    
            national_id_no.delete(0, ctk.END)
            national_id_no.insert(0, student_data[10])
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
            if student_data[35] is not None:
                register_term.delete(0, ctk.END)
                register_term.insert(0, student_data[35])
            else:
                register_term.delete(0, ctk.END)
                register_term.insert(0, '')
            # 梯次
            batch.configure(state='normal')
            batch.delete(0, ctk.END)
            batch.insert(0, student_data[7])
            batch.configure(state='readonly')
            # 筆試日期
            if student_data[36] is not None:
                written_exam_date.delete(0, ctk.END)
                written_exam_date.insert(0, student_data[36])
            # 場次
            driving_test_session.configure(state='normal')
            driving_test_session.delete(0, ctk.END)
            driving_test_session.insert(0, student_data[42])
            # 號碼
            driving_test_number.configure(state='normal')
            driving_test_number.delete(0, ctk.END)
            driving_test_number.insert(0, student_data[41])
            driving_test_number.configure(state='readonly')
            # 代碼
            if student_data[43] is not None:
                driving_test_code.insert(0, student_data[43])
            else:
                driving_test_code.insert(0, '')
            driving_test_code.configure(state='readonly')
            

    # 獲取輸入欄位信息 
    def save_student_data():
        global current_student_id, current_driving_test_number, is_adding_new
        is_adding_new = True # 設置標誌表示正在添加新學員

        # 偵測號碼自動增加流水號
        current_driving_test_number += 1

        student_data = {
            'register_number': register_number.get(),  # 名冊號碼
            'driving_test_number': str(current_driving_test_number),  # 號碼
            'id': current_student_id,
            'student_number': student_number.get(),  # 學員編號
            'batch': batch.get(),  # 梯次
            'student_name': student_name.get(),  # 學員姓名
            'birth_date': birth_date.get(),  # 出生日期
            'national_id_no': national_id_no.get(),  # 身分證字號
            'driving_test_session': driving_test_session.get(),  # 場次
            'written_exam_date': written_exam_date.get(),  # 筆試日期
            'driving_test_code': driving_test_code.get(),  # 代碼
            'training_type_code': training_type_code.get(),  # 訓練班別代號      
        }

        if current_student_id is None:
            messagebox.showwarning('警告', '請先搜尋學員資料')
            is_adding_new = False # 重製新增學員標誌
            return
        
        update_student_data(student_data, uid=2)

        # 更新顯示的考試號碼
        driving_test_number.configure(state='normal')
        driving_test_number.delete(0, ctk.END)
        driving_test_number.insert(0, str(current_driving_test_number))
        driving_test_number.configure(state='readonly')

        # 讀取 save_student_data 的資料寫入 treeview
        data_list.insert('', 'end', values=(
            student_data['driving_test_number'],
            student_data['register_number'],
            student_data['batch'],
            student_data['student_number'],
            student_data['student_name'],
            student_data['national_id_no'],
            student_data['birth_date'],
            student_data['driving_test_session'],
            student_data['written_exam_date'],
            student_data['driving_test_code']
        ))

        # 清空输入字段，但保留某些字段
        keep_entries = [written_exam_date, driving_test_session, driving_test_number, current_driving_test_number, driving_test_code]
        clear_entries_and_comboboxes(written_exam_roster, keep_entries)
        current_student_id = None
        is_adding_new = False  # 重置

    # 新增此函數以獲取所有新增到 treeview 的學員 ID
    def get_all_added_student_ids():
        all_ids = []  # 用於存儲所有新增學員的 ID
        for item in data_list.get_children():  # 獲取所有項目
            all_ids.append(data_list.item(item)['values'][0])  # 假設學員 ID 在第一列
        return all_ids

    def print_html_report():
        # 獲取當前腳本的目錄 (ui 目錄) 
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 獲取父目錄
        
        # 動態生成 HTML 文件的完整路徑
        html_path = os.path.join(base_dir, "print", "written_exam_roster.html")
        # html_path = os.path.join(base_dir, "print", "test.html")
        
        # 打開 HTML 文件
        webbrowser.open_new_tab(html_path)
        
        # 等待瀏覽器加載
        time.sleep(3) 
        
        # 模擬鍵盤操作觸發打印 (Ctrl+P)
        pyautogui.hotkey('ctrl', 'p')
        
        # 等待打印窗口出現
        time.sleep(2)
        
        # 模擬鍵盤操作確認打印 (Enter)
        pyautogui.press('enter')

    # 新增按鈕
    add_btn(written_exam_roster, text='新增筆試清冊', command=save_student_data).grid(row=7, column=1, sticky='wen', padx=(10,0))
    # 列印按鈕
    print_btn(written_exam_roster, text='列印筆試清冊 (監理站用)', command=print_html_report).grid(row=7, column=2, sticky='wen', padx=(10,0))
    print_btn(written_exam_roster, text='列印筆試清冊 (駕訓班用)', command=lambda: None).grid(row=7, column=3, sticky='wen', padx=(10,0))
    # 匯出按鈕
    export_btn(written_exam_roster, text='匯出 筆試清冊 文件', command=lambda: export_written_exam_roster(database_path, get_all_added_student_ids())).grid(row=8, column=0, columnspan=4, sticky='wen', padx=(10,0), pady=10)