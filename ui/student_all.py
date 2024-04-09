# 學員新增 - 修改 - 刪除 - 查詢
from utils.widget import *
from utils.config import *


def student_all(content):
    # 驗證控件是否存在
    global checkbox_added
    clear_frame(content)
    checkbox_added = False 
    
    student_all = frame(content)
    student_all.columnconfigure(0, weight=1)
    student_all.columnconfigure(1, weight=1)
    student_all.columnconfigure(2, weight=1)
    student_all.columnconfigure(3, weight=1)
    student_all.place(relwidth=1, relheight=1)
    
    
    # 訓練班別（抓取資料庫呈現）
    label(student_all, text='訓練班別').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    combobox(student_all,  values=['1','2','3']).grid(row=1, column=0, sticky='wen', padx=(10,0))
    entry(student_all).grid(row=1, column=1, sticky='wen', padx=(10,0))

    # 考照類別（抓取資料庫呈現）
    label(student_all, text='考照類別').grid(row=2, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    combobox(student_all,  values=['1','2','3']).grid(row=3, column=0, sticky='wen', padx=(10,0))
    entry(student_all).grid(row=3, column=1, sticky='wen', padx=(10,0))

    #學員編號
    label(student_all, text='學員編號').grid(row=4, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    number = entry(student_all)
    number.grid(row=5, column=0, columnspan=2, sticky='wen', padx=10)
    
    
    # 梯次（抓取資料庫呈現）
    label(student_all, text='梯次').grid(row=6, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    combobox(student_all, values=['A','B']).grid(row=7, column=0, columnspan=2, padx=10)

    # 學員姓名
    label(student_all, text='學員姓名').grid(row=8, column=0, sticky='ws', padx=(10,0), pady=(20,0 ))
    name = entry(student_all)
    name.grid(row=9, column=0, sticky='wen', padx=10)

    # 身分證號碼
    label(student_all, text='身分證號碼').grid(row=10, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    national_id_no = entry(student_all)
    national_id_no.grid(row=11, column=0, columnspan=2, sticky='wen', padx=10)

    # 出生日期
    label(student_all, text='出生日期').grid(row=12, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    birth_date = entry(student_all)
    birth_date.grid(row=13, column=0, columnspan=2, sticky='wen', padx=10)
    
    # 戶籍地址 ######
    label(student_all, text='戶籍地址').grid(row=14, column=0, sticky='ws', padx=(10,0), pady=(20,0))
    # 郵遞區號
    combobox(student_all, values=['231', '116']).grid(row=15, column=0, sticky='wen', padx=10)
    # 區域別
    combobox(student_all, values=['台北市中山區', '新北市新店區']).grid(row=15, column=1, sticky='wen', padx=(0,10))
    # 地址
    r_address = entry(student_all)
    r_address.grid(row=16, column=0, columnspan=2, sticky='wen', padx=10)


    # 行動電話
    label(student_all, text='市話').grid(row=0, column=2, sticky='ws', padx=(10,0), pady=(10,0))
    entry(student_all).grid(row=0, column=2, columnspan=2, sticky='wen',padx=(10,0))

    # 家用電話
    label(student_all, text='手機').grid(row=0, column=2, sticky='ws', padx=(10,0))
    entry(student_all).grid(row=0, column=2, columnspan=2, sticky='wen', padx=10)

    # 信箱
    label(student_all, text='信箱').grid(row=0, column=2, sticky='ws', padx=(10,0))
    email = entry(student_all)
    email.grid(row=0, column=2, columnspan=2, sticky='wen', padx=10)
    

    # 性別
    label(student_all, text='性別').pack(side='left', padx=(20, 0))
    combobox(student_all, values=['男', '女']).pack(side='left')
    # 學歷
    label(student_all, text='學歷').pack(side='left', padx=(20, 0))
    combobox(student_all,  values=['國中', '高中', '大學']).pack(side='left')
    #指導教練
    label(student_all, text='指導教練').pack(side='left', padx=(20, 0))
    combobox(student_all,  values=['000', '001', '002']).pack(side='left')
    entry(student_all).pack(side='left')
    
    
    # 通訊地址
    label(student_all, text='通訊地址').pack(side='left', padx=(20, 0))
    combobox(student_all,  values=['231', '116']).pack(side='left') # 郵遞區號
    combobox(student_all, values=['台北市中山區', '新北市新店區']).pack(side='left') # 縣市區域
    m_address = entry(student_all)
    m_address.pack(side='left') # 地址
    # 備註
    label(student_all, text='備註').pack(side='left', padx=(20, 0))
    remarks = entry(student_all)
    remarks.pack(side='left')
    

    # 點擊按鈕觸發事件，並顯示隱藏的控件顯示學員資料
    def click_btn():
        global checkbox_added
        if not checkbox_added:
        # 讀取資料（暫時留空）

            
            # 顯示是否退訓
            label(student_all, text='該學員是否退訓').pack(side='left', padx=(20, 0))
            display_entry_value(student_all, width=5).pack(side='left')
            
            # 顯示名冊號碼 opening_closing_register 關聯資料庫欄位
            label(student_all, text='名冊號碼').pack(side='left', padx=(20, 0))
            display_entry_value(student_all, width=7).pack(side='left')
            # 顯示學照日期
            label(student_all, text='學照日期').pack(side='left', padx=(20, 0))
            display_entry_value(student_all, width=7).pack(side='left')
            # 顯示學照號碼
            label(student_all, text='學照號碼').pack(side='left', padx=(20, 0))
            display_entry_value(student_all, width=7).pack(side='left')
            # 顯示路試日期
            label(student_all, text='路試日期').pack(side='left', padx=(20, 0))
            display_entry_value(student_all, width=7).pack(side='left')
            # 顯示建檔日期
            label(student_all, text='建檔日期').pack(side='left', padx=(20, 0))
            display_entry_value(student_all, width=7).pack(side='left')

            checkbox_added = True 


    # 新增，修改，刪除，查詢 按鈕
    add_btn(student_all, text='新增', command=lambda: None).pack(side='left', padx=(20,0))
    search_btn(student_all, text='查詢', command=click_btn).pack(side='left', padx=(10,0))
    edit_btn(student_all, text='修改', command=lambda: None).pack(side='left', padx=(10,0))
    delete_btn(student_all, text='刪除', command=lambda: None).pack(side='left', padx=(10,0))
    