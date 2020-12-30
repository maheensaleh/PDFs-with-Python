#=============== IMPORTS =================#

import datetime

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle,Image, SimpleDocTemplate, Paragraph, PageBreak ,ListFlowable, ListItem, Frame, PageTemplate, BaseDocTemplate
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.units import mm, inch, cm



#======================== DATA ==============================#

task_id = 17
title = "CUCKOO ANALYSIS REPORT"
category = "file"
filename = "cerber.exe"
score = 4
guest_machine = "Cukcoo Guest 01"
start_time =  datetime.datetime(2020, 12, 22, 5, 36, 26)
end_time = datetime.datetime(2020, 12, 22, 5, 43, 40)
duration = 434
headers =['Queries for the computername',
'Checks if process is being debugged by a debugger',
'Collects information to fingerprint the system (MachineGuid, DigitalProductId, SystemBiosDate)',
'Checks amount of memory in system, this can be used to detect virtual machines that have a low amount of memory available',
'One or more potentially interesting buffers were extracted, these generally contain injected code, configuration data, etc.',
]






#======================= functions ==============================#


def add_signatures(sig_list):
    style_sheet = getSampleStyleSheet()
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

def get_gap():
    title_ss0 = getSampleStyleSheet()
    title_style0 = title_ss0['Normal']
    title_style0.alignment = 0
    title_style0.fontSize  = 15
    title_style0.textColor = "#FFFFFF"
    gap = Paragraph("Text For Gap", title_style0)
    return gap


def get_title(title = "CUKCOO ANALYSIS REPORT"):

    title_ss = getSampleStyleSheet()
    title_style = title_ss['Title']
    title_style.font_size =30

    c_logo = Image("c_logo.jpeg", 1.3*inch, 0.6*inch)
    c_logo.hAlign="LEFT"

    title_tbl_style = TableStyle([
            ('ALIGN', (0, 0), (1,1), 'LEFT'),
            ('VALIGN', (0, 0), (1,1), 'MIDDLE'),
            ])

    title_tbl_data = [
        [c_logo, Paragraph(title,title_style)],
    ]

    title_tbl = Table(
        title_tbl_data,
        colWidths=[1 * inch,5*inch ],
        style = title_tbl_style
        )

    return title_tbl



def get_score(ascore):

    score_ss = getSampleStyleSheet()
    score_style = score_ss['BodyText']
    score_style.alignment = 1
    score_style.leading = 20
    score_style.fontSize =13
    score_style.borderPadding= (3,6,3,6)
    score_style.borderRadius = 2
    score_style.borderWidth = 0.1*mm

    if float(ascore)>5.0:
        # set score display theme as red
        score_style.borderColor = "#e86f6f"
        score_style.backColor = "#ff8f8f"
        score_text = "Analysis score for this file is <b>"+ascore+"</b> which indicates that it is a <b>very suspicious file</b>."
    else:
        #set score tehme as green
        score_style.borderColor = "#13ba66"
        score_style.backColor = "#2aeb8a"
        score_text = "Analysis score for this file is <b>"+ascore+"</b> which indicates that it is a <b>very suspicious file</b>."

    
    return Paragraph(score_text,    score_style)

def get_heading(heading):
    
    heading_ss = getSampleStyleSheet()
    heading_style = heading_ss['Heading2']
    heading_style.leading =30
    heading_style.borderPadding =(3,0,-6,6)
    heading_style.fontSize = 15
    heading_style.backColor = "#4472c4"
    heading_style.textColor ="#FFFFFF"
    
    return Paragraph(heading,heading_style)

        
def addPageNumber(canvas, doc):

    canvas.setFont("Arial", 14)
    page_num = canvas.getPageNumber()
    text = "Page No. %s" % page_num
    canvas.drawRightString(110*mm, 20*mm, text)



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


def make_pdf(file_name, report):

    my_doc = SimpleDocTemplate("{}.pdf".format(file_name))
    my_doc.title = file_name+".pdf"

    flowables = []

    # data dicts

    file_info = {
        "Task ID": report['task_id'],
        "Filename":report['filename'],
        "Category":report['category']
        }


    exec_info = {
        "Guest Machine":report['guest_machine'],
        "Start Time":report['start_time'].strftime("%d %b'%Y , %H:%I %p"),
        "End Time":report['end_time'].strftime("%d %b'%Y , %H:%I %p"),
        "Duration":"{} seconds".format(report['duration']),
        
        }



    # add flowable elements

    flowables.append(get_title(report['title']))
    flowables.append(get_gap())
    flowables.append(get_score(report['score']))
    flowables.append(get_gap())
    flowables.append(get_heading("FILE INFORMATION"))
    flowables.append(get_table(file_info))
    flowables.append(get_gap())
    flowables.append(get_heading("EXECUTION INFORMATION"))
    flowables.append(get_table(exec_info))
    flowables.append(get_gap())
    flowables.append(get_heading("SIGNATURES"))
    flowables.append(add_signatures(report['signatures']))

    my_doc.build(flowables,onFirstPage= add_main_header, onLaterPages= addPageNumber)



if __name__ == "__main__":


    data={

        "title" : "CUCKOO ANALYSIS REPORT",
        "score" : str(score),
        "task_id":str(task_id),
        "filename":filename,
        "category":category,
        "guest_machine":guest_machine,
        "start_time":start_time,
        "end_time":end_time,
        "duration":duration,
        "signatures":headers

    }
    make_pdf("test_report", data)








