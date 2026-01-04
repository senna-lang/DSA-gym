"""
Code 14.5 Implementation of Floyd-Warshall Algorithm

An algorithm for finding all-pairs shortest paths in a weighted graph.
Can handle negative weights and detect negative cycles.

Complexity: O(V^3)
- V: Number of vertices

Characteristics:
- Finds shortest paths between all pairs of vertices
- Can handle negative weights
- Can detect negative cycles
- Uses dynamic programming approach
- Simpler to implement than running Bellman-Ford V times

Comparison with other algorithms:
- Dijkstra: O((V+E)logV), single-source, no negative weights
- Bellman-Ford: O(VE), single-source, handles negative weights
- Floyd-Warshall: O(V^3), all-pairs, handles negative weights
"""

INF = float("inf")


def floydWarshall(edges: list[tuple[int, int, float]]) -> tuple[list[list[float]], bool]:
    """
    Finds all-pairs shortest paths using Floyd-Warshall algorithm.

    Algorithm flow:
    1. Initialize dp[i][j] with edge weights, dp[i][i] = 0
    2. For each intermediate vertex k:
       For each pair (i, j):
           dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    3. If dp[v][v] < 0 for any v, a negative cycle exists

    Why does this work?
    - dp[i][j] represents the shortest path from i to j
    - After k iterations, dp[i][j] is the shortest path using vertices 0..k as intermediates
    - By trying all intermediate vertices, we find the optimal path

    Why can it detect negative cycles?
    - Initially dp[v][v] = 0 (distance from v to itself)
    - If there's a negative cycle containing v, dp[v][v] becomes negative
    - This happens because we can go from v back to v with negative total weight

    Args:
        n: Number of vertices
        edges: List of edges as (from, to, weight) tuples

    Returns:
        (dp, has_negative_cycle) tuple
        - dp: 2D array where dp[i][j] is the shortest distance from i to j
        - has_negative_cycle: Whether a negative cycle exists
    """

    N = len(edges)
    # Initialize dp array with INF
    dp = [[INF] * N for _ in range(N)]

    # Distance from a vertex to itself is 0
    for v in range(N):
        dp[v][v] = 0

    # Set initial edge weights
    for a, b, w in edges:
        dp[a][b] = w

    # Floyd-Warshall main loop
    # k: intermediate vertex to consider
    for k in range(N):
        # i: starting vertex
        for i in range(N):
            # j: ending vertex
            for j in range(N):
                # Update shortest path from i to j through k
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    # Check for negative cycle
    # If dp[v][v] < 0, there's a negative cycle containing vertex v
    has_negative_cycle = False
    for v in range(N):
        if dp[v][v] < 0:
            has_negative_cycle = True
            break

    return dp, has_negative_cycle
