# 筆試，場考，道考 功能邏輯介面
# 對應介面 ui/road_test_roster.py , written_exam_roster.py , driving_test_roster.py
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
def update_student_data(student_data, uid):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            UPDATE student SET
                register_number = ?,
                road_test_date = ?,
                road_test_items_type = ?,
                driving_test_group = ?,
                driving_test_number = ?  -- 添加此行以更新driving_test_number
            WHERE id = ?
        ''', (
            student_data['register_number'],
            student_data['road_test_date'],
            student_data['road_test_items_type'],
            student_data['driving_test_group'],
            student_data['driving_test_number'],  # 确保传入driving_test_number
            student_data['id']
        ))

        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror("錯誤", f"更新學員資料發生錯誤：{str(e)}")
    finally:
        conn.close()


# 場考清冊匯出csv 
def export_driving_test_data(database_path):
    try:
        # 连接到数据库
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # 获取最新的上课期别代码
        cursor.execute("SELECT MAX(term_class_code) FROM annual_plan")
        term_class_code = cursor.fetchone()[0]

        if not term_class_code:
            messagebox.showerror("錯誤", "未找到有效的上課期別代碼")
            return

        # 创建文件名
        file_name = f"400032{term_class_code}_E.csv"

        # 打开文件保存对话框
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile=file_name)
        if not file_path:
            return

        # 查询所有学员的路考数据
        cursor.execute("""
            SELECT register_number, national_id_no, birth_date, driving_test_group, 
                   road_test_date, driving_test_number, road_test_items_type, batch, training_type_code
            FROM student
            WHERE road_test_date IS NOT NULL
            ORDER BY driving_test_number
        """)
        data = cursor.fetchall()

        # 写入CSV文件
        with open(file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                register_number = row[0]  # 名册号码
                training_type_code = row[8]  # 训练班别代号
                batch = row[7]  # 梯次

                # 省略名册号码字母后面的数字
                modified_register_number = register_number.rstrip('0123456789')  # 去掉最后的数字

                # 组合训练班别代号和名册号码
                final_register_number = f"{training_type_code}{modified_register_number}"

                writer.writerow([final_register_number, row[1], row[2], row[3], row[4], row[5], row[6]])

        messagebox.showinfo("成功", f"文件已成功匯出至 {file_path}")

    except Exception as e:
        messagebox.showerror("錯誤", f"匯出文件發生錯誤：{str(e)}")

    finally:
        if conn:
            conn.close()


# 筆試清冊匯出csv
def export_written_exam_roster(database_path):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute("SELECT MAX(term_class_code) FROM annual_plan")
        latest_term_class_code = cursor.fetchone()[0]

        if not latest_term_class_code:
            messagebox.showerror("錯誤", "未找到有效的上課期別代碼")
            return

        filename = f"400032{latest_term_class_code}_D.csv"
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile=filename)
        if not file_path:
            return

        # cursor.execute("""
        #     SELECT s.student_term_class_code, s.register_term, s.national_id_no, s.birth_date, s.driving_test_group, 
        #            s.written_exam_date, s.driving_test_number
        #     FROM student s
        #     WHERE s.written_exam_date IS NOT NULL
        #     ORDER BY s.register_term, s.driving_test_number
        # """)
        cursor.execute("""
            SELECT s.student_term_class_code, s.national_id_no, s.birth_date, s.driving_test_group, 
                   s.written_exam_date, s.driving_test_number
            FROM student s
            WHERE s.written_exam_date IS NOT NULL
            ORDER BY s.driving_test_number
        """)
        data = cursor.fetchall()

        with open(file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                student_term_class_code = row[0]
                if student_term_class_code:
                    # 找到第一個字母的位置
                    alpha_index = next((i for i, c in enumerate(student_term_class_code) if c.isalpha()), None)
                    if alpha_index is not None:
                        # 保留到字母（包括字母）
                        student_term_class_code = student_term_class_code[:alpha_index+1]
                processed_row = [student_term_class_code] + [str(item) if item is not None else '' for item in row[1:]]
                writer.writerow(processed_row)

        # messagebox.showinfo("成功", f"文件已成功匯出至 {file_path}")
        messagebox.showinfo("成功", f"文件已成功匯出")

    except Exception as e:
        messagebox.showerror("錯誤", f"匯出文件發生錯誤：{str(e)}")

    finally:
        if conn:
            conn.close()
