from tkinter import *
from tkinter import ttk
import customtkinter as ck
from utils.config import app_icon
from utils.widget import frame
from ui.admin_login import admin_login
from .menu_list import menu_list


def main_window():
    root = ck.CTk()
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
    menu = frame( root , fg_color = "#669bbc" )
    menu.columnconfigure((0), weight=1, uniform='a')
    # menu.rowconfigure((0,1,2,3,4,5), weight=1 , uniform='a')
    # 固定分配空間比例
    menu.place(x=0, y=0, relwidth=0.2, relheight=1)
    
    # 右方主要畫面
    content = frame( root )
    content.columnconfigure( ( 0 ) , weight = 1 , uniform = 'a')
    content.rowconfigure( ( 0 ) , weight = 1 , uniform = 'a' )
    content.place(relx=0.2, y=0, relwidth=0.8, relheight=1)
    
    # 載入 ui/menu_list.py 中的 menu_list() 函式，並將其傳入 content_frame 中
    menu_list(menu , content)
    
    # 禁用左側導覽列
    # disable_frame_widgets(menu)
    
    # 載入 ui/admin_login.py 中的 admin_login() 以便使其可以被優先觸發登入介面
    admin_login(menu, content)

    return root