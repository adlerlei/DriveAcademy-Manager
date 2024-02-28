# 管理員登入介面
import tkinter as tk
from tkinter import messagebox
from utils.utility_functions import clear_frame
from utils.utility_functions import enable_buttons
from db.database import validate_admin_login
from ui.start_window import start_window


def create_login_window(frame_main, buttons):
    clear_frame(frame_main)
    from .register_window import create_register_window
    tk.Label(frame_main, text="管理員帳號：").place(x=500, y=150)
    admin_username = tk.Entry(frame_main, width=30)
    admin_username.place(x=600, y=150)
    admin_username.focus()  # 設定 entry_username 的焦點位置

    tk.Label(frame_main, text="管理員密碼：").place(x=500, y=200)
    admin_password = tk.Entry(frame_main, width=30, show="*")
    admin_password.place(x=600, y=200)
    
    # 處理登入驗證邏輯
    def on_login_clicked():
        username = admin_username.get()
        password = admin_password.get()
        
        # 檢查帳號密碼是否已輸入
        if not username or not password:
            messagebox.showerror("錯誤", "請輸入帳號和密碼！")
            return
        
        # 檢查用戶登入的帳號密碼是否正確
        validation_result = validate_admin_login(username, password)
        if validation_result == "success":
            messagebox.showinfo("成功", "登入成功！")
            # 顯示 left_frame 按鈕選單
            enable_buttons(buttons)
            start_window(frame_main)
        elif validation_result == "username_error":
            messagebox.showerror("失敗", "用戶名不存在！")
        elif validation_result == "password_error":
            messagebox.showerror("失敗", "密碼錯誤！")
        else:
            messagebox.showerror("錯誤", "無此帳號及密碼！")

    
    button_login = tk.Button(frame_main, text="登入", width=15, command=on_login_clicked)
    button_login.place(x=600, y=250)

    label_register = tk.Label(frame_main, text="如果沒有管理員帳號，請先點擊下方按鈕註冊帳號")
    label_register.place(x=600, y=320)

    button_register = tk.Button(frame_main, text="註冊", width=15, command=lambda: create_register_window(frame_main, buttons))
    button_register.place(x=600, y=350)
