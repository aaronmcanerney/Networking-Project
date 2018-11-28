To run python networkSim.py

Need to have matplotlib installed
Need to have networkx installed

The program creates a network of 17 nodes and reads in the edges from edges.txt.
After the graph is created, 1-5 nodes are chosen to fail. On failure, thier corresponding edges are saved,
they are removed from the graph, and an all pairs shortest path is run on the new graph.

After the path is unpacked, the remaining edges consituting a connected network are highlighted in blue
and the edges that were affected by the node failure are highlighted in red.

The animation is updated every 7 seconds, with new failures each time.

