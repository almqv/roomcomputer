import sys

def getValueOfKey(key): # get the value of an input key, example: -c {VALUE}
    for i in sys.argv:
        if( i == key ):
            return sys.argv[sys.argv.index(key) + 1]
    return -1 # if no value was found return -1

def inputHasKeys(keyList):
    return all(key in sys.argv for key in keyList)
