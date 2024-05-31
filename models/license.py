# 學照日期送件，登錄
import sqlite3
import os
from tkinter import messagebox


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
        
        messagebox.showinfo('訊息', '學照登錄完成！')
    elif uid == 0:
        cursor.execute('''
            UPDATE student SET
                submission_date = :submission_date
            WHERE id = :id
        ''', data)
        messagebox.showinfo('訊息', '學照送件完成！')

    conn.commit()
    conn.close()


# 搜尋學員資料庫
# 根據指定的條件查詢學員資料
def get_student_data(identifier, value):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    query = f"SELECT * FROM student WHERE {identifier} = ?"
    cursor.execute(query, (value,))
    result = cursor.fetchone()
    
    conn.close()

    return result