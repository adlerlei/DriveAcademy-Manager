from tkinter import ttk
from tkinter import *
import customtkinter as ck
from utils.config import create_font
from PIL import Image

menu_buttons = []  # 創建一個全局列表來存儲按鈕實例
# 選單logo
def menu_logo(menu, load_image, text=""):
    logo_image = load_image("resources/img/logo.png")
    logo_img = ck.CTkImage(light_image=logo_image, size=(250,250))
    return ck.CTkLabel(menu, text=text, image=logo_img, compound='top')


# 選單按鈕
def menu_btn(frame, text, menu_icon_path, height=40, fg_color="#669bbc", font = create_font(), command=None):
    menu_icon = Image.open(f"resources/img/menu/{menu_icon_path}")
    menu_icon_ctk = ck.CTkImage(light_image=menu_icon)
    button = ck.CTkButton(frame, text=text, height=height, fg_color=fg_color, font=font, image=menu_icon_ctk, command=command, state='disabled')
    button.grid(sticky='nsew')
    return button

# 禁用選單按鈕
def disable_menu_btn(button):
    button.configure(state='disabled')

# 啟用選單按鈕
def enable_menu_btn(button):
    button.configure(state='normal')

# 禁用所有選單按鈕
def disable_all_menu_buttons(buttons):
    for button in buttons:
        if button is not None:
            disable_menu_btn(button)


# 按鈕
def btn(frame, text, command):
    button = ck.CTkButton( 
        frame, 
        text = text,
        height = 40,
        fg_color = '#669bbc', 
        font = create_font(), 
        command = command
        )
    return button

# 刪除按鈕
def delete_btn(frame, text, command):
    button = ck.CTkButton( 
        frame, 
        text = text,
        height = 40,
        fg_color = '#E0645D', 
        font = create_font(), 
        command = command
        )
    return button

# 匯出按鈕
def export_btn(frame, text, command):
    button = ck.CTkButton( 
        frame, 
        text = text,
        height = 40,
        fg_color = '#a3b18a', 
        font = create_font(), 
        command = command
        )
    return button


# label frame 標題容器
def label_frame(frame, text):
    return ttk.LabelFrame(frame, text=text)


# frmae 容器
def frame(frame, fg_color='#fdfdff'):
    return ck.CTkFrame(frame, fg_color=fg_color) 


# Label 文字顯示
def label(frame, text, text_color='#669bbc', font=create_font()):
    return ck.CTkLabel(frame, text=text, text_color=text_color, font=font)


# Combobox 下拉選單 
def combobox(
    frame, 
    height=40, 
    text_color='#8b8c89', 
    fg_color='#d9d9d9', 
    button_color='#bcb8b1', 
    font = create_font(), 
    dropdown_fg_color='#d9d9d9', 
    **kwargs
    ):
    return ck.CTkComboBox(
        frame, 
        height=height, 
        text_color=text_color, 
        border_color='#fdfdff', 
        font=font, 
        button_color=button_color, 
        dropdown_fg_color=dropdown_fg_color, 
        fg_color=fg_color, **kwargs
        )


# entry 用戶輸入欄位
def entry(
    frame , 
    placeholder_text = '',
    # width = 200,
    height = 40,
    font = create_font() , 
    fg_color = '#d9d9d9',
    text_color = '#8b8c89',
    **kwargs
    ):
    return ck.CTkEntry(
        frame, 
        placeholder_text = placeholder_text ,
        border_color = '#fdfdff',
        # width = width ,
        height = height ,
        font = font , 
        fg_color = fg_color,
        text_color = text_color ,
        **kwargs 
        )


# entry 用戶資料顯示欄位，禁止用戶輸入
def display_entry_value(
    frame, 
    placeholder_text = '',
    # width = 200,
    height = 40,
    font = create_font(),
    state = "readonly",
    fg_color = '#d9d9d9',
    text_color = '#8b8c89',
    **kwargs
    ):
    return ck.CTkEntry(
        frame,
        placeholder_text = placeholder_text,
        border_color = '#fdfdff',
        # width = width,
        height = height,
        font = font,
        state = state,
        fg_color = fg_color,
        text_color = text_color ,
        **kwargs 
        )