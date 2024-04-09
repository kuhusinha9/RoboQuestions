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

### studentDataScripting.py
This converts data in json or csv files to string scripts

### file_handling.py
This contains functions for saving or working with existing data or checkpoints

### tests.py
alternate to main.py for experimentation

### outputs
This folder contains function outputs for final use

### data
This folder contains data about students or any other data files

### stories
This folder contains the chapters, summaries or book texts
