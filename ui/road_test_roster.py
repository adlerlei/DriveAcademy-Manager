# 道考清冊作業 介面
# 對應資料庫邏輯介面 models/test.py
# 該介面不需要匯出文件功能
from utils.widget import *
from utils.config import *
from models.test import *
from models.annual_plan import annual_plan_data
import customtkinter as ctk
from tkinter import messagebox
import webbrowser
import pyautogui
import time
import os
from jinja2 import Environment, FileSystemLoader


current_student_id = None # 檢測學員資料庫 id 欄位來判定是否修改或新增
current_driving_test_number = 0 # 考試號碼監聽
is_adding_new = False # 監聽是否新增學員
is_searchint = False 

def  road_test_roster(content):
    global current_driving_test_number, is_adding_new, is_searchint
    current_driving_test_number = 0 # 每次載入界面時，考試號碼歸零
    clear_frame(content)

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
    student_number.bind("<KeyRelease>", lambda event: check_and_populate('student_number', student_number.get()))
    
    # 學員姓名
    label(road_test_roster, text='學員姓名').grid(row=0, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    student_name = entry(road_test_roster, placeholder_text=" 🔎")
    student_name.grid(row=1, column=1, sticky='wen', padx=(10,0))
    student_name.bind("<KeyRelease>", lambda event: check_and_populate('student_name', student_name.get()))

    # 名冊號碼
    label(road_test_roster, text='名冊號碼').grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    register_number = entry(road_test_roster)
    register_number.grid(row=1, column=2, sticky='wen', padx=(10,0))

    # 身分證號碼
    label(road_test_roster, text='身分證號碼').grid(row=0, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    national_id_no = entry(road_test_roster, placeholder_text=" 🔎")
    national_id_no.grid(row=1, column=3, sticky='wen',padx=10)
    national_id_no.bind("<KeyRelease>", lambda event: check_and_populate('national_id_no', national_id_no.get()))

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
    driving_test_number = entry(road_test_roster, placeholder_text='此欄位自動生成，無須輸入')
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
        'driving_test_group', # 組別
        'road_test_items_type', # 路考項目
    )
    data_list = ttk.Treeview(road_test_roster, show='headings', column=columns)
    
    data_list.column('driving_test_number', width=50, anchor='center')
    data_list.column('student_number', width=50, anchor='center')
    data_list.column('register_number', width=50, anchor='center')
    data_list.column('batch', width=50, anchor='center')
    data_list.column('student_name', width=50, anchor='center')
    data_list.column('birth_date', width=50, anchor='center')
    data_list.column('national_id_no', width=50, anchor='center')
    data_list.column('road_test_date', width=50, anchor='center')
    data_list.column('driving_test_group', width=50, anchor='center')
    data_list.column('road_test_items_type', width=50, anchor='center')
    
    data_list.heading('driving_test_number', text='號碼', anchor='center')
    data_list.heading('student_number', text='學員編號', anchor='center')
    data_list.heading('register_number', text='名冊號碼', anchor='center')
    data_list.heading('batch', text='梯次', anchor='center')
    data_list.heading('student_name', text='學員姓名', anchor='center')
    data_list.heading('birth_date', text='出生日期', anchor='center')
    data_list.heading('national_id_no', text='身分證號碼', anchor='center')
    data_list.heading('road_test_date', text='路試日期', anchor='center')
    data_list.heading('driving_test_group', text='組別', anchor='center')
    data_list.heading('road_test_items_type', text='路考項目', anchor='center')

    data_list.grid(row=9, column=0, columnspan=4, sticky='wens', padx=10, pady=10)

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
    road_test_roster.grid_rowconfigure(9, weight=1)
    road_test_roster.grid_columnconfigure(0, weight=1)
    road_test_roster.grid_columnconfigure(1, weight=1)
    road_test_roster.grid_columnconfigure(2, weight=1)
    road_test_roster.grid_columnconfigure(3, weight=1)

    # 邏輯功能
    def check_and_populate(identifier, value):
        global is_searching, is_adding_new
        if not is_adding_new and value and len(value) >=3: # 監聽至少輸入3個字符串才搜尋
            is_searching = True
            populate_student_data(identifier, value)
        elif not is_adding_new and not value:
            clear_all_fields()
        is_searching = False

    def clear_all_fields():
        global current_student_id
        clear_entries_and_comboboxes(road_test_roster, [road_test_date, road_test_items_type])
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
            # 路試日期
            if student_data[37]:
                road_test_date.delete(0, ctk.END)
                road_test_date.insert(0, student_data[37])
            # 路考項目
            if student_data[39]:
                road_test_items_type.set(student_data[39])
                                    

    # 獲取輸入欄位信息
    def save_student_data():
        global current_student_id, current_driving_test_number, is_adding_new
        is_adding_new = True # 設置標誌表示正在添加新學員

        # 偵測號碼自動增加流水號
        current_driving_test_number += 1

        student_data = {
            'register_number': register_number.get(),
            'road_test_date': road_test_date.get(),
            'road_test_items_type': road_test_items_type.get(),
            'driving_test_number': str(current_driving_test_number),
            'id': current_student_id,
            'student_number': student_number.get(),
            'batch': batch.get(),
            'student_name': student_name.get(),
            'birth_date': birth_date.get(),
            'national_id_no': national_id_no.get(),
            'driving_test_group': driving_test_group.get(),
        }

        if current_student_id is None:
            messagebox.showwarning('警告', '請先搜尋學員資料！')
            is_adding_new = False # 重製新增學員標誌
            return
        
        update_student_data(student_data, uid=1)

        # 更新顯示的考試號碼
        driving_test_number.configure(state='normal')
        driving_test_number.delete(0, ctk.END)
        driving_test_number.insert(0, str(current_driving_test_number))
        driving_test_number.configure(state='readonly')

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
            student_data['driving_test_group'],
            student_data['road_test_items_type']
        ))

        # 清空輸入字段，但保留某些字段 
        keep_entries = [road_test_date, road_test_items_type, driving_test_number, driving_test_group]
        clear_entries_and_comboboxes(road_test_roster, keep_entries)
        current_student_id = None
        is_adding_new = False # 重置

    # 新增此函數以獲取所有新增到 treeview 的學員 ID
    def get_all_added_student_ids():
        all_ids = []  # 用於存儲所有新增學員的 ID
        for item in data_list.get_children():  # 獲取所有項目
            all_ids.append(data_list.item(item)['values'][0])  # 假設學員 ID 在第一列
        return all_ids
    
    def get_treeview_data():
        data = []
        for item in data_list.get_children():
            values = data_list.item(item)['values']
            data.append({
                'driving_test_number': values[0],
                'student_name': values[4],
                'birth_date': values[5],
                'national_id_no': values[6],
                'register_number': values[2],
            })
        return data

    def print_html_report(for_dmv=True):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir = os.path.join(base_dir, "print")
        env = Environment(loader=FileSystemLoader(template_dir))
        
        # 根據 for_dmv 的值選擇不同的模板 
        if for_dmv:
            template = env.get_template("road_test_roster.html")
        else:
            template = env.get_template("road_test_roster_駕訓班公告.html")

        data = get_treeview_data()
        if not data:
            messagebox.showwarning("警告", "沒有數據可以打印")
            return
        elif not for_dmv:
            for item in data:
                item['national_id_no'] = '0000'

        # 讀取年度計畫表資料供 exam_type 使用
        results = annual_plan_data()

        # 获取其他需要的数据
        exam_date = road_test_date.get()
        class_name = "佑名駕訓班"  # 请替换为实际的班名
        exam_type = results[0][6]
        period = f"第 {results[0][2]} 期 {'&nbsp;'*2} {results[0][4]} 梯次 {'&nbsp;'*2} 第 {driving_test_group.get()} 組"  # 请替换为实际的期别
        exam_date = f"{road_test_date.get()}{'&nbsp;'*10}午  {'&nbsp;'*2} 第{'&nbsp;'*10}組"

        html_content = template.render(
            students=data,
            class_name=class_name,
            exam_type=exam_type,
            period=period,
            exam_date=exam_date
        )

        temp_html_path = os.path.join(base_dir, "print", "temp_written_exam_roster.html")
        with open(temp_html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        webbrowser.open_new_tab(f'file://{temp_html_path}')
        
        # 等待瀏覽器加載
        time.sleep(3)
        # 模擬鍵盤操作觸發打印 (Ctrl+P)
        pyautogui.hotkey('ctrl', 'p')
        # 等待打印窗口出現
        time.sleep(2)
        # 模擬鍵盤操作確認打印 (Enter)
        # pyautogui.press('enter')

        # 删除临时文件
        time.sleep(1)  # 等待打印完成
        os.remove(temp_html_path)

    # 新增按鈕
    add_btn(road_test_roster, text='新增道考清冊', command=save_student_data).grid(row=7, column=1, sticky='wen', padx=(10,0))
    # 列印按鈕
    print_btn(road_test_roster, text='列印道考清冊 (監理站用)', command=lambda: print_html_report(for_dmv=True)).grid(row=7, column=2, sticky='wen', padx=(10,0))
    print_btn(road_test_roster, text='列印道考清冊 (駕訓班用)', command=lambda: print_html_report(for_dmv=False)).grid(row=7, column=3, sticky='wen', padx=(10,0))
