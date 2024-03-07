import tkinter as tk
from utils.utility_functions import clear_frame


def start_window(frame_main):
    clear_frame(frame_main)

    # 這裡將圖片引用存储在 frame_main 的一個屬性中以保持引用
    frame_main.img = tk.PhotoImage(file="img/stay.png")
    img_label = tk.Label(frame_main, image=frame_main.img)
    img_label.place(x=300, y=200)