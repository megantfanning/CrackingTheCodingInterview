#Singlely Linked List

class Node:
    def __init__(self,value):
        self.value = value
        self.nextNode = None

class LinkedList:
    def __init__(self, value):
        aNode = Node(value)
        self.head = aNode
        self.tail = aNode
    
    def push(self, value):
        aNode = Node(value)
        self.tail.nextNode = aNode
        self.tail = aNode        

    def returnHead(self):
        return self.head

    def returnTail(self):
        return self.tail

    def getNext(self, aNode):
        return aNode.nextNode

    def pop(self):
        current = self.returnHead
        while current.nextNode.nextNode != None :
            current = current.nextNode
        self.tail = current

    def getLengthLL(myLL):
        count = 0
        currentNode = self.head
        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode
            #print(currentNode.value)
            count += 1
        return count   


