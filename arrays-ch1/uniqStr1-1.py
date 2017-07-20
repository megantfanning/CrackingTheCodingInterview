#! /usr/bin/python
myStr=input("Give me a string")

def findUniqStr(myStr):
    dict = {}
    #check if each character is unique
    for i in myStr:
        if i in dict:
            return False
        else:
            dict[i] = 1
        print(dict)
    return True

print(findUniqStr(myStr))
#check if each character is unique don't us additional data structures.
