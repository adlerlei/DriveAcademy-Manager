# 應用程序入口
import tkinter as tk
from ui.login import login_window # 引入登录窗口

def main():
    root = tk.Tk()
    login_window(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()