# SWDV 660 Applied DevOps Week 1 Assignment
Developed by:  Sony Yang

## Requirement:
Compatible only on Windows PC.  

## Executable File: DiceApp
Using pyinstaller, I compiled a working app that works only on the Windows platform.  

## Packages and Dependencies
I used Random as a random integer generator and Tkinter for GUI.  

## What the app does
When users open the executable file, they will see a Windows with two buttons.  "Roll" or "Exit".  

By clicking "Roll", the user will see a random integer between 1-6 displayed on the window.  They can continue to click the "Roll" button to get a new integer.  

If user clicks "Exit", the program will close.  


## Using App from Repository


### Open App from Repository
After cloning the repository, you can run the program by navigating to the /dist folder, then open the "DiceApp" executable file.  

### Run App via python command
This is typically preferred if you want to make changes to the program for your own purpose.  

After cloning the repository, you need to make sure that all dependencies are installed properly. You can do the following.  

1. Open Command Prompt or Windows Powershell

2. CD into the directory.  For example:
```python
cd "C:\Users\Sony\Github\DiceAppRepository"
```

3. Use pipenv to install all the dependencies in this environment.  
```python
pipenv install
```
4. Run the app, by calling the main.py file in the virtual environment.  
```python
pipenv run python .\main.py
```
