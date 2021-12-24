import json


# converting list to string using iteration
def listToString(s): 
    
    # initialize an empty string 
    string = "" 
    
    # traverse in the string 
    for element in s:
        string += element 
    
    # return string 
    return string 


# JSON file 
f = open ('data.json', "r") 
  
# Reading from file 
data = json.loads(f.read()) 

print(listToString(data))

