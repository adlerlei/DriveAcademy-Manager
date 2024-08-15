import os
import platform
import tempfile
import subprocess
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def print_written_exam_roster(treeview):
    # 讀取 treeview 數據資料
    data = [['序號', '姓名', '出生日期', '筆試', '路試', '身分證字號', '備註']]
    for item in treeview.get_children():
        values = treeview.item(item)['values']
        data.append([
            str(values[0]),  # 學生編號
            str(values[4]),  # 學生姓名
            str(values[6]),  # 生日
            '',              # 筆試（留空）
            '',              # 路試（留空）
            str(values[5]),  # 身分證號碼
            str(values[1])   # 名冊號碼
        ])

    # 創建臨時PDF文件
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf', mode='wb') as temp_pdf_file:
        temp_pdf_path = temp_pdf_file.name

    # 根據操作系統選擇字體
    if platform.system() == 'Darwin':  # macOS
        chinese_fonts = [
            ('/System/Library/Fonts/PingFang.ttc', 'PingFang'),
            ('/Library/Fonts/Arial Unicode.ttf', 'Arial Unicode MS'),
            ('/Library/Fonts/Songti.ttc', 'Songti TC'),
        ]
    elif platform.system() == 'Windows':  # Windows
        chinese_fonts = [
            (r'C:\Windows\Fonts\msyh.ttc', 'Microsoft YaHei'),  # 微軟雅黑
            (r'C:\Windows\Fonts\simsun.ttc', 'SimSun'),         # 宋體
        ]
    else:
        chinese_fonts = []

    for font_path, font_name in chinese_fonts:
        try:
            pdfmetrics.registerFont(TTFont(font_name, font_path))
            default_font = font_name
            default_bold_font = font_name
            print(f"成功加载 {font_name} 字体。")
            break
        except:
            print(f"无法加载 {font_name} 字体。")
    else:
        print("无法加载任何中文字体，将使用默认字体。中文可能无法正确显示。")

    # 創建PDF，指定A4大小
    doc = SimpleDocTemplate(temp_pdf_path, pagesize=A4)

    # 創建 pdf 樣式表格
    styles = getSampleStyleSheet()
    styles['Normal'].fontName = default_font
    styles['Heading1'].fontName = default_bold_font

    # 創建表格
    table_data = [[Paragraph(str(cell), styles['Normal']) for cell in row] for row in data]
    table = Table(table_data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), default_font),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)

    # 構建PDF内容
    elements = []
    elements.append(Paragraph('監理所（站）汽車駕駛人考驗記錄清冊', styles['Heading1']))
    elements.append(table)
    
    # 生成PDF
    doc.build(elements)
    print(f"PDF文件已生成: {temp_pdf_path}")

    # 根據不同的作業系統選擇列印方式
    system = platform.system()
    if system == "Darwin":  # macOS
        try:
            # 使用 lpr 打印，指定 A4 紙張大小
            subprocess.run(["lpr", "-o", "media=A4", temp_pdf_path], check=True)
            print("文件已經發送至系統默認印表機，指定A4紙張，請檢查你的列表機。")
        except subprocess.CalledProcessError:
            print("列印文件失敗，請檢查你的列表機設置。")
    elif system == "Windows":
        try:
            # Windows 無法通过命令行指定紙張大小
            # pdf預設為A4
            os.startfile(temp_pdf_path, "print")
            print("列印對話框應該已經打開，PDF已設置為A4大小，請確保列表機設置正確。")
        except AttributeError:
            print("無法直接列印，正在使用默認PDF查看器打開文件。")
            os.startfile(temp_pdf_path)
    else:
        print(f"不支持的操作系统: {system}")
        print(f"請手動打開並且列印文件: {temp_pdf_path}")

    # 删除临时文件
    os.unlink(temp_pdf_path)
    print("臨時文件已經刪除")