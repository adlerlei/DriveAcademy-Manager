# 學照日期送件，登錄
import sqlite3
import os
from tkinter import messagebox
import customtkinter as ctk


# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 學照登陸更新學員資料庫函式
def license_update_student_data(learner_permit_login_data, learner_permit_date, learner_permit_number):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    update_sql = """
    UPDATE student SET 
        learner_permit_login_data = ?, learner_permit_date = ?, learner_permit_number = ?
    WHERE id = ?
    """

    c.execute(update_sql, (learner_permit_login_data, learner_permit_date, learner_permit_number))
    conn.commit()
    conn.close()
    messagebox.showinfo('訊息', '學照日期登錄完成！')


# 學員資料庫搜尋函式
def search_student_info(student_number_value):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT student_number, student_name, national_id_no, mobile_phone, birth_date, license_type_code, license_type_name, remarks, r_address_zip_code, r_address_city, r_address 
        FROM student WHERE student_number = ?
    """, (student_number_value,))
    student = cursor.fetchone()
    conn.close()
    
    # 調試訊息
    print(f"查詢學員編號: {student_number_value}")
    print(f"查詢結果: {student}")
    
    if student:
        student_number.configure(state='normal')
        student_number.delete(0, ctk.END)
        student_number.insert(0, student[5])
        student_number.configure(state='readonly')

        student_name.configure(state='normal')
        student_name.delete(0, ctk.END)
        student_name.insert(0, student[1])
        student_name.configure(state='readonly')

        national_id_no.configure(state='normal')
        national_id_no.delete(0, ctk.END)
        national_id_no.insert(0, student[2])
        national_id_no.configure(state='readonly')

        birth_date.configure(state='normal')
        birth_date.delete(0, ctk.END)
        birth_date.insert(0, student[3])
        birth_date.configure(state='readonly')

        mobile_phone.configure(state='normal')
        mobile_phone.delete(0, ctk.END)
        mobile_phone.insert(0, student[4])
        mobile_phone.configure(state='readonly')

        # license_type_code.configure(state='normal')
        # license_type_code.delete(0, ctk.END)
        # license_type_code.insert(0, student[5])
        # license_type_code.configure(state='readonly')

        license_type_name.configure(state='normal')
        license_type_name.delete(0, ctk.END)
        license_type_name.insert(0, student[2])
        license_type_name.configure(state='readonly')

        remarks.configure(state='normal')
        remarks.delete(0, ctk.END)
        remarks.insert(0, student[7])
        remarks.configure(state='readonly')

        r_address_zip_code.configure(state='normal')
        r_address_zip_code.delete(0, ctk.END)
        r_address_zip_code.insert(0, student[8])
        r_address_zip_code.configure(state='readonly')

        r_address_city.configure(state='normal')
        r_address_city.delete(0, ctk.END)
        r_address_city.insert(0, student[9])
        r_address_city.configure(state='readonly')

        r_address.configure(state='normal')
        r_address.delete(0, ctk.END)
        r_address.insert(0, student[10])
        r_address.configure(state='readonly')
    else:
        messagebox.showinfo('訊息', '查找不到學員！')




def load_data_into_treeview(treeview):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    for row in rows:
        treeview.insert("", "end", values=row)
    conn.close()