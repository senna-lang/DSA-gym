"""
Problem 14.3: Hopscotch Addict (ケンケン)

Find the minimum path length from s to t where the path length is divisible by 3.

Algorithm:
Extended Dijkstra with state (vertex, path_length % 3)
- State: (v, mod) where mod = current path length mod 3
- For each edge, update dist[next_v][(current_mod + 1) % 3]
- Answer: dist[t][0] (reaching t with path length ≡ 0 mod 3)

Complexity: O((V + E) log V)
- Same as Dijkstra but with 3 states per vertex
"""

import heapq

INF = float("inf")


class Edge:
    """Class representing an edge (weighted directed edge)"""

    def __init__(self, to: int, weight: float):
        self.to = to
        self.weight = weight

    def __repr__(self):
        return f"Edge(to={self.to}, w={self.weight})"


Graph = list[list[Edge]]


def chmin(a: list[float], index: int, b: float) -> bool:
    """
    Function to perform relaxation.
    Updates a[index] with min(a[index], b) and returns True if updated.
    """
    if a[index] > b:
        a[index] = b
        return True
    return False


def dijkstra(graph: Graph, start: int) -> list[float]:
    """
    Finds the single-source shortest path using Dijkstra's algorithm.
    """
    N = len(graph)
    dist = [INF] * N
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        d, v = heapq.heappop(pq)

        # Skip stale entries
        if d > dist[v]:
            continue

        for edge in graph[v]:
            if chmin(dist, edge.to, dist[v] + edge.weight):
                heapq.heappush(pq, (dist[edge.to], edge.to))

    return dist


def hopscotch_addict(graph: Graph, s: int, t: int) -> float:
    """
    Problem 14.3: Find minimum path length from s to t where length is divisible by 3

    Args:
        graph: Unweighted directed graph (adjacency list)
        s: Starting vertex
        t: Target vertex

    Returns:
        Minimum path length from s to t that is divisible by 3,
        or -1 if no such path exists
    """
    N = len(graph)

    # dist[v][mod] = minimum number of edges to reach v with (path_length % 3 == mod)
    dist = [[INF] * 3 for _ in range(N)]
    dist[s][0] = 0

    # Priority queue: (distance, vertex, mod)
    pq = [(0, s, 0)]

    while pq:
        d, v, mod = heapq.heappop(pq)

        # Skip stale entries
        if d > dist[v][mod]:
            continue

        # Relax edges
        for edge in graph[v]:
            next_v = edge.to
            # Moving to next vertex increases path length by 1
            next_mod = (mod + 1) % 3
            next_dist = d + 1

            if dist[next_v][next_mod] > next_dist:
                dist[next_v][next_mod] = next_dist
                heapq.heappush(pq, (next_dist, next_v, next_mod))

    # We want to reach t with path length divisible by 3 (mod = 0)
    result = dist[t][0]
    return result if result != INF else -1
