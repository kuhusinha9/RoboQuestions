import json
 
'''
TODO: Info change
- no names
-id
-hobbies
-pets
-  ?? ethnicity
- fav food
- ? what do you do on a happy day
- fav books
- gender
- fav themes
- fav subject

TODO: work in dutch from summary stage
'''


# Opening JSON file
f = open('data/students.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)

def get_student_data(name):
    try:
        temp=data['students']['student'][name]
        
        # base script
        base = f"{name} is {temp['age']}. They like {temp['hobby']}. They like reading {temp['favGenre']} books. "

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
        return f"You have no information about {name}."

# Closing file
f.close()
