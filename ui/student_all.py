# 學員新增 - 修改 - 刪除 - 查詢
from utils.widget import *
from utils.config import *


def student_all(content):
    # 驗證控件是否存在
    global checkbox_added
    clear_frame(content)
    checkbox_added = False
    
    window_title = label_frame(content, '  學員資料 - 新增 - 修改 - 查詢 - 刪除  ', fg=font_color['學員管理'])
    window_title.pack(fill='x', padx=(20,20), pady=(10,0))
    
    
    row1 = frame(window_title)
    row1.pack(fill='x', padx=(30, 0), pady=(30, 0))
    # 訓練班別（抓取資料庫呈現）
    label(row1, text='訓練班別：', fg=font_color['required_font']).pack(side='left', padx=(20,0))
    combobox(row1, width=3, values=['1','2','3']).pack(side='left')
    entry(row1, width=13).pack(side='left')
    # 考照類別（抓取資料庫呈現）
    label(row1, text='考照類別：', fg=font_color['required_font']).pack(side='left', padx=(20,0))
    combobox(row1, width=3, values=['1','2','3']).pack(side='left')
    entry(row1, width=13).pack(side='left')
    #學員編號
    label(row1, text='學員編號：', fg=font_color['required_font']).pack(side='left', padx=(20, 0))
    number = entry(row1, width=10)
    number.pack(side='left')
    
    
    row2 = frame(window_title)
    row2.pack(fill='x', padx=(30, 0), pady=(20, 0))
    # 梯次（抓取資料庫呈現）
    label(row2, text='梯次：', fg=font_color['required_font']).pack(side='left', padx=(20, 0))
    combobox(row2, width=3, values=['A','B']).pack(side='left')
    # 學員姓名
    label(row2, text='學員姓名：', fg=font_color['required_font']).pack(side='left', padx=(20, 0))
    name = entry(row2, width=8)
    name.pack(side='left')
    # 身分證號碼
    label(row2, text='身分證號碼：', fg=font_color['required_font']).pack(side='left', padx=(20, 0))
    national_id_no = entry(row2, width=14)
    national_id_no.pack(side='left')
    # 出生日期
    label(row2, text='出生日期：', fg=font_color['required_font']).pack(side='left', padx=(20, 0))
    birth_date = entry(row2, width=10)
    birth_date.pack(side='left')
    
    
    row3 = frame(window_title)
    row3.pack(fill='x', padx=(30, 0), pady=(20, 0))
    # 戶籍地址
    label(row3, text='戶籍地址：', fg=font_color['required_font']).pack(side='left', padx=(20, 0))
    combobox(row3, width=3, values=['231', '116']).pack(side='left') # 郵遞區號
    combobox(row3, width=10, values=['台北市中山區', '新北市新店區']).pack(side='left') # 區域別
    r_address = entry(row3, width=25)
    r_address.pack(side='left') # 地址
    # 信箱
    label(row3, text='信箱：', fg=font_color['required_font']).pack(side='left', padx=(20, 0))
    email = entry(row3, width=18)
    email.pack(side='left')
    
    
    row4 = frame(window_title)
    row4.pack(fill='x', padx=(30, 0), pady=(20, 0))
    # 家用電話
    label(row4, text='手機：').pack(side='left', padx=(20, 0))
    entry(row4, width=9).pack(side='left')
    # 行動電話
    label(row4, text='市話：').pack(side='left', padx=(20, 0))
    entry(row4, width=9).pack(side='left')
    # 性別
    label(row4, text='性別：').pack(side='left', padx=(20, 0))
    combobox(row4, width=2, values=['男', '女']).pack(side='left')
    # 學歷
    label(row4, text='學歷：').pack(side='left', padx=(20, 0))
    combobox(row4, width=3, values=['國中', '高中', '大學']).pack(side='left')
    #指導教練
    label(row4, text='指導教練：').pack(side='left', padx=(20, 0))
    combobox(row4, width=3, values=['000', '001', '002']).pack(side='left')
    entry(row4, width=7).pack(side='left')
    
    
    row5 = frame(window_title)
    row5.pack(fill='x', padx=(30, 0), pady=(20, 0))
    # 通訊地址
    label(row5, text='通訊地址：').pack(side='left', padx=(20, 0))
    combobox(row5, width=3, values=['231', '116']).pack(side='left') # 郵遞區號
    combobox(row5, width=10, values=['台北市中山區', '新北市新店區']).pack(side='left') # 縣市區域
    m_address = entry(row5, width=25)
    m_address.pack(side='left') # 地址
    # 備註
    label(row5, text='備註：').pack(side='left', padx=(20, 0))
    remarks = entry(row5, width=18)
    remarks.pack(side='left')
    

    # 點擊按鈕觸發事件，並顯示隱藏的控件顯示學員資料
    def click_btn():
        global checkbox_added
        if not checkbox_added:
        # 讀取資料（暫時留空）

            # 水平線
            row_hr = frame(window_title)
            row_hr.pack(fill='x', padx=(30, 0), pady=(0, 10))
            hr(row_hr, height=2, bd=1, relief='sunken').pack(fill='x', padx=(20, 30), pady=(0,10))
            
            row7 = frame(window_title)
            row7.pack(fill='x', padx=(30, 0), pady=(20, 10))
            # 顯示是否退訓
            label(row7, text='該學員是否退訓：').pack(side='left', padx=(20, 0))
            display_entry_value(row7, width=5).pack(side='left')
            
            row8 = frame(window_title)
            row8.pack(fill='x', padx=(30, 0), pady=(0, 10))
            # 顯示名冊號碼 opening_closing_register 關聯資料庫欄位
            label(row8, text='名冊號碼：').pack(side='left', padx=(20, 0))
            display_entry_value(row8, width=7).pack(side='left')
            # 顯示學照日期
            label(row8, text='學照日期：').pack(side='left', padx=(20, 0))
            display_entry_value(row8, width=7).pack(side='left')
            # 顯示學照號碼
            label(row8, text='學照號碼：').pack(side='left', padx=(20, 0))
            display_entry_value(row8, width=7).pack(side='left')
            # 顯示路試日期
            label(row8, text='路試日期：').pack(side='left', padx=(20, 0))
            display_entry_value(row8, width=7).pack(side='left')
            # 顯示建檔日期
            label(row8, text='建檔日期：').pack(side='left', padx=(20, 0))
            display_entry_value(row8, width=7).pack(side='left')

            checkbox_added = True 


    row6 = frame(window_title)
    row6.pack(fill='x', padx=(30, 0), pady=(20, 40))
    # 新增，修改，刪除，查詢 按鈕
    add_btn(row6, text='新增', command=lambda: None).pack(side='left', padx=(20,0))
    search_btn(row6, text='查詢', command=click_btn).pack(side='left', padx=(10,0))
    edit_btn(row6, text='修改', command=lambda: None).pack(side='left', padx=(10,0))
    delete_btn(row6, text='刪除', command=lambda: None).pack(side='left', padx=(10,0))

    
    # row_hr = frame(window_title)
    # row_hr.pack(fill='x', padx=(30, 0), pady=(0, 10))
    # hr(row_hr, height=2, bd=1, relief='sunken').pack(fill='x', padx=(20, 30), pady=(0,10))
    
    
    # row7 = frame(window_title)
    # row7.pack(fill='x', padx=(30, 0), pady=(20, 10))
    # # 顯示是否退訓
    # label(row7, text='該學員是否退訓：').pack(side='left', padx=(20, 0))
    # # dropout = combobox(row_dropout, width=5, values=['無', '退訓'])
    # # dropout.pack(side='left')
    # # # 設定下拉選單的預設值
    # # dropout.set('無')  # 這裡將 '無' 設為預設值
    # display_entry_value(row7, width=5).pack(side='left')
    
    # row8 = frame(window_title)
    # row8.pack(fill='x', padx=(30, 0), pady=(0, 10))
    # # 顯示名冊號碼 opening_closing_register 關聯資料庫欄位
    # label(row8, text='名冊號碼：').pack(side='left', padx=(20, 0))
    # display_entry_value(row8, width=7).pack(side='left')
    # # 顯示學照日期
    # label(row8, text='學照日期：').pack(side='left', padx=(20, 0))
    # display_entry_value(row8, width=7).pack(side='left')
    # # 顯示學照號碼
    # label(row8, text='學照號碼：').pack(side='left', padx=(20, 0))
    # display_entry_value(row8, width=7).pack(side='left')
    # # 顯示路試日期
    # label(row8, text='路試日期：').pack(side='left', padx=(20, 0))
    # display_entry_value(row8, width=7).pack(side='left')
    # # 顯示建檔日期
    # label(row8, text='建檔日期：').pack(side='left', padx=(20, 0))
    # display_entry_value(row8, width=7).pack(side='left')
    