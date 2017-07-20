#https://www.hackerrank.com/challenges/ctci-making-anagrams
#Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

a = input().strip()
b = input().strip()

def number_needed(a, b):
    #pass
    total = len(a) + len(b)
    match = 0

    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i] == b[j]):
                match+=2
    return total-match

print(number_needed(a, b))
