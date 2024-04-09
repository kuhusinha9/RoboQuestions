import os
import steps
from file_handling import save, get, pdf_extract, to_json, epub_extract

NEW_TEXT=False
text="regelsVanFloor"
NEW_STUDENT=True
stu=0
NEW_QUESTIONS=False
FLAVOR=True

#NEW_OBS = False
#NEW_JOKES = False

 #Create or find a summary of the text
if NEW_TEXT:
    #a= pdf_extract("TomSawyer.pdf", 30, 6)
    # with open(f"stories/vettePech.txt", 'r', encoding='utf-8') as f:
    #     a= f.read()

    # save summary to checkpoint file
    save("summarise", text,steps.findSummary("De regels van floor (marjon hofman)", "dutch"))

# retrive summary from checkpoint file
sum= get("summarise", text)

# Generate questions based on given information
if NEW_QUESTIONS or FLAVOR:
    # save questions to checkpoint
    save("Script", text, steps.pipeline(sum, text, stu, NEW_TEXT, NEW_STUDENT, NEW_QUESTIONS))

# retrieve questions from checkpoint
#script = get("Script", text)

#save("AddedFlavor3", text, steps.addFlavour(script))
#print(script)

# save the questions to json database
#to_json(questions,text,stu,"question_database.json")

print("Done", stu, text)

