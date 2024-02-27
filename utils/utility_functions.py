import tkinter as tk
from tkinter import PhotoImage
import os


# clear frame content
def clear_frame(frame):
    # remove frame all element
    for widget in frame.winfo_children():
        widget.destroy()
        
# admin login and state button
def enable_buttons(buttons):
    for button in buttons:
        button['state'] = 'normal'

# setting app icon
def set_app_icon(root):
    # app icon image path
    icon_path = os.path.join(os.path.dirname(__file__), '..', 'img', 'logo.png')
    # create img 
    img_icon = PhotoImage(file=icon_path)
    # set app window icon
    root.iconphoto(False, img_icon)
    

    