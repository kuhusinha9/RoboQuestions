import os
from json_converter import get_student_data
import steps
from file_handling import save, get, to_json

version = input("Type 'pipe' or 'direct' to select version\n")
result = ""

name = input("Enter the name of the student. \n")
data = get_student_data(name)

reading=input("Enter the name of the txt file that the student has read \n")
if os.path.exists(f"stories/{reading}.txt") and reading != "":
  with open(f"stories/{reading}.txt", 'r', encoding='utf-8') as f:
    text= f.read()
else:
  print("Invalid filename, opening default chapter")
  with open(f"stories/chapter25.txt", 'r', encoding='utf-8') as f:
    text= f.read()

additional= input("Add any additional information here \n")

if version == "direct":
  result = steps.generateQuestions(text)
elif version == "pipe":
  result = steps.pipeline(text, reading, name)
else:
  print("Invalid version input")

with open("outputs.txt", "w") as out:
  out.write(result)
  print(result)
  print("Questions added to output file")
