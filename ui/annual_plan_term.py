# 期別新增 - 年度計畫表與期別新增
import tkinter as tk
from utils.widget import *
from utils.config import *
from models.annual_plan import insert_annual_plan_data, fetch_and_populate_treeview

def annual_plan_term(content):
    clear_frame(content)
    
    annual_plan_term = frame(content)
    annual_plan_term.columnconfigure(0, weight=1)
    annual_plan_term.columnconfigure(1, weight=1)
    annual_plan_term.columnconfigure(2, weight=1)
    annual_plan_term.columnconfigure(3, weight=1)
    annual_plan_term.place(relwidth=1, relheight=1)
    
    # 訓練班別
    label(annual_plan_term, text='訓練班別').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    training_type_code = combobox(annual_plan_term, values=['1'])
    training_type_code.grid(row=1, column=0, sticky='wen', padx=(10,0))
    training_type_name = combobox(annual_plan_term, values=['普通小型車班'])
    training_type_name.grid(row=1, column=1, sticky='wen', padx=10)

    # 年度
    label(annual_plan_term, text='年度').grid(row=2, column=0, sticky='ws',padx=(10,0), pady=(20,0))
    year = entry(annual_plan_term)
    year.grid(row=3, column=0, columnspan=2, sticky='wen', padx=10)
    
    # 期別
    label(annual_plan_term, text='期別').grid(row=4, column=0, sticky='ws',padx=(10,0), pady=(20,0))
    term = entry(annual_plan_term)
    term.grid(row=5, column=0, columnspan=2, sticky='wen', padx=10)
    
    # 梯次（抓取資料庫呈現）
    label(annual_plan_term, text='梯次').grid(row=0, column=2, sticky='ws', padx=(10,0))
    batch = combobox(annual_plan_term, values=['A', 'B'])
    batch.grid(row=1, column=2, sticky='wen', padx=10)

    # 上課期別代碼
    label(annual_plan_term, text='上課期別代碼').grid(row=0, column=3, sticky='ws', padx=(10,0))
    term_class_code = entry(annual_plan_term)
    term_class_code.grid(row=1, column=3, sticky='wen', padx=(0,10))
    
    # 開訓日期
    label(annual_plan_term, text='開訓日期').grid(row=2, column=2, sticky='ws',padx=(10,0), pady=(20,0))
    start_date = entry(annual_plan_term)
    start_date.grid(row=3, column=2, columnspan=2, sticky='wen', padx=10)
    
    # 結訓日期
    label(annual_plan_term, text='結訓日期').grid(row=4, column=2, sticky='ws',padx=(10,0), pady=(20,0))
    end_date = entry(annual_plan_term)
    end_date.grid(row=5, column=2, columnspan=2, sticky='wen', padx=10)

    # 新增按鈕觸發
    def add_btn_click():
        training_type_code_value = training_type_code.get()
        training_type_name_value = training_type_name.get()
        year_value = year.get()
        term_value = term.get()
        batch_value = batch.get()
        start_date_value = start_date.get()
        end_date_value = end_date.get()
        # 新增資料到資料庫
        insert_annual_plan_data(training_type_code_value, training_type_name_value, year_value, term_value, batch_value, start_date_value, end_date_value)
        # 新增成功後，清空輸入欄位
        year.delete(0, 'end')
        term.delete(0, 'end')
        batch.set('')
        start_date.delete(0, 'end')
        end_date.delete(0, 'end')

    
    # 新增，修改，刪除 按鈕
    btn(annual_plan_term, text='新增', command=add_btn_click).grid(row=6, column=0, sticky='wen', padx=10, pady=20)
    btn(annual_plan_term, text='修改', command=None).grid(row=6, column=2, sticky='wen', padx=10, pady=20)
    btn(annual_plan_term, text='刪除', command=None).grid(row=6, column=3, sticky='wen', padx=10, pady=20)
    
    # 列表框 - 期別新增 - 年度計畫表與期別新增
    data_list = ttk.Treeview(annual_plan_term, show='headings', columns=('訓練班別名稱', '年度', '期別編號', '開訓日期', '結訓日期', '上課期別代碼'))
    
    data_list.column("訓練班別名稱", width=300, anchor='w')
    data_list.column("年度", width=50, anchor='w')
    data_list.column("期別編號", width=150, anchor='w')
    data_list.column("開訓日期", width=150, anchor='w')
    data_list.column("結訓日期", width=150, anchor='w')
    data_list.column("上課期別代碼", width=200, anchor='w')
    

    data_list.heading("訓練班別名稱", text="訓練班別名稱")
    data_list.heading("年度", text="年度")
    data_list.heading("期別編號", text="期別編號")
    data_list.heading("開訓日期", text="開訓日期")
    data_list.heading("結訓日期", text="結訓日期")
    data_list.heading("上課期別代碼", text="上課期別代碼")
    
    data_list.grid(row=8, column=0, columnspan=4, sticky='wens', padx=10)
    
    # 調用函數填充 Treeview
    fetch_and_populate_treeview(data_list)