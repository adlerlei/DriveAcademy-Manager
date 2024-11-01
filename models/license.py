# 學照日期送件，登錄 功能邏輯介面
# 對應計面 ui/learner_license_date_registration.py , learner_license_submission.py
import sqlite3
import os
from tkinter import messagebox
from tkinter import filedialog
import re


# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 驗證學員資料輸入欄位
validation_fields = {
    'learner_permit_login_data': '登錄日期',
    'learner_permit_date': '學照日期',
    'learner_permit_number': '學照號碼',
    'submission_date': '送件日期'
}


# 更新 學照登錄 學員資料庫
def update_student_data(data, uid):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    if uid == 1:
        cursor.execute('''
            UPDATE student SET
                learner_permit_login_data = :learner_permit_login_data,
                learner_permit_date = :learner_permit_date,
                learner_permit_number = :learner_permit_number
            WHERE id = :id
        ''', data)
        
        # messagebox.showinfo('訊息', '學照登錄完成！')
    elif uid == 0:
        cursor.execute('''
            UPDATE student SET
                submission_date = :submission_date
            WHERE id = :id
        ''', data)
        # messagebox.showinfo('訊息', '學照送件完成！')

    conn.commit()
    conn.close()


# 根据指定的条件查询学员资料
def get_student_data(identifier, value):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    if identifier in ['student_number', 'student_name', 'national_id_no', 'mobile_phone']:
        query = f"SELECT * FROM student WHERE {identifier} LIKE ?"
        cursor.execute(query, (f"%{value}%",))
    else:
        query = f"SELECT * FROM student WHERE {identifier} = ?"
        cursor.execute(query, (value,))
    
    result = cursor.fetchone()
    
    conn.close()

    return result 


# 創建 TXT 自動生成文件名稱
def generate_csv_filename(submission_date):
    # 根據你的固定格式生成文件名稱
    return f"400032{submission_date}.txt"

# 匯出 txt 文件按鈕觸發.
def export_selected_data(treeview, submission_date_entry):
    # print("submission_date_entry:", submission_date_entry)
    file_date_name = submission_date_entry.get()
    # print("file_date_name:", file_date_name)
    # 獲取所選行
    # selected_items = treeview.selection()
    selected_items = treeview.get_children() # 直接取得所有行
    if not selected_items:
        messagebox.showwarning("警告", "請先選擇要匯出的行!")
        return

    # 獲取所選行的數據
    data = []
    for item in selected_items:
        item_values = treeview.item(item)["values"]
        # 將數據轉換為字符串
        national_id_no = str(item_values[0])
        birth_date = str(item_values[1])
        student_name = str(item_values[2])
        r_address_zip_code = str(item_values[3])
        r_address = str(item_values[5])
        mobile_phone = str(item_values[6])
        email = str(item_values[7])

        # 去除字串 ( / , - , 空格 ) 符號
        national_id_no = re.sub(r'/','',national_id_no)
        birth_date = re.sub(r'/','',birth_date)
        student_name = re.sub(r'/','',student_name)
        r_address_zip_code = re.sub(r'/','',r_address_zip_code)
        r_address = re.sub(r'/','',r_address)
        # mobile_phone = re.sub(r'/','',mobile_phone)
        email = re.sub(r'/','',email)

        # 確保手機號碼保留前導0
        if mobile_phone and mobile_phone[0] != '0':
            mobile_phone = '0' + mobile_phone.lstrip('0')  # 如果沒有前導 0，則補上

        data.append(f"{national_id_no},{birth_date},{student_name},{r_address_zip_code},{r_address},{mobile_phone},{email}")

    file_date_name = submission_date_entry.get()

    # 生成文件名稱
    file_name = generate_csv_filename(file_date_name)

    # 創建文件保存對話框
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile = file_name)
    if file_path:
        try:
            # 將數據寫入文件
            with open(file_path, "w", newline='', encoding="utf-8") as f:
                f.write("\n".join(data))
            messagebox.showinfo("成功", "匯出文件成功!")
        except Exception as e:
            messagebox.showerror("錯誤", f"匯出文件失敗: {str(e)}")