#! /usr/bin/python
import graph

#set up graph
graph= graph.Graph()

vertex = {'A','B','C','D','E','F'}
for v in vertex:
    graph.addVertex(v)

edges = {('A', 'B', 1),
         ('A','C', 2),
         ('B','D', 3),
         ('B','E', 2),
         ('C','F', 2)
        }

for e in edges :
    graph.addUndirectedEdge(e[0],e[1],e[2])


#breadth first +greedy
def dijkstras(graph, edges):
    #set up
    unvisited= queue.Queue()
    distance =[]

    #add each key to the unvisited queue
    for v in graph:
        unvisited.add(v)
        distance[v] = float("inf")
    
    current = unvisited.pop
    distance[current] = 0

    for neighbor in current:
        weight=[i for i in edges if current in i and neighbor in i]

        alt = distance[current] # edge current|neighbor
        if alt < distance[current] :
            distance[current]=alt
            #prev =neighbor

    return


