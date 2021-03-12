
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
from reportlab.platypus import Paragraph


my_doc = SimpleDocTemplate('practice_report.pdf')
sample_style_sheet = getSampleStyleSheet()

# if you want to see all the sample styles, this prints them
# sample_style_sheet.list()

flowables = []
my_doc.build(flowables)


# data to enter:

title = "Cuckoo Analysis Report"

category = "Category : "+"file"

filename = "File name : "+"cerber.exe"

score = "score :" +"6.2"
start_time =  'datetime.datetime(2020, 12, 22, 5, 36, 26, 334000)'
end_time = 'datetime.datetime(2020, 12, 22, 5, 43, 40, 663000)'
duration = 434
headers =['Queries for the computername',
'Checks if process is being debugged by a debugger',
'Collects information to fingerprint the system (MachineGuid, DigitalProductId, SystemBiosDate)',
'Checks amount of memory in system, this can be used to detect virtual machines that have a low amount of memory available',
'One or more potentially interesting buffers were extracted, these generally contain injected code, configuration data, etc.',
]




paragraph_1 = Paragraph(title, sample_style_sheet['Heading1'])
paragraph_2 = Paragraph(category,    sample_style_sheet['BodyText'])
paragraph_3 = Paragraph(filename,    sample_style_sheet['BodyText'])
paragraph_4 = Paragraph(str(score),    sample_style_sheet['BodyText'])
paragraph_5 = Paragraph(start_time,    sample_style_sheet['BodyText'])
paragraph_6 = Paragraph(end_time,    sample_style_sheet['BodyText'])
paragraph_7 = Paragraph(str(duration),    sample_style_sheet['BodyText'])
# paragraph_8 = Paragraph(str(headers),    sample_style_sheet['BodyText'])

flowables.extend([paragraph_1,paragraph_2,paragraph_3,paragraph_4,
    paragraph_5,paragraph_6,paragraph_7])

for header in headers:
    print(header+"\n")
    flowables.append(Paragraph(str(header), sample_style_sheet['BodyText']))

my_doc.build(flowables)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch


PAGESIZE = (140 * mm, 216 * mm)
BASE_MARGIN = 5 * mm
class PdfCreator:
    def add_page_number(self, canvas, doc):
        canvas.saveState()
        canvas.setFont('Times-Roman', 10)
        page_number_text = "%d" % (doc.page)
        canvas.drawCentredString(
            0.75 * inch,
            0.75 * inch,
            page_number_text
        )
        canvas.restoreState()
    def get_body_style(self):
        sample_style_sheet = getSampleStyleSheet()
        body_style = sample_style_sheet['BodyText']
        body_style.fontSize = 18
        return body_style
    def build_pdf(self):
        pdf_buffer = BytesIO()
        my_doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=PAGESIZE,
            topMargin=BASE_MARGIN,
            leftMargin=BASE_MARGIN,
            rightMargin=BASE_MARGIN,
            bottomMargin=BASE_MARGIN
        )
        body_style = self.get_body_style()
        flowables = [
            Paragraph("First paragraph", body_style),
            Paragraph("Second paragraph", body_style)
        ]
        my_doc.build(
            flowables,
            onFirstPage=self.add_page_number,
            onLaterPages=self.add_page_number,
        )
        pdf_value = pdf_buffer.getvalue()
        pdf_buffer.close()
        return pdf_value

