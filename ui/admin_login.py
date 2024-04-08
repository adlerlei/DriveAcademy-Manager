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
    
    admin_login = frame(content)
    admin_login.columnconfigure(0, weight=1)
    admin_login.columnconfigure(1, weight=1)
    admin_login.columnconfigure(2, weight=2)
    admin_login.columnconfigure(3, weight=1)
    admin_login.columnconfigure(4, weight=1)
    # admin_login.rowconfigure(0, weight=1)
    admin_login.place(relwidth=1, relheight=1)
    
    label(admin_login, text='登入帳號').grid(row=3, column=2, sticky='ws', pady=(200,0))
    username = entry(admin_login)
    username.grid(row=4, column=2, sticky='wen')

    label(admin_login, text='登入密碼').grid(row=5, column=2, sticky='ws', pady=(20,0))
    password = entry(admin_login, show='*')
    password.grid(row=6, column=2, sticky='wen')

    # 驗證登入
    def login_check():
        username_value = username.get()
        password_value = password.get()
        if not all([username_value, password_value]):
            messagebox.showerror('錯誤', '請輸入帳號及密碼，欄位不可為空')
            return
        elif login_validation(username_value, password_value):
            messagebox.showinfo('成功', '登入成功')
            clear_frame(content)
            enable_frame_widgets(menu)
            start(content)
        else:
            messagebox.showerror('錯誤', '帳號或密碼錯誤')

    btn(admin_login, text='登入', command=login_check).grid(row=7, column=2, sticky='wen', pady=20)
    btn(admin_login, text='註冊管理員', command=lambda: admin_register(content)).grid(row=8, column=2, sticky='wen', pady=20)