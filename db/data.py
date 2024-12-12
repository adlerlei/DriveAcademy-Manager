import sqlite3
import csv

conn = sqlite3.connect('driving_school.db')
c = conn.cursor()

# Create table
sql_script = """
-- 創建期別新增資料表
CREATE TABLE IF NOT EXISTS annual_plan (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- id主鍵自增
    year VARCHAR, -- 年度
    term VARCHAR, -- 期別
    term_class_code VARCHAR, -- 上課期別代碼
    batch VARCHAR, -- 梯次
    training_type_code VARCHAR, -- 訓練班別代號
    training_type_name VARCHAR, -- 訓練班別名稱
    start_date VARCHAR, -- 開訓日期
    end_date VARCHAR, -- 結訓日期
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 創建學員資料表
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- id主鍵自增0
    license_type_code VARCHAR, -- 考照類別編號1
    license_type_name VARCHAR, -- 考照類別名稱2
    training_type_code VARCHAR, -- 訓練班別代號3
    training_type_name VARCHAR, -- 訓練班別名稱4
    student_number VARCHAR, -- 學員編號5
    student_name VARCHAR, -- 學員姓名6
    batch VARCHAR, -- 梯次7
    register_batch VARCHAR, -- 名冊梯次8
    birth_date VARCHAR, -- 出生日期9
    national_id_no VARCHAR, -- 身分證字號10
    mobile_phone VARCHAR, -- 手機11
    home_phone VARCHAR, -- 市話12
    education VARCHAR, -- 學歷13
    instructor_number VARCHAR, -- 指導教練編號14
    instructor_name VARCHAR, -- 指導教練名稱15
    gender VARCHAR, -- 性別16
    email VARCHAR, -- 信箱17
    remarks TEXT, -- 備註18
    r_address_zip_code VARCHAR, -- 戶籍地址郵遞區號19
    r_address_city VARCHAR, -- 戶籍地址縣市區域20
    r_address VARCHAR, -- 戶籍地址21
    m_address_zip_code VARCHAR, -- 通訊地址郵遞區號22
    m_address_city VARCHAR, -- 通訊地址縣市區域23
    m_address VARCHAR, -- 通訊地址24
    learner_permit_login_data VARCHAR, -- 學照登陸日期25
    learner_permit_date VARCHAR, -- 學照日期26
    learner_permit_number VARCHAR, -- 學照號碼27
    submission_date VARCHAR, -- 送件日期28
    exam_code VARCHAR, -- 來源編號29 
    exam_name VARCHAR, -- 來源名稱30
    transmission_type_code VARCHAR, -- 手自排類別編號31
    transmission_type_name VARCHAR, -- 手自排類別名稱32
    dropout VARCHAR, -- 是否退訓33
    register_number VARCHAR, -- 名冊號碼34
    register_term VARCHAR, -- 期別35
    written_exam_date VARCHAR, -- 筆試日期36
    road_test_date VARCHAR, -- 路試日期37
    driving_test_group VARCHAR, -- 組別38
    road_test_items_type VARCHAR, -- 路考項目39
    exam_type_name VARCHAR, -- 筆試 , 路試40
    driving_test_number VARCHAR, -- 號碼41
    driving_test_session VARCH, -- 場次42
    driving_test_code VARCH, -- 代碼43
    student_term_class_code VARCHAR, -- 學員上課期別代碼44
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間45
);

-- 教練資料表
CREATE TABLE IF NOT EXISTS instructor (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- id主鍵自增0
    number VARCHAR, -- 教練編號1
    name VARCHAR, -- 教練姓名2
    birth_date VARCHAR, -- 出生日期3
    instructor_number VARCHAR, -- 教練證號4
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間5
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
# 讀取 郵遞區號 CSV檔案並讀取內容
with open('addcsv.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # 跳過第一行標題
    next(reader)
    
    # 逐行處理資料
    for row in reader:
        city = row[0]
        zip_code = row[1]
        
        # 插入資料到address_data資料表
        c.execute("INSERT INTO address_data (city, zip_code) VALUES (?, ?)", (city, zip_code))

# 讀取 CTM3-28 年度計劃表 CSV 檔案并将資料寫入資料庫
with open('annual-plan.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # 獲取 CSV 檔案的標題信息
    csv_headers = reader.fieldnames
    
    for row in reader:
        # 構建 INSERT 語句和參數列表
        columns = []
        values = []
        for header in csv_headers:
            if header in row and row[header]:  # 檢查欄位是否存在且不为空
                columns.append(header)
                values.append(row[header])

        if columns:  # 確保有資料需要寫入
            sql = f"""
                INSERT INTO annual_plan ({', '.join(columns)})
                VALUES ({', '.join(['?'] * len(columns))})
            """
            c.execute(sql, values)

# 讀取 CTM3-28 教練清冊 CSV 檔案並將資料寫入資料庫
with open('instructor.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    # 獲取 csv 檔案的標題信息
    csv_headers = reader.fieldnames

    for row in reader:
        # 構建 INSERT 語句和參數列表
        columns = []
        values = []
        for header in csv_headers:
            if header in row and row[header]: # 檢查欄位是否存在且不為空
                columns.append(header)
                values.append(row[header])

        if columns:
            sql = f"""
            INSERT INTO instructor ({', '.join(columns)})
            VALUES ({', '.join(['?'] * len(columns))})
        """
        c.execute(sql, values)

# 讀取 學員基本資料 CSV 檔案並將資料寫入資料庫
with open('student.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    # 獲取 csv 檔案的標題信息
    csv_headers = reader.fieldnames

    for row in reader:
        # 構建 INSERT 語句和參數列表
        columns = []
        values = []
        for header in csv_headers:
            if header in row and row[header]: # 檢查欄位是否存在且不為空
                columns.append(header)
                values.append(row[header])

        if columns:
            sql = f"""
            INSERT INTO student ({', '.join(columns)})
            VALUES ({', '.join(['?'] * len(columns))})
        """
        c.execute(sql, values)

# 提交資料庫
conn.commit()

# 關閉資料庫連線
conn.close()