# 導入 ttkbootstrap 模組
import ttkbootstrap as ttk
from utils.config import app_icon
# from utils.widget import frame, label_frame
from utils.widget import *
from ui.admin_login import admin_login
from .menu_list import menu_list
import tkinter as tk
from ttkbootstrap.constants import *


def main_window():
    root = ttk.Window(themename="minty")
    root.title("DriveAcademyManager V1.0")
    
    # tk視窗針對用戶視窗縮放至最大
    try:
        root.state('zoomed')
    except Exception:
        root.attributes('-fullscreen', True)
        
    # 禁止視窗拖曳
    # root.resizable(False, False)
    
    # 變更系統 icon
    app_icon(root)

    
    # 左方選單導覽列
    menu = frame(root, bootstyle="light")
    # menu.pack(side='left', fill='y', padx=5, pady=5)
    menu.columnconfigure((0), weight=1)
    menu.rowconfigure((0,1,2,3,4,5), weight=1)
    menu.place(x=0, y=0, relwidth=0.2)
    
    # 固定分配空間比例
    # menu.place(x=0, y=0, relwidth=0.2, relheight=1)
    
    # btnfr = label_frame(menu, '  期別新增  ' )
    # btnfr.grid(row=0, column=0, sticky='nwe', padx=20, pady=(10,10))
    # style = ttk.Style()
    # style.configure('My.TButton',font=('default', 16), padding=15)
    # menu_btn(btnfr , text='年度期別新增',style='My.TButton').pack(fill='x', padx=20, pady=10)
    
    # label_frame(menu, '  學員管理  ' ).grid(row=1, column=0, sticky='nswe', padx=20, pady=(0,10))
    # label_frame(menu, '  學習駕照  ' ).grid(row=2, column=0, sticky='nswe', padx=20 , pady=(0,10))
    # label_frame(menu, '  開結訓名冊  ').grid(row=3, column=0, sticky='nswe', padx=20, pady=(0, 10))
    # label_frame(menu, '  筆路試清冊  ').grid(row=4, column=0, sticky='nswe', padx=20, pady=(0, 10))
    # label_frame(menu, '  監理站名冊  ').grid(row=5, column=0, sticky='nswe', padx=20, pady=(0, 10))
    
    
    # 右方主要畫面
    content = frame(root)
    # content.pack(side='right', fill='both', padx=15, pady=15, expand=True)
    content.place(relx=0.2, y=0, relwidth=0.8, relheight=1)
    
    # 載入 ui/menu_list.py 中的 menu_list() 函式，並將其傳入 content_frame 中
    # menu_list(menu, content)
    menu_list(menu)
    
    # 禁用左側導覽列
    # disable_frame_widgets(menu)
    
    # 載入 ui/admin_login.py 中的 admin_login() 以便使其可以被優先觸發登入介面
    admin_login(menu, content)

    return root
    
# if __name__ == "__main__":
#     main_window()
#     ctk.mainloop()