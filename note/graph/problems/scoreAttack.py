def chmax(a: list[float], index: int, b: float) -> bool:
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
    if a[index] < b:
        a[index] = b
        return True
    return False


def scoreAttack(graph: list[list[tuple[int, int]]], start: int = 0):
    """
    Problem 14.2: Find maximum score in a graph (longest path problem)

    Similar to Bellman-Ford but maximizing instead of minimizing.
    If scores can grow infinitely (positive cycle), returns "inf".

    Algorithm:
    1. Run N-1 iterations to find longest paths
    2. Run N-th iteration to detect positive cycles

    Complexity: O(VE)

    Args:
        graph: Weighted directed graph (adjacency list with (to, weight) tuples)
        start: Starting vertex (default 0)

    Returns:
        Maximum score if finite, "inf" if infinite
    """
    N = len(graph)
    dist = [-float('inf')] * N
    dist[start] = 0

    # Run N iterations (similar to Bellman-Ford)
    for iter_count in range(N):
        update = False

        # Relax all edges
        for v in range(N):
            # Skip unreachable vertices
            if dist[v] == -float('inf'):
                continue

            for to, weight in graph[v]:
                if chmax(dist, to, dist[v] + weight):
                    update = True

        # Early termination if no updates
        if not update:
            break

        # N-th iteration detecting positive cycle
        if iter_count == N - 1 and update:
            return "inf"

    return max(dist)
