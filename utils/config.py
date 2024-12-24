# 清除 frame 佈局內容
def clear_frame(frame):
    # remove frame all element
    for widget in frame.winfo_children():
        widget.destroy()
        
# 變更字體以及字體大小
def create_font(size=19, font_family=''):
    return (font_family, size)