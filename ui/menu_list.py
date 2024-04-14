from utils.widget import menu_btn, menu_logo
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
    
    logo_label = menu_logo(menu, load_image)
    logo_label.grid(row=0, column=0, sticky='nsew', pady=(30,0))

    # 年度期別新增
    menu_btn(
        menu, 
        '年度期別新增', 
        menu_icon_path = "annual_plan_term.png",
        command = lambda: annual_plan_term(content)).grid(row=1, column=0)

    # 學員資料作業
    menu_btn(
        menu,
        '學員資料作業',
        menu_icon_path = "student_all.png",
        command = lambda: student_all(content)).grid(row=2, column=0)
    

    # 學照日期登錄
    menu_btn(
        menu,
        '學照日期登錄',
        menu_icon_path = "learner_license_date_registration.png",
        command = lambda: learner_license_date_registration(content)).grid(row=3, column=0)
    

    # 學照統一送件
    menu_btn(
        menu,
        '學照統一送件',
        menu_icon_path = "learner_license_submission.png",
        command = lambda: learner_license_submission(content)).grid(row=4, column=0)

    # 開訓名冊作業
    menu_btn(
        menu,
        '開訓名冊作業',
        menu_icon_path = "opening_training_roster.png",
        command = lambda: opening_training_roster(content)).grid(row=5, column=0)

    # 結訓名冊作業
    menu_btn(
        menu,
        '結訓名冊作業',
        menu_icon_path = "closing_training_roster.png",
        command = lambda: closing_training_roster(content)).grid(row=6, column=0)

    # 筆試清冊作業
    menu_btn(
        menu,
        '筆試清冊作業',
        menu_icon_path = "written_exam_roster.png",
        command = lambda: written_exam_roster(content)).grid(row=7, column=0)

    # 路試清冊作業
    menu_btn(
        menu,
        '道考清冊作業',
        menu_icon_path = "road_test_roster.png",
        command = lambda: road_test_roster(content)).grid(row=8, column=0)

    # 場考清冊作業
    menu_btn(
        menu,
        '場考清冊作業',
        menu_icon_path = "driving_test_roster.png",
        command = lambda: driving_test_roster(content)).grid(row=9, column=0)

    # M2  補訓名冊
    menu_btn(
        menu,
        'M2  補訓名冊',
        menu_icon_path = "m2_retraining_roster_creation.png",
        command = lambda: m2_retraining_roster_creation(content)).grid(row=10, column=0)