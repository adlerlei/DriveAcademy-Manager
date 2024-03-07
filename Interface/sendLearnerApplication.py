# 學照送件介面 - sendLearnerApplication
import tkinter as tk
from tkinter import ttk
from utils.utility_functions import *


def sendLearnerApplication(frame_main):
    clear_frame(frame_main)

    
    frame_title = frame_fun(frame_main)
    frame_title.pack(fill='x')
    label_fun(frame_title, '學照資料作業 - 學照送件').pack(side='left', padx=(20,0), pady=7)
    
    button_frame = frame_fun(frame_main)
    button_frame.pack(fill='x')

    button_fun(button_frame, '學照日期登入', width=8, height=3, command=lambda: sendLearnerApplication(frame_main)).pack(side='left', padx=(20, 0), pady=7)