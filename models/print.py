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
    # 获取treeview中的数据
    data = [['序號', '姓名', '出生日期', '筆試', '路試', '身分證字號', '備註']]
    for item in treeview.get_children():
        values = treeview.item(item)['values']
        data.append([
            str(values[0]),  # 号码
            str(values[4]),  # 学员姓名
            str(values[6]),  # 出生日期
            '',              # 笔试（留空）
            '',              # 路试（留空）
            str(values[5]),  # 身份证号码
            str(values[1])   # 名册号码作为备注
        ])

    # 创建临时PDF文件
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf', mode='wb') as temp_pdf_file:
        temp_pdf_path = temp_pdf_file.name

    # 使用系统默认字体
    default_font = 'Helvetica'
    default_bold_font = 'Helvetica-Bold'

    # 如果是macOS，尝试使用内建中文字体
    if platform.system() == 'Darwin':
        chinese_fonts = [
            ('/System/Library/Fonts/PingFang.ttc', 'PingFang'),
            ('/Library/Fonts/Arial Unicode.ttf', 'Arial Unicode MS'),
            ('/Library/Fonts/Songti.ttc', 'Songti TC'),
        ]
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

    # 创建PDF文档，明确指定A4大小
    doc = SimpleDocTemplate(temp_pdf_path, pagesize=A4)

    # 创建样式
    styles = getSampleStyleSheet()
    styles['Normal'].fontName = default_font
    styles['Heading1'].fontName = default_bold_font

    # 创建表格
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

    # 构建PDF内容
    elements = []
    elements.append(Paragraph('監理所（站）汽車駕駛人考驗記錄清冊', styles['Heading1']))
    elements.append(table)
    
    # 生成PDF
    doc.build(elements)
    print(f"PDF文件已生成: {temp_pdf_path}")

    # 根据操作系统选择打印方法
    system = platform.system()
    if system == "Darwin":  # macOS
        try:
            # 使用 lpr 命令打印，指定 A4 纸张大小
            subprocess.run(["lpr", "-o", "media=A4", temp_pdf_path], check=True)
            print("文档已发送至默认打印机，指定使用A4纸张。请检查您的打印机。")
        except subprocess.CalledProcessError:
            print("打印文档失败。请检查您的打印机设置。")
    elif system == "Windows":
        try:
            # 在 Windows 上，我们无法直接通过命令行指定纸张大小
            # 但是 PDF 本身已经设置为 A4 大小，大多数打印机应该会遵循这个设置
            os.startfile(temp_pdf_path, "print")
            print("打印对话框应该已经打开。PDF已设置为A4大小，请确保打印机设置正确。")
        except AttributeError:
            print("无法直接打印。正在使用默认PDF查看器打开文件。")
            os.startfile(temp_pdf_path)
    else:
        print(f"不支持的操作系统: {system}")
        print(f"请手动打开并打印文件: {temp_pdf_path}")

    # 删除临时文件
    os.unlink(temp_pdf_path)
    print("临时文件已删除。")