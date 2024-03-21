import ebooklib
from ebooklib import epub
from lxml import html
import pdfquery


def epub_extract(filename, chapNum):
    book = epub.read_epub(f'stories/{filename}')
    full_text=""
    c=0
    for item in book.get_items():
        
        try:
            temp = item.get_body_content()
            if c > 0 and c <= chapNum: 
                x=html.fromstring(item.get_content())
                text = x.xpath('//body//text()')
                t= [i.replace("\n", " ") for i in text]
                cleaned_text = ''.join(t).strip()
                full_text = full_text + cleaned_text
                print(cleaned_text[7:200])
            c+=1
        except:
            pass

def pdf_extract(filename, pageNum, start = 0):
    pdf = pdfquery.PDFQuery(f"stories/{filename}")
    pdf.load(list(range(start, pageNum)))
    a = pdf.pq('LTTextLineHorizontal')
    text=""
    for t in a:
        text= text + t.text
    
    return text

def save(functionName, story, result):
    with open(f"checkpoints/{functionName}_{story}.txt", 'w', encoding='utf-8') as f:
        f.write(result)

def get(functionName, story):
    with open(f"checkpoints/{functionName}_{story}.txt", 'r', encoding='utf-8') as f:
        return f.read()