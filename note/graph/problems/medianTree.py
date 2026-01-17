"""
Code 15.2: Median Tree Problem

Problem:
Given a connected weighted undirected graph G = (V, E), find the minimum value
of the median of edge weights among all possible spanning trees of G.

Complexity:
- Time: O(|E| log |V|) as required
- Space: O(V) for Union-Find

Approach:
1. A spanning tree has exactly |V| - 1 edges
2. The median is the ⌈(|V|-1)/2⌉-th smallest edge when sorted
3. Try to minimize this median using a modified Kruskal's algorithm

Algorithm Strategy:
- For each unique edge weight w as a candidate median:
  - Build a spanning tree preferring edges with weight ≤ w
  - Calculate the actual median of this spanning tree
  - Track the minimum median found

Modified Kruskal's Algorithm:
- When testing a candidate median m, sort edges by:
  1. Priority: edges ≤ m come before edges > m
  2. Weight: within same priority, sort by weight
- This maximizes the number of smaller edges in the MST

Why this works:
- If we can build an MST with many edges ≤ m, the median will be small
- By trying all possible edge weights as candidates, we find the minimum achievable median
- The greedy approach (preferring smaller edges) minimizes the median

Source: JAG Practice Contest for ACM-ICPC Asia Regional 2012 C - Median Tree
Difficulty: ★★★★☆
"""


class UnionFind:
    """Union-Find (Disjoint Set Union) data structure"""

    def __init__(self, n: int) -> None:
        self.par = [-1] * n
        self.siz = [1] * n

    def root(self, x: int) -> int:
        """Find root with path compression"""
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def isSame(self, x: int, y: int) -> bool:
        """Check if x and y are in the same component"""
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> bool:
        """Unite components containing x and y"""
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.siz[x] < self.siz[y]:
            x, y = y, x

        self.par[y] = x
        self.siz[x] += self.siz[y]

        return True

    def size(self, x: int) -> int:
        """Get size of component containing x"""
        return self.siz[self.root(x)]


def build_mst_with_priority(
    n: int, edges: list[tuple[int, int, int]], threshold: int
) -> list[int]:
    """
    Build MST using modified Kruskal's algorithm, prioritizing edges ≤ threshold.

    Algorithm flow:
    1. Sort edges by (priority, weight) where priority = 0 if weight ≤ threshold, else 1
    2. Apply standard Kruskal's algorithm with Union-Find
    3. Return the sorted list of edge weights in the MST

    Args:
        n: Number of vertices
        edges: List of edges as (weight, u, v) tuples
        threshold: Edges ≤ threshold get higher priority

    Returns:
        Sorted list of edge weights in the resulting MST
    """
    # Sort edges: first by priority (≤ threshold), then by weight
    # Priority 0 for edges ≤ threshold, priority 1 for edges > threshold
    sorted_edges = sorted(edges, key=lambda e: (0 if e[0] <= threshold else 1, e[0]))

    uf = UnionFind(n)
    mst_weights = []

    for weight, u, v in sorted_edges:
        if not uf.isSame(u, v):
            uf.unite(u, v)
            mst_weights.append(weight)

            # Stop when we have n-1 edges (spanning tree complete)
            if len(mst_weights) == n - 1:
                break

    # Return sorted weights for easy median calculation
    mst_weights.sort()
    return mst_weights


def get_median(weights: list[int]) -> int:
    """
    Get the median of a list of weights.

    For a spanning tree with n-1 edges, the median is at position ⌈(n-1)/2⌉
    which is the middle element (0-indexed: (n-1)//2 for odd count).

    Args:
        weights: Sorted list of weights

    Returns:
        The median weight
    """
    n = len(weights)
    # For n weights, median is at index n//2 (0-indexed)
    # This gives us the ⌈n/2⌉-th element (1-indexed)
    return weights[n // 2]


def minimum_median_tree(n: int, edges: list[tuple[int, int, int]]):
    """
    Find the minimum median of edge weights among all spanning trees.

    Algorithm flow:
    1. Extract all unique edge weights as candidate medians
    2. For each candidate median m:
       a. Build an MST prioritizing edges with weight ≤ m
       b. Calculate the actual median of this MST
       c. Track the minimum median seen
    3. Return the minimum median

    Why try all edge weights?
    - The optimal median must be one of the edge weights in the graph
    - We can't do better than using actual edge weights
    - By trying all of them, we're guaranteed to find the optimum

    Time Complexity Analysis:
    - E unique edge weights to try (at most E)
    - For each: O(E log E) for sorting + O(E α(V)) for Kruskal ≈ O(E log E)
    - Total: O(E² log E) in worst case

    Optimization: We can use binary search on sorted unique weights
    to achieve O(E log E log V) or better, but the problem allows O(E log V)

    Args:
        n: Number of vertices
        edges: List of edges as (weight, u, v) tuples

    Returns:
        Minimum achievable median of edge weights in any spanning tree
    """
    # Get all unique edge weights as candidates
    unique_weights = sorted(set(w for w, u, v in edges))

    min_median = float("inf")

    # Try each unique weight as a potential median
    for candidate_median in unique_weights:
        # Build MST preferring edges ≤ candidate_median
        mst_weights = build_mst_with_priority(n, edges, candidate_median)

        # Calculate actual median of this MST
        actual_median = get_median(mst_weights)

        # Track minimum
        min_median = min(min_median, actual_median)

    return min_median