## Importing all the required libraries

## For creating UI
from tkinter import *
## For connecting ibm assistant from IBM Watson
import ibm_watson
## For fetchinf context variables
import json
## Importing data from chatbot to your local database file
import sqlite3
## For some manipulation
import pandas as pd



##----------------------------------------CREDENTIALS THING--------------------------------##
## Setting credentials of ibm assistant
service = ibm_watson.AssistantV2(iam_apikey='enter_your_apikey', version='version_date')

assistant_id = 'enter_assistant_id' # replace with assistant ID

# Create session.
session_id = service.create_session(
    assistant_id = assistant_id
).get_result()['session_id']


##-----------------------------------------Initializing Tkinter Frame--------------------------##


## Creating a window for tkinter
window = Tk()
window.title("Insurance Bot")
#window.configure(bg='black')

## Scrollbar in a window
scrollbar = Scrollbar(window)
scrollbar.pack( side = RIGHT, fill = Y )

## Message window for all messages to be displayed
messages = Text(window, yscrollcommand = scrollbar.set)
messages.pack()

## Synchronizing scrollbar with Text window
scrollbar.config(command = messages.yview)

## Entry box with label(message-> "Enter message") for message from user
label = Label(text="Enter message")
label.pack(side=LEFT)

input_user = StringVar()
input_field = Entry(window, text=input_user, width=60)
input_field.pack(side=LEFT)


##--------------------------------------------------INITIALIZING WITH CONVERSATION------------------------------------##

## This block so that first message from bot should come up and then following user message whole conversation goes on

# Initialize with empty value to start the conversation.


message_input = {
    'message_type:': 'text',
    'text': '',
    'options': {
            'return_context': True
        }
    } 

response = service.message(
        assistant_id,
        session_id,
        input = message_input
    ).get_result()


if response['output']['generic']:
        for e in response['output']['generic']:
            if e['response_type'] == 'text':
                messages.insert(INSERT, "BOT: %s\n" % e['text'])
            if e['response_type'] == 'option':
                messages.insert(INSERT, 'BOT: %s\n' %  e['title'])
                for opt in e['options']:
                    messages.insert(INSERT, 'BOT: %s\n' % opt['label'])




##------------------------------------------------CHATTING IBM AND TKINTER INTEGRATED---------------------------------------------##

## This is the event happen after pressing enter
## (whole chatting after first message from bot. i,e as user type some message this event will trigeer)

def Enter_pressed(event):

    ## Refrencing to the global variables so that updation should be done in global variable itself
    global message_input
    global response


    ## getting value entered in the entry box by user
    input_get = input_field.get()
    print(input_get)

    ## inserting that message into the text window
    messages.insert(INSERT, 'USER: %s\n' % input_get)

    ## Updating message_input for the next round of conversation
    message_type = response['output']['generic'][0]['response_type']
    message_input = {
        'message_type:': message_type,
        'text': input_get,
        'options': {
            'return_context': True
        }
        
    }
    
    ## Getting response from the updated message_input
    response = service.message(
        assistant_id,
        session_id,
        input = message_input
    ).get_result()


    ## This is just formatting the response from BOT and appending messages to Text window(messages)
    if response['output']['generic']:
            for e in response['output']['generic']:
                if e['response_type'] == 'text':
                    messages.insert(INSERT, 'BOT: %s\n' % e['text'])
                if e['response_type'] == 'option':
                    messages.insert(INSERT, 'BOT: %s\n' % e['title'])
                    messages.insert(INSERT, 'BOT: Choose among these -:\n')
                    for opt in e['options']:
                        messages.insert(INSERT, '\t %s\n' % opt['label'])
    

    input_user.set('')



##----------------------------------------------------------CALLING UP THE TKINTER FRAME---------------------------------------##
frame = Frame(window)  # , width=300, height=300)
## As the user press enter after inputing in the entry box, "Enter_pressed" function called up 
input_field.bind("<Return>", Enter_pressed)
frame.pack()

window.mainloop()

##How to connect to database, if you have context variables present in your BOT. How to store it
## Used sqlite for database
##---------------------------------------------DATABASE STUFF------------------------------------------------------##
print(json.dumps(response, indent=2))

## This will create a db if not exists
conn = sqlite3.connect("Chatbot-data.db")

c = conn.cursor()

# Create table - CLIENTS
c.execute('''CREATE TABLE USERS
             ([generated_id] INTEGER PRIMARY KEY, [A1] text, [A2] text)''')




## Storing context variables in variable for storing in a dataframe first and then dump into table USERS
## Replace "name_of_variable_in_your_bot" in below code with the name of your context variable
A1 = response['context']['skills']['main skill']['user_defined']['name_of_variable_in_your_bot']
A2 = response['context']['skills']['main skill']['user_defined']['name_of_variable_in_your_bot']



## Creating a dataframe for above variables
df = pd.DataFrame(columns=['A1','A2'])
df = df.append({'A2':A1,'A2':A2}, ignore_index=True)

## Pushing data from dataframe to USERS TABLE
df.to_sql('USERS', conn, if_exists='append', index = False)

## SQL statement just to fetch all data
c.execute('''SELECT * from USERS''')
print(c.fetchall())


# We're done, so we delete the session.
service.delete_session(
    assistant_id = assistant_id,
    session_id = session_id
)
