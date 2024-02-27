# 管理員登入介面
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils.utility_functions import clear_frame
from utils.utility_functions import enable_buttons
from db.database import validate_admin_login
from ui.stay_window import stay_window


def create_login_window(frame_main, buttons):
    clear_frame(frame_main)
    from .register_window import create_register_window
    label_username = ttk.Label(frame_main, text="管理員帳號：")
    label_username.place(x=500, y=150)
    entry_username = ttk.Entry(frame_main, width=30)
    entry_username.place(x=600, y=150)

    label_password = ttk.Label(frame_main, text="管理員密碼：")
    label_password.place(x=500, y=200)
    entry_password = ttk.Entry(frame_main, width=30, show="*")
    entry_password.place(x=600, y=200)
    
    # 處理登入驗證邏輯
    def on_login_clicked():
        username = entry_username.get()
        password = entry_password.get()
        
        # 檢查帳號密碼是否已輸入
        if not username or not password:
            messagebox.showerror("錯誤", "請輸入帳號和密碼！")
            return
        
        # 檢查用戶登入的帳號密碼是否正確
        if not validate_admin_login(username, password):
            messagebox.showerror("錯誤", "用戶名或密碼錯誤！")
            return
        
        if validate_admin_login(username, password):
            messagebox.showinfo("成功", "登入成功！")
            # 顯示 left_frame 按鈕選單
            enable_buttons(buttons)
            stay_window(frame_main)
        else:
            messagebox.showerror("失敗", "用戶名或密碼錯誤！")
    
    button_login = ttk.Button(frame_main, text="登入", width=15, command=on_login_clicked)
    button_login.place(x=600, y=250)

    label_register = ttk.Label(frame_main, text="如果沒有管理員帳號，請先點擊下方按鈕註冊帳號")
    label_register.place(x=600, y=320)

    button_register = ttk.Button(frame_main, text="註冊", width=15, command=lambda: create_register_window(frame_main, buttons))
    button_register.place(x=600, y=350)
