# M2補訓名冊資料介面 M2SupplementalRosterCreationInterface
import tkinter as tk
from utils.utility_functions import clear_frame



def M2SupplementalRosterCreationInterface(frame_main):
    clear_frame(frame_main)
    label = tk.Label(frame_main, text="這是M2補訓名冊界面",bg="#60C1FF")
    label.place(x=130, y=420)