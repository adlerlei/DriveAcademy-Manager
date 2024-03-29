from tkinter import PhotoImage
import os
    

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