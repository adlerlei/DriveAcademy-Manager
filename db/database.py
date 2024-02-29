import sqlite3
from sqlite3 import Error


# 訓練班別 ( 1 自用小客車班 )
create_training = """
CREATE TABLE IF NOT EXISTS training_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 主鍵，自增
    code TEXT UNIQUE NOT NULL, -- 訓練班別代號
    training TEXT UNIQUE NOT NULL,  -- 訓練班別
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 記錄創建時間
)
"""

# 考照類別 ( 0 自用小客車 / 1 職業小客車 )
create_license = """
CREATE TABLE IF NOT EXISTS license_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 主鍵，自增
    code TEXT UNIQUE NOT NULL, -- 考照類別代號
    license TEXT UNIQUE NOT NULL,  -- 考照類別
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 記錄創建時間
)
"""

# 梯次 ( A , B )
create_class = """
CREATE TABLE IF NOT EXISTS class_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 主鍵，自增
    class TEXT UNIQUE NOT NULL,  -- 梯次
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 記錄創建時間
)
"""

# 來源 ( 新考，晉考，換考 .. 與開訓名冊關聯)
create_source = """
CREATE TABLE IF NOT EXISTS source_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 主鍵，自增
    code TEXT UNIQUE NOT NULL, -- 來源代號
    source TEXT UNIQUE NOT NULL,  -- 來源
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 記錄創建時間
)
"""

# 手自排
create_manual_automatic = """
CREATE TABLE IF NOT EXISTS manual_automatic_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 主鍵，自增
    code TEXT UNIQUE NOT NULL, -- 手自排代號
    manual_automatic TEXT UNIQUE NOT NULL,  -- 手自排
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 記錄創建時間
)
"""

# 退訓
create_dropout = """
CREATE TABLE IF NOT EXISTS dropout_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 主鍵，自增
    dropout TEXT UNIQUE NOT NULL, -- 退訓
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 記錄創建時間
)
"""

# 補考類別(筆試補考，道路補考，新生)
create_resit = """
CREATE TABLE IF NOT EXISTS resit_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 主鍵，自增
    code TEXT UNIQUE NOT NULL, -- 補考類別代號
    resit TEXT UNIQUE NOT NULL,  -- 補考類別
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 記錄創建時間
)
"""

# 期別 (開訓名冊/結訓會用上，輸入期別自動帶出)
create_term = """
CREATE TABLE IF NOT EXISTS term_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 主鍵，自增
    term TEXT UNIQUE NOT NULL, -- 期別
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 記錄創建時間
)
"""

# 學員資料表 - 欄位
create_student = """
CREATE TABLE IF NOT EXISTS student_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 主鍵，自動增長的整數型
    code TEXT UNIQUE NOT NULL,  -- 學員編號，唯一且不為空
    name TEXT NOT NULL,  -- 學員姓名，不為空
    id_number TEXT UNIQUE NOT NULL,  -- 身份證號，唯一且不為空
    date_birth TEXT NOT NULL,  -- 出生日期，不為空
    gender TEXT NOT NULL,  -- 性別，不為空
    local_phone TEXT,  -- 室內電話
    mobile_phone TEXT,  -- 手機號碼
    email TEXT UNIQUE NOT NULL,  -- 電子郵箱，唯一且不為空
    registered_address TEXT NOT NULL,  -- 戶籍地址，不為空
    mailing_address TEXT,  -- 通訊地址
    training INTEGER,  -- 訓練班別ID，外鍵關聯到training_info表
    instructor INTEGER,  -- 指導教練ID，外鍵關聯到instructor_Info表
    license INTEGER,  -- 考照類別ID，外鍵關聯到license_info表
    class INTEGER,  -- 梯次ID，外鍵關聯到class_info表
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- 記錄創建時間
    ---------------------- 外鍵定義部分
    -- 定義training欄位為外鍵，參照training_info表的id欄位
    FOREIGN KEY(training) REFERENCES training_info(id),
    -- 定義instructor欄位為外鍵，參照instructor_Info表的id欄位
    FOREIGN KEY(instructor) REFERENCES instructor_Info(id),
    -- 定義license欄位為外鍵，參照license_info表的id欄位
    FOREIGN KEY(license) REFERENCES license_info(id),
    -- 定義class欄位為外鍵，參照class_info表的id欄位
    FOREIGN KEY(class) REFERENCES class_info(id)
)
"""

# 教練資料表 - 欄位
create_instructor = """
CREATE TABLE IF NOT EXISTS instructor_Info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 主鍵，自增
    code TEXT UNIQUE NOT NULL, -- 教練編號
    name TEXT NOT NULL,  -- 教練姓名
    id_number TEXT UNIQUE NOT NULL,  -- 身份證號，唯一
    date_birth TEXT,  -- 出生日期
    gender TEXT,  -- 性別
    instructor_number TEXT,  -- 教練證號
    driving_license TEXT,  -- 駕照類別
    driving_number TEXT,  -- 駕照號碼
    local_phone TEXT,  -- 室內電話
    mobile_phone TEXT,  -- 手機號碼
    email TEXT,  -- 電子郵箱
    registered_address TEXT,  -- 戶籍地址
    mailing_address TEXT,  -- 通訊地址
    minimum_wage REAL,  -- 基本工資
    hire_date TEXT,  -- 雇用日期
    firing_date TEXT,  -- 辭職日期
    remarks TEXT,  -- 備註
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 記錄創建時間
)
"""

# 管理員資料表 - 欄位
create_admin = """
CREATE TABLE IF NOT EXISTS admin_Info (
    id INTEGER PRIMARY KEY,  -- 主鍵，唯一標識一個管理員
    username TEXT UNIQUE NOT NULL,  -- 管理員用戶名，唯一且不可為空
    password TEXT NOT NULL,  -- 管理員密碼，不可為空
    -- 以下欄位暫時不需要 -----------------------------
    -- phone_mobile TEXT,  -- 手機號碼
    -- name TEXT,  -- 管理員姓名
    -- email TEXT,  -- 電子郵箱
    -- mailing_address TEXT,  -- 通訊地址
    -----------------------------------------------------------------
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 記錄創建時間
)
"""

# 駕校資料表 - 欄位
create_school = """
CREATE TABLE IF NOT EXISTS school_Info (
    id INTEGER PRIMARY KEY,  -- 主鍵，唯一標識一個駕校
    name TEXT,  -- 駕校名稱
    -- abbreviation TEXT,  -- 駕校縮寫
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
        create_table(conn, create_training) # 訓練班別
        create_table(conn,create_license) # 考照類別
        create_table(conn, create_class) # 梯次
        create_table(conn, create_source) # 來源
        create_table(conn, create_manual_automatic) # 手自排
        create_table(conn, create_term) # 期別
        create_table(conn, create_dropout) # 退訓
        create_table(conn, create_resit) # 補考類別
        create_table(conn, create_student) # 學員資料
        create_table(conn, create_instructor) # 教練資料
        create_table(conn, create_admin) # 管理員資料
        create_table(conn, create_school) # 駕訓班資料
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
            cur.execute(sql, (username, password))
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
            # 先檢查用戶名是否存在
            sql_username = ''' SELECT * FROM adminInfo WHERE username=? '''
            cur = conn.cursor()
            cur.execute(sql_username, (username,))
            if not cur.fetchone():
                return "username_error"  # 用戶名不存在

            # 用戶名存在，檢查密碼是否正確
            sql_password = ''' SELECT * FROM adminInfo WHERE username=? AND password=? '''
            cur.execute(sql_password, (username, password))
            if not cur.fetchone():
                return "password_error"  # 密碼錯誤

            return "success"  # 用戶名和密碼都正確
    except Error as e:
        print(e)  # 或者將錯誤記錄到日誌中
        return "error"  # 發生錯誤
    finally:
        if conn:
            conn.close()

        
if __name__ == '__main__':
    main()