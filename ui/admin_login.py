from tkinter import messagebox
from utils.config import *
from utils.widget import *
from ui.admin_register import admin_register
from models.admin import login_validation
from ui.annual_plan_term import annual_plan_term
from ui.start import start


# 管理員登入介面
def admin_login(menu, content):
    clear_frame(content)
    
    window_title = label_frame(content, ' 管理員登入 ', fg='#627254')
    window_title.pack(fill='x', padx=(20,20), pady=(10,0))
    
    # username_frame = frame(window_title)
    # username_frame.pack(fill='x', pady=(50, 15))
    label(window_title, '管理員帳號：').pack(side='left')
    username = entry(window_title, width=20)
    username.pack()
    username.focus_set()
    
    password_frame = frame(window_title)
    password_frame.pack(fill='x', pady=(0,15))
    label(password_frame, '管理員密碼：').pack(side='left', padx=(500, 0))
    password = entry(password_frame, width=20, show='*')
    password.pack(side='left')
    
    # 驗證登入
    def login_check():
        # 獲取輸入資料
        username_value = username.get()
        password_value = password.get()
        # 驗證欄位是否為空
        if not all([username_value, password_value]):
            messagebox.showerror('錯誤', '請輸入帳號及密碼，欄位不可為空')
            return
        # 驗證帳號是否存在
        elif login_validation(username_value, password_value):
            messagebox.showinfo('成功', '登入成功')
            clear_frame(content)
            enable_frame_widgets(menu)
            start(content)
        else:
            messagebox.showerror('錯誤', '帳號或密碼錯誤')
    
    login_register_frame = frame(window_title)
    login_register_frame.pack(fill='x', pady=(20, 20))
    
    # 直接傳遞 login_check 作為 command 的参数，而不是使用 lambda 表达式
    login_btn(login_register_frame, '登入', command=login_check).pack(padx=(0,0), pady=(0,100))
    
    label(login_register_frame, '沒有管理員帳號請點擊下方註冊').pack()
    
    register_btn(login_register_frame, '註冊', command=lambda: admin_register(content)).pack(pady=(10,50))