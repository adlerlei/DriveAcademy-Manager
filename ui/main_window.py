import customtkinter as ctk
import tkinter as tk
from utils.config import app_icon
from utils.widget import *
from ui.admin_login import admin_login
from .menu_list import menu_list


def main_window():
    root = ctk.CTk()
    root.title("DriveAcademyManager V1.0")
    
    # tk視窗針對用戶視窗縮放至最大
    try:
        root.state('zoomed')
    except Exception:
        root.attributes('-fullscreen', True)
        
    # 禁止視窗拖曳
    root.resizable(False, False)
    
    button = ctk.CTkButton(root, text="my button")
    button.pack(padx=20, pady=20)
    
    # 變更系統 icon
    app_icon(root)
    # print(font.families())

    
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