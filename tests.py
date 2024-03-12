import os
from json_converter import get_student_data
import steps
import pdfquery

with open("stories/chapter25.txt", 'r', encoding='utf-8') as f:
    text= f.read()

pdf = pdfquery.PDFQuery("stories/CHAPTERXXV.pdf")
pdf.load(3)
print(pdf.tree)