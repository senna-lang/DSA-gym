def longest_path_dag(graph: list[list[int]]) -> int:
    """
    14.1: Find the longest path in a DAG (Directed Acyclic Graph)

    Algorithm:
    1. Order vertices using topological sort
    2. Execute DP in that order

    Complexity: O(|V| + |E|)
    """
    N = len(graph)
    seen = [False] * N
    order = []

    # Topological sort (DFS post-order)
    def dfs(v: int):
        seen[v] = True

        for next_v in graph[v]:
            if seen[next_v]:
                continue

            dfs(next_v)

        order.append(v)

    # DFS from all vertices
    for v in range(N):
        if seen[v]:
            continue

        dfs(v)

    # Topological order (reversed)
    order.reverse()

    # DP: dp[v] = length of longest path starting from vertex v
    dp = [0] * N

    # Process in reverse topological order
    # Why re:reverse? 
    # We need dp[next_v] to already be computed when we calculate dp[v]
    for v in reversed(order):
        for next_v in graph[v]:
            dp[v] = max(dp[v], dp[next_v] + 1)

    return max(dp) if dp else 0
