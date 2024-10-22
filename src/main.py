import heapq

# Initialize the structure of the graph with their connecting nodes and their costs here
graph = {
    'A': {'B': 1, 'T': 5},
    'B': {'A': 1, 'C': 2},
    'C': {'B': 2, 'D': 7},
    'D': {'C': 7, 'U': 4},
    'E': {'O': 3, 'U': 4},
    'F': {'U': 4},
    'G': {'U': 4},
    'H': {'U': 4},
    'I': {'U': 4},
    'J1': {'N': 4, 'U': 4},
    'J2': {'U': 4},
    'K': {'U': 4},
    'L': {'U': 4},
    'M': {'S': 2},
    'N': {'J1': 4, 'S': 2},
    'O': {'E': 3, 'S': 2},
    'P': {'S': 2},
    'Q': {'S': 2},
    'R': {'S': 2},
    'S': {'M': 2, 'N': 2, 'O': 2, 'P': 2, 'Q': 2, 'R': 2, 'T': 2},
    'T': {'A': 5, 'S': 2},
    'U': {'D': 4, 'E': 4, 'F': 4, 'G': 4, 'H': 4, 'I': 4, 'J1': 4, 'J2': 4, 'K': 4, 'L': 4}
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