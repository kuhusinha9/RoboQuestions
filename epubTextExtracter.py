import ebooklib
from ebooklib import epub
from lxml import html



def extract(filename, chapNum):
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
        
#extract('PeterPan.epub', 10)