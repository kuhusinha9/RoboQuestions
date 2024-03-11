import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
from json_converter import get_student_data

load_dotenv()
client = OpenAI(
  api_key=os.environ["OPENAI_API_KEY"]
)

name = input("Enter the name of the student. \n")
data = get_student_data(name)

reading=input("Enter the filename (with extention) that the student has read \n")
with open(f"stories/{reading}", 'r', encoding='utf-8') as f:
  text= f.read()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a teaching assistant for an elementary school classroom. You write lists of questions that help the students, who are eight to eleven years old, connect with what they are reading."},
    {"role": "system", "content": text},
    {"role": "system", "content": f"{name} has read this text. "},
    {"role": "system", "content": data},
    {"role": "system", "content": f"Write 5 questions for {name}."}
  ],
  temperature= 1

)

with open("outputs.txt", "w") as out:
  out.write(completion.choices[0].message.content)
