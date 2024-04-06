from tkinter import messagebox
from utils.config import *
from utils.widget import *
from models.admin import register_insert_data


#  admin 註冊介面
def admin_register(content):
    clear_frame(content)
    
    admin_register = frame(content)
    admin_register.columnconfigure(0, weight=1)
    admin_register.columnconfigure(1, weight=2)
    admin_register.columnconfigure(2, weight=1)
    admin_register.place(relwidth=1, relheight=1)

    username = entry(admin_register , placeholder_text='登入帳號')
    username.grid(row = 0 , column = 1 , stick = 'ns' , pady = (200,0) )
    
    password = entry(admin_register , placeholder_text='登入密碼' ,  show='*')
    password.grid(row = 1, column = 1, stick = 'ns', pady = 10)
    
    # 重複密碼欄位
    repassword = entry(admin_register , placeholder_text='確認密碼' , show='*')
    repassword.grid(row = 2, column = 1, stick = 'ns', pady = 10)
    
    
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
            register_insert_data(content, username_value, password_value)
    

    btn(admin_register, '註冊' , command=register_validation).grid(row = 3, column = 1, stick = 'ns', pady = 50)