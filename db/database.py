import sqlite3
from sqlite3 import Error
from tkinter import messagebox


# 創建資料庫信息表的SQL語句
create_student_info_sql = """
CREATE TABLE IF NOT EXISTS student_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    identity_number TEXT UNIQUE,
    birth_date TEXT,
    gender TEXT,
    landline TEXT,
    mobile TEXT,
    email TEXT,
    residence_address TEXT,
    mailing_address TEXT,
    instructor_id INTEGER,
    training_type TEXT,
    license_type TEXT,
    batch INTEGER,
    source TEXT,
    transmission_type TEXT,
    dropout TEXT,
    retest_type TEXT,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (instructor_id) REFERENCES instructorInfo(id)
)
"""

create_instructor_info_sql = """
CREATE TABLE IF NOT EXISTS instructorInfo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    identity_number TEXT UNIQUE,
    birth_date TEXT,
    gender TEXT,
    instructor_license_number TEXT,
    license_category TEXT,
    license_number TEXT,
    landline TEXT,
    mobile TEXT,
    email TEXT,
    residence_address TEXT,
    mailing_address TEXT,
    base_salary REAL,
    employment_date TEXT,
    resignation_date TEXT,
    remarks TEXT,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

create_admin_info_sql = """
CREATE TABLE IF NOT EXISTS adminInfo (
    id INTEGER PRIMARY KEY,
    name TEXT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    phone_mobile TEXT,
    email TEXT,
    mailing_address TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

create_driving_school_info_sql = """
CREATE TABLE IF NOT EXISTS drivingSchoolInfo (
    id INTEGER PRIMARY KEY,
    name TEXT,
    abbreviation TEXT,
    supervisor_station_code TEXT,
    principal TEXT,
    phone TEXT,
    fax TEXT,
    address TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

# 實現一個函數來創建數據庫連接
def create_connection(db_file):
    ''''創建一個資料庫連接到SQLite3資料庫指定的db文件'''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('資料庫連線成功！')
    except Error as e:
        print(e)
    return conn

# 創建一個函數來初始化數據庫
def create_table(conn, create_table_sql):
    '''創建數據庫表格'''
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
# 創建數據庫表格的SQL語句
def main():
    database = 'db/school_database.db'
    
    # 創建學員信息表
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, create_student_info_sql)
        create_table(conn, create_instructor_info_sql)
        create_table(conn, create_admin_info_sql)
        create_table(conn, create_driving_school_info_sql)
        conn.close()
    else:
        print('資料庫連線失敗！')
        

# 管理員註冊資料寫入邏輯與 ui / register_window.py 連接
def register_admin(name, username, password, phone_mobile, email, mailing_address):
    database = 'db/school_database.db'
    try:
        conn = create_connection(database)
        if conn is not None:
            sql = ''' INSERT INTO adminInfo(name,username,password,phone_mobile,email,mailing_address) VALUES(?,?,?,?,?,?) '''
            cur = conn.cursor()
            cur.execute(sql, (name, username, password, phone_mobile, email, mailing_address))
            conn.commit()
            return True  # 返回True表示注册成功
    except Error as e:
        return str(e)  # 返回错误信息
    finally:
        if conn:
            conn.close()


        

def validate_admin_login(username, password):
    database = 'db/school_database.db'
    try:
        conn = create_connection(database)
        if conn is not None:
            sql = ''' SELECT * FROM adminInfo WHERE username=? AND password=? '''
            cur = conn.cursor()
            cur.execute(sql, (username, password))
            account = cur.fetchone()
            if account:
                return True  # 返回True表示登录成功
            else:
                return False  # 返回False表示登录失败
    except Error as e:
        return str(e)  # 返回错误信息
    finally:
        if conn:
            conn.close()
        
if __name__ == '__main__':
    main()