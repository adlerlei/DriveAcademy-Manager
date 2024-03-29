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


def menu_list(menu , content):

    # 定義 label_frame 統一間距
    x = 20
    y = 10
    # 定義按鈕統一間距
    bx = 5

    # 期別新增
    menu_title = label_frame( menu, '  期別新增  ' )
    menu_title.grid( row = 0 , column = 0 , sticky = 'nswe' , padx = x , pady = y)
    # 使按鈕填滿其所在的 label_frame
    menu_title.columnconfigure( 0 , weight = 1 )
    menu_title.rowconfigure( 0 , weight = 1 )

    menu_btn( menu_title , text = '年度期別新增'  , command = lambda: annual_plan_term(content)).grid( row = 0 , column = 0 , sticky = 'nswe' , padx = bx , pady = (15,5) )

    # 學員管理
    menu_title = label_frame( menu , '  學員管理  ' )
    menu_title.grid( row = 1 , column = 0 , sticky = 'nswe', padx = x , pady = y )
    # 使按鈕填滿其所在的 label_frame
    menu_title.columnconfigure( 0, weight = 1 )
    menu_title.rowconfigure( 0 , weight = 1 )

    menu_btn(menu_title, text='學員資料作業' , command = lambda: student_all(content)).grid(row=0, column=0, sticky='nswe' , padx=bx , pady=(15,5))

    # 學習駕照
    menu_title = label_frame(menu, '  學習駕照  ' )
    menu_title.grid(row=2, column=0, sticky='nswe', padx=x , pady=y)
    # 使按鈕填滿其所在的 label_frame
    menu_title.columnconfigure(0, weight=1)
    # 为两行配置权重，确保它们可以根据内容自动调整大小
    menu_title.rowconfigure(0, weight=1)
    menu_title.rowconfigure(1, weight=1)

    menu_btn(menu_title, text='學照日期登錄' , command =  lambda: learner_license_date_registration(content)).grid(row=0, column=0, sticky='nswe' , padx=bx , pady=(15,2))

    menu_btn(menu_title, text='學照統一送件' , command = lambda: learner_license_submission(content)).grid(row=1, column=0, sticky='nswe',padx=bx , pady=(0,5))

    # 開結訓名冊
    menu_title = label_frame(menu, '  開結訓名冊  ')
    menu_title.grid(row=3, column=0, sticky='nswe', padx=x , pady=y)
    # 使按鈕填滿其所在的 label_frame
    menu_title.columnconfigure(0, weight=1)
    # 为两行配置权重，确保它们可以根据内容自动调整大小
    menu_title.rowconfigure(0, weight=1)
    menu_title.rowconfigure(1, weight=1)

    menu_btn(menu_title, text='開訓名冊作業' , command = lambda: opening_training_roster(content)).grid(row=0, column=0, sticky='nswe', padx=bx , pady=(15,2))

    menu_btn(menu_title, text='結訓名冊作業' , command = lambda: closing_training_roster(content)).grid(row=1, column=0, sticky='nswe',padx=bx , pady=(0,5))

    # 筆路試清冊
    menu_title = label_frame(menu, '  筆路試清冊  ')
    menu_title.grid(row=4, column=0, sticky='nswe', padx=x , pady=y)
    # 使按鈕填滿其所在的 label_frame
    menu_title.columnconfigure(0, weight=1)
    # 为两行配置权重，确保它们可以根据内容自动调整大小
    menu_title.rowconfigure(0, weight=1)
    menu_title.rowconfigure(1, weight=1)
    menu_title.rowconfigure(2, weight=1)

    menu_btn(menu_title, text='筆試清冊作業' , command = lambda: written_exam_roster(content)).grid(row=0, column=0, sticky='nswe' ,  padx=bx , pady=(15,2))

    menu_btn(menu_title, text='路試清冊作業' , command = lambda: road_test_roster(content)).grid(row=1, column=0, sticky='nswe' ,  padx=bx , pady=(0,2))

    menu_btn(menu_title, text='場考清冊作業' , command = lambda: driving_test_roster(content)).grid(row=2, column=0, sticky='nswe' ,  padx=bx , pady=(0,5))

    # 監理站名冊
    menu_title = label_frame(menu, '  監理站名冊  ')
    menu_title.grid(row=5, column=0, sticky='nswe', padx=x , pady=y)
    # 使按鈕填滿其所在的 label_frame
    menu_title.columnconfigure(0, weight=1)
    menu_title.rowconfigure(0, weight=1)

    menu_btn(menu_title, text='M2  補訓名冊' , command = lambda: m2_retraining_roster_creation(content)).grid(row=0, column=0, sticky='nswe' ,  padx=bx , pady=(15,5))
    
    # # 學習駕照
    # menu_title = label_frame(menu, '  學習駕照  ' )
    # menu_title.grid(row=2, column=0, sticky='nswe', padx=x , pady=y)
    # # 使按鈕填滿其所在的 label_frame
    # menu_title.columnconfigure(0, weight=1)
    # # 为两行配置权重，确保它们可以根据内容自动调整大小
    # menu_title.rowconfigure(0, weight=1)
    # menu_title.rowconfigure(1, weight=1)
    
    # menu_btn(menu_title, text='學照日期登錄' , command = lambda: learner_license_date_registration(content)).grid(row=0, column=0, sticky='nswe' , padx=bx , pady=(15,2))
    
    # menu_btn(menu_title, text='學照統一送件' , command = lambda: learner_license_submission(content)).grid(row=1, column=0, sticky='nswe',padx=bx , pady=(0,5))
    
    # # 開結訓名冊
    # menu_title = label_frame(menu, '  開結訓名冊  ')
    # menu_title.grid(row=3, column=0, sticky='nswe', padx=x , pady=y)
    # # 使按鈕填滿其所在的 label_frame
    # menu_title.columnconfigure(0, weight=1)
    # # 为两行配置权重，确保它们可以根据内容自动调整大小
    # menu_title.rowconfigure(0, weight=1)
    # menu_title.rowconfigure(1, weight=1)
    
    # menu_btn(menu_title, text='開訓名冊作業' , command = lambda: opening_training_roster(content)).grid(row=0, column=0, sticky='nswe', padx=bx , pady=(15,2))
    
    # menu_btn(menu_title, text='結訓名冊作業' , command = lambda: closing_training_roster(content)).grid(row=1, column=0, sticky='nswe',padx=bx , pady=(0,5))
    
    # # 筆路試清冊
    # menu_title = label_frame(menu, '  筆路試清冊  ')
    # menu_title.grid(row=4, column=0, sticky='nswe', padx=x , pady=y)
    # # 使按鈕填滿其所在的 label_frame
    # menu_title.columnconfigure(0, weight=1)
    # # 为两行配置权重，确保它们可以根据内容自动调整大小
    # menu_title.rowconfigure(0, weight=1)
    # menu_title.rowconfigure(1, weight=1)
    # menu_title.rowconfigure(2, weight=1)
    
    # menu_btn(menu_title, text='筆試清冊作業' , command = lambda: written_exam_roster(content)).grid(row=0, column=0, sticky='nswe' ,  padx=bx , pady=(15,2))
    
    # menu_btn(menu_title, text='路試清冊作業' , command = lambda: road_test_roster(content)).grid(row=1, column=0, sticky='nswe' ,  padx=bx , pady=(0,2))
    
    # menu_btn(menu_title, text='場考清冊作業' , command = lambda: driving_test_roster(content)).grid(row=2, column=0, sticky='nswe' ,  padx=bx , pady=(0,5))
    
    # # 監理站名冊
    # menu_title = label_frame(menu, '  監理站名冊  ')
    # menu_title.grid(row=5, column=0, sticky='nswe', padx=x , pady=y)
    # # 使按鈕填滿其所在的 label_frame
    # menu_title.columnconfigure(0, weight=1)
    # menu_title.rowconfigure(0, weight=1)
    
    # menu_btn(menu_title, text='M2  補訓名冊' , command = lambda: m2_retraining_roster_creation(content)).grid(row=0, column=0, sticky='nswe' ,  padx=bx , pady=(15,5))