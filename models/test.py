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
                road_test_items_type = ?
            WHERE id = ?
        ''', (
            student_data['register_number'],
            student_data['road_test_date'],
            student_data['road_test_items_type'],
            student_data['id']
        ))

        conn.commit()
        print(f"Data updated successfully for student ID: {student_data['id']}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


# 場考清冊匯出csv
def export_driving_test_data(database_path):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute("SELECT MAX(term_class_code) FROM annual_plan")
        latest_term_class_code = cursor.fetchone()[0]

        if not latest_term_class_code:
            messagebox.showerror("錯誤", "未找到有效的上課期別代碼")
            return

        filename = f"400032{latest_term_class_code}_E.csv"
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile=filename)
        if not file_path:
            return

        cursor.execute("""
            SELECT s.register_term, s.national_id_no, s.birth_date, s.driving_test_group, 
                   s.road_test_date, s.driving_test_number, s.road_test_items_type
            FROM student s
            WHERE s.road_test_date IS NOT NULL
            ORDER BY s.register_term, s.driving_test_number
        """)
        data = cursor.fetchall()

        with open(file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                processed_row = [str(item) if item is not None else '' for item in row]
                writer.writerow(processed_row)

        messagebox.showinfo("成功", f"文件已成功匯出至 {file_path}")

    except Exception as e:
        messagebox.showerror("錯誤", f"匯出文件發生錯誤：{str(e)}")

    finally:
        if conn:
            conn.close()

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
