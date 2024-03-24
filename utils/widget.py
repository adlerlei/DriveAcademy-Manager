import tkinter as tk
from tkinter import ttk
from utils.config import custom_font, font_color
from tkinter import PhotoImage

# 設定按鈕的大小
btnx = 10
btny = 10
# 新增按鈕
def add_btn(frame, text, compound='left', fg=font_color['button_font'], **kwargs):
    add_icon = PhotoImage(file='resources/img/add.png') # 載入圖片
    button = tk.Button(frame, text=text, fg=fg, padx=btnx, pady=btny, font=custom_font(), image=add_icon, compound=compound, **kwargs)
    button.add_icon = add_icon  # 保持對圖像的引用
    return button

# 修改按鈕
def edit_btn(frame, text, compound='left', fg=font_color['button_font'], **kwargs):
    edit_icon = PhotoImage(file='resources/img/edit.png') # 載入圖片
    button = tk.Button(frame, text=text, fg=fg, padx=btnx, pady=btny, font=custom_font(), image=edit_icon, compound=compound, **kwargs)
    button.edit_icon = edit_icon  # 保持對圖像的引用
    return button

# 查詢按鈕
def search_btn(frame, text, compound='left', fg=font_color['button_font'], **kwargs):
    search_icon = PhotoImage(file='resources/img/search.png') # 載入圖片
    button = tk.Button(frame, text=text, fg=fg, padx=btnx, pady=btny, font=custom_font(), image=search_icon, compound=compound, **kwargs)
    button.search_icon = search_icon  # 保持對圖像的引用
    return button

# 刪除按鈕
def delete_btn(frame, text, compound='left', fg=font_color['button_font'], **kwargs):
    delete_icon = PhotoImage(file='resources/img/delete.png') # 載入圖片
    button = tk.Button(frame, text=text, fg=fg, padx=btnx, pady=btny, font=custom_font(), image=delete_icon, compound=compound, **kwargs)
    button.delete_icon = delete_icon  # 保持對圖像的引用
    return button


# 選單按鈕
def menu_btn(frame, text, compound='left', fg=font_color['button_font'], **kwargs):
    muen_icon = PhotoImage(file='resources/img/menu.png') # 載入圖片
    button = tk.Button(frame, text=text, padx=7, pady=7, fg=fg, font=custom_font(), image=muen_icon, compound=compound, **kwargs)
    button.muen_icon = muen_icon  # 保持對圖像的引用
    return button


# 登入按鈕
def login_btn(frame, text, compound='left', fg=font_color['button_font'], **kwargs):
    login_icon = PhotoImage(file='resources/img/login.png') # 載入圖片
    button = tk.Button(frame, text=text, fg=fg, padx=10, pady=10, font=custom_font(), image=login_icon, compound=compound, **kwargs)
    button.login_icon = login_icon  # 保持對圖像的引用
    return button


# 註冊按鈕
def register_btn(frame, text, compound='left', fg=font_color['button_font'], **kwargs):
    register_icon = PhotoImage(file='resources/img/register.png') # 載入圖片
    button = tk.Button(frame, text=text, fg=fg, padx=10, pady=10, font=custom_font(), image=register_icon, compound=compound, **kwargs)
    button.register_icon = register_icon  # 保持對圖像的引用
    return button


# label frame 標題容器
def label_frame(frame, text, fg=font_color['button_font'], **kwargs):
    return tk.LabelFrame(frame, text=text, fg=fg, font=custom_font(), **kwargs)


# frmae 容器
def frame(frame, **kwargs):
    return tk.Frame(frame, **kwargs) 


# Label 文字顯示
def label(frame, text, fg=font_color['label_font'], **kwargs):
    return tk.Label(frame, text=text, fg=fg, font=custom_font(), **kwargs)

# display info title 說明文字
def display_info_label(frame, text, fg=font_color['display_info_label'], **kwargs):
    return tk.Label(frame, text=text, fg=fg, font=custom_font(), **kwargs)


# Combobox 下拉選單
def combobox(frame, **kwargs):
    style = ttk.Style()
    style.theme_use('default')  # 使用預設主題
    style.configure('TCombobox', foreground=font_color['entry_font'])
    return ttk.Combobox(frame, style='TCombobox', font=custom_font(), **kwargs)


# entry 用戶輸入欄位
def entry(frame, fg=font_color['entry_font'], **kwargs):
    return tk.Entry(frame, fg=fg, font=custom_font(), **kwargs)


# entry 顯示值禁止用戶輸入
def display_entry_value(frame, state="readonly", fg=font_color['entry_display_value'], **kwargs):
    return tk.Entry(frame, fg=fg, state=state, font=custom_font(), **kwargs)


# frame hr 水平分隔線
def hr(frame, height=2, bd=1, relief='sunken'):
    return tk.Frame(frame, height=height, bd=bd, relief=relief)

# hr_fun(display_students_data_row2, height=2, bd=1, relief='sunken').pack(fill='x', padx=(20, 20), pady=(0,10))


# 查看 frame 中的所有控件，并禁用它们
def disable_frame_widgets(frame):
    for widget in frame.winfo_children():
        try:
            if 'state' in widget.configure():
                widget.configure(state='disabled')
            disable_frame_widgets(widget)  # 递归调用以禁用嵌套子控件
        except Exception as e:
            print(f"Error disabling widget {widget}: {e}")


# 查看 frame 中的所有控件，并启用它们
def enable_frame_widgets(frame):
    for widget in frame.winfo_children():
        try:
            if 'state' in widget.configure():
                widget.configure(state='normal')
            enable_frame_widgets(widget)  # 递归调用以启用嵌套子控件
        except Exception as e:
            print(f"Error enabling widget {widget}: {e}")