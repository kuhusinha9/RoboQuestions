import os
from json_converter import get_student_data
import steps
from pdfTextExtracter import extract
from handleCheckpoints import save, get

with open("stories/chapter25.txt", 'r', encoding='utf-8') as f:
    text= f.read()

#a= extract("TomSawyer.pdf", 30, 6)
sum= get("summarise", "tomSawyer")
char= get("characters", "tomSawyer")
moti= get("motivations", "tomSawyer")
plot= get("plotPoints", "tomSawyer")
connect = get("studentConnection", "tomSawyer")

student= get_student_data("Maria")

save("Observations", "tomSawyer", steps.generateObservations(plot + moti+ char + connect))
print("Done")