#Graph unidirectional

class Node:
    def __init__(self,value):
        self.value = value
        self.nextNode = None

class Graph:
    def __init__(self, value):
        aNode = Node(value)
    
    def push(self, root, value):
        aNode = Node(value)
        root.nextNode = aNode
  
