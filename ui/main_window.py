import tkinter as tk
from tkinter import ttk, font
from utils.config import app_icon
from utils.widget import *
from ui.admin_login import admin_login
from .menu_list import menu_list
from tkinter import PhotoImage


def main_window():
    root = tk.Tk()
    root.title("DriveAcademyManager V1.0")
    
    # # 主題
    # root.tk.call("source", "Azure/azure.tcl")  # 確保這裡的路徑是正確的
    # root.tk.call("set_theme", "light")
    
    #更改背景顏色
    # root.configure(bg='#000000')
    
    # tk視窗針對用戶視窗縮放至最大
    try:
        root.state('zoomed')
    except Exception:
        root.attributes('-fullscreen', True)
    #設定視窗大小
    # root.geometry("1920x1080")
        
    # 禁止視窗拖曳
    #root.resizable(False, False)
    
    # 變更系統 icon
    app_icon(root)
    # print(font.families())
    # 加载背景图片
    # 持久的引用是将图片保存为 root 的属性
    # bg_image = PhotoImage(file='resources/img/bg.png')  # 替换为你的图片路径
    # # 设置背景图片
    # bg_label = tk.Label(root, image=bg_image)
    # bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # 更改 tkinter 主題樣式
    # style = ttk.Style(root)
    # style.theme_use('clam')
    
    # 左方選單導覽列
    menu = frame(root, relief='flat', borderwidth=0)
    menu.pack(side='left', fill='y', padx=5, pady=5)
    
    # 右方主要畫面
    content = frame(root, relief='flat', borderwidth=0)
    content.pack(side='right', fill='both', padx=5, pady=5, expand=True)
    
    # 載入 ui/menu_list.py 中的 menu_list() 函式，並將其傳入 content_frame 中
    menu_list(menu, content)
    
    # 禁用左側導覽列
    # disable_frame_widgets(menu)
    
    # 載入 ui/admin_login.py 中的 admin_login() 以便使其可以被優先觸發登入介面
    admin_login(menu, content)

    
if __name__ == "__main__":
    main_window()
    tk.mainloop()