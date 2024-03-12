# RoboQuestions

This code is for generating questions for a robot reading companion
## Requirements
### Libraries
- [ ] openai
- [ ] dotenv
### Other
A .env file with an API key for openAI
This should be formatted as such-

OPENAI_API_KEY = 'your_key_here'

## How to run
 `python main.py`
 Then enter the name of a student and a filename from the stories folder.
 Enter any additional information
 The results currently save in output.txt
 Dutch story text generates questions in dutch.

## What is in each file or folder
### main.py
This is what is the main script to run

### steps.py
The subcomponents and API calls are in this file

### json_converster.py
This converts data in json files to string scripts

### data
This folder contains data about students or the robot

### stories
This folder contains the chapters, summaries or book texts
