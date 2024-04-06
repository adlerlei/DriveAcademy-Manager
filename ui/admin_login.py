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
    admin_login.columnconfigure(1, weight=2)
    admin_login.columnconfigure(2, weight=1)
    admin_login.place(relwidth=1, relheight=1)
    
    username = entry(admin_login , placeholder_text='輸入帳號')
    username.grid(row = 0 , column = 1 , stick = 'ns' , pady = (200,0) )
    # username.focus_set()

    password = entry(admin_login, placeholder_text='輸入密碼' , show='*')
    password.grid(row = 1 , column = 1 , stick = 'ns' , pady = 10)

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

    btn(admin_login, text='登入', command=login_check).grid(row = 2 , column = 1 , stick = 'ns' , pady = 10)
    btn(admin_login, text='註冊', command=lambda: admin_register(content)).grid(row = 3 , column = 1 , stick = 'ns' , pady = 50)