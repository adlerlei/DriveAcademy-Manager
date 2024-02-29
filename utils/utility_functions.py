import tkinter as tk
from tkinter import PhotoImage
import os
from tkinter import font


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
    
# ui font
def ui_font():
    return font.Font(family='PingFang', size=13)

# # title font
# def title_font():
#     return font.Font(family='burnfont-1.1', size=40)
# # button font
# def button_font():
#     return font.Font(family='PingFang', size=15)


# # option menu font
# def option_menu_font(option_menu_var_name, menu):
#     xx = font.Font(family='PingFang', size=20)
#     option_menu_var_name.config(font=xx)
#     option_menu_var_name[menu].config(font=xx)