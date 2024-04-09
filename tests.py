from os.path import exists
import csv
import steps
import random
from file_handling import save, get, pdf_extract, to_json, epub_extract

NEW_TEXT=True
NEW_STUDENT=True
NEW_QUESTIONS=True
FLAVOR=True

with open("data/books.csv","r", encoding='utf-8') as f:
    booklist=csv.reader(f,delimiter=',')

    for book in booklist:
        text=book[1].strip()
        stu=random.choice([0,1,2,3])
        if text != "":
            #Create or find a summary of the text
            # NEW_TEXT= (False if exists(f"checkpoints/summarise_{text}.txt") else True)
            # if NEW_TEXT:
            #     # save summary to checkpoint file
            #     save("summarise", text,steps.findSummary(book[0], "dutch"))

            # retrive summary from checkpoint file
            #sum= get("summarise", text)

            # Generate questions based on given information
            #if NEW_QUESTIONS or FLAVOR:
            #    # save questions to checkpoint
            #    save("Script", text, steps.pipeline(sum, text, stu, NEW_TEXT, NEW_STUDENT, NEW_QUESTIONS))
            
            if exists(f"checkpoints/Script_{text}.txt"):
                print(text)
                responses=get("Script", text)
                # save the questions to json database
                to_json(responses,"question_database1.json",stu,text)

print("Done")

