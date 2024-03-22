import sqlite3


conn = sqlite3.connect('driving_school.db')
cursor = conn.cursor()

# 創建資料表
sql_script = """
-- 期別資料表
CREATE TABLE IF NOT EXISTS term (
  id INTEGER PRIMARY KEY,
  year VARCHAR NOT NULL, -- 年度
  term VARCHAR NOT NULL, -- 期別
  start_date VARCHAR NOT NULL, -- 開訓日期
  end_date VARCHAR NOT NULL, -- 結訓日期
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 建檔時間
  batch_id INTEGER NOT NULL, -- 梯次外鍵
  FOREIGN KEY (batch_id) REFERENCES batch(id)
);

-- 學員資料表
CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY,
  student_number VARCHAR NOT NULL, -- 學員編號
  student_name VARCHAR NOT NULL, -- 學員姓名
  national_id_no VARCHAR NOT NULL, -- 身分證字號
  birth_date VARCHAR NOT NULL, -- 出生日期
  home_phone VARCHAR, -- 住家電話
  work_phone VARCHAR, -- 公司電話
  mobile_phone VARCHAR, -- 手機
  email VARCHAR, -- 信箱
  dropout VARCHAR - 退訓
  -- 戶籍地址道路 -----------------------------------------------
  r_address VARCHAR NOT NULL -- 地址
  -- 通訊地址道路 -----------------------------------------------
  m_address VARCHAR -- 地址
  ------------------------------------------------------------------------
  remarks TEXT, -- 備註
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 建檔時間
  address_data_id INTEGER, -- 地址資料
  gender_id INTEGER NOT NULL, -- 性別
  education_level_id INTEGER, -- 學歷
  instructor_id INTEGER, -- 指導教練
  training_type_id INTEGER NOT NULL, -- 訓練班別
  license_type_id INTEGER NOT NULL, -- 考照類別
  batch_id INTEGER NOT NULL, -- 梯次
  FOREIGN KEY (address_data_id) REFERENCES address_data(id),
  FOREIGN KEY (gender_id) REFERENCES gender(id),
  FOREIGN KEY (education_level_id) REFERENCES education_level(id),
  FOREIGN KEY (instructor_id) REFERENCES instructor(id),
  FOREIGN KEY (training_type_id) REFERENCES training_type(id),
  FOREIGN KEY (license_type_id) REFERENCES license_type(id),
  FOREIGN KEY (batch_id) REFERENCES batch(id)
);

-- 管理員註冊資料表
CREATE TABLE IF NOT EXISTS admin (
	id INTEGER PRIMARY KEY,
	name VARCHAR NOT NULL,
	password VARCHAR NOT NULL,
	creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 教練資料表
CREATE TABLE IF NOT EXISTS instructor (
 id INTEGER PRIMARY KEY, -- 主鍵，教練ID
 number VARCHAR NOT NULL, -- 教練編號
 name VARCHAR NOT NULL, -- 教練姓名
 national_id_no VARCHAR NOT NULL, -- 身份證號
 birth_date VARCHAR NOT NULL, -- 出生日期
 home_phone VARCHAR, -- 住宅電話
 mobile_phone VARCHAR, -- 手機號碼
 email VARCHAR, -- 電子郵箱
  -- 戶籍地址道路 -----------------------------------------------
  r_address VARCHAR NOT NULL -- 地址
  -- 通訊地址道路 -----------------------------------------------
  m_address VARCHAR -- 地址
  ------------------------------------------------------------------------
 instructor_license_number VARCHAR, -- 教練證號碼
 driving_license_category VARCHAR, -- 駕照類別
 driving_license_number VARCHAR, -- 駕照號碼
 base_salary INTEGER, -- 基本薪資
 start_date VARCHAR, -- 入職日期
 end_date VARCHAR, -- 離職日期
 remarks TEXT, -- 備註
 creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 建檔時間
 gender_id INTEGER NOT NULL, -- 性別ID，外鍵關聯到性別表
 address_data_id INTEGER, -- 地址資料
 FOREIGN KEY (address_data_id) REFERENCES address_data(id), -- 地址外鍵關聯
 FOREIGN KEY (gender_id) REFERENCES gender(id) -- 性別外鍵關聯
);

-- 學習駕照資料表
CREATE TABLE IF NOT EXISTS learning_license (
  id INTEGER PRIMARY KEY,
  registration_date VARCHAR NOT NULL, -- 登錄日期
  learner_permit_date VARCHAR, -- 學照日期
  learner_permit_number VARCHAR, -- 學照號碼
  submission_date VARCHAR, -- 送件日期
  remarks TEXT, -- 備註
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 建檔時間
  students_id INTEGER NOT NULL, -- 學員關鏈
  FOREIGN KEY (students_id) REFERENCES students(id)
);

-- 開結訓資料表
CREATE TABLE IF NOT EXISTS opening_closing_register (
  id INTEGER PRIMARY KEY,
  register_number VARCHAR NOT NULL, -- 名冊號碼
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 建檔時間
  students_id INTEGER, -- 學員資料
  training_type_id INTEGER, -- 訓練班別
  term_id INTEGER, -- 期別
  batch_id INTEGER, -- 梯次
  exam_source_type_id INTEGER, -- 來源
  transmission_type_id INTEGER, -- 手自排
  instructor_id INTEGER, -- 教練
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (training_type_id) REFERENCES training_type(id),
  FOREIGN KEY (term_id) REFERENCES term(id),
  FOREIGN KEY (batch_id) REFERENCES batch(id),
  FOREIGN KEY (exam_source_type_id) REFERENCES exam_source_type(id),
  FOREIGN KEY (transmission_type_id) REFERENCES transmission_type(id),
  FOREIGN KEY (instructor_id) REFERENCES instructor(id),
);

-- 筆路試資料表
CREATE TABLE IF NOT EXISTS exam (
  id INTEGER PRIMARY KEY,
  written_exam_date VARCHAR NOT NULL, -- 筆試日期
  road_test_date VARCHAR NOT NULL, -- 路試日期
  list_number VARCHAR, -- 資料列表號碼
  session_number VARCHAR, -- 場次
  code VARCHAR, -- 代碼
  group_number VARCHAR, -- 組別
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 建檔時間
  students_id INTEGER, -- 學員資料
  opening_closing_register_id INTEGER, -- 名冊號碼
  training_type_id INTEGER, -- 訓練班別
  term_id INTEGER, -- 期別
  batch_id INTEGER, -- 梯次
  road_test_items_id, -- 	路考項目
  FOREIGN KEY (students_id) REFERENCES students(id),
  FOREIGN KEY (opening_closing_register_id) REFERENCES opening_closing_register(id),
  FOREIGN KEY (training_type_id) REFERENCES training_type(id),
  FOREIGN KEY (term_id) REFERENCES term(id),
  FOREIGN KEY (term_id) REFERENCES term(id),
  FOREIGN KEY (road_test_items_id) REFERENCES road_test_items(id)
);

-- 監理站資料表
CREATE TABLE IF NOT EXISTS supervision (
  id INTEGER PRIMARY KEY,
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 建檔時間
  exam_type_id INTEGER, -- 筆路試
  students_id INTEGER, -- 學員資料
  opening_closing_register_id INTEGER, -- 名冊號碼
  training_type_id INTEGER, -- 訓練班別
  term_id INTEGER, -- 期別
  batch_id INTEGER, -- 梯次
  exam_source_type_id INTEGER, -- 來源
  transmission_type_id INTEGER, -- 手自排
  instructor_id INTEGER, -- 教練
  FOREIGN KEY (exam_type_id) REFERENCES exam_type(id),
  FOREIGN KEY (students_id) REFERENCES students(id),
  FOREIGN KEY (opening_closing_register_id) REFERENCES opening_closing_register(id),
  FOREIGN KEY (training_type_id) REFERENCES training_type(id),
  FOREIGN KEY (term_id) REFERENCES term(id),
  FOREIGN KEY (batch_id) REFERENCES batch(id),
  FOREIGN KEY (exam_source_type_id) REFERENCES exam_source_type(id),
  FOREIGN KEY (transmission_type_id) REFERENCES transmission_type(id),
  FOREIGN KEY (instructor_id) REFERENCES instructor(id)
);

-- 獨立資料表
-- 郵局地址信息資料表
CREATE TABLE IF NOT EXISTS address_data (
  id INTEGER PRIMARY KEY,
  zip_code VARCHAR, -- 郵遞區號
  city VARCHAR, -- 城市
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 考照類別
CREATE TABLE IF NOT EXISTS license_type (
  id INTEGER PRIMARY KEY,
  type_code VARCHAR NOT NULL,
  type_name VARCHAR NOT NULL, -- 考照類型名稱
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 訓練班別
CREATE TABLE IF NOT EXISTS training_type (
  id INTEGER PRIMARY KEY,
  type_code VARCHAR NOT NULL,
  type_name VARCHAR NOT NULL, -- 訓練班別名稱
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 來源
CREATE TABLE IF NOT EXISTS exam_source_type (
  id INTEGER PRIMARY KEY,
  type_code VARCHAR NOT NULL,
  type_name VARCHAR NOT NULL, -- 來源類型名稱
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 手自排
CREATE TABLE IF NOT EXISTS transmission_type (
  id INTEGER PRIMARY KEY,
  type_code VARCHAR NOT NULL,
  type_name VARCHAR NOT NULL, -- 手自排類型名稱
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 筆路試
CREATE TABLE IF NOT EXISTS exam_type (
  id INTEGER PRIMARY KEY,
  type_code VARCHAR NOT NULL,
  type_name VARCHAR NOT NULL, -- 筆路試類型名稱
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 梯次
CREATE TABLE IF NOT EXISTS batch (
  id INTEGER PRIMARY KEY,
  batch_type VARCHAR NOT NULL, -- 梯次類型
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 性別
CREATE TABLE IF NOT EXISTS gender (
  id INTEGER PRIMARY KEY,
  gender_type VARCHAR NOT NULL, -- 性別類型
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 學歷
CREATE TABLE IF NOT EXISTS education_level (
  id INTEGER PRIMARY KEY,
  education VARCHAR NOT NULL, -- 學歷類型
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);

-- 路考項目
CREATE TABLE IF NOT EXISTS road_test_items (
  id INTEGER PRIMARY KEY,
  road_test_items_code VARCHAR NOT NULL, -- 代號
  road_test_items_type VARCHAR NOT NULL, -- 路考，場考，路考+場考
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 建檔時間
);    
"""

# 拆分SQL腳本為單條語句並執行
for statement in sql_script.split(';'):
    if statement.strip():
        cursor.execute(statement)

# 提交變更
conn.commit()

# 關閉連接
conn.close()