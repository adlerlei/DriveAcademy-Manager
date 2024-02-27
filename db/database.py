import sqlite3
from sqlite3 import Error


# 創建資料庫表以及資料庫欄位的SQL語句
# 學員資料表 - 欄位
create_student_info_sql = """
CREATE TABLE IF NOT EXISTS student_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 主鍵，自增
    -- instructor_id INTEGER,  -- 指導教練ID
    student_number TEXT, -- 學員編號
    name TEXT,  -- 學員姓名
    identity_number TEXT UNIQUE,  -- 身份證號，唯一
    birth_date TEXT,  -- 出生日期
    gender TEXT,  -- 性別
    landline TEXT,  -- 室內電話
    mobile TEXT,  -- 手機號碼
    email TEXT,  -- 電子郵箱
    residence_address TEXT,  -- 戶籍地址
    mailing_address TEXT,  -- 通訊地址
    instructor TEXT,  -- 指導教練
    training_type TEXT,  -- 訓練班別
    license_type TEXT,  -- 考照類別
    batch TEXT,  -- 期別
    class TEXT,  -- 梯次
    source TEXT,  -- 來源
    transmission_type TEXT,  -- 手自排
    dropout TEXT,  -- 退訓
    retest_type TEXT,  -- 補考類別
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 記錄創建時間
    -- FOREIGN KEY (instructor_id) REFERENCES instructorInfo(id)
)
"""

# 教練資料表 - 欄位
create_instructor_info_sql = """
CREATE TABLE IF NOT EXISTS instructorInfo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 主鍵，自增
    instructor_number TEXT, -- 教練編號
    name TEXT,  -- 教練姓名
    identity_number TEXT UNIQUE,  -- 身份證號，唯一
    birth_date TEXT,  -- 出生日期
    gender TEXT,  -- 性別
    instructor_license_number TEXT,  -- 教練證號
    license_category TEXT,  -- 駕照類別
    license_number TEXT,  -- 駕照號碼
    landline TEXT,  -- 室內電話
    mobile TEXT,  -- 手機號碼
    email TEXT,  -- 電子郵箱
    residence_address TEXT,  -- 戶籍地址
    mailing_address TEXT,  -- 通訊地址
    base_salary REAL,  -- 基本工資
    employment_date TEXT,  -- 雇用日期
    resignation_date TEXT,  -- 辭職日期
    remarks TEXT,  -- 備註
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 記錄創建時間
)
"""

# 管理員資料表 - 欄位
create_admin_info_sql = """
CREATE TABLE IF NOT EXISTS adminInfo (
    id INTEGER PRIMARY KEY,  -- 主鍵，唯一標識一個管理員
    username TEXT UNIQUE NOT NULL,  -- 管理員用戶名，唯一且不可為空
    password TEXT NOT NULL,  -- 管理員密碼，不可為空
    phone_mobile TEXT,  -- 手機號碼
    -- 以下欄位暫時不需要 -----------------------------
    -- name TEXT,  -- 管理員姓名
    -- email TEXT,  -- 電子郵箱
    -- mailing_address TEXT,  -- 通訊地址
    -----------------------------------------------------------------
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 記錄創建時間
)
"""

# 駕校資料表 - 欄位
create_driving_school_info_sql = """
CREATE TABLE IF NOT EXISTS drivingSchoolInfo (
    id INTEGER PRIMARY KEY,  -- 主鍵，唯一標識一個駕校
    name TEXT,  -- 駕校名稱
    abbreviation TEXT,  -- 駕校縮寫
    supervisor_station_code TEXT,  -- 監理站代號
    principal TEXT,  -- 駕訓班主任
    phone TEXT,  -- 駕校電話
    fax TEXT,  -- 駕校傳真
    address TEXT,  -- 駕校地址
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 記錄創建時間
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
    
    # 創建資料庫表及欄位信息
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
# def register_admin(name, username, password, phone_mobile, email, mailing_address):
def register_admin(username, password):
    database = 'db/school_database.db'
    try:
        conn = create_connection(database)
        if conn is not None:
            # sql = ''' INSERT INTO adminInfo(name,username,password,phone_mobile,email,mailing_address) VALUES(?,?,?,?,?,?) '''
            sql = ''' INSERT INTO adminInfo(username,password) VALUES(?,?) '''
            cur = conn.cursor()
            # cur.execute(sql, (name, username, password, phone_mobile, email, mailing_address))
            cur.execute(sql, (username, password, phone_mobile, email, mailing_address))
            conn.commit()
            return True  # 返回True表示注册成功
    except Error as e:
        return str(e)  # 返回错误信息
    finally:
        if conn:
            conn.close()


        
# 管理員登入資料寫入邏輯與 ui / login_window.py 連接
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