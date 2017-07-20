#determine if two strings are permutations

str1 = input("give me a string \n")
str2 = input("give me a possible permutation \n")
def permutation(str1,str2):
    if len(str1) != len(str2):
        return False
    strDict={}
    #make a dictionary from the first string
    for i in str1:
        if i in strDict:
            strDict[i]=strDict[i]+1
        else:
            strDict[i]=1
    
    for j in str2:
        if j in strDict:
            if strDict[j] > 0 :
                strDict[j]=strDict[j]-1
            else:
                return False
        else:
            return False
    return True


print(permutation(str1,str2))


