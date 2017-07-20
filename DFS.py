#! /usr/bin/python

#discovered= set()

def DFS(graph,start,goal, discovered=set()):
    if start not in discovered:
        discovered.add(start)

    if goal in discovered:
        return discovered
    else:
        for node in graph[start]:
            if node not in discovered:
                discovered.add(node)
                
                if DFS(graph,node,goal,discovered):
                    return discovered
    return False
            
                   

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B']),
         'F': set(['C'])}

end=DFS(graph,'A','E')
print("finished ")
print(end)
