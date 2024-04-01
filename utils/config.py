from tkinter import PhotoImage
import os
from PIL import Image


def load_image(path, size=(500, 250)):
    # 使用 Pillow 加載圖像
    pil_image = Image.open(path)
    # 調整圖像大小
    # pil_image.thumbnail(size)
    pil_image = pil_image.resize(size)
    return pil_image

# system icon
def app_icon(root):
    # app icon image path
    icon_path = os.path.join(os.path.dirname(__file__), '..', 'resources','img', 'icon.png')
    # create img 
    img_icon = PhotoImage(file=icon_path)
    # set app window icon
    root.iconphoto(False, img_icon)
    
# 清除 frame 佈局內容
def clear_frame(frame):
    # remove frame all element
    for widget in frame.winfo_children():
        widget.destroy()
        
# 變更字體以及字體大小
def create_font(size=17, font_family=''):
    return (font_family, size)