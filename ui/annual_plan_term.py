# 期別新增 - 年度計畫表與期別新增
import tkinter as tk
from utils.widget import *
from utils.config import *

def annual_plan_term(content):
    clear_frame(content)
    
    annual_plan_term = frame(content)
    annual_plan_term.columnconfigure(0, weight=1)
    annual_plan_term.columnconfigure(1, weight=1)
    annual_plan_term.columnconfigure(2, weight=1)
    annual_plan_term.columnconfigure(3, weight=1)
    annual_plan_term.place(relwidth=1, relheight=1)
    
    # 訓練班別（抓取資料庫呈現）
    label(annual_plan_term, text='訓練班別').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    combobox_var = combobox(annual_plan_term, values=['1'])
    combobox_var.grid(row=1, column=0, sticky='wen', padx=(10,0))
    combobox_var.set('1')
    entry(annual_plan_term).grid(row=1, column=1, sticky='wen', padx=(0,10))
    
    # 年度
    label(annual_plan_term, text='年度').grid(row=2, column=0, sticky='ws',padx=(10,0), pady=(20,0))
    year = entry(annual_plan_term)
    year.grid(row=3, column=0, columnspan=2, sticky='wen', padx=10)
    
    # 期別
    label(annual_plan_term, text='期別').grid(row=4, column=0, sticky='ws',padx=(10,0), pady=(20,0))
    term = entry(annual_plan_term)
    term.grid(row=5, column=0, columnspan=2, sticky='wen', padx=10)
    
    # 梯次（抓取資料庫呈現）
    label(annual_plan_term, text='梯次').grid(row=0, column=2, sticky='ws')
    combobox(annual_plan_term, values=['A', 'B']).grid(row=1, column=2, columnspan=2, sticky='wen', padx=(0,10))
    
    # 開訓日期
    label(annual_plan_term, text='開訓日期').grid(row=2, column=2, sticky='ws', pady=(20,0))
    start_date = entry(annual_plan_term)
    start_date.grid(row=3, column=2, columnspan=2, sticky='wen', padx=(0,10))
    
    # 結訓日期
    label(annual_plan_term, text='結訓日期').grid(row=4, column=2, sticky='ws', pady=(20,0))
    end_date = entry(annual_plan_term)
    end_date.grid(row=5, column=2, columnspan=2, sticky='wen', padx=(0,10))
    
    # 新增，修改，刪除 按鈕
    btn(annual_plan_term, text='新增', command=None).grid(row=6, column=0, sticky='wen', padx=10, pady=20)
    btn(annual_plan_term, text='修改', command=None).grid(row=6, column=2, sticky='wen', padx=(0,10), pady=20)
    btn(annual_plan_term, text='刪除', command=None).grid(row=6, column=3, sticky='wen', padx=10, pady=20)
    
    # 列表框 - 期別新增 - 年度計畫表與期別新增
    data_list = ttk.Treeview(annual_plan_term, show='headings', columns=('id', 'class_name', 'year', 'class_num', 'start_date', 'end_date', 'class_code'))
    
    data_list.column("id", width=20, anchor='w')
    data_list.column("class_name", width=300, anchor='w')
    data_list.column("year", width=50, anchor='w')
    data_list.column("class_num", width=150, anchor='w')
    data_list.column("start_date", width=150, anchor='w')
    data_list.column("end_date", width=150, anchor='w')
    data_list.column("class_code", width=200, anchor='w')
    
    data_list.heading("id", text="ID")
    data_list.heading("class_name", text="訓練班別名稱")
    data_list.heading("year", text="年度")
    data_list.heading("class_num", text="期別編號")
    data_list.heading("start_date", text="開訓日期")
    data_list.heading("end_date", text="結訓日期")
    data_list.heading("class_code", text="上課期別代碼")
    
    data_list.grid(row=8, column=0, columnspan=4, sticky='wens', padx=10)
    
    for i in range(100):
        data_list.insert("", "end", values=(f"202{i % 10}", f"張{i}", f"A{i}", f"202{i % 10}-01-01", f"男", f"02{i % 10}", f"09{i % 10}", f"test{i}@gmail.com", f"台北市", f"台北市"))