import pdfquery

#TODO: find starting page, adjust page number to ignore non numbered pages

def extract(filename, pageNum, start = 0):
    pdf = pdfquery.PDFQuery(f"stories/{filename}")
    pdf.load(list(range(start, pageNum)))
    a = pdf.pq('LTTextLineHorizontal')
    text=""
    for t in a:
        text= text + t.text
    
    return text