from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
from reportlab.platypus import Paragraph


from io import BytesIO
from reportlab.platypus import Frame,PageTemplate,SimpleDocTemplate,BaseDocTemplate, Paragraph, PageBreak ,ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle as PS
from functools import partial

styles = getSampleStyleSheet()
styleN = styles['Normal']
print(styleN.fontSize)
styleN.alignment=2
styleN.fontSize = 8
stylesG = getSampleStyleSheet()
styleH = stylesG['Normal']



def header(canvas, doc, content):
    canvas.saveState()
    w, h = content.wrap(doc.width, doc.topMargin)
    # content.drawOn(canvas, )
    content.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin)
    canvas.restoreState()


doc = BaseDocTemplate('head_foot.pdf', pagesize=letter)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height-2*cm, id='normal')
header_content = Paragraph("<i>Cuckoo Analysis Report </i>", styleN)
template = PageTemplate(id='head_foot', frames=frame, onPage=partial(header, content=header_content))
doc.addPageTemplates([template])





text = []
for i in range(111):
    text.append(Paragraph("This is line %d." % i, styleH))
doc.build(text)
