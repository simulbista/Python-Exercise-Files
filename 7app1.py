import json
import difflib

from difflib import get_close_matches

data = json.load(open("7app1-data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
        # simul.title() returns Simul (first letter capital)
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
        # get_close_matches gets the list of closest matched beween the two parameters.
        # len(get_close_matches)>0 is true if the result has 1 or more values
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes & N if No!" % get_close_matches(w,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exist."
        else:
            return "Invalid entry!"
    else:
        return "The word doesn't exist."

word = input("Input the word you want to know the meaning of!")

output = translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
