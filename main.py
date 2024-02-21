# 應用程序入口
import tkinter as tk
from ui.main_window import MainWindow # 引入主介面

def main():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()