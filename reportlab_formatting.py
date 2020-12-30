
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
from reportlab.platypus import Table, Image, SimpleDocTemplate, Paragraph, PageBreak ,ListFlowable, ListItem, Frame, PageTemplate, BaseDocTemplate
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


def footer(canvas, my_doc):
    page_info = "Cuckoo Analysis Result"
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (my_doc.page, pageinfo))
    canvas.restoreState()



#==============================================#


sample_style_sheet = getSampleStyleSheet()# if you want to see all the sample styles, this prints them

# pdf_buffer = BytesIO()

my_doc = SimpleDocTemplate("report_format2.pdf")

flowables = []
# my_doc.build(flowables)


# data to enter:

title = "CUCKOO ANALYSIS REPORT"

category = "Category : "+"file"

filename = "File name : "+"cerber.exe"

score = "Analysis Score : " +"6.2"
start_time =  datetime.datetime(2020, 12, 22, 5, 36, 26)
end_time = datetime.datetime(2020, 12, 22, 5, 43, 40)
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




# We really want to scale the image to fit in a box and keep proportions.
im = Image("c_logo.jpeg", 1.5*inch, 0.8*inch)
im.hAlign="RIGHT"

score_ss = getSampleStyleSheet()
score_style = sample_style_sheet['Heading2']
score_style.alignment = 2
score_style.fontSize =13
score_style.borderColor = "#000000"
score_style.borderPadding= (3,6,3,-312)
score_style.borderRadius = 1
# score_style.borderWidth = 0.01*mm
score_style.backColor = "#ff8f8f"

heading_ss = getSampleStyleSheet()
heading_style = heading_ss['Heading2']
heading_style.leading =30
heading_style.borderPadding =(5,0,0,3)
heading_style.fontSize = 18
# heading_style.backColor = "#79b8fc"
# heading_style.textColor ="#FFFFFF"


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

# style_head.textColor = "#000000"
 #FFFF00

# flowables.append(''' <imgsrc= "pic.png" valign="middle"/>'''))

# flowables.append(im)
tbl = Table([
    [Paragraph(title,title_style),im]
])

# flowables.append(tbl)
flowables.append(Paragraph(title,title_style0))

flowables.append(Paragraph(title,title_style))
#
# flowables.append(im)

flowables.append(Paragraph(score,    score_style))

flowables.append(Paragraph("File Information : ",heading_style))
flowables.append(add_info(file_info,fileinfo_ss))

flowables.append(Paragraph("Execution Information : ",heading_style))
flowables.append(add_info(exec_info,execinfo_ss))

flowables.append(Paragraph("Signatures : ",heading_style))
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
    canvas.drawImage( "c_logo.jpeg", 160*mm,265*mm, width=1.5*inch,height=0.8*inch) 

    # header line
    canvas.setStrokeColorRGB(0.203,0.682, 0.921)
    canvas.setLineWidth(1*mm)     
    canvas.line(20*mm,277*mm,154*mm,277*mm)

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
