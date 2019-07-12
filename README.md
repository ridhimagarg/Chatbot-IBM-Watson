### Intro

  Connecting IBM Assistant with Python with simple GUI using tkinter.
  
  More about IBM assistant and how to build chatbot using IBM Watson read this -: [IBM Assistant](https://www.ibm.com/cloud/watson-assistant/). 
  
  Here using ibm_watson open source library for connecting IBM and Python is used to build this whole interface.
  
  More for demo see below images
  
  ### Dependencies
  ---
  #### Getting Started
  
  Requirements
  
  > Tkinter
  > Ibm_watson 
  > sqlite3
  > Pandas
  
  > Databse(SQLITE3) 
  
  In this library Sqlite is been used but you can use any othet too. If you want to download DB Browser for Sqlite for showing up all     tables, download it from [here](https://download.sqlitebrowser.org/SQLiteDatabaseBrowserPortable_3.11.2_English.paf.exe)
  
  You can just install all the required libraries using this command in command line 
  
  Tkinter and sqlite3 is standard library. You don't need to install it.
  
  You can either use these commands -:
  
  ``` 
  pip install pandas ibm_watson
  
  ```
  
  **OR**
  
  ```
  pip install requirements.txt
  
  ```
  
  ### How to use
  
  #### Setting up app.py
  
  You have to just clone this [repo](https://github.com/ri-dhimagarg1/ibm_deployment) or download this code and extract it.
  
  After cloning, just go this folder and go to **app.py**
  
  In **app.py** modify your credentials of ibm in the **CREDENTIALS THING** section.
  
  In IBM Assistant we have apikey, url.
  
  <img src='https://github.com/ri-dhimagarg1/ibm_deployment/blob/master/IBM1.PNG'>

Other details are also present like Assistant ID etc.

So, just launch your assistant and go to assistant tab. In that you will have options like setting in the right corner. Like below shown -:

<img src='https://github.com/ri-dhimagarg1/ibm_deployment/blob/master/ibm2.PNG'>

After that in settings go to API details tab. You will get all details.

You have to replace all these details in **app.py**







  
  
  
  
  
  
  
  
  
  
  
 
  
  
  
