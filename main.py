import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
from json_converter import get_student_data

load_dotenv()
client = OpenAI(
  api_key=os.environ["OPENAI_API_KEY"]
)

data = get_student_data("Maria")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a teaching assistant for an elementary school classroom. You write lists of questions that help the students, who are eight to eleven years old, connect with what they are reading."},
    {"role": "system", "content": "Maria is reading Anne of Green Gables. "},
    {"role": "system", "content": data},
    {"role": "system", "content": "What questions should you ask her?"}
  ],
  temperature= 1

)

print(completion.choices[0].message.content)
