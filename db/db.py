import tkinter as tk
from tkinter import ttk
import sqlite3

conn = sqlite3.connect('db/xxx.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               email TEXT NOT NULL)''')
conn.commit()

# 创建主窗口
root = tk.Tk()
root.title("用户输入")

# 添加输入字段
name_label = ttk.Label(root, text="姓名:")
name_label.pack()
name_entry = ttk.Entry(root)
name_entry.pack()

email_label = ttk.Label(root, text="电邮:")
email_label.pack()
email_entry = ttk.Entry(root)
email_entry.pack()

def save_data():
    name = name_entry.get()
    email = email_entry.get()
    
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    
    conn.commit()
    
# 添加按钮并绑定函数
submit_button = ttk.Button(root, text="提交", command=save_data)
submit_button.pack()

root.mainloop()