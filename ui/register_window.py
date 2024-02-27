# 管理員註冊
import tkinter as tk
from tkinter import ttk, messagebox
from utils.utility_functions import clear_frame
from db.database import register_admin

def create_register_window(frame_main, buttons):
    clear_frame(frame_main)
    from .login_window import create_login_window
    
    ttk.Label(frame_main, text="註冊新管理員").place(x=500, y=150)
    ttk.Label(frame_main, text="管理者名稱：").place(x=500, y=200)
    admin_name_var = tk.StringVar()
    ttk.Entry(frame_main, textvariable=admin_name_var, width=30).place(x=600, y=200)
    
    ttk.Label(frame_main, text="登入帳號：").place(x=500, y=250)
    admin_username_var = tk.StringVar()
    ttk.Entry(frame_main, textvariable=admin_username_var, width=30).place(x=600, y=250)
    
    ttk.Label(frame_main, text="密碼：").place(x=500, y=300)
    admin_password_var = tk.StringVar()
    ttk.Entry(frame_main, textvariable=admin_password_var, width=30, show="*").place(x=600, y=300)
    
    ttk.Label(frame_main, text="確認密碼：").place(x=500, y=350)
    admin_repassword_var = tk.StringVar()
    ttk.Entry(frame_main, textvariable=admin_repassword_var, width=30, show="*").place(x=600, y=350)
    
    ttk.Label(frame_main, text="手機號碼：").place(x=500, y=400)
    admin_phone_var = tk.StringVar()
    ttk.Entry(frame_main, textvariable=admin_phone_var, width=30).place(x=600, y=400)
    
    ttk.Label(frame_main, text="信箱：").place(x=500, y=450)
    admin_mail_var = tk.StringVar()
    ttk.Entry(frame_main, textvariable=admin_mail_var, width=30).place(x=600, y=450)
    
    ttk.Label(frame_main, text="通訊地址：").place(x=500, y=500)
    admin_address_var = tk.StringVar()
    tk.Entry(frame_main, textvariable=admin_address_var, width=30).place(x=600, y=500)
    
    # 驗證管理員註冊信息以及處理邏輯
    def on_register_clicked():
        name = admin_name_var.get()
        username = admin_username_var.get()
        password = admin_password_var.get()
        repassword = admin_repassword_var.get()
        phone_mobile = admin_phone_var.get()
        email = admin_mail_var.get()
        mailing_address = admin_address_var.get()

        # 检查所有必填字段是否已填写
        if not all([name, username, password, repassword, phone_mobile, email, mailing_address]):
            messagebox.showerror("錯誤", "欄位不能為空！")
            return
        # 检查密码是否匹配
        elif password != repassword:
            messagebox.showerror("錯誤", "两次密码输入不相同！")
            return
        else:
            # 所有检查都通过后，调用register_admin进行注册
            registration_success = register_admin(name, username, password, phone_mobile, email, mailing_address)
            if registration_success is True:
                messagebox.showinfo("提示", "注册成功！")
                create_login_window(frame_main, buttons)
            else:
                # 如果注册失败，registration_success将包含错误信息
                messagebox.showerror("錯誤", "註冊失敗！" if registration_success is False else registration_success)


    # 修改注册按钮，设置其command属性
    ttk.Button(frame_main, text="註冊", width=15, command=on_register_clicked).place(x=600, y=550)


    ttk.Button(frame_main, text="返回登入", width=15, command=lambda: create_login_window(frame_main, buttons)).place(x=600, y=600)