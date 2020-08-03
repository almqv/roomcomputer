eng_alphabet = *"abcdefghijklmnopqrstuvwxyz",
swe_alphabet = *"abcdefghijklmnopqrstuvwxyzåäö",

# Definitions
alphabet = dict()

alphabet["ENG"] = eng_alphabet
alphabet["SWE"] = swe_alphabet 

# Functions
def listToString( l ):
    returnStr = ""

    for char in l:
        returnStr += char

    return returnStr
