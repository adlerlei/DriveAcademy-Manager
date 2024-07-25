# 筆試，場考，道考
import sqlite3
import os
import csv
from tkinter import messagebox, filedialog
from tkinter import filedialog
# 導入 re 模組,用於處理字符串的正則表達式操作
import re

# 資料庫路徑
database_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'driving_school.db')

# 根據指定的條件查詢學員資料
def get_student_data(identifier, value):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    query = f"SELECT * FROM student WHERE {identifier} = ?"
    cursor.execute(query, (value,))
    result = cursor.fetchone()
    
    conn.close()

    return result


# 更新學員資料
def update_student_data(data, uid):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor() 
    if uid == 1: # 場考 , 道考
        cursor.execute('''
            UPDATE student SET
                road_test_date = :road_test_date, -- 路試日期38
                driving_test_group = :driving_test_group, -- 組別39
                road_test_items_type = :road_test_items_type, -- 路考項目40
                driving_test_number = :driving_test_number -- 號碼42
            WHERE id = :id
        ''', data)
        messagebox.showinfo('訊息', '已加入 道考 名冊！')
    elif uid == 2: # 筆試
        cursor.execute('''
            UPDATE student SET
                written_exam_date = :written_exam_date, -- 筆試日期36
                driving_test_code = :driving_test_code, -- 代碼44
                driving_test_session = :driving_test_session, -- 場次43
                driving_test_number = :driving_test_number -- 號碼42
            WHERE id = :id
        ''', data)
        messagebox.showinfo('訊息', '已加入 筆試 名冊')

    conn.commit()
    conn.close()


import csv
import sqlite3
from tkinter import filedialog, messagebox

def export_driving_test_data(database_path):
    try:
        # 连接到数据库
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # 获取最新的上课期别代码
        cursor.execute("SELECT MAX(term_class_code) FROM annual_plan")
        latest_term_class_code = cursor.fetchone()[0]

        if not latest_term_class_code:
            messagebox.showerror("错误", "未找到有效的上课期别代码")
            return

        # 构造文件名
        filename = f"400032{latest_term_class_code}_E.csv"

        # 打开文件对话框
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile=filename)
        if not file_path:
            return  # 用户取消了保存

        # 查询所有需要导出的数据
        cursor.execute("""
            SELECT s.register_term, s.national_id_no, s.birth_date, s.driving_test_group, 
                   s.road_test_date, s.driving_test_number, s.road_test_items_type
            FROM student s
            WHERE s.road_test_date IS NOT NULL
            ORDER BY s.register_term, s.driving_test_number
        """)
        data = cursor.fetchall()

        # 写入CSV文件
        with open(file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                # 确保每个字段都有值，如果为None则替换为空字符串
                processed_row = [str(item) if item is not None else '' for item in row]
                writer.writerow(processed_row)

        messagebox.showinfo("成功", f"文件已成功匯出至 {file_path}")

    except Exception as e:
        messagebox.showerror("错误", f"匯出文件發生錯誤：{str(e)}")
        print(f"错误详情: {e}")  # 打印详细错误信息

    finally:
        if conn:
            conn.close()