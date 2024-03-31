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
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Summarise the following text. Keep all important details about characters and plot."},
        {"role": "system", "content": extendedText},
    ],
    temperature= 0.2
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
        {"role": "system", "content": "List what motivates the story and the charecters in the following text."},
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
        {"role": "system", "content": plot},
        {"role": "system", "content": characters},
        {"role": "system", "content": motivations},
        {"role": "user", "content": studentBio},
        {"role": "system", "content": "What connections can you make between the student and the story."}
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

def generateQuestions(inputs,studentInfo=""):
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a teaching assistant for an elementary school classroom. You write questions that help the students connect with what they are reading. You get the information about the story and student when available. The questions are about getting the student to speak about themselves and their thoughts on the story."},
        {"role": "system", "content": inputs},
        {"role": "system", "content": studentInfo},
        {"role": "system", "content": "Create a list of 5 main questions, with appropriate follow up questions for each. Only ask 1 question per line. Format it as follows ' ;1: [main question] \n 1.1: [follow-up] \n 1.2: [follow-up] \n ;2: [main question]...'. "},
        {"role": "system", "content": "Make sure the questions are conversational and fit for an 8 year old."}
    ],
    temperature= 1
    )
    return completion.choices[0].message.content 

def generateObservations(inputs,studentInfo):
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a twelve year old child who likes reading and adventures. Given the following information about a story, and information about your friend, pick out interesting observations you would make in a conversation with your friend."},
        {"role": "system", "content": inputs},
        {"role": "system", "content": studentInfo},
        {"role": "system", "content": "Create a list of 5 observations."}
    ],
    temperature= 1
    )
    return completion.choices[0].message.content 

def rankQuestions(questions):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Reorder the following questions by importance, given an objective of inciting reflection."},
        {"role": "system", "content": questions},
    ],
    temperature= 0.2
    )
    return completion.choices[0].message.content

def findSummary(title, language="english"):
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": f"Based on the following title, generate a plot summary in {language}. Include all important characters and plot moments."},
        {"role": "system", "content": title}
    ],
    temperature= 0.2
    )
    return completion.choices[0].message.content 

def translate(text):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Translate the following text to Dutch, in words that an eight year old might use."},
        {"role": "system", "content": text},
    ],
    temperature= 0.2
    )
    return completion.choices[0].message.content