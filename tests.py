import os
from json_converter import get_student_data
import steps
from file_handling import save, get, pdf_extract


#a= pdf_extract("TomSawyer.pdf", 30, 6)
sum= get("summarise", "tomSawyer")
char= get("characters", "tomSawyer")
moti= get("motivations", "tomSawyer")
plot= get("plotPoints", "tomSawyer")
connect = get("studentConnection", "tomSawyer")

student= get_student_data("Maria")

save("Questions", "tomSawyer", steps.generateQuestions(plot + moti+ char, student+connect))
#print(steps.findSummary("Dodo by Mohana van den Kroonenberg"))
print("Done")