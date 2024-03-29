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

    window_title = label_frame(content, '  管理員登入  ')
    window_title.grid(row=0, column=0, sticky='nsew', padx=20, pady=10)

    row1 = frame(window_title)
    row1.pack(pady=(300,0))
    label(row1, '管理員帳號：').pack(side='left')
    username = entry(row1)
    username.pack(side='left' , padx = (20,0))
    username.focus_set()

    row2 = frame(window_title)
    row2.pack(pady=(20,0))
    label(row2, '管理員密碼：').pack(side='left')
    password = entry(row2, show='*')
    password.pack(side='left' , padx = (20,0))

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

    row3 = frame(window_title)
    row3.pack(pady = (20,0))
    login_btn(row3, text='登入', width=19 , command=login_check).pack(side='left')

    register_btn(row3, text='註冊', width=8 , command=lambda: admin_register(content)).pack(side='left' , padx=(18,0))