# 期別新增 - 年度計畫表與期別新增
from utils.widget import *
from utils.config import *

def annual_plan_term(content):
    clear_frame(content)
    
    
    annual_plan_term = frame(content)
    annual_plan_term.grid(row=0, column=0, sticky='nsew', padx=20, pady=10)
    
    row1 = frame(annual_plan_term)
    row1.pack(fill='x',padx=(30,0), pady=(30, 0))
    # 訓練班別（抓取資料庫呈現）
    label(row1, text='訓練班別：').pack(side='left', padx=(20,0))
    combobox_var = combobox(row1, values=['1'])
    combobox_var.pack(side='left')
    combobox_var.set('1')
    entry(row1).pack(side='left' , padx = (10,0))
    
    # 年度
    label(row1, text='年度：').pack(side='left', padx=(20, 0))
    year = entry(row1)
    year.pack(side='left')
    
    row2 = frame(annual_plan_term)
    row2.pack(fill='x', padx=(30, 0), pady=(20, 0))
    # 期別
    label(row2, text='期別：').pack(side='left', padx=(20, 0))
    term = entry(row2)
    term.pack(side='left')
    
    # 梯次（抓取資料庫呈現）
    label(row2, text='梯次：').pack(side='left', padx=(20, 0))
    combobox(row2, values=['A', 'B']).pack(side='left')
    
    # 開訓日期
    label(row2, text='開訓日期：').pack(side='left', padx=(20, 0))
    start_date = entry(row2)
    start_date.pack(side='left')
    
    # 結訓日期
    label(row2, text='結訓日期：').pack(side='left', padx=(20, 0))
    end_date = entry(row2)
    end_date.pack(side='left')
    
    # 新增，修改，刪除 按鈕
    row3 = frame(annual_plan_term)
    row3.pack(fill='x', padx=(30, 0), pady=(20, 0))
    add_btn(row3, text='新增', command=None).pack(side='left', padx=(20, 0))
    edit_btn(row3, text='修改', command=None).pack(side='left', padx=(10, 0))
    delete_btn(row3, text='刪除', command=None).pack(side='left', padx=(10, 0))
    
    
    # 列表框 - 期別新增 - 年度計畫表與期別新增
    row4 = frame(annual_plan_term)
    row4.pack(fill='both', expand=True, padx=(30,0), pady=(20,0))
    data_list = ttk.Treeview(row4, show='headings', columns=('id', 'class_name', 'year', 'class_num', 'start_date', 'end_date', 'class_code'))
    
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
    
    data_list.pack(side="left", fill="both", expand=True, padx=(20,30), pady=(20,50))
    
    for i in range(100):  # 生成100行数据来测试滚动条
        data_list.insert("", "end", values=(f"202{i % 10}", f"張{i}", f"A{i}", f"202{i % 10}-01-01", f"男", f"02{i % 10}", f"09{i % 10}", f"test{i}@gmail.com", f"台北市", f"台北市"))