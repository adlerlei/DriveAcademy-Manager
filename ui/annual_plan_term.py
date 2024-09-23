# 期別新增 - 年度計畫表與期別新增
from utils.widget import *
from utils.config import *
from tkinter import messagebox
from models.annual_plan import insert_annual_plan_data, fetch_and_populate_treeview, export_selected_data, delete_btn_click

def annual_plan_term(content):
    clear_frame(content)
    
    annual_plan_term = frame(content)
    annual_plan_term.columnconfigure(0, weight=1)
    annual_plan_term.columnconfigure(1, weight=1)
    annual_plan_term.columnconfigure(2, weight=1)
    annual_plan_term.columnconfigure(3, weight=1)
    annual_plan_term.place(relwidth=1, relheight=1)

    # 監聽 term 輸入值，並且再次設定 term_class_code 值
    def on_value_changed(event):
        value = training_type_code.get() + '0' + term.get() + batch.get()
        term_class_code.delete(0, END)
        term_class_code.insert(0, value)


    # 訓練班別
    training_type_codes = ['1', '2', '3', '4', '5', '6', '7', '8']
    training_type_names = ['普通小型車班', '大貨車班', '大客車班', '聯結車班', '職業小型車班', '普通重機車班', '大型重機車班', '小型車逕升大客車班']
    training_type_dict_c = dict(zip(training_type_codes, training_type_names))
    training_type_dict_n = dict(zip(training_type_names, training_type_codes))
    label(annual_plan_term, text='✍🏻 訓練班別').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    training_type_code = combobox(annual_plan_term, values=training_type_codes, command=lambda x: on_training_type_code_changed(x, training_type_name, training_type_dict_c))
    training_type_code.grid(row=1, column=0, sticky='wen', padx=(10,0))
    training_type_name = combobox(annual_plan_term, values=training_type_names, command=lambda x: on_training_type_name_changed(x, training_type_code, training_type_dict_n))
    training_type_name.grid(row=1, column=1, sticky='wen', padx=(10,0))

    # 綁定函數到第一個下拉選單的選擇變化事件
    def on_training_type_code_changed(selected_code, training_type_name, training_type_dict):
        selected_name = training_type_dict.get(selected_code, "")
        training_type_name.set(selected_name)

    def on_training_type_name_changed(selected_name, training_type_code, training_type_dict):
        selected_code = training_type_dict.get(selected_name, "")
        training_type_code.set(selected_code)

    # 梯次
    label(annual_plan_term, text='✍🏻 梯次').grid(row=2, column=0, sticky='ws', padx=(10,0))
    batch = combobox(annual_plan_term, values=['A', 'B'])
    batch.grid(row=3, column=0, columnspan=2, sticky='wen', padx=(10,0))
    batch.set('')
    
    # 期別
    label(annual_plan_term, text='✍🏻 期別').grid(row=4, column=0, sticky='ws',padx=(10,0), pady=(20,0))
    term = entry(annual_plan_term)
    term.grid(row=5, column=0, columnspan=2, sticky='wen', padx=(10,0))

    # 年度
    label(annual_plan_term, text='✍🏻 年度').grid(row=0, column=2, sticky='ws',padx=(10,0), pady=(20,0))
    year = entry(annual_plan_term)
    year.grid(row=1, column=2, sticky='wen', padx=(10,0))

    # 上課期別代碼 
    label(annual_plan_term, text='上課期別代碼').grid(row=0, column=3, padx=(10,0), sticky='ws')
    term_class_code = entry(annual_plan_term, placeholder_text='此欄位自動生成，無須輸入！')
    term_class_code.grid(row=1, column=3, sticky='wen', padx=10)

    # 監聽 term 輸入值，並且再次設定 term_class_code 值
    term.bind("<KeyRelease>", on_value_changed)
    
    # 開訓日期
    label(annual_plan_term, text='✍🏻 開訓日期').grid(row=2, column=2, sticky='ws',padx=(10,0), pady=(20,0))
    start_date = entry(annual_plan_term)
    start_date.grid(row=3, column=2, columnspan=2, sticky='wen', padx=10)
    
    # 結訓日期
    label(annual_plan_term, text='✍🏻 結訓日期').grid(row=4, column=2, sticky='ws',padx=(10,0), pady=(20,0))
    end_date = entry(annual_plan_term) 
    end_date.grid(row=5, column=2, columnspan=2, sticky='wen', padx=10)

    # 新增按鈕觸發
    def add_btn_click():
        year_value = year.get()
        term_value = term.get()
        term_class_code_value = term_class_code.get()
        batch_value = batch.get()
        training_type_code_value = training_type_code.get()
        training_type_name_value = training_type_name.get()
        start_date_value = start_date.get()
        end_date_value = end_date.get()

        # 驗證輸入欄位
        if not all([year_value, term_value, term_class_code_value, batch_value, training_type_code_value, training_type_name_value, start_date_value, end_date_value]):
            messagebox.showerror('錯誤', '所有欄位不可為空')
            return

        # 新增資料到資料庫
        else:
            insert_annual_plan_data(year_value, term_value, term_class_code_value, batch_value, training_type_code_value, training_type_name_value, start_date_value, end_date_value)
            
            # 需要保留的 entry 列表，clear_entries_and_comboboxes 函式中的參數之一 ###
            keep_entries = [training_type_code, training_type_name]
            # 新增成功後，清空輸入欄位 
            clear_entries_and_comboboxes(annual_plan_term, keep_entries)
            # 即時更新 Treeview
            fetch_and_populate_treeview(data_list)

    
    # 新增，刪除，匯出文件 按鈕
    add_btn(annual_plan_term, text='新增', command=add_btn_click).grid(row=6, column=1, sticky='wen', padx=(10,0), pady=20)
    delete_btn(annual_plan_term, text='刪除', command=lambda: delete_btn_click(data_list)).grid(row=6, column=2, sticky='wen', padx=(10,0), pady=20)
    export_btn(annual_plan_term, text='匯出文件', command=lambda: export_selected_data(data_list)).grid(row=6, column=3, sticky='wen', padx=10, pady=20)
    
    # 列表框 - 期別新增 - 年度計畫表與期別新增
    data_list = ttk.Treeview(annual_plan_term, show='headings', 
                             columns=('訓練班別名稱', '年度', '期別編號', '開訓日期', '結訓日期', '上課期別代碼'), height=25)
    
    data_list.column("訓練班別名稱", width=150, anchor='center')
    data_list.column("年度", width=50, anchor='center')
    data_list.column("期別編號", width=50, anchor='center')
    data_list.column("開訓日期", width=50, anchor='center')
    data_list.column("結訓日期", width=50, anchor='center')
    data_list.column("上課期別代碼", width=50, anchor='center')
    

    data_list.heading("訓練班別名稱", text="訓練班別名稱")
    data_list.heading("年度", text="年度")
    data_list.heading("期別編號", text="期別編號")
    data_list.heading("開訓日期", text="開訓日期")
    data_list.heading("結訓日期", text="結訓日期")
    data_list.heading("上課期別代碼", text="上課期別代碼")
    
    data_list.grid(row=8, column=0, columnspan=4, sticky='wens', padx=10)

    # 創建水平捲軸
    h_scrollbar = ttk.Scrollbar(annual_plan_term, orient="horizontal", command=data_list.xview)
    data_list.configure(xscrollcommand=h_scrollbar.set)

    # 創建垂直捲軸
    v_scrollbar = ttk.Scrollbar(annual_plan_term, orient="vertical", command=data_list.yview)
    data_list.configure(yscrollcommand=v_scrollbar.set)

    # 使用 grid 布局管理器來排列 Treeview 和捲軸
    h_scrollbar.grid(row=9, column=0, columnspan=4, sticky="ew", padx=10)
    v_scrollbar.grid(row=8, column=4, rowspan=2, sticky="ns", pady=10)

    # 配置行和列的權重，使其在窗口調整大小時自動調整
    annual_plan_term.grid_rowconfigure(14, weight=1)
    annual_plan_term.grid_columnconfigure(0, weight=1)
    annual_plan_term.grid_columnconfigure(1, weight=1)
    annual_plan_term.grid_columnconfigure(2, weight=1)
    annual_plan_term.grid_columnconfigure(3, weight=1)
        
    # 調用函數填充 Treeview（進入介面時會直接抓取資料庫呈現資料列表）
    fetch_and_populate_treeview(data_list)