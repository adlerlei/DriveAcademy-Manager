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


# 新增按鈕
def add_btn(frame, text, command):
    button = ck.CTkButton(
        frame,
        text = text,
        height = 40,
        fg_color = '#669bbc', 
        font = create_font(), 
        command = command
        )
    return button

# 修改按鈕
def modify_btn(frame, text, command):
    button = ck.CTkButton( 
        frame, 
        text = text,
        height = 40,
        fg_color = '#a09382', 
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

# 查詢按鈕
def search_btn(frame, text, command):
    button = ck.CTkButton( 
        frame, 
        text = text,
        height = 40,
        fg_color = '#edafb8', 
        font = create_font(), 
        command = command
        )
    return button

# 列印按鈕
def print_btn(frame, text, command):
    button = ck.CTkButton(
        frame,
        text = text,
        height = 40,
        fg_color = '#fb8500',
        font = create_font(),
        command = command
    )
    return button

# 登入，註冊 按鈕
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
    command=None, 
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
        command=command, 
        fg_color=fg_color, **kwargs
        )


# entry 用戶輸入欄位
def entry(
    frame, 
    placeholder_text = '',
    height = 40,
    font = create_font(),
    fg_color = '#d9d9d9',
    text_color = '#8b8c89',
    placeholder_text_color = '#a78a7f',  # 添加這個參數，設置一個默認值
    **kwargs
):
    return ck.CTkEntry(
        frame, 
        placeholder_text = placeholder_text,
        border_color = '#fdfdff',
        height = height,
        font = font, 
        fg_color = fg_color,
        text_color = text_color,
        placeholder_text_color = placeholder_text_color,  # 添加這個參數
        **kwargs 
    )


# entry 用戶資料顯示欄位，禁止用戶輸入
def display_entry_value(
    frame, 
    placeholder_text = '',
    height = 40,
    font = create_font(),
    state = "readonly",
    fg_color = '#d9d9d9',
    text_color = '#8b8c89',
    placeholder_text_color = '#aa998f',  # 添加這個參數，設置一個默認值
    **kwargs
    ):
    return ck.CTkEntry(
        frame,
        placeholder_text = placeholder_text,
        border_color = '#fdfdff',
        height = height,
        font = font,
        state = state,
        fg_color = fg_color,
        text_color = text_color ,
        placeholder_text_color = placeholder_text_color,  # 添加這個參數
        **kwargs 
        )


# 清空所有 entry 和 combobox 的函式
def clear_entries_and_comboboxes(frame, keep_entries=None):
    # 移除对 current_student_id 的引用
    # 遍历父元件的所有子元件
    for child in frame.winfo_children():
        # 如果是 CTkEntry 或 Entry
        if isinstance(child, ck.CTkEntry) or isinstance(child, Entry):
            if keep_entries is None or child not in keep_entries:
                child.configure(state='normal')  # 设置为可编辑状态
                child.delete(0, ck.END)  # 清空内容
                if child.cget('state') == 'readonly':
                    child.configure(state='readonly')
        # 如果是 CTkComboBox
        elif isinstance(child, ck.CTkComboBox):
            if keep_entries is None or child not in keep_entries:
                child.set('')  # 清空选项