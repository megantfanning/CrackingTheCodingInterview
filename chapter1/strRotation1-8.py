#given a function called isSubString determine if it's a rotation 
# of another string using only one call to is subString

ustr= input("Give me a string \n")
rotation=input("give me a possible rotation \n")

def isSubString(str1,str2):
    if str1 in str2:
        return True
    else:
        return False

def rotationChecker(str1, rotated):
    counter = 0
    if len(str1) == len(rotated):
        rotated += rotated
        return isSubString(str1,rotated)

print(rotationChecker(ustr,rotation))

