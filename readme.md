# Create PDF with Python

This repo includes helper functions and scripts to create PDF from text data or html file / url using Python


- - -

## **FROM HTML / URL**

- **Library used** : pdfkit

- **Limitation:** Can only be used for those URLs or HTML files where CSS and JS code lies within the same html file and not included or imported as a link/reference.


## **FROM PLAIN TEXT**

- **Library used** : ReportLab

ReportLab is best for creating PDFs using plain text. All formatting of font, images, headers, footers etc can be easily customized. 

Two methods of creating pdf using report lab are :

1. **Canvas** : Specify the element along with its position on the page

2. **Flowables** : Specify all elements in a list in the order of their position in the PDF and they will be rendered in the same sequence. No need to specify the position of each


***Documentations and Guide***

- https://vonkunesnewton.medium.com/generating-pdfs-with-reportlab-ced3b04aedef
- https://www.reportlab.com/docs/reportlab-userguide.pdf
- https://www.coursehero.com/file/21350854/reportlab-userguide/