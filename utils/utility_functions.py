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
    
# custom font 自定義字體
def custom_font():
    return font.Font(family='.AppleSystemUIFont', size=13)

# frmae 容器
def frame_fun(frame, **kwargs):
    return tk.Frame(frame, **kwargs) 
    # 禁止Frame根据里面放置的控件的大小自动调整其大小
    # frame.pack_propagate(False)
    
# label frame 標題容器
def label_frame_fun(frame, text, fg='#626262', **kwargs):
    # 設定標題字體
    # label_frame.config(font=custom_font())
    # 設定標題背景色
    # label_frame.config(bg='#f8f8f8')
    # 設定標題圓角
    # label_frame.config(relief='groove')
    # 設定標題圓角距離
    # label_frame.config(bd=5)
    # 設定標題圓角距離
    # label_frame.config(padx=10, pady=10)
    # 設定標題圓角距離
    # label_frame.config(borderwidth=5)
    return tk.LabelFrame(frame, text=text, fg=fg , font=custom_font(), **kwargs)

# Label 文字顯示
def label_fun(frame, text, fg='#626262', **kwargs):
    return tk.Label(frame, text=text, fg=fg, font=custom_font(), **kwargs)

# 必填小圖示
def required(frame, text='㊒', side='left', fg='#eb9f9f', padx=(20,0)):
    return tk.Label(frame, text=text, fg=fg).pack(side=side, padx=padx)

# button 按鈕
def button_fun(frame, text, fg='#626262',  **kwargs):
    return tk.Button(frame, text=text, fg=fg, font=custom_font(), **kwargs)


# Combobox 下拉選單
def combobox_fun(frame, **kwargs):
    return ttk.Combobox(frame, font=custom_font(), **kwargs)
# def combobox_fun(frame, width=None, values=None, side=None, padx=None, pady=None):
#     combobox = ttk.Combobox(
#         frame,
#         width = width,
#         font = custom_font(),
#         values = values
#     )
#     combobox.pack(side=side, padx=padx, pady=pady)
#     return combobox
    
# entry 用戶輸入欄位
def entry_fun(frame, **kwargs):
    return tk.Entry(frame,  font=custom_font(), **kwargs)
    
# frame hr 水平分隔線
def hr_fun(frame, relief=None, **kwargs):
    return tk.Frame(frame, relief=relief, **kwargs)

# hr_fun(display_students_data_row2, height=2, bd=1, relief='sunken').pack(fill='x', padx=(20, 20), pady=(0,10))

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