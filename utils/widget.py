# 導入 ttkbootstrap 模組
import ttkbootstrap as ttk


# 新增按鈕 
def add_btn(frame, text, **kwargs):
    button = ttk.Button(frame, text=text, **kwargs)
    return button

# 修改按鈕
def edit_btn(frame, text, **kwargs):
    button = ttk.Button(frame, text=text, **kwargs)
    return button

# 查詢按鈕
def search_btn(frame, text, **kwargs):
    button = ttk.Button(frame, text=text, **kwargs)
    return button

# 刪除按鈕
def delete_btn(frame, text, **kwargs):
    button = ttk.Button(frame, text=text, **kwargs)
    return button


# 選單按鈕
def menu_btn(frame, text, **kwargs):
    button = ttk.Button(frame, text=text, **kwargs)
    return button


# 登入按鈕
def login_btn(frame, text, **kwargs):
    button = ttk.Button(frame, text=text, **kwargs)
    return button


# 註冊按鈕
def register_btn(frame, text, **kwargs):
    button = ttk.Button(frame, text=text, **kwargs)
    return button


# label frame 標題容器
def label_frame(frame, text, bootstyle="info", **kwargs):
    return ttk.LabelFrame(frame, text=text, bootstyle=bootstyle, **kwargs)


# frmae 容器
def frame(frame, **kwargs):
    return ttk.Frame(frame, **kwargs) 


# Label 文字顯示
def label(frame, text, **kwargs):
    return ttk.Label(frame, text=text, **kwargs)

# # display info title 說明文字
# def display_info_label(frame, text, fg=font_color['display_info_label'], **kwargs):
#     return tk.Label(frame, text=text, fg=fg, font=custom_font(), **kwargs)


# Combobox 下拉選單
def combobox(frame, **kwargs):
    # style = ttk.Style()
    # style.theme_use('default')  # 使用預設主題
    # style.configure('TCombobox')
    return ttk.Combobox(frame, **kwargs)


# entry 用戶輸入欄位
def entry(frame,**kwargs):
    return ttk.Entry(frame,**kwargs)


# entry 顯示值禁止用戶輸入
def display_entry_value(frame, state="readonly", **kwargs):
    return ttk.Entry(frame, state=state, **kwargs)


# # frame hr 水平分隔線
# def hr(frame, height=2, bd=1, relief='sunken'):
#     return tk.Frame(frame, height=height, bd=bd, relief=relief)

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