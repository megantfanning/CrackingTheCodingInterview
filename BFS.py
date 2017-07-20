#! /usr/bin/python
import queue

#Breadth First Search
def breadthFirstSearch(Graph, root,goal):
    S = set()
    Q = queue.Queue()      

    S.add(root)
    Q.put(root)                      
    empty = queue.Queue()
    while not Q.empty():
        print("-")
        current = Q.get()
        if current == goal:
            print("Goal found")
            return current
        for n in graph[current]:
            #print(n)
            #if n is not in S
            if n not in S:
                S.add(n)
                print(n)
                #n.parent = current
                Q.put(n)


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

goal = breadthFirstSearch(graph,'A','F')
print(goal)

