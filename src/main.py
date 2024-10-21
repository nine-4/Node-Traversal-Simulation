# Initialize the structure of the graph with their connecting nodes here
graphwcost = {
    'A': {'B': 1, 'T': 5},
    'B': {'A': 1, 'C': 2},
    'C': {'B': 2, 'D': 7},
    'D': {'C': 7, 'U': 12},
    'E': {'O': 3, 'U': 11},
    'F': {'U': 10},
    'G': {'U': 8},
    'H': {'U': 9},
    'I': {'U': 7},
    'J1': {'U': 5, 'N': 4},
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
    'T': {'A': 5, 'S': 7, 'R': 5, 'Q': 3},
    'U': {'D': 12, 'E': 11, 'F': 10, 'G': 8, 'H': 9, 'I': 7, 'J1': 5, 'J2': 4, 'K': 3, 'L': 6}
}


def dfs(graphwcost, start, goal, closed_nodes):

    stack = [(start, [start])]  # Format = (current node, path to current node)
    visited = []  # To keep track of the already visited nodes

    while stack:
        (node, path) = stack.pop()

        # Do not evaluate closed nodes (if there is any)
        if node in closed_nodes:
            continue

        print(f"Evaluating: {node}")
        if node not in visited:
            visited.append(node)

            if node == goal:
                return path

            # Sort neighbors alphabetically and add unvisited neighbors to the stack
            for neighbor in sorted(graphwcost[node], reverse=True):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    # No path found
    return None


def main():
    #********************************************--USER INPUTS--**********************************************#
    start = input("Enter the starting node: ").upper()
    goal = input("Enter the goal node: ").upper()
    closed_nodes = input("Enter closed nodes (comma separated, or leave blank if none): ").upper().split(',')
    #********************************************************************************************************#

    closed_nodes = [node.strip() for node in closed_nodes if node.strip() != '']
    print(f"Closed Nodes: {closed_nodes}")

    # Simulate traversal
    path = dfs(graphwcost, start, goal, closed_nodes)

    if path:
        print(f"Path from {start} to {goal}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {goal}.")


if __name__ == "__main__":
    main()
