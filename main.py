from ui.main_window import main_window


def main():
    root = main_window()
    root.mainloop()
    
if __name__ == '__main__':
    main()
# import customtkinter as ctk

# def get_term_data():
#     # 模擬獲取期別數據
#     return ["第1期", "第2期", "第3期"]

# def register_number_data_changed(event):
#     print("事件觸發了")
#     value = register_term.get()
#     print(f"選擇的名冊期別: {value}")
#     register_number.delete(0, ctk.END)
#     register_number.insert(0, value)

# # 設置 CustomTkinter 外觀
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")

# # 創建主窗口
# app = ctk.CTk()
# app.title("測試 - 名冊期別和名冊號碼")
# app.geometry("400x200")

# # 名冊號碼
# ctk.CTkLabel(app, text="名冊號碼").pack(pady=(20, 5))
# register_number = ctk.CTkEntry(app)
# register_number.pack()

# # 名冊期別
# ctk.CTkLabel(app, text="名冊期別").pack(pady=(10, 5))
# term_data = get_term_data()
# register_term = ctk.CTkComboBox(app, values=term_data, command=register_number_data_changed)
# register_term.pack()
# # register_term.bind("<<ComboboxSelected>>", register_number_data_changed)

# # 測試按鈕
# def test_func():
#     print("測試按鈕被點擊")
#     value = "測試值"
#     register_number.delete(0, ctk.END)
#     register_number.insert(0, value)

# ctk.CTkButton(app, text="測試按鈕", command=test_func).pack(pady=20)

# app.mainloop()