import networkx as nx
import matplotlib.pyplot as plt
import random
import matplotlib.animation
import copy
import itertools

#nx graph object to be used by the whole file
G = nx.Graph()
nodes = [x for x in range(1,18)]
G.add_nodes_from(nodes)
pos = nx.spring_layout(G)

#set inital node color
node_colors = ['blue' for x in range(1,18)]

# Build plot
fig, ax = plt.subplots(figsize=(8,6))

#graph edge init function
def edgeInit(edges):
    G.add_edges_from(edges) 

#create color list for all nodes in graph
def initNodeColor():
    return 

#initialize nx graph
def initGraph():
    edges = readEdgesFromFile()
    edgeInit(edges)
    
#read edges from a file... cus irwin fucking loves file i/o
def readEdgesFromFile():
    edges = [tuple(map(int, line.rstrip('\n').split(' '))) for line in open('edges.txt')]
    return edges

def calculateFailurePercentage():
    return random.randint(1,5)

# update function for graph animation
# runs shortest path on graph after failure and 
# updates the animation accordingly  
def updateGraph(num):
    #clear the fig
    ax.clear()

    #how many nodes fail on a given iteration
    number_of_failures = calculateFailurePercentage()

    failures = {random.randint(2,17) for x in range(0,number_of_failures)}
    #creaate a node failure
    #node_failure = random.randint(2,17)
    
    edges = []
    #make copy of edges to be reinserted
    for failure in failures:
        edges.append(copy.deepcopy(list(G.edges(failure))))

    #flatten list
    all_edges = list(itertools.chain(*edges))

    #remove the node from the graph
    G.remove_nodes_from(failures)

    #generate a shortest path from node 1 to all others
    path = dict(nx.all_pairs_shortest_path(G))
    

    #create edges of path fro coloring
    path_edges = createEdgesFromPath(path)

    #emplace node into graph
    G.add_nodes_from(failures)
   

    #show node failure
    for x in range(len(node_colors) - number_of_failures, len(node_colors)):
        node_colors[x] = 'red'

    #update the graph
    nx.draw_networkx_edges(G, pos=pos, edgelist = path_edges, width=4, alpha=0.2, edge_color='b')
    nx.draw_networkx_edges(G, pos=pos, edgelist = all_edges, width=2, alpha=0.3, edge_color='r')
    nx.draw(G, pos=pos,node_color = node_colors, with_labels=True,alpha=.8, font_weight='bold', ax=ax)

    #add title with node failure
    title = "Node failue at Node(s): " + ''.join(str(node) + ' ' for node in sorted(failures))
    ax.set_title(title, fontsize="8",fontweight="bold")

    #reset node for next iteration
    for x in range(len(node_colors) - number_of_failures, len(node_colors)):
        node_colors[x] = 'blue'
        
    #put edges back into graph for next iteration
    G.add_edges_from(all_edges)

#create edges from the single source shortest path
def createEdgesFromPath(path):
    all_edges = set()
    for key in path.keys():
        shortest = path[key]
        paths = shortest.values()
        for l in paths:
            if len(l) > 1:
                edges = [(x,y) for x,y in zip(l, l[1:])]
                for edge in edges:
                    all_edges.add(edge)

    return all_edges
    
#create the initial network graph
initGraph()

#produce animation
ani = matplotlib.animation.FuncAnimation(fig, updateGraph, frames=30, interval=9000, repeat=True)
plt.show()



