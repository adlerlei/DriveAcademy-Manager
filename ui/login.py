import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import font as tkFont  # 導入字體模塊

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("登入介面")
        self.root.geometry('400x600')
        self.root.resizable(False, False)  # 禁止調整尺寸

        # 設定背景圖片
        self.background_image = tk.PhotoImage(file="img/login_bk.png")
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # 定義字體和大小
        self.entry_font = tk.font.Font(family='清松手寫體2', size=20)
        self.login_font = tk.font.Font(family='清松手寫體2', size=15)


        # 帳號輸入欄位
        self.username_entry = tk.Entry(self.root, font=self.entry_font)
        self.username_entry.place(x=100, y=297, width=230, height=35) 

        # 密碼輸入欄位
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.place(x=100, y=363, width=230, height=35) 

        # 記住帳號
        self.remember_me = tk.IntVar()
        self.remember_me_check = tk.Checkbutton(self.root, text="記住帳號", variable=self.remember_me, bg='#60C1FF', font=self.login_font)
        self.remember_me_check.place(x=94, y=400)  # 調整位置

        # 加載按鈕圖片
        # self.login_button_image = tk.PhotoImage(file="img/bt.png") 
        
        # self.login_button = tk.Button(self.root, image=self.login_button_image, borderwidth=0, command=self.login)
        # self.login_button.place(x=100, y=435, width=230, height=30) 

        # 登入按鈕
        self.login_button = tk.Button(self.root, text='管理員登入', borderwidth=0, command=self.login, font=self.login_font)
        self.login_button.place(x=100, y=435, width=230, height=30)  # 調整位置和大小
        
        # 提示註冊帳號
        self.login_label = tk.Label(self.root, text="沒有管理員帳號？", bg='#60C1FF', font=self.login_font)
        self.login_label.place(x=98, y=475)  # 調整位置和大小

        # 註冊按鈕
        self.register_button = tk.Button(self.root, borderwidth=0, text="註冊管理員帳號", command=self.register, font=self.login_font)
        self.register_button.place(x=100, y=500, width=230, height=30)  # 調整位置和大小


    def login(self):
        # 登入功能的實現
        pass

    def register(self):
        # 跳轉到註冊介面的功能
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
