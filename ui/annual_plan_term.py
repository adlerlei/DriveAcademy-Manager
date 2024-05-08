# 期別新增 - 年度計畫表與期別新增
from utils.widget import *
from utils.config import *
from tkinter import messagebox
import customtkinter as ctk
from models.annual_plan import insert_annual_plan_data, fetch_and_populate_treeview, delete_btn_click, export_selected_data
# from models.annual_plan import update_record_in_db
# selected_record_id = None

def annual_plan_term(content):
    clear_frame(content)
    
    annual_plan_term = frame(content)
    annual_plan_term.columnconfigure(0, weight=1)
    annual_plan_term.columnconfigure(1, weight=1)
    annual_plan_term.columnconfigure(2, weight=1)
    annual_plan_term.columnconfigure(3, weight=1)
    annual_plan_term.place(relwidth=1, relheight=1)

    # 監聽 term 輸入值，並且再次設定 term_class_code 值
    def on_value_changed(event):
        value = '10' + term.get() # 前面 + 10 字串
        term_class_code.delete(0, 'end')
        term_class_code.insert(0, value)

    # 處理訓練班別第一個下拉選單training_type_code的選擇變化
    def on_combobox_changed(event): 
        # 獲取第一個下拉選單的當前選擇
        selected_code = training_type_code.get()
        # 根據選擇更新第二個下拉選單的值
        match selected_code:
            case '1':
                training_type_name.set('普通小型車班')
            case '2':
                training_type_name.set('大貨車班')
            case '3':
                training_type_name.set('大客車班')
            case '4':
                training_type_name.set('聯結車班')
            case '5':
                training_type_name.set('職業小型車班')
            case '6':
                training_type_name.set('普通重機車班')
            case '7':
                training_type_name.set('大型重機車班')
            case '8':
                training_type_name.set('小型車逕升大客車班')

    # 訓練班別
    label(annual_plan_term, text='訓練班別').grid(row=0, column=0, sticky='ws', padx=(10,0), pady=(10,0))
    training_type_code = combobox(annual_plan_term, values=['1','2','3','4','5','6','7','8'], command=on_combobox_changed)
    training_type_code.grid(row=1, column=0, sticky='wen', padx=(10,0))
    training_type_name = combobox(annual_plan_term, values=['普通小型車班','大貨車班','大客車班','聯結車班','職業小型車班','普通重機車班','大型重機車班','小型車逕升大客車班'])
    training_type_name.grid(row=1, column=1, sticky='wen', padx=10)

    # 綁定函數到第一個下拉選單的選擇變化事件
    training_type_code.bind("<<ComboboxSelected>>", on_combobox_changed)


    # 年度
    label(annual_plan_term, text='年度').grid(row=2, column=0, sticky='ws',padx=(10,0), pady=(20,0))
    year = entry(annual_plan_term)
    year.grid(row=3, column=0, columnspan=2, sticky='wen', padx=10)
    
    # 期別
    label(annual_plan_term, text='期別').grid(row=4, column=0, sticky='ws',padx=(10,0), pady=(20,0))
    term = entry(annual_plan_term)
    term.grid(row=5, column=0, columnspan=2, sticky='wen', padx=10)
    
    # 梯次（抓取資料庫呈現）
    label(annual_plan_term, text='梯次').grid(row=0, column=2, sticky='ws', padx=(10,0))
    batch = combobox(annual_plan_term, values=['A', 'B'])
    batch.grid(row=1, column=2, sticky='wen', padx=10)

    # 上課期別代碼
    label(annual_plan_term, text='上課期別代碼').grid(row=0, column=3, sticky='ws', padx=(10,0))
    term_class_code = entry(annual_plan_term)
    term_class_code.grid(row=1, column=3, sticky='wen', padx=(0,10))

    # 監聽 term 輸入值，並且再次設定 term_class_code 值
    term.bind("<KeyRelease>", on_value_changed)
    
    # 開訓日期
    label(annual_plan_term, text='開訓日期').grid(row=2, column=2, sticky='ws',padx=(10,0), pady=(20,0))
    start_date = entry(annual_plan_term)
    start_date.grid(row=3, column=2, columnspan=2, sticky='wen', padx=10)
    
    # 結訓日期
    label(annual_plan_term, text='結訓日期').grid(row=4, column=2, sticky='ws',padx=(10,0), pady=(20,0))
    end_date = entry(annual_plan_term)
    end_date.grid(row=5, column=2, columnspan=2, sticky='wen', padx=10)

    # 新增按鈕觸發
    def add_btn_click():
        year_value = year.get()
        term_value = term.get()
        term_class_code_value = term_class_code.get()
        batch_value = batch.get()
        training_type_code_value = training_type_code.get()
        training_type_name_value = training_type_name.get()
        start_date_value = start_date.get()
        end_date_value = end_date.get()

        # 驗證輸入欄位
        if not all([year_value, term_value, term_class_code_value, batch_value, training_type_code_value, training_type_name_value, start_date_value, end_date_value]):
            messagebox.showerror('錯誤', '所有欄位不可為空')
            return

        # 新增資料到資料庫
        else:
            insert_annual_plan_data(year_value, term_value, term_class_code_value, batch_value, training_type_code_value, training_type_name_value, start_date_value, end_date_value)
            # 新增成功後，清空輸入欄位
            year.delete(0, ctk.END)
            term.delete(0, ctk.END)
            term_class_code.delete(0, ctk.END)
            batch.set('')
            start_date.delete(0, ctk.END)
            end_date.delete(0, ctk.END)

            # 即時更新 Treeview
            fetch_and_populate_treeview(data_list)

    
    # 當選中 Treeview 中的一行時,將數據填充到輸入欄位中
    # def on_treeview_select(event):
    #     selected_item = data_list.selection()
    #     global selected_record_id
    #     if selected_item:
    #         item_values = data_list.item(selected_item)["values"]
    #         training_type_name.set(item_values[0])
    #         year.delete(0, tk.END)
    #         year.insert(0, item_values[1])
    #         term.delete(0, tk.END)
    #         term.insert(0, item_values[2])
    #         start_date.delete(0, tk.END)
    #         start_date.insert(0, item_values[3])
    #         end_date.delete(0, tk.END)
    #         end_date.insert(0, item_values[4])
    #         term_class_code.delete(0, tk.END)
    #         term_class_code.insert(0, item_values[5])
    #         selected_record_id = data_list.item(selected_item)["text"]

    # 修改按鈕觸發
    # def modify_btn_click():
    #     # 獲取選中行
    #     selected_item = data_list.selection()
    #     if not selected_item:
    #         messagebox.showwarning("警告", "請先選擇要修改的行!")
    #         return

        # 獲取新的數據
        # new_training_type_name = training_type_name.get()
        # new_year = year.get()
        # new_term = term.get()
        # new_start_date = start_date.get()
        # new_end_date = end_date.get()
        # new_term_class_code = term_class_code.get()
        # new_batch = batch.get()
        # new_training_type_code = training_type_code.get()

        # 更新資料庫
        # update_record_in_db(selected_record_id, new_training_type_name, new_year, new_term, new_start_date, new_end_date, new_term_class_code, new_batch, new_training_type_code)

        # 刷新 Treeview
        # fetch_and_populate_treeview(data_list)
        

    # # 匯出文件按鈕觸發
    # def export_selected_data(treeview):
    #     # 获取选中的行
    #     selected_items = treeview.selection()
    #     if not selected_items:
    #         messagebox.showwarning("警告", "請先選擇要匯出的資料列表!")
    #         return

    #     # 获取选中行的数据
    #     data = []
    #     for item in selected_items:
    #         item_values = treeview.item(item)["values"]
    #         data.append(item_values)

    #     # 创建一个文件对话框,让用户选择保存路径
    #     file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    #     if file_path:
    #         try:
    #             # 写入数据到文件
    #             with open(file_path, "w", encoding="utf-8") as f:
    #                 for row in data:
    #                     f.write("\t".join(str(value) for value in row) + "\n")
    #             messagebox.showinfo("成功", "匯出文件成功!")
    #         except Exception as e:
    #             messagebox.showerror("錯誤", f"匯出文件失敗: {str(e)}")

    
    # 新增，刪除，匯出文件 按鈕
    btn(annual_plan_term, text='新增', command=add_btn_click).grid(row=6, column=0, columnspan=2, sticky='wen', padx=10, pady=20)
    # btn(annual_plan_term, text='修改', command=modify_btn_click).grid(row=6, column=2, sticky='wen', padx=10, pady=20)
    delete_btn(annual_plan_term, text='刪除', command=lambda: delete_btn_click(data_list)).grid(row=6, column=2, sticky='wen', padx=10, pady=20)
    export_btn(annual_plan_term, text='匯出文件', command=lambda: export_selected_data(data_list)).grid(row=6, column=3, sticky='wen', padx=10, pady=20)
    
    # 列表框 - 期別新增 - 年度計畫表與期別新增
    data_list = ttk.Treeview(annual_plan_term, show='headings', 
                             columns=('訓練班別名稱', '年度', '期別編號', '開訓日期', '結訓日期', '上課期別代碼'), height=25)
    
    data_list.column("訓練班別名稱", width=150, anchor='w')
    data_list.column("年度", width=50, anchor='w')
    data_list.column("期別編號", width=50, anchor='w')
    data_list.column("開訓日期", width=50, anchor='w')
    data_list.column("結訓日期", width=50, anchor='w')
    data_list.column("上課期別代碼", width=50, anchor='w')
    

    data_list.heading("訓練班別名稱", text="訓練班別名稱")
    data_list.heading("年度", text="年度")
    data_list.heading("期別編號", text="期別編號")
    data_list.heading("開訓日期", text="開訓日期")
    data_list.heading("結訓日期", text="結訓日期")
    data_list.heading("上課期別代碼", text="上課期別代碼")
    
    data_list.grid(row=8, column=0, columnspan=4, sticky='wens', padx=10)

    # 綁定 Treeview 的選擇事件
    # data_list.bind("<<TreeviewSelect>>", on_treeview_select)
    
    # 調用函數填充 Treeview（進入介面時會直接抓取資料庫呈現資料列表）
    fetch_and_populate_treeview(data_list)