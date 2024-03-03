# 學員資料介面
import tkinter as tk
from tkinter import ttk
from utils.utility_functions import clear_frame, ui_font



def create_student_window(frame_main):
    clear_frame(frame_main)
    
    # 視窗標題 - 年度計畫編排文字 ###########################
    frame_title = tk.Frame(frame_main)
    frame_title.pack( fill="x")
    frame_title_label = tk.Label(frame_title, text="學員資料作業 / 新增 - 修改 - 刪除 - 查找", font=ui_font())
    frame_title_label.pack(side="left", padx=20, pady=7)
    
    # row1 - 新增，修改，刪除按鈕 ###########################
    frame_btn = tk.Frame(frame_main)
    frame_btn.pack( fill="x")
    
    add_btn = tk.Button(frame_btn, font=ui_font(), text="新增", width=8, height=3)
    add_btn.pack(side="left", padx=(20, 0), pady=7)
    # 修改英文 amend
    fix_btn = tk.Button(frame_btn, font=ui_font(), text="修改", width=8, height=3)
    fix_btn.pack(side="left", pady=7)
    
    delete_btn = tk.Button(frame_btn, font=ui_font(), text="刪除", width=8, height=3)
    delete_btn.pack(side="left", pady=7)
    
    search_btn = tk.Button(frame_btn, font=ui_font(), text="查詢", width=8, height=3)
    search_btn.pack(side="left", pady=7)
    
    # row2 - 輸入欄位表單 ###########################
    frame_form = tk.Frame(frame_main)
    frame_form.pack( fill="x")
    
    tk.Label(frame_form, text="✸ 訓練班別：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    
    # 訓練班別代號下拉選單
    training_var = ['1','2','3']
    training_box = ttk.Combobox(
        frame_form, 
        width=3, 
        font=ui_font(),
        values=training_var)
    training_box.pack(side="left", pady=7)

    
    # 顯示訓練班別的值
    training_data = tk.Entry(frame_form, width=15, font=ui_font())
    training_data.pack(side="left", pady=7)
    
    # 考照類別 label
    tk.Label(frame_form, text="✸ 考照類別：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    
    
    # license 考照類別下拉選單
    license_var = ['0','1','2','3','4','5','6','7']
    license_box = ttk.Combobox(
        frame_form,
        width=3,
        font=ui_font(),
        values=license_var)
    license_box.pack(side="left", pady=7)
    
    # label 學員編號
    tk.Label(frame_form, text="✸ 學員編號：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    student_id = tk.Entry(frame_form, width=5, font=ui_font())
    student_id.pack(side="left", pady=7)
    # 學員編號兩個輸入欄位中間多一個字串 -
    tk.Label(frame_form, text="-", font=ui_font()).pack(side="left", pady=7)
    student_id2 = tk.Entry(frame_form, width=5, font=ui_font())
    student_id2.pack(side="left", pady=7)
    
    # label 梯次
    tk.Label(frame_form, text="✸ 梯次：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    
    # class 梯次下拉選單
    class_var = ['A','B']
    class_box = ttk.Combobox(
        frame_form,
        width=3,
        font=ui_font(),
        values=class_var
    )
    class_box.pack(side="left", pady=7)
    
    # 學員姓名
    tk.Label(frame_form, text="✸ 學員姓名：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    student_name = tk.Entry(frame_form, width=10, font=ui_font())
    student_name.pack(side="left", pady=7)
    
    # row3 - 輸入欄位表單 ###########################
    frame_form1 = tk.Frame(frame_main)
    frame_form1.pack( fill="x")
    
    # 身分證字號
    tk.Label(frame_form1, text="✸ 身分證字號：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    student_id_card = tk.Entry(frame_form1, width=15, font=ui_font())
    student_id_card.pack(side="left", pady=7)
    
    
    # 出生日期
    tk.Label(frame_form1, text="✸ 出生日期：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    student_birthday = tk.Entry(frame_form1, width=10, font=ui_font())
    student_birthday.pack(side="left", pady=7)
    
    # email
    tk.Label(frame_form1, text="✸ 信箱：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    student_email = tk.Entry(frame_form1, width=15, font=ui_font())
    student_email.pack(side="left", pady=7)
    
    # 性別
    tk.Label(frame_form1, text="✸ 性別：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    #性別下拉選單
    gender_var = ['男','女','無性別']
    gender_box = ttk.Combobox(
        frame_form1,
        width=3,
        font=ui_font(),
        values=gender_var
    )
    gender_box.pack(side="left", pady=7)
    
    # 指導教練
    tk.Label(frame_form1, text="指導教練：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    # 指導教練下拉選單
    teacher_var = ['AAA','BBB','CCC']
    teacher_box = ttk.Combobox(
        frame_form1,
        width=9,
        font=ui_font(),
        values=teacher_var
    )
    teacher_box.pack(side="left", pady=7)
    
    # row3 - 輸入欄位表單 ###########################
    frame_form2 = tk.Frame(frame_main)
    frame_form2.pack( fill="x")
    
    # 戶籍地址
    tk.Label(frame_form2, text="✸ 戶籍地址：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    # 戶籍地址縣市下拉選單
    address_var = ['台北市','新北市','板橋區']
    address_box = ttk.Combobox(
        frame_form2,
        width=5,
        font=ui_font(),
        values=address_var
    )
    address_box.pack(side="left", pady=7)
    # 戶籍地址欄位
    address = tk.Entry(frame_form2, width=38, font=ui_font())
    address.pack(side="left", pady=7)
    
    # 通訊地址
    tk.Label(frame_form2, text="通訊地址：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    # 通訊地址縣市下拉選單
    address_var = ['台北市','新北市','板橋區']
    address_box = ttk.Combobox(
        frame_form2,
        width=5,
        font=ui_font(),
        values=address_var
    )
    address_box.pack(side="left", pady=7)
    # 通訊地址欄位
    address = tk.Entry(frame_form2, width=37, font=ui_font())
    address.pack(side="left", pady=7)

    # row4 - 輸入欄位表單 ###########################
    frame_form3 = tk.Frame(frame_main)
    frame_form3.pack( fill="x")
    
    # 室內電話
    tk.Label(frame_form3, text="室內電話：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    local_phone = tk.Entry(frame_form3, width=10, font=ui_font())
    local_phone.pack(side="left", pady=7)
    
    # 行動電話
    tk.Label(frame_form3, text="行動電話：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    moblie_phone = tk.Entry(frame_form3, width=10, font=ui_font())
    moblie_phone.pack(side="left", pady=7)
    
    # 學歷文憑
    tk.Label(frame_form3, text="學歷：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    #學歷下拉選單
    diploma_var = ['大學','碩士','博士']
    diploma_box = ttk.Combobox(
        frame_form3,
        width=5,
        font=ui_font(),
        values=diploma_var
    )
    diploma_box.pack(side="left", pady=7)
    
    # 欠資料
    tk.Label(frame_form3, text="欠資料：", font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    missing_document = tk.Entry(frame_form3, width=47, font=ui_font())
    missing_document.pack(side="left", pady=7)
    
    # 创建一个作为水平分隔线的 Frame，高度设置为2像素
    frame_hr = tk.Frame(frame_main, height=2, bd=1, relief="sunken")
    frame_hr.pack(fill="x", padx=(20,20), pady=7)
    
    # 搜尋說明
    frame_search_explain = tk.Frame(frame_main)
    frame_search_explain.pack(fill="x")
    tk.Label(frame_search_explain, text='🔎 學員查詢專區，請依照以下三個欄位選擇一樣查詢即可。', fg='#737373', font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    
    # 搜尋區域
    frame_search = tk.Frame(frame_main)
    frame_search.pack(fill="x")
    
    # 使用學員姓名，手機，學員編號，身分證號來查詢學員
    tk.Label(frame_search, text='學員姓名查詢：', font=ui_font()).pack(side="left", padx=(20, 0), pady=7)
    
    search_name = tk.Entry(frame_search, width=15, font=ui_font())
    search_name.pack(side="left", pady=7)
    
    tk.Label(frame_search, text='學員手機查詢：', font=ui_font()).pack(side='left', padx=(20,0), pady=7)
    
    search_phone = tk.Entry(frame_search, width=15, font=ui_font())
    search_phone.pack(side='left', pady=7)
    
    tk.Label(frame_search, text='學員身分證號查詢：', font=ui_font()).pack(side='left', padx=(20,0), pady=7)
    
    search_id_number = tk.Entry(frame_search, width=15, font=ui_font())
    search_id_number.pack(side='left', pady=7)
    