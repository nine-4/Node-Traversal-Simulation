import time
# Initialize the structure of the graph with their connecting nodes here
graph = {
    'A': ['B', 'T'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'U', 'E', 'F', 'H'],
    'E': ['O', 'U'],
    'F': ['U'],
    'G': ['U'],
    'H': ['U'],
    'I': ['U'],
    'J1': ['U', 'N'],
    'J2': ['U'],
    'K': ['U'],
    'L': ['U'],
    'M': ['S'],
    'N': ['J1','S'],
    'O': ['E', 'S'],
    'P': ['S'],
    'Q': ['S'],
    'R': ['S'],
    'S': ['M', 'N', 'O', 'P', 'Q', 'R', 'T'],
    'T': ['A', 'S', 'R', 'Q'],
    'U': ['D', 'E', 'F', 'G', 'H', 'I', 'J1', 'J2', 'K', 'L']
}


def dfs(graph, start, goal, closed_nodes):

    stack = [(start, [start])]  # Format = (current node, path to current node)
    visited = []  # To keep track of the already visited nodes

    while stack:
        (node, path) = stack.pop()

        # Do not evaluate closed nodes (if there is any)
        if node in closed_nodes:
            continue

        if node not in visited:
            visited.append(node)
            print(f"Evaluating: {node}")

            if node == goal:
                return path

            # Sort neighbors alphabetically and add unvisited neighbors to the stack
            for neighbor in sorted(graph[node], reverse=True):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    # No path found
    return None

def bfs(graph, start, goal, closed_nodes):
    queue = [(start, [start])]  # Format = (current node, path to current node)
    visited = []  # To keep track of the already visited nodes

    while queue:
        (node, path) = queue.pop(0)

        # Do not evaluate closed nodes (if there is any)
        if node in closed_nodes:
            continue

        if node not in visited:
            visited.append(node)
            print(f"Evaluating: {node}")

            if node == goal:
                return path

            # Sort neighbors alphabetically and add unvisited neighbors to the queue
            for neighbor in sorted(graph[node]):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    time.sleep(0.01)
            
    # No path found
    return None

# Function to find a path based on selected algorithm
def find_path(algo, graph, start, goal, closed_nodes):
    if algo == 1:
        print("Depth First Search (DFS)")
        return dfs(graph, start, goal, closed_nodes)
    elif algo == 2:
        print("Breadth First Search (BFS)")
        return bfs(graph, start, goal, closed_nodes)
    elif algo == 3:
        print("Greedy Best First Search (GBFS) - Not implemented yet")
        return "Not Here Yet"
    else:
        print("Invalid algorithm selection")
        return None

def main():
    #********************************************--USER INPUTS--**********************************************#
    start = input("Enter the starting node: ").upper()
    goal = input("Enter the goal node: ").upper()
    closed_nodes = input("Enter closed nodes (comma separated, or leave blank if none): ").upper().split(',')
    algo = int(input("Choose Algorithm: \n1 Depth First Search (DFS) \n2 Breadth First Search (BFS) \n3 Greedy Best First Search (GBFS)\n"))
    #********************************************************************************************************#

    closed_nodes = [node.strip() for node in closed_nodes if node.strip() != '']
    print(f"Closed Nodes: {closed_nodes}")

    # Simulate traversal
    # path = dfs(graph, start, goal, closed_nodes)

    path = find_path(algo, graph, start, goal, closed_nodes)

    if path:
        print(f"Path from {start} to {goal}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {goal}.")


if __name__ == "__main__":
    main()
