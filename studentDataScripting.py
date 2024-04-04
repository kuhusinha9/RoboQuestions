import json
import csv
 
'''
TODO: Info change
-  ?? ethnicity
- ? what do you do on a happy day

TODO: work in dutch from summary stage
'''


# Opening JSON file
f = open('data/students.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)

def json_data(id):
    '''
    Generates text script based on json data about student
    id: student number for experiment purpose
    Returns string with data about student
    '''
    try:
        temp=data['students']['student'][id]
        
        # base script
        base = f"The student is {temp['age']}. They like {temp['hobby']}. They like reading {temp['favGenre']} books. "

        # siblings script
        num= len(temp['siblings'])
        s = ""
        if  num == 1:
            s = f"They have a sibling called {temp['siblings'][0]['name']} who is {temp['siblings'][0]['age']} years old. "
        elif num > 1:
            s = f"They have {num} siblings- "
            for i in range(num - 1):
                s = s + temp['siblings'][i]['name'] + " is " + temp['siblings'][i]['age'] + ", "
            s = s + "and " + temp['siblings'][num-1]['name'] + " is " + temp['siblings'][num-1]['age'] + ". "

        # pets script
        num= len(temp['pet'])
        p = ""
        if  num == 1:
            p = f"They have a {temp['pet'][0]['animal']} called {temp['pet'][0]['name']}. "
        elif num > 1:
            p = f"They have {num} pets- "
            for i in range(num - 1):
                p = p + "a "+ temp['pet'][i]['animal'] + " called " + temp['pet'][i]['name'] + ", "
            p = p + "and a " + temp['pet'][num-1]['animal'] + " called " + temp['pet'][num-1]['name']  + ". "

        final= base + s + p
        return final
    except KeyError:
        return f"You have no information about {id}."

# Closing file
f.close()

with open("data/students.csv", 'r') as f:
    dict_reader = csv.DictReader(f)
    list_of_dict = list(dict_reader)

def csv_data(id):
    '''
    Generates text script based on json data about student
    id: student number for experiment purposes
    Returns string with data about student
    '''
    try:
        student=list_of_dict[id]
    except KeyError:
        return f"You have no information about {id}."

    gender = student[' gender']
    g2 = ("His" if gender == "He" else "Her")
    base= f"The student is{student[' age']}. {gender} likes{student[' hobby1']},{student[' hobby2']} and{student[' hobby3']}.{gender} has a{student[' petsSpecies']} called{student[' petsName']}. {g2} favourite subject is{student[' favSubject']}.{gender} likes eating{student[' favFood']}. "
    book= f"{gender} likes reading{student[' favGenre']} books or books about{student[' favBookTopic']}. {g2} favourite books are{student[' favBook1']},{student[' favBook2']} and{student[' favBook3']}. "
    return base+book
