
from tkinter import PhotoImage
import os
from tkinter import font


# 設定所有介面文字顏色
font_color = {
    '期別新增': '#A1CCD1',
    '學員管理': '#E9B384',
    '學習駕照': '#8CC0DE',
    '開結訓名冊': '#FFCACC',
    '筆路試清冊': '#DBC4F0',
    '監理站名冊': '#FF9B9B',
    'required_font': "#DE847B", # 必填寫顯示文字顏色
    'entry_display_value': '#9ab1cd', # entry 顯示值
    'entry_font': '#bb9e88', # entry 輸入文字顏色
    'button_font': '#a2a2a2', # button 文字顏色
    'label_font': '#a2a2a2', # label 文字顏色
    'display_info_label': '#de6276' # display info title 文字顏色
}
    

# 更改系統 icon
def app_icon(root):
    # app icon image path
    icon_path = os.path.join(os.path.dirname(__file__), '..', 'resources','img', 'icon.png')
    # create img 
    img_icon = PhotoImage(file=icon_path)
    # set app window icon
    root.iconphoto(False, img_icon)
    
    
# custom font 自定義字體
def custom_font():
    return font.Font(family='HanyiSentyCrayon', size=30)
    # return font.Font(family='.AppleSystemUIFont', size=14)
    

# 清除 frame 佈局內容
def clear_frame(frame):
    # remove frame all element
    for widget in frame.winfo_children():
        widget.destroy()