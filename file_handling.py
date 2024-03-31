import ebooklib
from ebooklib import epub
from lxml import html
import pdfquery
import json


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
    return full_text

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
    
def to_json(questions, book, student):
    d={}
    count = 1
    #questions=questions.replace("\n", "")
    for number in questions.strip().split(";"):
        if number == "":
            continue
        else:
            temp_dict = {}
            n = number.strip().split("\n")
            if "" in n:
                n.remove("")
            for q in n:
                temp=(q.split(":"))
                temp_dict[temp[0]]=temp[1]
            d[count]=temp_dict
            count += 1

    try:
        # Load existing data from the JSON file
        with open("question_database.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, initialize with an empty dictionary
        data = {}

    # Add new questions with the given label
    data[f"{student}_{book}"] = d

    # Write the updated data back to the JSON file
    with open("question_database.json", 'w') as file:
        json.dump(data, file, indent=4)
    