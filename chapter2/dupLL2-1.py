import LL

#initialize a LL
myLL = LL.LinkedList(0)
for i in range(1,10):
    myLL.push(i)

def printLL(myLL):
    #iterate through list
    current=myLL.returnHead()
    print(current.value)

    while myLL.getNext(current) != None:
        current = myLL.getNext(current)
        print(current.value)

    return myLL

def duplicateRemover(myLL):
    current=myLL.getNext(myLL.returnHead())
    #print(current.value)
    pointer=myLL.returnHead()
    while current != pointer:
        while myLL.getNext(current) != None:
            current = myLL.getNext(current)
            #print(current.value)
            if current.nextNode == None:
                print("bah")  
            elif current.nextNode.value == pointer.value:
                print(current.value)
                print(pointer.value)
                #remove duplicate
                current.nextNode = current.nextNode.nextNode
            else:
                print("boo")
        pointer = myLL.getNext(pointer)
    return myLL


printLL(myLL)
print("--")
duplicateRemover(myLL)
print("--")
printLL(myLL)
