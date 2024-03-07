# 管理員註冊介面 AdminRegistrationInterface
import tkinter as tk
from tkinter import messagebox
from utils.utility_functions import *
from db.database import register_admin

def AdminRegistrationInterface(frame_main, buttons):
    clear_frame(frame_main)
    from .AdminLoginInterface import AdminLoginInterface
    
    # frmae title
    frame_title = frame_fun(frame_main)
    frame_title.pack(fill='x')
    label_fun(frame_title, '駕訓班管理員註冊').pack(side='left', padx=20, pady=7)
    
    tk.Label(frame_main,font=custom_font(), fg='#626262', text="登入帳號：").place(x=500, y=250)
    admin_username = tk.Entry(frame_main,font=custom_font(), width=30)
    admin_username.place(x=600, y=250)
    admin_username.focus()  # 設定預設焦點在帳號欄位上
    
    tk.Label(frame_main,font=custom_font(), fg='#626262', text="密碼：").place(x=500, y=300)
    admin_password = tk.Entry(frame_main,font=custom_font(), width=30, show="*")
    admin_password.place(x=600, y=300)
    
    tk.Label(frame_main,font=custom_font(), fg='#626262', text="確認密碼：").place(x=500, y=350)
    admin_repassword = tk.Entry(frame_main,font=custom_font(),  width=30, show="*")
    admin_repassword.place(x=600, y=350)
    
    # ttk.Label(frame_main, text="手機號碼：").place(x=500, y=400)
    # admin_phone_var = tk.StringVar()
    # ttk.Entry(frame_main, textvariable=admin_phone_var, width=30).place(x=600, y=400)
    
    # ttk.Label(frame_main, text="信箱：").place(x=500, y=450)
    # admin_mail_var = tk.StringVar()
    # ttk.Entry(frame_main, textvariable=admin_mail_var, width=30).place(x=600, y=450)
    
    # ttk.Label(frame_main, text="通訊地址：").place(x=500, y=500)
    # admin_address_var = tk.StringVar()
    # tk.Entry(frame_main, textvariable=admin_address_var, width=30).place(x=600, y=500)
    
    # 驗證管理員註冊信息以及處理邏輯
    def on_register_clicked():
        # name = admin_name_var.get()
        username = admin_username.get()
        password = admin_password.get()
        repassword = admin_repassword.get()
        # phone_mobile = admin_phone_var.get()
        # email = admin_mail_var.get()
        # mailing_address = admin_address_var.get()

        # 检查所有必填字段是否已填写
        # if not all([name, username, password, repassword, phone_mobile, email, mailing_address]):
        if not all([username, password, repassword]):
            messagebox.showerror("錯誤", "欄位不能為空！")
            return
        # 检查密码是否匹配
        elif password != repassword:
            messagebox.showerror("錯誤", "两次密码输入不相同！")
            return
        else:
            # 所有检查都通过后，调用register_admin进行注册
            # registration_success = register_admin(name, username, password, phone_mobile, email, mailing_address)
            registration_success = register_admin(username, password)
            if registration_success is True:
                messagebox.showinfo("提示", "註冊成功！")
                AdminLoginInterface(frame_main, buttons)
            else:
                # 如果注册失败，registration_success将包含错误信息
                messagebox.showerror("錯誤", "註冊失敗！" if registration_success is False else registration_success)


    # 修改注册按钮，设置其command属性
    tk.Button(frame_main,font=custom_font(), fg='#626262', text="註冊", width=15, command=on_register_clicked).place(x=600, y=550)


    tk.Button(frame_main,font=custom_font(), fg='#626262', text="返回登入", width=15, command=lambda: AdminLoginInterface(frame_main, buttons)).place(x=600, y=600)