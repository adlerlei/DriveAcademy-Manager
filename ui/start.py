import tkinter as tk
from tkinter import PhotoImage
from utils.config import *

def start(content):
    clear_frame(content)
    
    # 加载背景图片
    # 持久的引用是将图片保存为 root 的属性
    content.bg_image = PhotoImage(file='resources/img/startbg.png')  # 替换为你的图片路径
    # 设置背景图片
    bg_label = tk.Label(content, image=content.bg_image, width=500, height=500)
    bg_label.place(x=0, y=0, relheight=1, relwidth=1)