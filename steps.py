import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
from file_handling import get, save
from json_converter import get_student_data

# TODO: rename to be more descriptive
# TODO:  questions (no followups)-> add observations, followups and jokes/ questions, followups, observations to ChatGPT to generate flow 
# flow based on engagingness 
# add notes for thesis

load_dotenv()
client = OpenAI(
  api_key=os.environ["OPENAI_API_KEY"]
)

DEFAULT_INFO="You are part of an educational intervention in schools focused on improving reading motivation in students. You are a robot that has one-on-one conversations with students, talking to them about the book they are reading. The idea is to help students build connections between themselves and their reading material."

def summarise(extendedText, language="english"):
    '''
    Function summarises the given text
    extendedText: (str) A chapter or section of a book
    language: (str) the target language in which the summary should be generated
    Returns the summary as a string
    '''
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": f"Summarise the following text in {language}. Keep all important details about characters and plot."},
        {"role": "system", "content": extendedText},
    ],
    temperature= 0.2
    )
    return completion.choices[0].message.content



def findSummary(title, language="english"):
    '''
    Function that searches the web for an approprate summary of a title
    title: (str) Contains name of book, and if helpful the author's name
    language: (str) the target language in which the summary should be generated
    Returns the summary as a string
    '''
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": f"Based on the following title, generate a plot summary in {language}. Include all important characters and plot moments."},
        {"role": "system", "content": title}
    ],
    temperature= 0.2
    )
    return completion.choices[0].message.content 

def characters(summary):
    '''
    Generates a list of characters from a summary
    summary: (str) information about a story
    Returns a list of characters as a string
    '''
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
    '''
    Extracts motivations or themes from text
    summary: (str) information about a story
    Returns a list of motivation as a string
    '''
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
    '''
    Extracts key plot events
    summary: (str) information about a story
    Returns a list of plot events as a string
    '''
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
    '''
    Creates links between the plot and the student information
    plot: (str) key plot events
    characters: (str) a list of characters
    motivations: (str) some details about why a character is doing what they are, or the plot is focused on what it is
    studentBio: (str) some basic information about a student
    Returns some connections between the story and the student as a string
    '''
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

# not currently in use
def robotConnections(plot, characters, motivations, robotBio):
    '''
    Creates links between the plot and the robot
    plot: (str) key plot events
    characters: (str) a list of characters
    motivations: (str) some details about why a character is doing what they are, or the plot is focused on what it is
    robotBio: (str) some basic information about the robot / backstory
    Returns some connections between the story and the robot as a string
    '''
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
    '''
    Generates a list of questions to ask the students
    inputs: (str) any information about the story, can include plot points, motivations, characters, etc
    studentBio: (str) Optional information about student
    Returns string containing a list of questions 
    '''
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

def generateObservations(inputs,studentInfo=""):
    '''
    Generates a list of observations about the story and/or the student
    inputs: (str) any information about the story, can include plot points, motivations, characters, etc
    studentBio: (str) Optional information about student
    Returns string containing a list of observations
    '''
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

# not currently in use
def rankQuestions(questions):
    '''
    Reorders the questions based on importance 
    questions: (str) a list of questions
    Returns string containing a list of questions 
    '''
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Reorder the following questions by importance, given an objective of inciting reflection."},
        {"role": "system", "content": questions},
    ],
    temperature= 0.2
    )
    return completion.choices[0].message.content

def translate(text, targetLanguage="Dutch"):
    '''
    Translates text to a target language
    text: (str) the text to be translated
    targetLanguage: (str) the language in which the output should be, Dutch by default
    Returns string containing translated text
    '''
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"Translate the following text to {targetLanguage}, in words that an eight year old might use."},
        {"role": "system", "content": text},
    ],
    temperature= 0.2
    )
    return completion.choices[0].message.content

def pipeline(summary, text, studentName, NEW_TEXT=True, NEW_STUDENT=True):
    '''
    Generates questions based on a summary and the name/ id of the student, running all intermediate functions
    summary: (str) a text summary of a section of a book
    text: (str) the name or id of a book for naming the checkpoint files
    studentName: (str) name/id of student
    NEW_TEXT: (bool) false if motivations and plot checkpoints already exist, true to generate new ones, true by default
    NEW_STUDENT: (bool) false if student connection to plot already exists, true to generate new one, true by default
    Returns string containing questions
    '''
    if NEW_TEXT:
        save("characters", text,characters(summary))
        save("motivations", text,motivations(summary))
        save("plotPoints", text,plotPoints(summary))

    char= get("characters", text)
    moti= get("motivations", text)
    plot= get("plotPoints", text)

    student= get_student_data(studentName)
    if NEW_TEXT or NEW_STUDENT:
        save("studentConnection", text, studentConnections(plot,char,moti,student))
    connect = get("studentConnection", text)

    return generateQuestions(plot + moti+ char, student+connect)

# not currently in use
def superPrompt(inputs,studentInfo=""):
    '''
    TODO: create a single GPT call to generate questions
    returns a string containing questions
    '''
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
