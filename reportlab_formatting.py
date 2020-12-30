
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch, cm
from reportlab.platypus import Paragraph
from functools import partial
from cStringIO import StringIO
from reportlab.lib import colors

from io import BytesIO
from reportlab.platypus import Table, TableStyle,Image, SimpleDocTemplate, Paragraph, PageBreak ,ListFlowable, ListItem, Frame, PageTemplate, BaseDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle as PS

import datetime
#======================= functions ==============================#


def add_signatures(sig_list, style_sheet):
    style= style_sheet['Normal']
    style.leading = 24
    style.fontSize = 12

    # make sig list
    list_items = []

    for item in sig_list:
        list_items.append(
            ListItem(Paragraph(item,style))
        )

    listFlowables = ListFlowable(list_items,bulletType='bullet',leftIndent=10)
    return listFlowables

def add_info(data, style_sheet):
    style = style_sheet['Normal']
    style.leading = 20
    style.fontSize = 12

    # style.borderWidth = 1*mm
    # style.borderColor = "#000000"

    list_items=[]

    for key in data.keys():
        list_items.append(ListItem(Paragraph("<b>{}</b> : {}".format(key,data[key]),style)))

    
    listFlowables = ListFlowable(list_items,bulletType='bullet',leftIndent=10)
    return listFlowables 


def get_table(data_dict):
    ss = getSampleStyleSheet()
    style = ss['BodyText']

    chart_style = TableStyle([
                ('ALIGN', (0, 0), (0,0), 'CENTER'),
                ('VALIGN', (0, 0), (0,0), 'TOP'),
                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                
                ])

    tbl_data = []

    for key in data_dict.keys():
        tbl_data.append(
        [Paragraph("<b>{}</b>".format(key)),Paragraph(data_dict[key])],

        )

    tbl = Table(tbl_data,style = chart_style)

    return tbl


# flowables.append(Table([[im, im2]],
#                      colWidths=[2 * inch,5*inch ],
#                      rowHeights=[1 * inch], style=chart_style))


def footer(canvas, my_doc):
    page_info = "Cuckoo Analysis Result"
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (my_doc.page, pageinfo))
    canvas.restoreState()



#==============================================#


sample_style_sheet = getSampleStyleSheet()# if you want to see all the sample styles, this prints them

# pdf_buffer = BytesIO()

my_doc = SimpleDocTemplate("test_report2.pdf")

flowables = []
# my_doc.build(flowables)


# data to enter:

title = "CUCKOO ANALYSIS REPORT"

category = "Category : "+"file"

filename = "File name : "+"cerber.exe"

score = "Analysis score for this file is <b>6.2</b> which indicates that it is a <b>very suspicious file</b>."

report_time = datetime.datetime.now()
report_time =  report_time.strftime("%d %b'%Y")

start_time =  datetime.datetime(2020, 12, 22, 5, 36, 26)

start_time =  start_time.strftime("%d %b'%Y , %H:%I %p")
print(start_time)
end_time = datetime.datetime(2020, 12, 22, 5, 43, 40)
end_time =  end_time.strftime("%d %b'%Y , %H:%I %p")

duration = 434
headers =['Queries for the computername',
'Checks if process is being debugged by a debugger',
'Collects information to fingerprint the system (MachineGuid, DigitalProductId, SystemBiosDate)',
'Checks amount of memory in system, this can be used to detect virtual machines that have a low amount of memory available',
'One or more potentially interesting buffers were extracted, these generally contain injected code, configuration data, etc.',
]



title_ss0 = getSampleStyleSheet()
title_style0 = sample_style_sheet['Normal']
title_style0.alignment = 0
title_style0.fontSize  = 15
title_style0.textColor = "#FFFFFF"
# title_style.backColor = "#012345"



title_ss = getSampleStyleSheet()
title_style = sample_style_sheet['Title']
title_style.alignment = 0
title_style.fontSize  = 24
# title_style.backColor = "#012345"
title_style.leading =44




#

score_ss = getSampleStyleSheet()
score_style = sample_style_sheet['BodyText']
score_style.alignment = 1
score_style.leading = 20
score_style.fontSize =13
score_style.borderColor = "#e86f6f"
score_style.borderPadding= (3,6,3,6)
score_style.borderRadius = 2
score_style.borderWidth = 0.1*mm
score_style.backColor = "#ff8f8f"

heading_ss = getSampleStyleSheet()
heading_style = heading_ss['Heading2']
heading_style.leading =30
heading_style.borderPadding =(3,0,-6,6)
heading_style.fontSize = 15
# heading_style.under
heading_style.backColor = "#4472c4"
heading_style.textColor ="#FFFFFF"


fileinfo_ss = getSampleStyleSheet()
file_info = {
    "Task ID":"17",
    "Filename":"cerber.exe",
    "Category":"file"}

execinfo_ss = getSampleStyleSheet()
exec_info = {
    "Guest Machine":"Machine Name",
    "Start Time":start_time,
    "End Time":end_time,
    "Duration":"{} seconds".format(duration),
    
    }

sig_ss = getSampleStyleSheet()


date_ss = getSampleStyleSheet()
date_style = date_ss['BodyText']
# flowables.append(Paragraph(title,title_style0)) # gap
# flowables.append(Paragraph(title,title_style0)) # gap

# flowables.append(Paragraph(title,title_style))
# flowables.append(Paragraph("<i>Dated : {} </i>".format(report_time),date_style))

#
# flowables.append(im)
# flowables.append(Paragraph(title,title_style0)) # gap

#  We really want to scale the image to fit in a box and keep proportions.
im = Image("c_logo.jpeg", 1.3*inch, 0.6*inch)
im.hAlign="LEFT"

head_ss = getSampleStyleSheet()
head_style = head_ss['Title']
head_style.font_size =30
# head_style.alignment=0
# head_style

head_tbl_style = TableStyle([('ALIGN', (0, 0), (1,1), 'LEFT'),
                          ('VALIGN', (0, 0), (1,1), 'MIDDLE')])

head_tbl_data = [
    [im, Paragraph("CUKCOO ANALYSIS REPORT",head_style)],
]

flowables.append(Table(
    head_tbl_data,
    colWidths=[1 * inch,5*inch ],
     style = head_tbl_style))

flowables.append(Paragraph(title,title_style0)) # gap
flowables.append(Paragraph(score,    score_style))

flowables.append(Paragraph(title,title_style0)) # gap
flowables.append(Paragraph(title,title_style0)) # gap

flowables.append(Paragraph("FILE INFORMATION: ",heading_style))
# flowables.append(add_info(file_info,fileinfo_ss))
flowables.append(get_table(file_info))

flowables.append(Paragraph(title,title_style0)) # gap
flowables.append(Paragraph("EXECUTION INFORMATION : ",heading_style))
# flowables.append(add_info(exec_info,execinfo_ss))
flowables.append(get_table(exec_info))

flowables.append(Paragraph(title,title_style0)) # gap
flowables.append(Paragraph("SIGNATURES : ",heading_style))
flowables.append(add_signatures(headers,sig_ss))

# def addPageNumber(canvas, my_doc):
#     """
#     Add the page number
#     """
#     page_num = canvas.getPageNumber()
#     text = "Page #%s" % page_num
#     canvas.drawRightString(200*mm, 20*mm, text)

def addPageNumber(canvas, doc):
    canvas.setFont("Arial", 14)
    page_num = canvas.getPageNumber()
    text = "Page No. %s" % page_num
    canvas.drawRightString(110*mm, 20*mm, text)
    # canvas.drawString(150*mm, 280*mm, "Cuckoo Sandbox")

def add_main_header(canvas,doc):

    # header image
    canvas.drawInlineImage( "nccs.jpeg", 165*mm,268*mm, width=0.7*inch,height=0.7*inch) 


    # header line
    r,g,b = 68.0/255.0,114.0/255.0,196.0/255.0
    canvas.setStrokeColorRGB(r,g,b)
    canvas.setLineWidth(1*mm)     
    canvas.line(20*mm,277*mm,160*mm,277*mm)

    # first page number
    page_num = canvas.getPageNumber()
    text = "Page No. %s" % page_num
    canvas.drawRightString(110*mm, 10*mm, text)

    # footer line
    canvas.setStrokeColorRGB(0,0,0)
    canvas.setLineWidth(1*mm)     
    canvas.line(20*mm,20*mm,190*mm,20*mm)

# flowables=[Paragraph("hello world")]

my_doc.build(flowables,  onFirstPage=add_main_header, onLaterPages=addPageNumber)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
