# 期別管理界面
import tkinter as tk
from tkinter import ttk
from utils.utility_functions import clear_frame



def create_batch_window(frame_main):
    clear_frame(frame_main)
    label = tk.Label(frame_main, text="這是期別界面",bg="#60C1FF")
    label.place(x=130, y=420)