# 4) write code to parition a linked list around a value x 
# such that all nodes less than x come before all nodes greater than or equal to x
#sorting is one obvious choice here but perhaps not the fastest
import LL

#----------------------
#initialize a LL
myLL = LL.LinkedList(0)
for i in range(6,8):
    myLL.push(i)
for i in range(1,7):
    myLL.push(i)

def getLengthLL(myLL):
    count = 0
    currentNode = myLL.returnHead()
    while currentNode.nextNode != None:
       currentNode = currentNode.nextNode
       print(currentNode.value)
       count += 1
    print("----")
    return count   

getLengthLL(myLL)

#------------------

def partition(myLL,x):
    current = myLL.returnHead().nextNode
    previous = myLL.returnHead()
    head = myLL.returnHead()
    #if previous > x:
        #swap head and previous
    while current.nextNode != None:
        print(current.value)
        if current.value < x:
            #shift to head
            print("shift")
            previous.nextNode = current.nextNode
            current.nextNode = head
            myLL.head = current
            current = previous.nextNode
        else:
            current = current.nextNode
        print(current.value)
        print("-")
    return myLL

newList = partition(myLL,5)
getLengthLL(newList)

