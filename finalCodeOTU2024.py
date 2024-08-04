#INFR2820U Final Project: EV Charging Route Optimization Application
#Group Members: Kenil Patel and Krupa Shah

##########################################################################################

#Import libraries
import networkx as nx
import matplotlib.pyplot as plt

#Create an empty graph
G = nx.Graph()

#List of nodes
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']

#Add nodes to the graph
G.add_nodes_from(nodes)

#Load edges
def loadEdges(filePath):
    with open(filePath, 'r') as file:
        #Read each lines in the text file
        for line in file:
            #Split each lines into node1, node2, and weight 
            node1, node2, weight = line.strip().split()
            #Add edge to edges list
            G.add_edge(node1, node2, weight=int(weight))

#Find shortest path to a charging station
def findShortestPath(startNode, chargingStations):
    shortestPath = {}
    #Shortest path to each charging station
    for station in chargingStations:
        path = nx.dijkstra_path(G, startNode, station, weight='weight')
        distance = nx.dijkstra_path_length(G, startNode, station, weight='weight')
        shortestPath[station] = (path, distance)
    return shortestPath

#Find smallest distance
def findClosestPath(shortestPath):
    closestPath = min(shortestPath, key=shortestPath.get)
    return closestPath

#Main function
def main():
    #Data file
    filePath = 'route_data.txt'
    loadEdges(filePath)

    #Charging stations list
    chargingStations = ['H', 'K', 'Q', 'T']
    #
    while True:
        startNode = input(f"Enter a starting location {nodes} or type 'exit' to end the code: ")
        #If user types "exit", end the program
        if startNode.lower() == 'exit':
            print("Exiting the code.")
            break
        #If user enters a different value ask them to enter the valid node
        if startNode not in nodes:
            print(f"Enter a valid node {nodes}.")
            continue

        #List of all the possible paths
        shortestPath = findShortestPath(startNode, chargingStations)

        #Print shortest paths
        for station, (path, distance) in shortestPath.items():
            print(f"Shortest path to station {station}:{path} with distance {distance}")

        #Prints out the path closest to the nearest charging station
        closestPath = findClosestPath(shortestPath)                                                         
        recommendedPath,recommendedDistance = shortestPath[closestPath]
        print(f"")
        print(f"Recommended Path: {closestPath}:{recommendedPath} with distance: {recommendedDistance}")

        #Graph layout
        pos = nx.spring_layout(G)
        #Get edge weights
        edgeLabels = nx.get_edge_attributes(G, 'weight')                                                    
        #Graph with edges and labels
        nx.draw(G, pos, with_labels=True, node_color='grey',node_size=500,edge_color='blue', font_size=12)
        #Display edge labels
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edgeLabels, font_color='red', font_size=12)

        #Highlights the recommended path in green
        if recommendedPath:
            #Creates a list of edges by pairing consecutive nodes in recommended path
            pathEdges = list(zip(recommendedPath, recommendedPath[1:]))    ###fix
            #Draws highlight on th graph
            nx.draw_networkx_edges(G, pos, edgelist=pathEdges, edge_color='green', width=5)  ###fix

        #Show plot
        plt.show()

#Run main function when script starts
if __name__== "__main__":
    main()

##########################################################################################
