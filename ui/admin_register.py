from tkinter import messagebox
from utils.config import *
from utils.widget import *
from models.admin import register_insert_data


#  admin 註冊介面
def admin_register(content_frame):
    clear_frame(content_frame)
    
    window_title = label_frame(content_frame, ' 管理員註冊 ')
    window_title.pack(fill='x', padx=(20,20), pady=(15,0))
    
    username_frame = frame(window_title)
    username_frame.pack(fill='x', pady=(50, 15))

    label(username_frame, '登入帳號：').pack(side='left', padx=(500,0))
    username = entry(username_frame, width=20)
    username.pack(side='left')
    username.focus_set()
    
    password_frame = frame(window_title)
    password_frame.pack(fill='x', pady=(0,15))
    label(password_frame, '登入密碼：').pack(side='left', padx=(500, 0))
    password = entry(password_frame, width=20, show='*')
    password.pack(side='left')
    
    # 重複密碼欄位
    repassword_frame = frame(window_title)
    repassword_frame.pack(fill='x', pady=(0, 15))
    label(repassword_frame, '密碼確認：').pack(side='left', padx=(500, 0))
    repassword = entry(repassword_frame, width=20, show='*')
    repassword.pack(side='left')
    
    
    #  admin 註冊驗證
    def register_validation():
        # 取得輸入資料
        username_value = username.get()
        password_value = password.get()
        repassword_value = repassword.get()
        
        # 驗證欄位是否為空
        if not all([username_value, password_value, repassword_value]):
            messagebox.showerror('錯誤', '欄位不能為空！')
            return
        # 驗證密碼是否相同
        elif password_value != repassword_value:
            messagebox.showerror('錯誤', '两次密码输入不相同！')
            return
        else:
            # 檢查通過調用函式寫入資料庫
            register_insert_data(content_frame, username_value, password_value)
    
    register_frame = frame(window_title)
    register_frame.pack(fill='x', pady=(20, 20))
    register_btn(register_frame, '註冊', command=register_validation).pack(pady=(10,50))