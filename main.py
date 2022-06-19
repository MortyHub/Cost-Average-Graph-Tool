import os

# Sends an error to the user of the program
def error(text="Unknown Problem Has Occured"):
    print(f"Error: {text}")

# Checks if a file is an existing one as a replacement for a long contents list
def CheckIfValid(name):
    try:
        with open(f'data/{name}.txt', 'x') as c:
            c.close()
        os.remove(f"data/{name}.txt")
        return False
    except:
        return True

# Creating a data File in /data
def add(name=None):
    global contents
    if name == None:
        error("Name Not Specified")
        return
    try:
        with open(f"data/{name}.txt", "x") as f:
            f.write('0')
    except:
        error("Unable To Create Data Holder")
# Adds things into the file
def addContents(name,contents):
    if CheckIfValid(name) == True:
        with open(f'data/{name}.txt', 'a') as f:
            f.write(f'{str(contents)}')

# Returns with the requested item(s)
def gatherContents(name,line):
    if CheckIfValid(name) == True:
        fileContents = open(f"data/{name}.txt")
        clock = fileContents.read()
        if line == "all":
            return clock
        else:
            return clock[line]
            
# Will clear the data of a data file
def clearData(name):
    if CheckIfValid(name) == True:
        with open(f'data/{name}.txt', 'r+') as file:
            file.truncate(0)
            



