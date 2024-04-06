# 導入 ck.CTkbootstrap 模組
from tkinter import ttk
import customtkinter as ck
from utils.config import create_font
from PIL import Image


# 選單logo
def menu_logo(menu, load_image, text=""):
    logo_image = load_image("resources/img/logo.png")
    logo_img = ck.CTkImage(light_image=logo_image, size=(500, 250))
    return ck.CTkLabel(menu , text=text , image = logo_img , compound = 'top')
    #.pack(side = "top" , fill='x', pady = (50,0) , expand=False)
    
# 新增按鈕
def add_btn( frame , text , font = create_font() ,**kwargs ):
    button = ck.CTkButton( frame , text = text , font = font ,**kwargs )
    return button

# 修改按鈕
def edit_btn( frame , text , font = create_font() , **kwargs ):
    button = ck.CTkButton( frame , text = text , font = font , **kwargs )
    return button

# 查詢按鈕
def search_btn( frame , text , font = create_font() , **kwargs ):
    button = ck.CTkButton( frame , text = text , font = font , **kwargs )
    return button

# 刪除按鈕
def delete_btn( frame , text , font = create_font() , **kwargs ):
    button = ck.CTkButton( frame , text = text , font = font , **kwargs )
    return button


# 選單按鈕
def menu_btn(frame, text, menu_icon_path, height=40, fg_color="#669bbc", font=create_font(), command=None):
    menu_icon = Image.open(f"resources/img/menu/{menu_icon_path}")
    menu_icon_ctk = ck.CTkImage(light_image=menu_icon)
    button = ck.CTkButton(frame, text=text, height=height, fg_color=fg_color, font=font, image=menu_icon_ctk, command=command)
    button.grid(sticky='nsew')
    return button


# 按鈕
def btn(
    frame, 
    text,
    width = 200,
    height = 40,
    fg_color = '#669bbc', 
    font = create_font(), 
    **kwargs
    ):
    button = ck.CTkButton( 
        frame, 
        text = text,
        width = width,
        height = height,
        fg_color = fg_color, 
        font = font, 
        **kwargs
        )
    return button


# label frame 標題容器
def label_frame( frame , text , **kwargs ):
    return ttk.LabelFrame( frame , text = text , **kwargs )


# frmae 容器
def frame( frame , fg_color = '#fdfdff' , **kwargs ):
    return ck.CTkFrame( frame , fg_color = fg_color , **kwargs ) 


# Label 文字顯示
def label( frame , text , font = ('defoult' , 17) , **kwargs ):
    return ck.CTkLabel( frame , text=text , font = font , **kwargs )


# Combobox 下拉選單
def combobox( frame , **kwargs ):
    # style = ck.CTkStyle()
    # style.theme_use('default')  # 使用預設主題
    # style.configure('TCombobox')
    return ck.CTkComboBox( frame , **kwargs )


# entry 用戶輸入欄位
def entry(
    frame , 
    placeholder_text = '',
    width = 200,
    height = 40,
    font = ( 'default' , 17 ) , 
    **kwargs
    ):
    return ck.CTkEntry(
        frame , 
        placeholder_text = placeholder_text ,
        width = width ,
        height = height ,
        font = font , 
        **kwargs 
        )


# entry 顯示值禁止用戶輸入
def display_entry_value( frame , font = ( 'default' , 17 ) , state = "readonly" , **kwargs ):
    return ck.CTkEntry( frame , font = font , state = state , **kwargs )


# 查看 frame 中的所有控件，并禁用它们
def disable_frame_widgets( frame ):
    for widget in frame.winfo_children():
        try:
            if 'state' in widget.configure():
                widget.configure( state = 'disabled' )
            disable_frame_widgets( widget )  # 递归调用以禁用嵌套子控件
        except Exception as e:
            print( f"Error disabling widget { widget } : { e }")


# 查看 frame 中的所有控件，并启用它们
def enable_frame_widgets( frame ):
    for widget in frame.winfo_children():
        try:
            if 'state' in widget.configure():
                widget.configure( state = 'normal' )
            enable_frame_widgets( widget )  # 递归调用以启用嵌套子控件
        except Exception as e:
            print( f"Error enabling widget { widget } : { e }" )