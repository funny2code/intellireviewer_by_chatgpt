from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate
from io import BytesIO
import json
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch

sample_style_sheet = getSampleStyleSheet()
# sample_style_sheet.list()

def export_pdf(js_obj):
    pagesize = (140 * mm, 216 * mm)  # width, height
    pdf_buffer = BytesIO()
    my_doc = SimpleDocTemplate(
        pdf_buffer, 
        pagesize=pagesize, 
        topMargin=1*inch,
        leftMargin=1*inch,
        rightMargin=1*inch,
        bottomMargin=1*inch
    )
    # my_doc = SimpleDocTemplate('hello.pdf')
    flowables = []

    for key in js_obj:
        paragraph_1 = Paragraph(
            key, 
            sample_style_sheet['Heading1']
        )
        paragraph_2 = Paragraph(
            js_obj[key],
            sample_style_sheet['BodyText']
        )
        
        flowables.append(paragraph_1)
        flowables.append(paragraph_2)

    my_doc.build(flowables)
    pdf_value = pdf_buffer.getvalue()
    pdf_buffer.close()

    return pdf_value