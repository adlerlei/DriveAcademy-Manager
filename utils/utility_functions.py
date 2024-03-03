import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import os
from tkinter import font


# clear frame content
def clear_frame(frame):
    # remove frame all element
    for widget in frame.winfo_children():
        widget.destroy()
        
# admin login and state button menu
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
    
# ui font 自定義字體
def ui_font():
    return font.Font(family='.AppleSystemUIFont', size=13)

# frmae 容器
def frame_function(frame, fill_var, padx=None , pady=None, side=None, expand=None, bg=None):
    frame = tk.Frame(frame, bg=bg)
    frame.pack( fill=fill_var, expand=expand, padx=padx, pady=pady, side=side)
    return frame

# Label 文字顯示
def label_function(frame, text, side, padx, pady, fg='#626262'):
    label = tk.Label(frame, text=text, font=ui_font(), fg=fg)
    label.pack(side=side, padx=padx, pady=pady)

# button 按鈕
def button_function(frame, text, width, height, side, padx, pady, fg='#626262', command=None):
    button = tk.Button(frame, text=text, font=ui_font(), fg=fg, width=width, height=height)
    button.pack(side=side, padx=padx, pady=pady)

# Combobox 下拉選單
def combobox_function(frame, width, values, side, padx, pady):
    combobox = ttk.Combobox(
        frame,
        width = width,
        font = ui_font(),
        values = values
    )
    combobox.pack(side=side, padx=padx, pady=pady)
    
# entry 用戶輸入欄位
def entry_function(frame, width, side, padx, pady):
    entry = tk.Entry(frame, width=width, font=ui_font())
    entry.pack(side=side, padx=padx, pady=pady)
    

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