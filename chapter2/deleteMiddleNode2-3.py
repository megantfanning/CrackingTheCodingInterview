import LL
#delete middle node given only access to that node
#question what it there is an even number of nodes? or there is not a next node
def iteration(LL):
    count = 0
    currentNode = LL.head
    print("---")
    while currentNode.nextNode != None:
        currentNode = currentNode.nextNode
        print(currentNode.value)
        count += 1
    print("---")
    return count   

def removeMiddle(LL,current):
    #skip the middle node and add the node after middle as the new middle
    current.nextNode = current.nextNode.nextNode
    #if this is c we'd need to deallocate
    return LL

#initialize a LL
myLL = LL.LinkedList(1)
for i in range(1,6):
    myLL.push(i)

shorterLL = removeMiddle(myLL,myLL.head.nextNode.nextNode)

iteration(shorterLL)
