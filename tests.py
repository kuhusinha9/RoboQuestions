import os
from json_converter import get_student_data
import steps
from file_handling import save, get, pdf_extract, to_json, epub_extract

NEW_TEXT=False
text="peterPan"
NEW_STUDENT=True
stu="Ruth"
NEW_QUESTIONS=True


#a= pdf_extract("TomSawyer.pdf", 30, 6)
a= epub_extract("PeterPan.epub", 2)

if NEW_TEXT:
    save("summarise", text,steps.summarise(a))

sum= get("summarise", text)

if NEW_TEXT:
   save("characters", text,steps.characters(sum))
   save("motivations", text,steps.motivations(sum))
   save("plotPoints", text,steps.plotPoints(sum))

char= get("characters", text)
moti= get("motivations", text)
plot= get("plotPoints", text)

student= get_student_data(stu)
if NEW_TEXT or NEW_STUDENT:
    save("studentConnection", text, steps.studentConnections(plot,char,moti,student))
connect = get("studentConnection", text)

if NEW_QUESTIONS:
    save("Questions", text, steps.generateQuestions(plot + moti+ char, student+connect))
questions = get("Questions", text)

to_json(questions,text,stu)
print("Done")

