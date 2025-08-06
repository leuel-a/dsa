from collections import deque, defaultdict
from typing import Optional, List


class Node:
    def __init__(self, val: int = 0, neighbors: List['Node'] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None: return None

        self.root = node.val
        self.graph = defaultdict(list)
        self.visited = set([node.val])

        queue = deque([node])
        while queue:
            curr_node = queue.popleft()

            for neighbour in curr_node.neighbors:
                self.graph[curr_node.val].append(neighbour)

                if neighbour.val not in self.visited:
                    self.visited.add(neighbour.val)
                    queue.append(neighbour)

        self.nodes = [Node() for _ in range(len(self.visited))]
        new_queue = deque([(node, None)])


        while new_queue:
            current_node, parent = new_queue.popleft()

            new_current_node = self.nodes[current_node.val - 1]
            if new_current_node.val == 0:
                new_current_node.val = current_node.val

            if parent is not None:
                new_parent_node = self.nodes[parent.val - 1]
                new_current_node.neighbors.append(new_parent_node)

            for neighbor in current_node.neighbors:
                if parent is not None and parent.val == neighbor.val:
                    continue
                
                new_neighbor = self.nodes[neighbor.val - 1]
                if new_neighbor.val == 0:
                    new_neighbor.val = neighbor.val
                    new_queue.append((neighbor, current_node))

                new_current_node.neighbors.append(new_neighbor)
        return self.nodes[self.root - 1]

