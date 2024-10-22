# Initialize the structure of the graph with their connecting nodes here
import heapq
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
    'T': {'A': 5, 'S': 7},
    'U': {'D': 12, 'E': 11, 'F': 10, 'G': 8, 'H': 9, 'I': 7, 'J1': 5, 'J2': 4, 'K': 3, 'L': 6}
}


def ucs(graphwcost, start, goal, closed_nodes):
    queue = [(0, start, [start])]  # Format = (Total cost, current node, path to current node)
    visited = set() 

    while queue:
        cost, node, path = heapq.heappop(queue) # gets the node with the lowest cost

        if node in closed_nodes:
            continue

        print(f"Evaluating: {node} with total cost: {cost}")

        if node not in visited:
            visited.add(node)

            if node == goal:
                return path

            # Explore neighbors
            for neighbor, edge_cost in graphwcost[node].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + edge_cost, neighbor, path + [neighbor]))

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
    path = ucs(graphwcost, start, goal, closed_nodes)

    if path:
        print(f"Path from {start} to {goal}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {goal}.")


if __name__ == "__main__":
    main()
