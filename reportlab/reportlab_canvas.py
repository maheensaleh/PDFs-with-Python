# from reportlab.pdfgen import canvas

# c = canvas.Canvas("hello.pdf")
# c.drawString(100,750,"Welcome to Reportlab!")
# c.save()

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
my_doc = SimpleDocTemplate('myfile.pdf')


file_name ='cerber.exe'
type = 'file'
score =  6.2
start_time =  "datetime.datetime(2020, 12, 22, 5, 36, 26, 334000)"
end_time = "datetime.datetime(2020, 12, 22, 5, 43, 40, 663000)"
duration = 434
headers =['Queries for the computername'
'Checks if process is being debugged by a debugger'
'Collects information to fingerprint the system (MachineGuid, DigitalProductId, SystemBiosDate)'
'Checks amount of memory in system, this can be used to detect virtual machines that have a low amount of memory available'
'One or more potentially interesting buffers were extracted, these generally contain injected code, configuration data, etc.'
]


canvas = canvas.Canvas("with_canvas.pdf", pagesize=letter)

#add title
canvas.setTitle("title")
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 12)

canvas.drawString(30,750,'CUCKOO ANALYSIS REPORT')
canvas.drawString(30,735,'OF ACME INDUSTRIES')
canvas.drawString(500,750,"12/12/2010")
canvas.line(480,747,580,747)
canvas.drawString(275,725,'AMOUNT OWED:')
canvas.drawString(500,725,"$1,000.00")
canvas.line(378,723,580,723)
canvas.drawString(30,703,'RECEIVED BY:')
canvas.line(120,700,580,700)
canvas.drawString(120,703,"JOHN DOE")

canvas.save()