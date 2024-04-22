import sqlite3

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
)

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
    dropout VARCHAR, - 是否退訓
    register_number VARCHAR, -- 名冊號碼（期別增加修改為名冊號碼）
    written_exam_date VARCHAR, -- 筆試日期
    session_number VARCHAR, -- 場次
    road_test_date VARCHAR, -- 路試日期
    group_number VARCHAR, -- 組別
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 建檔時間
)

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
    m_address VARCHAR -- 通訊地址
    instructor_license_number VARCHAR, -- 教練證號碼
    driving_license_category VARCHAR, -- 駕照類別
    driving_license_number VARCHAR, -- 駕照號碼
    base_salary INTEGER, -- 基本薪資
    start_date VARCHAR, -- 入職日期
    end_date VARCHAR, -- 離職日期
    remarks TEXT, -- 備註
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
)
"""