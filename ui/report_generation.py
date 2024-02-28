# M2補訓名冊
import tkinter as tk
from utils.utility_functions import clear_frame



def create_report_window(frame_main):
    clear_frame(frame_main)
    label = tk.Label(frame_main, text="這是M2補訓名冊界面",bg="#60C1FF")
    label.place(x=130, y=420)