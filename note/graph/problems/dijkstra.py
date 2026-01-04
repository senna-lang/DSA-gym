"""
Code 14.3 Implementation of Dijkstra's Algorithm

An efficient algorithm for finding the shortest path in a graph with non-negative weights.
Based on the greedy approach.

Complexity: O((V + E) log V)
- V: Number of vertices
- E: Number of edges
- Fastened using a priority queue

Difference from Bellman-Ford algorithm:
- Bellman-Ford: O(VE), supports negative weights, detects negative cycles
- Dijkstra: O((V+E)logV), no negative weights allowed, faster
"""

import heapq

INF = float("inf")


class Edge:
    """Class representing an edge (weighted directed edge)"""

    def __init__(self, to: int, weight: int):
        self.to = to  # Index of the adjacent vertex
        self.weight = weight  # Weight of the edge

    def __repr__(self):
        return f"Edge(to={self.to}, w={self.weight})"


Graph = list[list[Edge]]


def chmin(a: list[float], index: int, b: float) -> bool:
    """
    Function to perform relaxation.
    Updates a[index] with min(a[index], b) and returns True if updated.

    Args:
        a: Array to be updated
        index: Index of the element to update
        b: Value to compare with

    Returns:
        True if an update occurred, False otherwise
    """
    if a[index] > b:
        a[index] = b
        return True
    return False


def dijkstra(graph: Graph, start: int) -> list[float]:
    """
    Finds the single-source shortest path using Dijkstra's algorithm.

    Algorithm flow:
    1. Initialize dist[start] = 0, and others to INF
    2. Add (0, start) to the priority queue (heap)
    3. Pop (d, v) from the queue
    4. If d > dist[v], it's old information, so skip it
    5. Relax edges from vertex v
    6. Repeat until the queue is empty

    Why is it faster than Bellman-Ford?
    - Processes vertices in order of "settled" distance (greedy approach)
    - Always selects the vertex with the minimum distance using a priority queue
    - Each vertex is processed only once (old information is skipped)

    Why doesn't it work with negative weights?
    - Once a vertex's distance is settled, it's never updated again
    - If there are negative edges, a shorter path might be found later
    - Therefore, the premise of the greedy approach fails

    Args:
        graph: Weighted directed graph (adjacency list representation)
        start: Starting vertex

    Returns:
        List of shortest distances to each vertex
    """
    N = len(graph)

    # Initialize distance array
    dist = [INF] * N
    dist[start] = 0

    # Priority queue: pairs of (distance, vertex index)
    # Python's heapq is a min-heap
    pq = [(dist[start], start)]

    # Start Dijkstra's algorithm iterations
    while pq:
        # v: Vertex with the minimum dist[v] among unprocessed vertices
        # d: Key value (distance) for v
        d, v = heapq.heappop(pq)

        # d > dist[v] means (d, v) is stale (garbage)
        # A better distance has already been found
        if d > dist[v]:
            continue

        # Relax each edge starting from vertex v
        for edge in graph[v]:
            # Relaxation process
            if chmin(dist, edge.to, dist[v] + edge.weight):
                # If updated, push the new distance to the heap
                # (dist[edge.to], edge.to) is the current shortest distance to start edge
                heapq.heappush(pq, (dist[edge.to], edge.to))

    return dist
