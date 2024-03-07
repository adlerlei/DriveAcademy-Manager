import tkinter as tk
from .TermAdditionInterface import TermAdditionInterface
from .LearnerLicenseOperationInterface import LearnerLicenseOperationInterface
from .AdminLoginInterface import AdminLoginInterface
from .M2SupplementalRosterCreationInterface import M2SupplementalRosterCreationInterface
from .StudentAdditionInterface import StudentAdditionInterface
from .WrittenRoadTestOperationInterface import WrittenRoadTestOperationInterface
from .TrainingSessionOperationInterface import TrainingSessionOperationInterface
from utils.utility_functions import set_app_icon, custom_font


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
    ("期別新增作業", TermAdditionInterface),
    ("學員資料作業", StudentAdditionInterface),
    ("學照資料作業", LearnerLicenseOperationInterface),
    ("開結訓作業", TrainingSessionOperationInterface),
    ("筆試 / 路試作業", WrittenRoadTestOperationInterface),
    ("M2補訓名冊製作", M2SupplementalRosterCreationInterface)
]

    # main_window.py
    for button_text, action in buttons_info:
        button = tk.Button(frame_left, fg="#626262",  font=custom_font(), text=button_text, anchor='w', padx=20, pady=10, width=18, height=6,
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
    AdminLoginInterface(frame_main, buttons)


if __name__ == "__main__":
    create_main_window()
    tk.mainloop()
