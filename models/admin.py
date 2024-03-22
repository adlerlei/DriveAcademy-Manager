import sqlite3
import os
from tkinter import messagebox


# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 用戶註冊信息寫入資料庫
def register_insert_data(frame_main, name, password):
    # 載入登入介面，註冊完成返回登錄界面
    from ui.admin_login import admin_login
    # 連接到 sqlite3 資料庫
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    
    # 檢查用戶名稱是否存在
    c.execute('SELECT * FROM admin WHERE name = ?', (name,))
    if c.fetchone():
        messagebox.showerror('錯誤', '用戶名稱已存在！')
        return  # 如果用户名已存在，显示错误消息并返回，不执行以下的插入操作
    else:
        # 寫入資料
        c.execute('INSERT INTO admin (name, password) VALUES (?, ?)', (name, password))
    

    # 檢查寫入資料是否成功
    if c.rowcount == 1:
        messagebox.showinfo('成功', '註冊成功！')
        admin_login(frame_main)  # 返回登入頁面
    else:
        messagebox.showerror('錯誤', '註冊失敗！')

    # 提交變更
    conn.commit()
    # 關閉連接
    conn.close()
    

# 管理員登入驗證
def login_validation(name, password):

    # 連接到 sqlite3 資料庫
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    
    # 查詢資料庫驗證管理員帳號密碼
    c.execute('SELECT * FROM admin WHERE name = ? AND password = ?', (name, password))
    # 檢查 admin 資料表中帳號密碼欄位是否存在，並告知用戶登入成功或失敗
    admin = c.fetchone()
    
    
    # 關閉資料庫
    conn.close()
    
    # 確認帳號密碼後返回 True
    return admin is not None