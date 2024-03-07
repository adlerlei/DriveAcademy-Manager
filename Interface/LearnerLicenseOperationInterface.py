# 學照資料作業主介面 LearnerLicenseOperationInterface
from utils.utility_functions import *
from .sendLearnerApplication import sendLearnerApplication



def LearnerLicenseOperationInterface(frame_main):
    clear_frame(frame_main)

    # title frame
    frame_title = frame_fun(frame_main)
    frame_title.pack(fill='x')
    label_fun(frame_title, '學照資料作業 - 學照登入').pack(side='left', padx=20, pady=7)

    # button frame
    button_frame = frame_fun(frame_main)
    button_frame.pack(fill='x')
    
    # button_fun(button_frame, '學照送件', width=8, height=3, 'left', (20,0), 7, command=lambda: sendLearnerApplication(frame_main))
    
    button_fun(button_frame, '學照送件', width=8, height=3, command=lambda: sendLearnerApplication(frame_main)).pack(side='left', padx=(20,0), pady=7)

    
    # search frame
    frame_search = frame_fun(frame_main)
    frame_search.pack(fill='x')
    
    label_fun(frame_search, '輸入學號：').pack(side='left', padx=(20,0), pady=7)
    entry_fun(frame_search, width=10).pack(side='left', pady=7)
    button_fun(frame_search, '查詢', width=5, height=1).pack(side='left', padx=10, pady=7)


    
    # form fr0000
    
    frame_form = frame_fun(frame_main)
    frame_form.pack(fill='x')
    
    label_fun(frame_form, '登錄日期：').pack(side='left', padx=20, pady=7)
    entry_fun(frame_form, width=10).pack(side='left', pady=7)
    
    label_fun(frame_form, '學照日期：').pack(side='left', padx=(20,0), pady=7)
    entry_fun(frame_form, width=10).pack(side='left', pady=7)
    
    label_fun(frame_form, '學照號碼：').pack(side='left', padx=(20,0), pady=7)
    entry_fun(frame_form, width=10).pack(side='left', pady=7)
    
    label_fun(frame_form, text='欠資料：').pack(side='left',padx=(20, 0), pady=7)

    entry_fun(frame_form, width=30).pack(side='left', pady=7)
    
    # hr frame
    hr_fun(frame_main, height=2, bd=1, relief='sunken').pack(fill='x', padx=(20,20), pady=7)
    
    # display student data title frame
    display_student_title = frame_fun(frame_main)
    display_student_title.pack(fill='x')
    label_fun(display_student_title, '學員資料顯示區').pack(side='left',padx=(20,0), pady=7)
    
    # display_student_data frame
    display_student_data = frame_fun(frame_main).pack(fill='x')
    
    



    # 使用兩個按鈕來區分 frame 上下兩個介面
    # 學照日期登陸介面 - LearnerLicenseDateRegistrationInterface
    # frame_registerLicenseDate = frame_fun(frame_main, 'x', padx=(20,20))


    # # 學照送件介面 - LearnerLicenseSubmissionInterface
    # frame_sendLearnerApplication = frame_fun(frame_main, 'x', padx=(20,20))