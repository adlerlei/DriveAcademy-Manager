# 筆試，場考，道考 功能邏輯介面
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

    if uid == 1:
        try:
            cursor.execute('''
                UPDATE student SET
                    register_number = ?,
                    road_test_date = ?,
                    road_test_items_type = ?,
                    driving_test_group = ?,
                    driving_test_number = ?  -- 號碼41
                WHERE id = ?
            ''', (
                student_data['register_number'], # 名冊號碼34
                student_data['road_test_date'], # 路試日期37
                student_data['road_test_items_type'], # 路考項目39
                student_data['driving_test_group'], # 組別38
                student_data['driving_test_number'],  # 號碼41
                student_data['id']
            ))

            conn.commit() # 
        except sqlite3.Error as e:
            messagebox.showerror("錯誤", f"更新UID1學員資料發生錯誤：{str(e)}")
        finally:
            conn.close()
    elif uid ==2:
        try:
            cursor.execute('''
                UPDATE student SET
                    register_number = ?, -- 名冊號碼
                    written_exam_date = ?, -- 筆試日期
                    driving_test_number = ?, -- 號碼41
                    driving_test_session = ?, -- 場次42
                    driving_test_code = ? -- 代碼43
                WHERE id = ?
            ''', (
                student_data['register_number'], # 名冊號碼34
                student_data['written_exam_date'], # 筆試日期36
                student_data['driving_test_number'],  # 號碼41
                student_data['driving_test_session'], # 場次42
                student_data['driving_test_code'], # 代碼43
                student_data['id']
            ))

            conn.commit() # 
        except sqlite3.Error as e:
            messagebox.showerror("錯誤", f"更新UID2學員資料發生錯誤 : {str(e)}")
        finally:
            conn.close()
        


# 場考清冊匯出csv 
def export_driving_test_data(database_path, student_ids):  # 修改此行，新增 student_ids 參數
    try:
        # 连接到数据库
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # 获取最新的上课期别代码
        cursor.execute("SELECT MAX(term_class_code) FROM annual_plan")
        term_class_code = cursor.fetchone()[0]

        if not term_class_code:
            messagebox.showerror("錯誤", "未找到有效的上課期别代码")
            return

        # 创建文件名
        file_name = f"400032{term_class_code}_E.csv"

        # 打开文件保存对话框
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile=file_name)
        if not file_path:
            return

        # 查询指定学员的路考数据
        query = f"""
            SELECT register_number, national_id_no, birth_date, driving_test_group, 
                   road_test_date, driving_test_number, road_test_items_type, batch, training_type_code
            FROM student
            WHERE id IN ({','.join('?' for _ in student_ids)})  -- 修改此行以查詢指定學員
            AND road_test_date IS NOT NULL
            ORDER BY driving_test_number
        """
        cursor.execute(query, student_ids)  # 修改此行以傳入 student_ids
        data = cursor.fetchall()
        if not data:
            messagebox.showerror("錯誤", "場考清冊學員資料為空")
            return

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

        messagebox.showinfo("成功", "文件已成功匯出")

    except Exception as e:
        messagebox.showerror("錯誤", f"匯出文件發生錯誤：{str(e)}")

    finally:
        if conn:
            conn.close()


# 筆試清冊匯出csv
def export_written_exam_roster(database_path, student_ids):
    try:
        # 連接到數據庫
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # 獲取最新的上課期別代碼
        cursor.execute("SELECT MAX(term_class_code) FROM annual_plan")
        term_class_code = cursor.fetchone()[0]

        if not term_class_code:
            messagebox.showerror("錯誤", "未找到有效的上課期別代碼")
            return

        # 創建文件名
        file_name = f"400032{term_class_code}_D.csv"

        # 打開文件保存對話框
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile=file_name)
        if not file_path:
            return

        # 查詢指定學員的筆試試卷數據
        query = f"""
            SELECT student_term_class_code, national_id_no, birth_date, driving_test_group, 
                   written_exam_date, driving_test_number, training_type_code
            FROM student
            WHERE id IN ({','.join('?' for _ in student_ids)})
            AND written_exam_date IS NOT NULL
            ORDER BY driving_test_number
        """
        cursor.execute(query, student_ids)
        data = cursor.fetchall()
        if not data:
            messagebox.showerror("錯誤", "筆試清冊學員資料為空")
            return
        
        # 寫入CSV文件
        with open(file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                student_term_class_code = row[0]  # 名冊號碼
                training_type_code = row[6]  # 訓練班別代號

                # 移除名冊號碼開頭的 "1" 和末尾的數字
                modified_register_number = re.sub(r'^1', '', student_term_class_code)
                modified_register_number = re.sub(r'\d+$', '', modified_register_number)

                # 組合訓練班別代號和名冊號碼
                final_register_number = f"{training_type_code}{modified_register_number}"
                
                writer.writerow([final_register_number, row[1], row[2], row[3], row[4], row[5]])

        messagebox.showinfo("成功", "文件已成功匯出")

    except Exception as e:
        messagebox.showerror("錯誤", f"匯出文件發生錯誤：{str(e)}")

    finally:
        if conn:
            conn.close()