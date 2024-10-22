# Initialize the structure of the graph with their connecting nodes and their costs here
graph = {
    'A': {'B': 1, 'T': 5},
    'B': {'A': 1, 'C': 2},
    'C': {'B': 2, 'D': 7},
    'D': {'C': 7, 'U': 12},
    'E': {'O': 3, 'U': 11},
    'F': {'U': 10},
    'G': {'U': 8},
    'H': {'U': 9},
    'I': {'U': 7},
    'J1': {'N': 4, 'U': 5},
    'J2': {'U': 4},
    'K': {'U': 3},
    'L': {'U': 6},
    'M': {'S': 11},
    'N': {'J1': 4, 'S': 9},
    'O': {'E': 3, 'S': 4},
    'P': {'S': 2},
    'Q': {'S': 3},
    'R': {'S': 5},
    'S': {'M': 11, 'N': 9, 'O': 4, 'P': 2, 'Q': 3, 'R': 5, 'T': 7},
    'T': {'A': 5, 'S': 7},
    'U': {'D': 12, 'E': 11, 'F': 10, 'G': 8, 'H': 9, 'I': 7, 'J1': 5, 'J2': 4, 'K': 3, 'L': 6}
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
    print(f"HEURISTIC VALUES: {heuristic_values}")
    return heuristic_values


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
            print(f"Evaluating node {node}: {heuristic_value}")

            if node == goal:
                return path

            # Add unvisited neighbors to the queue with their heuristic values
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((heuristics[neighbor], neighbor, path + [neighbor]))

    # No path found
    return None

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

# Function to find a path based on selected algorithm
def find_path(algo, graph, start, goal, heuristics, closed_nodes):
    if algo == 1:
        print("Depth First Search (DFS)")
        return DFS(graph, start, goal, closed_nodes)
    elif algo == 2:
        print("Breadth First Search (BFS)")
        return BFS(graph, start, goal, closed_nodes)
    elif algo == 3:
        print("Greedy Best First Search (GBFS)")
        return GBFS(graph, start, goal, heuristics, closed_nodes)
    else:
        print("Invalid algorithm selection")
        return None

def main():
    #********************************************--USER INPUTS--**********************************************#
    start = input("Enter the starting node: ").upper()
    goal = input("Enter the goal node: ").upper()
    closed_nodes = input("Enter closed nodes (comma separated, or leave blank if none): ").upper().split(',')
    #********************************************************************************************************#

    algo = int(input("Choose Algorithm: \n1 Depth First Search (DFS) \n2 Breadth First Search (BFS) \n3 Greedy Best First Search (GBFS)\n"))
    #********************************************************************************************************#

    closed_nodes = [node.strip() for node in closed_nodes if node.strip() != '']
    print(f"Closed Nodes: {closed_nodes}")

    # Calculate dynamic heuristic values based on the goal
    heuristics = calculate_heuristics(goal)

    path = find_path(algo, graph, start, goal, heuristics, closed_nodes)

    if path:
        print(f"Path from {start} to {goal}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {goal}.")


if __name__ == "__main__":
    main()
