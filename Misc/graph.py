
import pandas
def add_vertex (vertex):
    global graph
    global vertices
    global vertices_count

    if vertex not in vertices:
    #     print (f"{vertex} already exist")
    # else:
        vertices_count += 1
        vertices.append(vertex)
        vertices.sort()
        if vertices_count > 1:
            for v in graph:
                v.append (0)
        temp = []
        for i in range (vertices_count):
            temp.append(0)
        graph.append(temp)

def addEdge (v1,v2,e):
    global graph
    global vertices_count
    global vertices

    if v1 not in vertices:
        print (f"{v1} does not exist")
    elif v2 not in vertices:
        print (f"{v2} does not exist")

    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

def print_graph():
    global graph
    global vertices_count
    for i in range (vertices_count):
        for j in range(vertices_count):
            if graph[i][j] != 0:
                print (f"{vertices[i]} -> {vertices[j]}, edge = {graph[i][j]}")

graph = []
vertices = []
vertices_count = 0

with open ("graph.txt", 'r') as f:
    lines  = f.readlines()
    for line in lines:
        line = line.split()
        line = [x.strip() for x in line]
        print (line)
        add_vertex(line[0])
        add_vertex(line[1])
        addEdge(line[0], line[1], line[2])
        
print_graph()
print (pandas.DataFrame(graph))


        


