import heapq

# Initialize the structure of the graph with their connecting nodes and their costs here
graph = {
    'A': {'B': 1, 'T': 5},
    'B': {'A': 1, 'C': 2},
    'C': {'B': 2, 'D': 7},
    'D': {'C': 7, 'E': 2, 'F': 3, 'G': 5, 'H': 4, 'I': 6, 'J1': 8, 'J2': 9, 'K': 10, 'L': 7, 'U': 11},
    'E': {'D': 2, 'F': 2, 'G': 4, 'H': 3, 'I': 5, 'J1': 7, 'J2': 8, 'K': 9, 'L': 6, 'O': 3, 'U': 10},
    'F': {'D': 3, 'E': 2, 'G': 3, 'H': 2, 'I': 4, 'J1': 6, 'J2': 7, 'K': 8, 'L': 5, 'U': 9},
    'G': {'D': 5, 'E': 4, 'F': 3, 'H': 2, 'I': 2, 'J1': 4, 'J2': 5, 'K': 6, 'L': 3, 'U': 7},
    'H': {'D': 4, 'E': 3, 'F': 2, 'G': 2, 'I': 3, 'J1': 5, 'J2': 6, 'K': 7, 'L': 4, 'U': 8},
    'I': {'D': 6, 'E': 5, 'F': 4, 'G': 2, 'H': 3, 'J1': 3, 'J2': 4, 'K': 5, 'L': 2, 'U': 6},
    'J1': {'D': 8, 'E': 7, 'F': 6, 'G': 4, 'H': 5, 'I': 3, 'J2': 2, 'K': 3, 'L': 2, 'N': 4, 'U': 4},
    'J2': {'D': 9, 'E': 8, 'F': 7, 'G': 5, 'H': 6, 'I': 4, 'J1': 2, 'K': 2, 'L': 3, 'U': 3},
    'K': {'D': 10, 'E': 9, 'F': 8, 'G': 6, 'H': 7, 'I': 5, 'J1': 3, 'J2': 2, 'L': 4, 'U': 2},
    'L': {'D': 7, 'E': 6, 'F': 5, 'G': 3, 'H': 4, 'I': 2, 'J1': 2, 'J2': 3, 'K': 4, 'U': 5},
    'M': {'N': 2, 'O': 4, 'S': 6},
    'N': {'J1': 4, 'M': 2, 'O': 3, 'S': 5},
    'O': {'E': 3, 'N': 3, 'M': 4, 'S': 3},
    'P': {'S': 1},
    'Q': {'R': 2, 'S': 2, 'T': 5},
    'R': {'Q': 2, 'S': 4, 'T': 3},
    'S': {'M': 6, 'N': 5, 'O': 3, 'P': 1, 'Q': 2, 'R': 4, 'T': 6},
    'T': {'A': 5, 'Q': 5, 'R': 3, 'S': 6},
    'U': {'D': 11, 'E': 10, 'F': 9, 'G': 7, 'H': 8, 'I': 6, 'J1': 4, 'J2': 3, 'K': 2, 'L': 5}
}

# Helper function to estimate heuristic values less than actual path costs
def calculate_heuristics(goal):
    heuristic_values = {node: float('inf') for node in graph}  # Default heuristic values set to infinity

    # Breadth-First Search (BFS) to calculate path costs to the goal
    def bfs_heuristics(goal):
        visited = []
        queue = [(goal, 0)]  # Format: (node, cumulative cost to goal)

        while queue:
            current_node, cumulative_cost = queue.pop(0)

            if current_node not in visited:
                visited.append(current_node)
                # Update heuristic value with a value slightly less than the real cost to goal
                heuristic_values[current_node] = max(0, cumulative_cost - 0.5)  # Ensures positive heuristic values

                # Traverse neighbors to calculate their heuristic costs
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        # Get the cost of moving from the neighbor to the current node
                        cost_to_goal = graph[neighbor].get(current_node, float('inf'))
                        queue.append((neighbor, cumulative_cost + cost_to_goal))

    bfs_heuristics(goal)
    return heuristic_values

# Helper function to calculate total path cost from the path found in GBFS
def calculate_total_path_cost(graph, path):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += graph[path[i]][path[i + 1]]
    return total_cost

# Greedy Best-First Search Algorithm
def GBFS(graph, start, goal, heuristics, closed_nodes):
    queue = [(heuristics[start], start, [start])]  # Format: (heuristic value, current node, path to current node)
    visited = []  # To keep track of already visited nodes

    while queue:
        # Sort by heuristic value (ascending)
        queue.sort(key=lambda x: x[0])
        (heuristic_value, node, path) = queue.pop(0)

        # Do not evaluate closed nodes (if there is any)
        if node in closed_nodes:
            continue

        if node not in visited:
            visited.append(node)
            print(f"Evaluating node {node} with heuristic value: {heuristic_value}")

            if node == goal:
                total_cost = calculate_total_path_cost(graph, path)
                return path, total_cost

            # Add unvisited neighbors to the queue with their heuristic values
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((heuristics[neighbor], neighbor, path + [neighbor]))

    # No path found
    return None, None

def DFS(graph, start, goal, closed_nodes):
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

def BFS(graph, start, goal, closed_nodes):
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

    # No path found
    return None

def UCS(graph, start, goal, closed_nodes):
    queue = [(0, start, [start])]  # Format = (Total cost, current node, path to current node)
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue) # gets the node with the lowest cost

        if node in closed_nodes:
            continue

        if node not in visited:
            visited.add(node)
            print(f"Evaluating: {node} with total cost: {cost}")

            if node == goal:
                return path, cost

            # Explore neighbors
            for neighbor, edge_cost in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + edge_cost, neighbor, path + [neighbor]))

    return None, None

# Function to find a path based on selected algorithm
def find_path(algo, graph, start, goal, closed_nodes):
    if algo == 1:
        print("\nDepth First Search (DFS)")
        return DFS(graph, start, goal, closed_nodes), None
    elif algo == 2:
        print("\nBreadth First Search (BFS)")
        return BFS(graph, start, goal, closed_nodes), None
    elif algo == 3:
        print("\nUniform Cost Search (UCS)")
        path, cost = UCS(graph, start, goal, closed_nodes)
        return path, cost
    elif algo == 4:
        print("\nGreedy Best First Search (GBFS)")
        heuristics = calculate_heuristics(goal)
        print(f"Heuristic Values: {heuristics}")
        path, cost = GBFS(graph, start, goal, heuristics, closed_nodes)
        return path, cost
    else:
        print("Invalid algorithm selection")
        return None, None

def main():
    #********************************************--USER INPUTS--**********************************************#
    start = input("Enter the starting node: ").upper()
    goal = input("Enter the goal node: ").upper()
    closed_nodes = input("Enter closed nodes (comma separated, or leave blank if none): ").upper().split(',')

    algo = int(input("\nChoose an Algorithm (enter number): \n1 Depth First Search (DFS) \n2 Breadth First Search (BFS) \n3 Uniform Cost Search (UCS)\n4 Greedy Best First Search (GBFS)\n"))
    #*********************************************************************************************************#

    closed_nodes = [node.strip() for node in closed_nodes if node.strip() != '']
    print(f"Closed Nodes: {closed_nodes}")

    path, cost = find_path(algo, graph, start, goal, closed_nodes)

    if path:
        print(f"\nPath from {start} to {goal}: {' -> '.join(path)}")
        if cost is not None:
            print(f"Total path cost: {cost}")
    else:
        print(f"\nNo path found from {start} to {goal}.")


if __name__ == "__main__":
    main()
    input("\nEnter any key to exit.")