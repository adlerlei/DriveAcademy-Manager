# 新增教練資料
import sqlite3
import os
from tkinter import messagebox


# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')


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


# 新增教練資料邏輯功能
def insert_instructor_data(data):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO instructor (
            number, name, national_id_no, birth_date, home_phone, mobile_phone,
            email, r_address_zip_code, r_address_city, r_address,
            m_address_zip_code, m_address_city, m_address,
            instructor_license_number, driving_license_category,
            driving_license_number, base_salary, start_date, end_date, remarks
        ) VALUES (
            :number, :name, :national_id_no, :birth_date, :home_phone, :mobile_phone,
            :email, :r_address_zip_code, :r_address_city, :r_address,
            :m_address_zip_code, :m_address_city, :m_address,
            :instructor_license_number, :driving_license_category,
            :driving_license_number, :base_salary, :start_date, :end_date, :remarks
        )
    ''', data)
    
    conn.commit()
    conn.close()
    messagebox.showinfo('訊息', '已新增教練資料！')

# 獲取資料庫教練資料信息
def get_instructor_data(identifier, value):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    query = f"SELECT * FROM instructor WHERE {identifier} = ?"
    cursor.execute(query, (value,))
    result = cursor.fetchone()
    
    conn.close()
    return result

# 更新教練資料資料庫
def update_instructor_data(data):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE instructor SET
            name = :name, national_id_no = :national_id_no, birth_date = :birth_date,
            home_phone = :home_phone, mobile_phone = :mobile_phone, email = :email,
            r_address_zip_code = :r_address_zip_code, r_address_city = :r_address_city,
            r_address = :r_address, m_address_zip_code = :m_address_zip_code,
            m_address_city = :m_address_city, m_address = :m_address,
            instructor_license_number = :instructor_license_number,
            driving_license_category = :driving_license_category,
            driving_license_number = :driving_license_number, base_salary = :base_salary,
            start_date = :start_date, end_date = :end_date, remarks = :remarks
        WHERE number = :number
    ''', data)

    conn.commit()
    conn.close()
    messagebox.showinfo('訊息', '已更新教練資料！')

# 刪除教練資料信息
def delete_instructor_data(instructor_number):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM instructor WHERE number = ?', (instructor_number,))

    conn.commit()
    conn.close()
    messagebox.showinfo('訊息', '已刪除教練資料！')