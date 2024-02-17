import sqlite3

# 連接到SQLite資料庫，如果文件不存在，會自動在當前目錄創建
conn = sqlite3.connect('school_management.db')

# 創建一個Cursor物件
cur = conn.cursor()

### 創建項目所需要的所有資料表 ###
# 創建學員資料表
cur.execute('''
CREATE TABLE IF NOT EXISTS student (
    student_id INTEGER PRIMARY KEY, -- 學員編號，主鍵，整數型
    training_class TEXT, -- 訓練班別，文字型
    batch TEXT, -- 梯次，文字型
    name TEXT, -- 姓名，文字型
    id_number TEXT, -- 身分證號，文字型
    birth_date TEXT, -- 出生日期，文字型
    phone_home TEXT, -- 市內電話，文字型
    phone_mobile TEXT, -- 手機，文字型
    email TEXT, -- 信箱，文字型
    address_residence TEXT, -- 戶籍地址，文字型
    address_mailing TEXT, -- 通訊地址，文字型
    gender TEXT, -- 性別，文字型
    instructor_id INTEGER, -- 指導教練編號，整數型，外鍵
    created_at TEXT, -- 建檔日期，文字型
    FOREIGN KEY (instructor_id) REFERENCES instructor (instructor_id) -- 與教練資料表的外鍵關聯
)
''')

# 創建教練資料表
cur.execute('''
CREATE TABLE IF NOT EXISTS instructor (
    instructor_id INTEGER PRIMARY KEY, -- 教練編號，主鍵，整數型
    name TEXT, -- 姓名，文字型
    birth_date TEXT, -- 出生日期，文字型
    certification_number TEXT, -- 教練證號碼，文字型
    id_number TEXT, -- 身分證號，文字型
    gender TEXT, -- 性別，文字型
    license_type TEXT, -- 駕照類別，文字型
    license_number TEXT, -- 駕照號碼，文字型
    remarks TEXT, -- 備註，文字型
    address_residence TEXT, -- 戶籍地址，文字型
    address_mailing TEXT, -- 通訊地址，文字型
    phone_mobile TEXT, -- 手機，文字型
    phone_home TEXT, -- 室內電話，文字型
    employment_date TEXT, -- 到職日，文字型
    resignation_date TEXT, -- 離職日，文字型
    base_salary REAL, -- 底薪，實數型
    created_at TEXT -- 建檔日期，文字型
)
''')

# 創建管理員資料表
cur.execute('''
CREATE TABLE IF NOT EXISTS admin (
    admin_id INTEGER PRIMARY KEY, -- 管理員編號，主鍵，整數型
    username TEXT UNIQUE NOT NULL, -- 使用者名稱，唯一且不可為空，文字型
    password TEXT NOT NULL, -- 密碼，不可為空，文字型
    phone_mobile TEXT, -- 手機，文字型
    name TEXT, -- 姓名，文字型
    email TEXT, -- 信箱，文字型
    created_at TEXT -- 建檔日期，文字型
)
''')

# 創建名冊資料表
cur.execute('''
CREATE TABLE IF NOT EXISTS roster (
    roster_id INTEGER PRIMARY KEY, -- 名冊編號，主鍵，整數型
    source TEXT, -- 來源，文字行
    transmission_type TEXT, -- 手自排，文字行
    withdraw BOOLEAN, -- 退訓，布林值
    test_type TEXT, -- 筆試路試，文字行
    created_at TEXT -- 建檔日期，文字型
)
''')

# 創建駕訓班學校資料表
cur.execute('''
CREATE TABLE IF NOT EXISTS driving_school (
    school_id INTEGER PRIMARY KEY, -- 駕訓班編號，主鍵，整數型
    name TEXT, -- 駕訓班名稱，文字型
    abbreviation TEXT, -- 駕訓班簡稱，文字型
    supervisor_station_code TEXT, -- 監理站代碼，文字型
    principal TEXT, -- 班主任，文字型
    phone TEXT, -- 電話，文字型
    fax TEXT, -- 傳真，文字型
    address TEXT, -- 地址，文字型
    created_at TEXT -- 建檔日期，文字型
)
''')

# 創建考照類別表
cur.execute('''
CREATE TABLE IF NOT EXISTS license_category (
    category_id INTEGER PRIMARY KEY, -- 類別編號，主鍵，整數型
    description TEXT -- 描述，文字型
)
''')

### 資料表創建完成 ###

# 提交操作
conn.commit()

# 關閉連線
conn.close()

print('資料表建立完成！')