# 學照資料作業主介面 LearnerLicenseOperationInterface
from utils.utility_functions import *
from .sendLearnerApplication import sendLearnerApplication




def LearnerLicenseOperationInterface(frame_main):
    clear_frame(frame_main)
    
    # lable frame 標題
    register_learner_license = label_frame_fun(frame_main, ' ✏️ 學照登錄', fg='#4ea1d3')
    register_learner_license.pack(fill='x', padx=(20,20), pady=7) 
    
    # 搜尋說明 register_learner_license_row1
    # register_learner_license_row1 = frame_fun(register_learner_license)
    # register_learner_license_row1.pack(fill='x', pady=(20,0))
    # label_fun(register_learner_license_row1, '第一步 - 選擇以下其中一樣學員信息搜尋：', fg='#a79c8e').pack(side='left', padx=(20, 0))
    
    # 搜尋表單 register_learner_license_row2
    register_learner_license_row2 = frame_fun(register_learner_license)
    register_learner_license_row2.pack(fill='x', pady=(10,0))
    
    label_fun(register_learner_license_row2, '輸入學號：').pack(side='left', padx=(20,0))
    entry_fun(register_learner_license_row2, width=10).pack(side='left')
    label_fun(register_learner_license_row2, '輸入學員手機：').pack(side='left', padx=(20, 0))
    entry_fun(register_learner_license_row2, width=10).pack(side='left')
    label_fun(register_learner_license_row2, '輸入學員編號：').pack(side='left', padx=(20, 0))
    entry_fun(register_learner_license_row2, width=10).pack(side='left')
    
    # 查詢按鈕
    search_button = frame_fun(register_learner_license)
    search_button.pack(fill='x', pady=(10, 0))
    button_fun(search_button, '查詢', width=8, height=2).pack(side='left', padx=(20,0))
    
    # 確認學員信息說明 register_learner_license_row3
    # register_learner_license_row3 = frame_fun(register_learner_license)
    # register_learner_license_row3.pack(fill='x', pady=(40,0))
    # label_fun(register_learner_license_row3, '第二步 - 確認學員信息是否正確：', fg='#a79c8e').pack(side='left', padx=(20, 0))
    
    # 確認學員信息表單 register_learner_license_row4
    register_learner_license_row4 = frame_fun(register_learner_license)
    register_learner_license_row4.pack(fill='x', pady=(50, 0))
    label_fun(register_learner_license_row4, '學員編號：').pack(side='left', padx=(20, 0))
    entry_fun(register_learner_license_row4, width=10).pack(side='left')
    label_fun(register_learner_license_row4, '學員姓名：').pack(side='left', padx=(20, 0))
    entry_fun(register_learner_license_row4, width=10).pack(side='left')
    label_fun(register_learner_license_row4, '出生日期：').pack(side='left', padx=(20, 0))
    entry_fun(register_learner_license_row4, width=10).pack(side='left')
    label_fun(register_learner_license_row4, '考照類別：').pack(side='left', padx=(20, 0))
    entry_fun(register_learner_license_row4, width=10).pack(side='left')
    label_fun(register_learner_license_row4, '身分證號：').pack(side='left', padx=(20, 0))
    entry_fun(register_learner_license_row4, width=10).pack(side='left')
    label_fun(register_learner_license_row4, '手機：').pack(side='left', padx=(20, 0))
    entry_fun(register_learner_license_row4, width=10).pack(side='left')
    
    # 確認學員信息表單2 register_learner_license_row5
    register_learner_license_row5 = frame_fun(register_learner_license)
    register_learner_license_row5.pack(fill='x', pady=(10,0))
    
    label_fun(register_learner_license_row5, '區號：').pack(side='left', padx=(20, 0))
    entry_fun(register_learner_license_row5, width=10).pack(side='left')
    label_fun(register_learner_license_row5, '戶籍地址：').pack(side='left', padx=(20, 0))
    entry_fun(register_learner_license_row5, width=29).pack(side='left')
    
    # 修改學員信息按鈕
    # amend_button = frame_fun(register_learner_license)
    # amend_button.pack(fill='x', pady=(10, 0))
    # button_fun(amend_button, '修改學員信息', width=8, height=2).pack(side='left', padx=(20,0))
    
    # 登錄日期說明register_learner_license_row6
    # register_learner_license_row6 = frame_fun(register_learner_license)
    # register_learner_license_row6.pack(fill='x', pady=(40,0))
    
    # label_fun(register_learner_license_row6, '第三步 - 登錄學員學照日期：', fg='#a79c8e').pack(side='left', padx=(20, 0))
    
    #登錄日期 register_learner_license_row7
    register_learner_license_row7 = frame_fun(register_learner_license)
    register_learner_license_row7.pack(fill='x', pady=(50, 0))
    
    label_fun(register_learner_license_row7, '登錄日期：').pack(side='left', padx=(20,0))
    entry_fun(register_learner_license_row7, width=10).pack(side='left')
    label_fun(register_learner_license_row7, '學照日期：').pack(side='left', padx=(20,0))
    entry_fun(register_learner_license_row7, width=10).pack(side='left')
    label_fun(register_learner_license_row7, '學照號碼：').pack(side='left', padx=(20,0))
    entry_fun(register_learner_license_row7, width=10).pack(side='left')
    label_fun(register_learner_license_row7, text='欠資料：').pack(side='left',padx=(20, 0))
    entry_fun(register_learner_license_row7, width=30).pack(side='left')
    
    # 顯示學員登錄日期 register_learner_license_row8
    # Treeview 資料顯示列表
    # 命名規範
    # 學照日期 - learner_license_date
    # 學照號碼 - learner_license_number
    # 考照類別 - license_type
    # 學員編號 - student_id
    # 學員姓名 - student_name
    # 出生日期 - birth_date
    # 身分證號 - id_number
    # 手機 - mobile_number
    # 區域號碼 - area_code
    # 戶籍地址 - residence_address
    register_learner_license_row8 = frame_fun(register_learner_license)
    register_learner_license_row8.pack(fill='x', pady=(40, 0))
    
    style = ttk.Style()
    style.configure("Custom.Treeview", foreground="#626262", background="#F9F9F9")
    
    register_learner_license = ttk.Treeview(register_learner_license_row8, columns=(
        'id','learner_license_date','learner_license_number','license_type','student_id','student_name','burth_date','id_number','mobile_number','area_code','residence_address'
    ),show="headings", style="Custom.Treeview", height=5)
    
    register_learner_license.heading("id", text="序列號")
    register_learner_license.heading("learner_license_date", text="學照日期")
    register_learner_license.heading("learner_license_number", text="學照號碼")
    register_learner_license.heading("license_type", text="考照類別")
    register_learner_license.heading("student_id", text="學員編號")
    register_learner_license.heading("student_name", text="學員姓名")
    register_learner_license.heading("burth_date", text="出生日期")
    register_learner_license.heading("id_number", text="身分證號")
    register_learner_license.heading("mobile_number", text="手機")
    register_learner_license.heading("area_code", text="區域號碼")
    register_learner_license.heading("residence_address", text="戶籍地址")
    
    register_learner_license.column("id", width=100, anchor='w')
    register_learner_license.column("learner_license_date", width=100, anchor='w')
    register_learner_license.column("learner_license_number", width=100, anchor='w')
    register_learner_license.column("license_type", width=100, anchor='w')
    register_learner_license.column("student_id", width=100, anchor='w')
    register_learner_license.column("student_name", width=100, anchor='w')
    register_learner_license.column("burth_date", width=100, anchor='w')
    register_learner_license.column("id_number", width=100, anchor='w')
    register_learner_license.column("mobile_number", width=100, anchor='w')
    register_learner_license.column("area_code", width=100, anchor='w')
    register_learner_license.column("residence_address", width=100, anchor='w')
    
    register_learner_license.pack(side="left", fill="both", expand=True)
    
    # 在 treeview 右邊垂直顯示Scrollbar滾動條
    register_learner_license_scroll = tk.Scrollbar(register_learner_license_row8, command=register_learner_license.yview)
    register_learner_license_scroll.pack(side="right", fill="y")
    register_learner_license.configure(yscrollcommand=register_learner_license_scroll.set)
    
    # 添加5條随机数据进行测试
    for i in range(5):  # 生成5行数据来测试滚动条
        register_learner_license.insert("", "end", values=(f"202{i % 10}", f"張{i}", f"A{i}", f"202{i % 10}-01-01", f"男", f"02{i % 10}", f"09{i % 10}", f"test{i}@gmail.com", f"台北市", f"台北市"))

    # 學照送件 submit_learner_license
    submit_learner_license = label_frame_fun(frame_main, ' 💼 學照送件')
    submit_learner_license.pack(fill='x', pady=(50, 0))
    



    # 使用兩個按鈕來區分 frame 上下兩個介面
    # 學照日期登陸介面 - LearnerLicenseDateRegistrationInterface
    # frame_registerLicenseDate = frame_fun(frame_main, 'x', padx=(20,20))


    # # 學照送件介面 - LearnerLicenseSubmissionInterface
    # frame_sendLearnerApplication = frame_fun(frame_main, 'x', padx=(20,20))