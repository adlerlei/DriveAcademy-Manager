 # 教練資料作業 新增 - 修改 - 刪除 - 查詢
from utils.widget import *
from utils.config import *
from models.instructor import *
import customtkinter as ctk
from tkinter import messagebox

is_editing = False
current_instructor_number = None

def instructor_all(content):
    clear_frame(content)

    instructor_all = frame(content)
    instructor_all.columnconfigure(0, weight=1)
    instructor_all.columnconfigure(1, weight=1)
    instructor_all.columnconfigure(2, weight=1)
    instructor_all.columnconfigure(3, weight=1)
    instructor_all.place(relwidth=1, relheight=1)


    # 教練編號
    label(instructor_all, text="教練編號").grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    number = entry(instructor_all, placeholder_text='編號查詢')
    number.grid(row=1, column=0, sticky='wen', padx=(10,0))
    number.bind("<KeyRelease>", lambda event: populate_instructor_data('number', number.get()))

    # 教練姓名
    label(instructor_all, text="教練姓名").grid(row=0, column=1, sticky='ws', padx=(10,0), pady=(10,0))
    name = entry(instructor_all)
    name.grid(row=1, column=1, sticky='wen', padx=(10,0))

    # 出生日期
    label(instructor_all, text="出生日期").grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    birth_date = entry(instructor_all)
    birth_date.grid(row=1, column=2, sticky='wen', padx=10)

    # 教練證號碼
    label(instructor_all, text="教練證號碼").grid(row=0, column=3, sticky='ws', padx=(10,0), pady=(10,0))
    instructor_number = entry(instructor_all)
    instructor_number.grid(row=1, column=3, sticky='wen', padx=(10,0))

    # 資料顯示區
    treeview_values = [
        'number',
        'name',
        'birth_date',
        'instructor_number',
    ]
    data_list = ttk.Treeview(instructor_all, columns=treeview_values, show='headings')

    data_list.heading('number', text='教練編號')
    data_list.heading('name', text='姓名')
    data_list.heading('birth_date', text='出生日期')
    data_list.heading('instructor_number', text='教練證號')

    data_list.column('number', width=50, anchor=CENTER)
    data_list.column('name', width=70, anchor=CENTER)
    data_list.column('birth_date', width=70, anchor=CENTER)
    data_list.column('instructor_number', width=70, anchor=CENTER)

    data_list.grid(row=4, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)
    
    # 創建水平捲軸
    h_scrollbar = ttk.Scrollbar(instructor_all, orient="horizontal", command=data_list.xview)
    data_list.configure(xscrollcommand=h_scrollbar.set)

    # 創建垂直捲軸
    v_scrollbar = ttk.Scrollbar(instructor_all, orient="vertical", command=data_list.yview)
    data_list.configure(yscrollcommand=v_scrollbar.set)

    # 使用 grid 布局管理器來排列 Treeview 和捲軸
    h_scrollbar.grid(row=5, column=0, columnspan=4, sticky="ew", padx=10)
    v_scrollbar.grid(row=4, column=4, rowspan=2, sticky="ns", pady=10)

    # 配置行和列的權重，使其在窗口調整大小時自動調整
    instructor_all.grid_rowconfigure(14, weight=1)
    instructor_all.grid_columnconfigure(0, weight=1)
    instructor_all.grid_columnconfigure(1, weight=1)
    instructor_all.grid_columnconfigure(2, weight=1)
    instructor_all.grid_columnconfigure(3, weight=1)

    # 邏輯功能區
    def populate_instructor_data(identifier, value):
        global is_editing, current_instructor_number
        # 監聽教練編號輸入框，如果教練編號为空，则清空所有输入框
        if identifier == 'number' and value == '':
            clear_entries_and_comboboxes(instructor_all)
        else:
            instructor_data = get_instructor_data(identifier, value)
            if instructor_data:
                is_editing = True
                current_instructor_number = instructor_data[0]
                number.delete(0, ctk.END)
                number.insert(0, instructor_data[1])
                name.delete(0, ctk.END)
                name.insert(0, instructor_data[2])
                birth_date.delete(0, ctk.END)
                birth_date.insert(0, instructor_data[3])
                instructor_number.delete(0, ctk.END)
                instructor_number.insert(0, instructor_data[4])
            else:
                is_editing = False
                current_instructor_number = None

    def save_instructor_data():
        global is_editing, current_instructor_number
        instructor_data = {
            'number': number.get(),
            'name': name.get(),
            'birth_date': birth_date.get(),
            'instructor_number': instructor_number.get(),
        }

        if is_editing:
            messagebox.showinfo('提示', '請使用 "修改" 功能來更新教練資料。')
            return
        
        # 判斷 instructor_data 是否為空值
        if not any(instructor_data.values()):
            messagebox.showwarning('提示', '您沒有任何資料可以儲存！')
            return
        else:      
            # 如果是編輯模式，更新教練資料
            insert_instructor_data(instructor_data)
            update_treeview()
            clear_entries_and_comboboxes(instructor_all)

    def update_instructor():
        global is_editing, current_instructor_number
        instructor_data = {
            'number': number.get(),  # 教練編號
            'name': name.get(),      # 教練姓名
            'birth_date': birth_date.get(),  # 出生日期
            'instructor_number': instructor_number.get(),  # 教練證號
            'id': current_instructor_number  # 当前教练的 ID
        }

        if current_instructor_number is None:
            messagebox.showwarning('提示', '請先搜尋需要修改的教練資料。')
            return
        
        update_instructor_data(instructor_data)
        is_editing = False
        current_instructor_number = None
        clear_entries_and_comboboxes(instructor_all)
        update_treeview()

    def delete_instructor():
        global is_editing, current_instructor_number
        if current_instructor_number:
            confirm = messagebox.askyesno('確認', '確定要刪除此教練資料嗎？此操作無法撤銷。')
            if confirm:
                delete_instructor_data(current_instructor_number)
                update_treeview()
                is_editing = False
                current_instructor_number = None
        else:
            messagebox.showwarning('提示', '請先搜尋需要刪除的教練資料。')
        clear_entries_and_comboboxes(instructor_all)


    def update_treeview():
        # 清空現有數據
        data_list.delete(*data_list.get_children())
        
        # 從資料庫獲取所有教練資料
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM instructor")
        instructors = cursor.fetchall()
        conn.close()

        # 將教練資料插入 Treeview
        for instructor in instructors:
            data_list.insert("", "end", values=(
                instructor[1],  # number
                instructor[2],  # name
                instructor[3],  # birth_date
                instructor[4],  # instructor_number
            ))

    # 修改按钮配置
    add_btn(instructor_all, text="新增", command=save_instructor_data).grid(row=3, column=1, sticky='wen', padx=10, pady=10)
    modify_btn(instructor_all, text="修改", command=update_instructor).grid(row=3, column=2, sticky='wen', padx=10, pady=10)
    delete_btn(instructor_all, text="刪除", command=delete_instructor).grid(row=3, column=3, sticky='wen', padx=10, pady=10)

    # 初始化 Treeview
    update_treeview()