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
    
    # logo ###########
    logo_image = load_image("resources/img/logo.png")
    logo_img = ck.CTkImage(light_image=logo_image, size=(500, 250))
    label(menu , "" , image = logo_img , compound = 'top').pack(side = "top" , fill='x', pady = (100,0) , expand=False)
    #################
    
    menu_btn( menu , text = '年度期別新增' , height = 40 , fg_color = "#669bbc" , command = lambda: annual_plan_term(content)).pack(fill = 'x')

    menu_btn(menu, text='學員資料作業' , command = lambda: student_all(content)).pack()

    menu_btn(menu, text='學照日期登錄' , command =  lambda: learner_license_date_registration(content)).pack()

    menu_btn(menu, text='學照統一送件' , command = lambda: learner_license_submission(content)).pack()

    menu_btn(menu, text='開訓名冊作業' , command = lambda: opening_training_roster(content)).pack()

    menu_btn(menu, text='結訓名冊作業' , command = lambda: closing_training_roster(content)).pack()

    menu_btn(menu, text='筆試清冊作業' , command = lambda: written_exam_roster(content)).pack()

    menu_btn(menu, text='路試清冊作業' , command = lambda: road_test_roster(content)).pack()

    menu_btn(menu, text='場考清冊作業' , command = lambda: driving_test_roster(content)).pack()

    menu_btn(menu, text='M2  補訓名冊' , command = lambda: m2_retraining_roster_creation(content)).pack()