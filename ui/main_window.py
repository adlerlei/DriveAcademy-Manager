import tkinter as tk
from login import LoginWindow

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("主介面 V1.0")
        # 嘗試跨平台最大化窗口的方法
        try:
            self.root.state('zoomed')
        except Exception:
            self.root.attributes('-zoomed', True)

        # 側邊欄
        self.sidebar = tk.Frame(self.root, bg='#dddddd', relief='flat', borderwidth=0)
        self.sidebar.pack(side='left', fill='y', padx=5, pady=5)

        # 主內容區
        self.main_content = tk.Frame(self.root, bg='#ffffff', relief='flat', borderwidth=0)
        self.main_content.pack(side='right', fill='both', expand=True)

        # 按鈕列表和對應功能
        self.buttons_info = [
            ("期別新增作業", self.show_batch),
            ("學員新增作業", self.show_students),
            ("學照資料", self.show_license),
            ("開結訓資料", self.show_training),
            ("筆試 / 路試資料作業", self.show_tests),
            ("監理資料補登", self.show_supervision),
        ]
        self.create_sidebar_buttons()

    def create_sidebar_buttons(self):
        for text, command in self.buttons_info:
            button = tk.Button(self.sidebar, text=text, command=command, anchor='w', padx=20, pady=10, width=20, height=2)
            button.pack(fill='x')

    def clear_main_content(self):
        # 清除主內容區的所有元件
        for widget in self.main_content.winfo_children():
            widget.destroy()
            
    def show_login(self):
        self.clear_main_content()  # 清除主内容区的现有内容
        login_frame = LoginWindow(self.main_content)  # 创建LoginFrame的实例
        login_frame.pack(expand=True, fill='both')  # 将登录界面添加到主内容区

    def show_batch(self):
        self.clear_main_content()
        # 顯示期別新增作業相關介面的代碼

    def show_students(self):
        self.clear_main_content()
        # 顯示學員新增作業相關介面的代碼

    def show_license(self):
        self.clear_main_content()
        # 顯示學照資料相關介面的代碼

    def show_training(self):
        self.clear_main_content()
        # 顯示開結訓資料相關介面的代碼

    def show_tests(self):
        self.clear_main_content()
        # 顯示筆試/路試資料作業相關介面的代碼

    def show_supervision(self):
        self.clear_main_content()
        # 顯示監理資料補登相關介面的代碼

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    app.show_login() # 顯示登入介面
    root.mainloop()
   
