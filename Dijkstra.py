graph = {
    'a':{'b':10, 'c':3},
    'b':{'c':1, 'd':2},
    'c':{'b':4, 'd':8, 'e':2},
    'd':{'e':7},
    'e':{'d':9}
}

def dijkstra(graph, start_node, end_node):
    shortest_dist = {}
    predecessor = {}
    unseen_nodes = graph
    large_number = 1_000_000_000
    path = []

    for node in unseen_nodes:
        shortest_dist[node] = large_number
    shortest_dist[start_node] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_dist[node] < shortest_dist[min_node]:
                min_node = node
        
        for child_node, weight in graph[min_node].items():
            if weight + shortest_dist[min_node] < shortest_dist[child_node]:
                shortest_dist[child_node] = weight + shortest_dist[min_node]
                predecessor[child_node] = min_node
        unseen_nodes.pop(min_node)
    
    current_node = end_node
    while current_node != start_node:
        try:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        except:
            print()
            print('Path not reachable')
            print()
            break
    path.insert(0, start_node)
    
    if shortest_dist[end_node] != large_number:
        print()
        print('Shortest distance: ', shortest_dist[end_node])
        print('Path: ', path)
        print()

dijkstra(graph, 'a', 'd')