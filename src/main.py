# Initialize the structure of the graph with their connecting nodes here
graph = {
    'A': ['B', 'T'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'U'],
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
    'N': ['S'],
    'O': ['E', 'S'],
    'P': ['S'],
    'Q': ['S'],
    'R': ['S'],
    'S': ['M', 'N', 'O', 'P', 'Q', 'R', 'T'],
    'T': ['A', 'S'],
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

            if node == goal:
                return path

            # Sort neighbors alphabetically and add unvisited neighbors to the stack
            for neighbor in sorted(graph[node], reverse=True):
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
    path = dfs(graph, start, goal, closed_nodes)

    if path:
        print(f"Path from {start} to {goal}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {goal}.")


if __name__ == "__main__":
    main()
