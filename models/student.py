# 學員資料作業 功能邏輯介面
import sqlite3
import os
from tkinter import messagebox

# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 驗證學員資料輸入欄位
validation_fields = {
    'training_type_code': '訓練班別代碼',
    'training_type_name': '訓練班別名稱',
    'license_type_code': '考照類別代碼',
    'license_type_name': '考照類別名稱',
    'student_number': '學員編號',
    'batch': '梯次',
    'student_name': '學員姓名',
    'national_id_no': '身分證號碼',
    'birth_date': '出生日期',
    'r_address_zip_code': '戶籍地址郵遞區號',
    'r_address_city': '戶籍地址縣市',
    'r_address': '戶籍地址',
    'email': '電子郵件'
}


# 抓取郵局地址信息資料表
def address_data():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # 查詢郵遞區號 zip_code 資料表
    cursor.execute("SELECT zip_code, city FROM address_data")
    zip_code_data = cursor.fetchall()

    # 關閉資料庫連接
    conn.close()

    address_zip_code_lists = []
    address_city_lists = []
    address_dict = {}

    for r_address_zip_code in zip_code_data:
        address_zip_code_lists.append(r_address_zip_code[0])
        address_city_lists.append(r_address_zip_code[1])
        address_dict[r_address_zip_code[0]] = r_address_zip_code[1]

    return address_zip_code_lists, address_city_lists, address_dict


# 抓取教練資料表（編號，名稱）下拉選單監聽 
def get_instructor_data():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute("SELECT number, name FROM instructor")
    instructor_data = cursor.fetchall()

    conn.close()

    instructor_numbers = []
    instructor_names = []
    instructor_dict = {}

    for item in instructor_data:
        instructor_numbers.append(item[0])
        instructor_names.append(item[1])
        instructor_dict[item[0]] = item[1]

    return instructor_numbers, instructor_names, instructor_dict


# 用戶輸入寫入資料表中
def insert_student_data(data):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO student (
            training_type_code, training_type_name, license_type_code, license_type_name,
            student_number, batch, student_name, national_id_no, birth_date, mobile_phone,
            r_address_zip_code, r_address_city, r_address, home_phone, gender, education,
            instructor_number, instructor_name, email, remarks, m_address_zip_code,
            m_address_city, m_address
        ) VALUES (
            :training_type_code, :training_type_name, :license_type_code, :license_type_name,
            :student_number, :batch, :student_name, :national_id_no, :birth_date, :mobile_phone,
            :r_address_zip_code, :r_address_city, :r_address, :home_phone, :gender, :education,
            :instructor_number, :instructor_name, :email, :remarks, :m_address_zip_code,
            :m_address_city, :m_address
        )
    ''', data)

    conn.commit()
    conn.close()

    # 重置 is_editing 和 current_student_id
    global is_editing, current_student_id
    is_editing = False
    current_student_id = None

    messagebox.showinfo('訊息', '已新增學員資料！')


# 根據指定的條件查詢學員資料
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


# 更新學員資料
def update_student_data(data):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE student SET
            training_type_code = :training_type_code,
            training_type_name = :training_type_name,
            license_type_code = :license_type_code,
            license_type_name = :license_type_name,
            student_number = :student_number,
            batch = :batch,
            student_name = :student_name,
            national_id_no = :national_id_no,
            birth_date = :birth_date,
            mobile_phone = :mobile_phone,
            r_address_zip_code = :r_address_zip_code,
            r_address_city = :r_address_city,
            r_address = :r_address,
            home_phone = :home_phone,
            gender = :gender,
            education = :education,
            instructor_number = :instructor_number,
            instructor_name = :instructor_name,
            email = :email,
            remarks = :remarks,
            m_address_zip_code = :m_address_zip_code,
            m_address_city = :m_address_city,
            m_address = :m_address
        WHERE id = :id
    ''', data)

    conn.commit()
    conn.close()
    messagebox.showinfo('訊息', '已更新學員資料！')


# 刪除學員資料
def delete_student_data(student_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM student WHERE id = ?', (student_id,))

    conn.commit()
    conn.close()
    messagebox.showinfo('訊息', '已刪除學員資料！')