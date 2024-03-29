# 導入 tbbootstrap 模組
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb


# 新增按鈕 
def add_btn( frame , text , **kwargs ):
    button = tb.Button( frame , text = text , **kwargs )
    return button

# 修改按鈕
def edit_btn( frame , text , **kwargs ):
    button = tb.Button( frame , text = text , **kwargs )
    return button

# 查詢按鈕
def search_btn( frame , text , **kwargs ):
    button = tb.Button( frame , text = text , **kwargs )
    return button

# 刪除按鈕
def delete_btn( frame , text , **kwargs ):
    button = tb.Button( frame , text = text , **kwargs )
    return button


# 選單按鈕
def menu_btn( frame , text , **kwargs ):
    style = tb.Style()
    style.configure( 'TButton' , font = ( 'default' , 17 ) )
    button = tb.Button( frame , text = text , **kwargs )
    return button


# 登入按鈕
def login_btn( frame , text  , **kwargs ):
    style = tb.Style()
    style.configure( 'TButton' , font = ( 'default' , 17 ) )
    button = tb.Button( frame , text = text , **kwargs )
    return button


# 註冊按鈕
def register_btn( frame , text , **kwargs ):
    button = tb.Button( frame , text = text , **kwargs )
    return button


# label frame 標題容器
def label_frame( frame , text , **kwargs ):
    style = tb.Style()
    style.configure( 'TLabelframe.Label' , font = ( 'default' , 17 ) )
    return tb.LabelFrame( frame , text = text , **kwargs )


# frmae 容器
def frame( frame , **kwargs ):
    return tb.Frame( frame , **kwargs ) 


# Label 文字顯示
def label( frame , text , font = ('defoult' , 17) , **kwargs ):
    return tb.Label( frame , text=text , font = font , **kwargs )


# Combobox 下拉選單
def combobox( frame , **kwargs ):
    # style = tb.Style()
    # style.theme_use('default')  # 使用預設主題
    # style.configure('TCombobox')
    return tb.Combobox( frame , **kwargs )


# entry 用戶輸入欄位
def entry( frame , font = ( 'default' , 17 ) , **kwargs ):
    return tb.Entry( frame , font = font , **kwargs )


# entry 顯示值禁止用戶輸入
def display_entry_value( frame , font = ( 'default' , 17 ) , state = "readonly" , **kwargs ):
    return tb.Entry( frame , font = font , state = state , **kwargs )


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