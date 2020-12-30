# import pdfkit, json
# data = {
#     "name":"maheen",
#     "year":2018,
# }
# # pdfkit.from_file(json.dumps(data))
# pdfkit.from_file('report.json', 'out.pdf')
# from pdfrw import PdfWriter as PDFWriter
# import sys
# import json


import pdfkit
# pdfkit.from_url('http://micropyramid.com', 'form_url.pdf')


pdfkit.from_url("http://127.0.0.1:8000/analysis/19/summary", 'form_url_cuckoo2.pdf')


# pdfkit.from_file('data.txt', 'micro.pdf')
# pdfkit.from_file('test.json', 'test.pdf')
