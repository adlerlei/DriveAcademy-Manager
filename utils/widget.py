# 導入 ck.CTkbootstrap 模組
from tkinter import ttk
import customtkinter as ck
from utils.config import create_font


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
def menu_btn( frame , text , font = create_font() , **kwargs ):
    button = ck.CTkButton( frame , text = text , font = font ,**kwargs )
    return button


# 登入按鈕
def login_btn( frame , text  , font = create_font() , **kwargs ):
    button = ck.CTkButton( frame , text = text , font = font , **kwargs )
    return button


# 註冊按鈕
def register_btn( frame , text , font = create_font() , **kwargs ):
    button = ck.CTkButton( frame , text = text , font = font , **kwargs )
    return button


# label frame 標題容器
def label_frame( frame , text , **kwargs ):
    return ttk.LabelFrame( frame , text = text , **kwargs )


# frmae 容器
def frame( frame , **kwargs ):
    return ck.CTkFrame( frame , **kwargs ) 


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
def entry( frame , font = ( 'default' , 17 ) , **kwargs ):
    return ck.CTkEntry( frame , font = font , **kwargs )


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