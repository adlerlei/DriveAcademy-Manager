import tkinter as tk
from .batch_management import create_batch_window # 期別管理
from .license_management import create_license_window # 學照資料管理
from .login_window import create_login_window # 登入
# from .register_window import create_register_window # 註冊
from .report_generation import create_report_window # M2補訓
from .student_management import create_student_window # 學員資料
from .test_management import create_test_window # 筆試路試
from .training_management import create_training_window # 開結訓
from utils.utility_functions import set_app_icon, ui_font


def create_main_window():
    root = tk.Tk()
    root.title("DriveAcademyManager V1.0")
    # root.configure(bg='#fffff5')
    try:
        root.state('zoomed')
    except Exception:
        root.attributes('-zoomed', True)
    # setting app iocn
    set_app_icon(root)
    
    # left frame button menu
    frame_left = tk.Frame(root, relief='flat', borderwidth=0)
    frame_left.pack(side='left', fill='y', padx=5, pady=5)

    # 初始化按钮并禁用
    buttons = []  # 存储所有按钮的引用
    buttons_info = [
    ("期別新增作業", create_batch_window),
    ("學員資料作業", create_student_window),
    ("學照資料作業", create_license_window),
    ("開結訓作業", create_training_window),
    ("筆試 / 路試作業", create_test_window),
    ("M2補訓名冊製作", create_report_window)
]

    # main_window.py
    for button_text, action in buttons_info:
        button = tk.Button(frame_left, bg='#fffff5', font=ui_font(), text=button_text, anchor='w', padx=20, pady=10, width=18, height=6,
                            command=lambda a=action: a(frame_main))  # 直接传递frame_main
        button.pack()
        buttons.append(button)
        # for button_text, action in buttons_info:
        # button = tk.Button(frame_left, text=button_text, anchor='w', padx=20, pady=10, width=18, height=6, state='disabled',
        #                     command=lambda a=action: a(frame_main))  # 直接传递frame_main
        # button.pack()
        # buttons.append(button)
    
    
    
    # right frame
    frame_main = tk.Frame(root, relief='flat', borderwidth=0)
    frame_main.pack(side='right', fill='both', expand=True)
    
    # start app display admin login interface
    create_login_window(frame_main, buttons)


if __name__ == "__main__":
    create_main_window()
    tk.mainloop()
