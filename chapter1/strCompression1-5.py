#return a1b2 unless orginal string would be same length the return orginal str

str1 = input("give me a string to compress \n")

def stringCompression(str1):
    compressedStr=""
    count = 0
    prevchr = "\00"    

    for ch in str1:
        if ch == prevchr:
            count += 1
        else:
            compressedStr += ch 
            compressedStr += str(count)
            count=0
            prevchr = ch

    if len(compressedStr) >= len(str1):
        return str1
    else:
        return compressedStr

print(stringCompression(str1))
                
