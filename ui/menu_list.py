from utils.widget import *
from utils.config import *
from .annual_plan_term import annual_plan_term
from .closing_training_roster import closing_training_roster
from .driving_test_roster import driving_test_roster
from .learner_license_date_registration import learner_license_date_registration
from .learner_license_submission import learner_license_submission
from .learner_license_date_registration import learner_license_date_registration
from .m2_retraining_roster_creation import m2_retraining_roster_creation
from .opening_training_rester import opening_training_roster
from .road_test_roster import road_test_roster
from .student_all import student_all
from .written_exam_roster import written_exam_roster

# def menu_list(menu, content):
def menu_list(menu):
    
    # 定義按鈕統一樣式
    style = ttk.Style()
    style.configure('My.TButton',font=('default', 18), padding=10)

    #期別新增
    menu_tiitle = label_frame(menu, '  期別新增  ' )
    menu_tiitle.grid(row=0, column=0, sticky='nswe', padx=20, pady=(20,10))
    menu_btn(menu_tiitle , text='年度期別新增', style='My.TButton').pack(fill='x', padx=20, pady=15)

    # 學員管理
    menu_tiitle = label_frame(menu, '  學員管理  ' )
    menu_tiitle.grid(row=1, column=0, sticky='nswe', padx=20, pady=10)
    menu_btn(menu_tiitle, text='學員資料作業', style='My.TButton').pack(fill='x', padx=20, pady=15)
    
    # 學習駕照
    menu_tiitle = label_frame(menu, '  學習駕照  ')
    menu_tiitle.grid(row=2, column=0, sticky='nswe', padx=20, pady=10)
    menu_btn(menu_tiitle, text='學照日期登錄', style='My.TButton').pack(fill='x', padx=20, pady=15)
    menu_btn(menu_tiitle, text='學照統一送件', style='My.TButton').pack(fill='x', padx=20, pady=(0,15))
    
    # 開結訓名冊
    menu_tiitle = label_frame(menu, '  開結訓名冊  ')
    menu_tiitle.grid(row=3, column=0, sticky='nswe', padx=20, pady=10)
    menu_btn(menu_tiitle, text='開訓名冊作業', style='My.TButton').pack(fill='x', padx=20, pady=15)
    menu_btn(menu_tiitle, text='結訓名冊作業', style='My.TButton').pack(fill='x', padx=20, pady=(0, 15))
    
    # 筆路試清冊
    menu_tiitle = label_frame(menu, '  筆路試清冊  ')
    menu_tiitle.grid(row=4, column=0, sticky='nswe', padx=20, pady=10)
    menu_btn(menu_tiitle, text='筆試清冊作業', style='My.TButton').pack(fill='x', padx=20, pady=15)
    menu_btn(menu_tiitle, text='路試清冊作業', style='My.TButton').pack(fill='x', padx=20, pady=(0, 15))
    menu_btn(menu_tiitle, text='場考清冊作業', style='My.TButton').pack(fill='x', padx=20, pady=(0, 15))
    
    # 監理站名冊
    menu_tiitle = label_frame(menu, '  監理站名冊  ')
    menu_tiitle.grid(row=5, column=0, sticky='nswe', padx=20, pady=10)
    menu_btn(menu_tiitle, text='M2  補訓名冊', style='My.TButton').pack(fill='x', padx=20, pady=15)
    
#     # 定義一個清單，包含選單標題，顏色，按鈕內容
#     menus = [
#         ('  期別新增  ', [('年度期別新增', lambda: annual_plan_term(content))]),
#         ('  學員管理  ', [('學員資料作業', lambda: student_all(content))]),
#         ('  學習駕照  ', [('學照日期登錄', lambda: learner_license_date_registration(content)), ('學照統一送件', lambda: learner_license_submission(content))]),
#         ('  開結訓名冊  ', [('開訓名冊作業', lambda: opening_training_roster(content)), ('結訓名冊作業', lambda: closing_training_roster(content))]),
#         ('  筆路試清冊  ', [('筆試清冊作業', lambda: written_exam_roster(content)), ('路試清冊作業', lambda: driving_test_roster(content)), ('場考清冊作業', lambda: road_test_roster(content))]),
#         ('  監理站名冊  ', [('M2  補訓名冊', lambda: m2_retraining_roster_creation(content))]),
#     ]
    
#     for title, buttons in menus:
#         menu_frame = label_frame(menu, title)  # 創建選單標題
#         menu_frame.pack(padx=(15, 0), pady=(10, 10))  # 定位選單標題
#         m = frame(menu_frame)  # 創建框架
#         m.pack(padx=10, pady=10)  # 定位框架
#         for btn_text, command in buttons:
#             menu_btn(m, btn_text, command=command).pack()  # 創建並定位按鈕