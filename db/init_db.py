import sqlite3

# 連接到SQLite資料庫，如果文件不存在，會自動在當前目錄創建
conn = sqlite3.connect('school_management.db')

# 創建一個Cursor物件
cur = conn.cursor()

# 使用變數儲存資料表名稱
db_studentInfo = 'student_info' # 學員資料表
db_instructorInfo = 'instructorInfo' # 教練資料表
db_adminInfo = 'adminInfo' # 管理員資料表
db_drivingSchoolInfo = 'drivingSchoolInfo' # 駕訓班學校資料表

# 刪除已存在的學員資料表
# cur.execute('DROP TABLE IF EXISTS student;')
# cur.execute('DROP TABLE IF EXISTS license_category;')
# cur.execute('DROP TABLE IF EXISTS driving_school;')
# cur.execute('DROP TABLE IF EXISTS admin;')
# cur.execute('DROP TABLE IF EXISTS instructor;')
# cur.execute('DROP TABLE IF EXISTS roster;')

### 創建項目所需要的所有資料表 ###
# 學員資料表
cur.execute(f'''
CREATE TABLE IF NOT EXISTS {db_studentInfo} (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- 主鍵，自動遞增
    name TEXT,                                   -- 學員姓名
    identity_number TEXT UNIQUE,    -- 身分證字號，唯一
    birth_date TEXT,                           -- 出生日期
    gender TEXT,                                -- 性別
    landline TEXT,                               -- 室內電話
    mobile TEXT,                                 -- 手機
    email TEXT,                                   -- 信箱
    residence_address TEXT,               -- 戶籍地址
    mailing_address TEXT,                  -- 通訊地址
    instructor_id INTEGER,                   -- 指導教練ID外鍵
    --  以下為監理站信息添加到學員資料表中
    training_type TEXT,               -- 訓練班別
    license_type TEXT,                 -- 考照類別
    batch INTEGER,                     -- 梯次
    source TEXT,                          -- 來源
    transmission_type TEXT,        -- 手自排
    dropout TEXT,                        -- 退訓
    retest_type TEXT,                   -- 補考類別
    -- 監理站信息結束
    creation_date TEXT,                       -- 建檔日期
    FOREIGN KEY (id) REFERENCES {db_instructorInfo}(id) -- 外鍵約束指向教練資料表的教練ID
)
''')

# 教練資料表
cur.execute(f'''
CREATE TABLE IF NOT EXISTS {db_instructorInfo} (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- 主鍵，自動遞增
    name TEXT,                                      -- 教練姓名
    identity_number TEXT UNIQUE,       -- 身分證字號，唯一
    birth_date TEXT,                               -- 出生日期
    gender TEXT,                                    -- 性別
    instructor_license_number TEXT,       -- 教練證號碼
    license_category TEXT,                      -- 駕照類別
    license_number TEXT,                        -- 駕照號碼
    landline TEXT,                                    -- 室內電話
    mobile TEXT,                                      -- 手機
    email TEXT,                                        -- 信箱
    residence_address TEXT,                    -- 戶籍地址
    mailing_address TEXT,                       -- 通訊地址
    base_salary REAL,                             -- 底薪
    employment_date TEXT,                    -- 到職日
    resignation_date TEXT,                      -- 離職日
    remarks TEXT,                                   -- 備註
    creation_date TEXT                            -- 建檔日期
)
''')

# 創建管理員資料表
cur.execute(f'''
CREATE TABLE IF NOT EXISTS {db_adminInfo} (
    id INTEGER PRIMARY KEY,             -- 管理員編號，主鍵，整數型
    name TEXT,                                      -- 管理員姓名，文字型
    username TEXT UNIQUE NOT NULL,              -- 帳號，唯一且不可為空，文字型
    password TEXT NOT NULL,                 -- 密碼，不可為空，文字型
    phone_mobile TEXT,                          -- 手機，文字型
    email TEXT,                             -- 信箱，文字型
    mailing_address TEXT,                       -- 通訊地址
    created_at TEXT                 -- 建檔日期，文字型
)
''')

# 創建駕訓班學校資料表
cur.execute(f'''
CREATE TABLE IF NOT EXISTS {db_drivingSchoolInfo} (
    id INTEGER PRIMARY KEY,     -- 駕訓班編號，主鍵，整數型
    name TEXT,      -- 駕訓班名稱，文字型
    abbreviation TEXT,      -- 駕訓班簡稱，文字型
    supervisor_station_code TEXT,       -- 監理站代碼，文字型
    principal TEXT,         -- 班主任，文字型
    phone TEXT,         -- 電話，文字型
    fax TEXT,       -- 傳真，文字型
    address TEXT,       -- 地址，文字型
    created_at TEXT         -- 建檔日期，文字型
)
''')
### 資料表創建完成 ###

# 提交操作
conn.commit()

# 關閉連線
conn.close()

print('資料表建立完成！')