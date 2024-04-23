import sqlite3
import csv

conn = sqlite3.connect('driving_school.db')
c = conn.cursor()

# Create table
sql_script = """
-- 創建期別新增資料表
CREATE TABLE annual_plan (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- id主鍵自增
    year varchar, -- 年度
    term varchar, -- 期別
    batch varchar, -- 梯次
    training_type varchar, -- 訓練班別
    start_date varchar, -- 開訓日期
    end_date varchar, -- 結訓日期
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 創建學員資料表
CREATE TABLE student (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- id主鍵自增
    license_type_code VARCHAR, -- 考照類別編號
    license_type_name VARCHAR, -- 考照類別名稱
    student_number VARCHAR, -- 學員編號
    student_name VARCHAR, -- 學員姓名
    birth_date VARCHAR, -- 出生日期
    national_id_no VARCHAR, -- 身分證字號
    mobile_phone VARCHAR, -- 手機
    home_phone VARCHAR, -- 市話
    education VARCHAR, -- 學歷
    gender VARCHAR, -- 性別
    email VARCHAR, -- 信箱
    remarks TEXT, -- 備註
    r_address VARCHAR, -- 戶籍地址
    m_address VARCHAR, -- 通訊地址
    learner_permit_date VARCHAR, -- 學照日期
    learner_permit_number VARCHAR, -- 學照號碼
    submission_date VARCHAR, -- 送件日期
    exam_code VARCHAR, -- 來源編號
    exam_name VARCHAR, -- 來源名稱
    transmission_type_code VARCHAR, -- 手自排類別編號
    transmission_type_name VARCHAR, -- 手自排類別名稱
    dropout VARCHAR, -- 是否退訓
    register_number VARCHAR, -- 名冊號碼（期別增加修改為名冊號碼）
    written_exam_date VARCHAR, -- 筆試日期
    session_number VARCHAR, -- 場次
    road_test_date VARCHAR, -- 路試日期
    group_number VARCHAR, -- 組別
    road_test_items_type VARCHAR, -- 路考項目
    exam_type_code VARCHAR, -- 筆路編號
    exam_type_name VARCHAR, -- 筆路名稱
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 教練資料表
CREATE TABLE IF NOT EXISTS instructor (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- id主鍵自增
    number VARCHAR, -- 教練編號
    name VARCHAR, -- 教練姓名
    national_id_no VARCHAR, -- 身份證號
    birth_date VARCHAR, -- 出生日期
    home_phone VARCHAR, -- 住宅電話
    mobile_phone VARCHAR, -- 手機號碼
    email VARCHAR, -- 電子郵箱
    r_address VARCHAR, -- 戶籍地址
    m_address VARCHAR, -- 通訊地址
    instructor_license_number VARCHAR, -- 教練證號碼
    driving_license_category VARCHAR, -- 駕照類別
    driving_license_number VARCHAR, -- 駕照號碼
    base_salary INTEGER, -- 基本薪資
    start_date VARCHAR, -- 入職日期
    end_date VARCHAR, -- 離職日期
    remarks TEXT, -- 備註
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 管理員註冊資料表
CREATE TABLE IF NOT EXISTS admin (
	id INTEGER PRIMARY KEY,
	name VARCHAR NOT NULL,
	password VARCHAR NOT NULL,
	creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 郵局地址信息資料表
CREATE TABLE IF NOT EXISTS address_data (
    id INTEGER PRIMARY KEY,
    zip_code VARCHAR, -- 郵遞區號
    city VARCHAR, -- 城市
    address VARCHAR, -- 地址
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);
"""

# 拆分SQL腳本為單條語句並執行
for statement in sql_script.split(';'):
    if statement.strip():
        c.execute(statement)

# 寫入資料庫
# 開啟CSV檔案並讀取內容
with open('addcsv.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # 跳過第一行標題
    next(reader)
    
    # 逐行處理資料
    for row in reader:
        city = row[0]
        zip_code = row[1]
        
        # 插入資料到address_data資料表
        c.execute("INSERT INTO address_data (zip_code, city) VALUES (?, ?)", (zip_code, city))


# 提交資料庫
conn.commit()

# 關閉資料庫連線
conn.close()