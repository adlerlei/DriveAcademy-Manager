# 新增教練資料
import sqlite3
import os
from tkinter import messagebox


# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')


# 抓取郵局地址信息資料表
# def address_data():
#     conn = sqlite3.connect(database_path)
#     cursor = conn.cursor()

#     # 查詢郵遞區號 zip_code 資料表
#     cursor.execute("SELECT zip_code, city FROM address_data")
#     zip_code_data = cursor.fetchall()

#     # 關閉資料庫連接
#     conn.close()

#     address_zip_code_lists = []
#     address_city_lists = []
#     address_dict = {}

#     for r_address_zip_code in zip_code_data:
#         address_zip_code_lists.append(r_address_zip_code[0])
#         address_city_lists.append(r_address_zip_code[1])
#         address_dict[r_address_zip_code[0]] = r_address_zip_code[1]

#     return address_zip_code_lists, address_city_lists, address_dict


# 新增教練資料邏輯功能
def insert_instructor_data(instructor_data):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO instructor (
                number, name, birth_date, instructor_number
            ) VALUES (
                :number, :name, :birth_date, :instructor_number
            )
        ''', {
            'number': instructor_data.get('number', ''),
            'name': instructor_data.get('name', ''),
            'birth_date': instructor_data.get('birth_date', ''),
            'instructor_number': instructor_data.get('instructor_number', '')
        })

        conn.commit()
        messagebox.showinfo('成功', '已成功新增教練資料！')
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        messagebox.showerror('錯誤', f'新增教練資料時發生錯誤：{e}')
    finally:
        conn.close()


# 獲取資料庫教練資料信息
def get_instructor_data(identifier, value):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    query = f"SELECT * FROM instructor WHERE {identifier} = ?"
    cursor.execute(query, (value,))
    result = cursor.fetchone()
    
    conn.close()
    if result:
        # 确保返回所有字段，如果某些字段为 None，用空字符串替代
        return tuple('' if v is None else v for v in result)
    return None

# 更新教練資料資料庫
def update_instructor_data(data):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE instructor SET
            number = :number, -- 教練編號
            name = :name, -- 教練姓名
            birth_date = :birth_date, -- 出生日期
            instructor_number = :instructor_number -- 教練證號
        WHERE id = :id
    ''', data)

    conn.commit()
    conn.close()
    messagebox.showinfo('訊息', '已更新教練資料！')

# 刪除教練資料信息
def delete_instructor_data(instructor_number):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM instructor WHERE id = ?', (instructor_number,))

    conn.commit()
    conn.close()
    messagebox.showinfo('訊息', '已刪除教練資料！')