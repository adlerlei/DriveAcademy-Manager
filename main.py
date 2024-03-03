import tkinter as tk
from ui.main_window import create_main_window
from tkinter import font


def main():
    create_main_window()
    
    # 获取默认字体的名称和大小
    default_font = font.nametofont("TkDefaultFont")
    default_font_name = default_font.cget("family")
    default_font_size = default_font.cget("size")

    print(f"默认字体是：{default_font_name}")
    print(f"默认字体大小是：{default_font_size}")
    
    tk.mainloop()

if __name__ == '__main__':
    main()
