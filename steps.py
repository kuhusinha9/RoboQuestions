import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

# Generate questions

load_dotenv()
client = OpenAI(
  api_key=os.environ["OPENAI_API_KEY"]
)

def summarise(extendedText):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Summarise the following text"},
        {"role": "system", "content": extendedText},
    ],
    temperature= 0.5
    )
    return completion.choices[0].message.content

def characters(summary):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "List the charecters in the following text by importance."},
        {"role": "system", "content": summary},
    ],
    temperature= 0.5
    )
    return completion.choices[0].message.content

def motivations(summary):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "What motivates the story and the charecters in the following text."},
        {"role": "system", "content": summary},
    ],
    temperature= 1
    )
    return completion.choices[0].message.content

def plotPoints(summary):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "List the key plot events that occur in the following text."},
        {"role": "system", "content": summary},
    ],
    temperature= 1
    )
    return completion.choices[0].message.content

def studentConnections(plot, characters, motivations, studentBio):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": studentBio},
        {"role": "system", "content": plot},
        {"role": "system", "content": characters},
        {"role": "system", "content": motivations},
        {"role": "system", "content": "What connections can you make between the student and the story"}
    ],
    temperature= 1
    )
    return completion.choices[0].message.content

def robotConnections(plot, characters, motivations, robotBio):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": robotBio},
        {"role": "system", "content": plot},
        {"role": "system", "content": characters},
        {"role": "system", "content": motivations},
        {"role": "system", "content": "What connections can you make between the robot and the story"}
    ],
    temperature= 1
    )
    return completion.choices[0].message.content

def generateQuestions(inputs):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a teaching assistant for an elementary school classroom. You write lists of questions that help the students, who are eight to eleven years old, connect with what they are reading."},
        {"role": "system", "content": inputs},
        {"role": "system", "content": "Create a list of 5 questions."}
    ],
    temperature= 1
    )
    return completion.choices[0].message.content 