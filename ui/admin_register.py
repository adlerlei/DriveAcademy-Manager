from tkinter import messagebox
from utils.config import *
from utils.widget import *
from models.admin import register_insert_data


#  admin 註冊介面
def admin_register(menu, content):
    clear_frame(content)
    
    admin_register = frame(content)
    admin_register.columnconfigure(0, weight=1)
    admin_register.columnconfigure(1, weight=1)
    admin_register.columnconfigure(2, weight=2)
    admin_register.columnconfigure(3, weight=1)
    admin_register.columnconfigure(4, weight=1)
    admin_register.place(relwidth=1, relheight=1)

    label(admin_register, text='管理員帳號').grid(row=3, column=2, sticky='ws', pady=(200,0))
    username = entry(admin_register )
    username.grid(row=4, column=2, stick='wen')
    
    label(admin_register, text='管理員密碼').grid(row=5, column=2, sticky='ws', pady=(20,0))
    password = entry(admin_register, show='*')
    password.grid(row=6, column=2, stick='wen')
    
    # 重複密碼欄位
    label(admin_register, text='密碼確認').grid(row=7, column=2, sticky='ws', pady=(20,0))
    repassword = entry(admin_register, show='*')
    repassword.grid(row=8, column=2, stick='wen')
    
    
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
            # register_insert_data(content, username_value, password_value)
            register_insert_data(menu, content, username_value, password_value)
    

    btn(admin_register, '註冊' , command=register_validation).grid(row=9, column=2, sticky='wen', pady=(40,0))