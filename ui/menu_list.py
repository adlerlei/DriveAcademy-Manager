from utils.widget import menu_btn, menu_logo, disable_all_menu_buttons
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
from .instructor_all import instructor_all
from .written_exam_roster import written_exam_roster


def menu_list(menu , content):
    buttons = [] # 創建一個空列表來存儲按鈕對象

    logo_label = menu_logo(menu, load_image)
    logo_label.grid(row=0, column=0, sticky='nsew', pady=(30,0))

    
    # 年度期別新增
    btn1 = menu_btn(
        menu,
        '年度期別新增',
        menu_icon_path = "annual_plan_term.png",
        command = lambda: annual_plan_term(content))
    btn1.grid(row=1, column=0)
    buttons.append(btn1)

    # 學員資料作業
    btn2 = menu_btn(
        menu,
        '學員資料作業',
        menu_icon_path = "student_all.png",
        command = lambda: student_all(content))
    btn2.grid(row=2, column=0)
    buttons.append(btn2)

    # 學照統一送件
    btn3 = menu_btn(
        menu,
        '學照統一送件',
        menu_icon_path = "learner_license_submission.png",
        command = lambda: learner_license_submission(content))
    btn3.grid(row=3, column=0)
    buttons.append(btn3)
    
    # 學照日期登錄
    btn4 = menu_btn(
        menu,
        '學照日期登錄',
        menu_icon_path = "learner_license_date_registration.png",
        command = lambda: learner_license_date_registration(content))
    btn4.grid(row=4, column=0)
    buttons.append(btn4)

    # 開訓名冊作業
    btn5 = menu_btn(
        menu,
        '開訓名冊作業',
        menu_icon_path = "opening_training_roster.png",
        command = lambda: opening_training_roster(content))
    btn5.grid(row=5, column=0)
    buttons.append(btn5)
    
    # M2  補訓名冊
    btn6 = menu_btn(
        menu,
        'M2  補訓名冊',
        menu_icon_path = "m2_retraining_roster_creation.png",
        command = lambda: m2_retraining_roster_creation(content))
    btn6.grid(row=6, column=0)
    buttons.append(btn6)

    # 結訓名冊作業
    btn7 = menu_btn(
        menu,
        '結訓名冊作業',
        menu_icon_path = "closing_training_roster.png",
        command = lambda: closing_training_roster(content))
    btn7.grid(row=7, column=0)
    buttons.append(btn7)
    
    # 場考清冊作業
    btn8 = menu_btn(
        menu,
        '場考清冊作業',
        menu_icon_path = "driving_test_roster.png",
        command = lambda: driving_test_roster(content))
    btn8.grid(row=8, column=0)
    buttons.append(btn8)
    
    # 路試清冊作業
    btn9 = menu_btn(
        menu,
        '道考清冊作業',
        menu_icon_path = "road_test_roster.png",
        command = lambda: road_test_roster(content))
    btn9.grid(row=9, column=0)
    buttons.append(btn9)

    # 筆試清冊作業
    btn10 = menu_btn(
        menu,
        '筆試清冊作業',
        menu_icon_path = "written_exam_roster.png",
        command = lambda: written_exam_roster(content))
    btn10.grid(row=10, column=0)
    buttons.append(btn10)
    
    # 教練資料作業
    btn11 = menu_btn(
        menu,
        '教練資料作業',
        menu_icon_path = "instructor.png",
        command = lambda: instructor_all(content))
    btn11.grid(row=11, column=0)
    buttons.append(btn11)


    disable_all_menu_buttons(buttons) # 將所有按鈕設為不可用狀態

    return buttons