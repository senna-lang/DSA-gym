"""
Code 15.1: Implementation of Kruskal's Algorithm

A greedy algorithm for finding the Minimum Spanning Tree (MST) in a weighted undirected graph.
Uses Union-Find data structure to efficiently detect cycles.

Complexity:
- Time: O(E log E) where E is the number of edges
  - Sorting edges: O(E log E)
  - Union-Find operations: O(E α(V)) ≈ O(E
- Space: O(V) for Union-Find structure

Characteristics:
- Greedy algorithm: always selects the minimum weight edge that doesn't create a cycle
- Works on disconnected graphs (finds Minimum Spanning Forest)
- Edge-based approach (considers edges in sorted order)
- Uses Union-Find to efficiently detect cycles

Comparison with other MST algorithms:
- Prim's Algorithm: O((V+E) log V) with binary heap, vertex-based, better for dense graphs
- Kruskal's Algorithm: O(E log E), edge-based, better for sparse graphs
- Borůvka's Algorithm: O(E log V), can be parallelized

When to use:
- Sparse graphs (E << V²)
- When you need all edges in sorted order anyway
- When edges are already sorted or can be efficiently sorted
"""

import sys
import os

# Add the data-structure directory to the path to import UnionFind
sys.path.append(os.path.join(os.path.dirname(__file__), '../../data-structure/structures'))
from unionFind import UnionFind


def kruskal(n: int, edges: list[tuple[int, int, int]]) -> tuple[int, list[tuple[int, int, int]]]:
    """
    Finds the Minimum Spanning Tree using Kruskal's algorithm.

    Algorithm flow:
    1. Sort all edges by weight in ascending order
    2. Initialize Union-Find with n vertices
    3. For each edge (w, u, v) in sorted order:
       a. If u and v are not in the same component (no cycle):
          - Add edge to MST
          - Unite u and v in Union-Find
       b. Otherwise, skip this edge (would create a cycle)
    4. Return total weight and MST edges

    Why does this work? (Greedy choice property)
    - At each step, we choose the minimum weight edge that doesn't create a cycle
    - This greedy choice is safe: any MST must include this edge, or we can swap
      a heavier edge for it without increasing total weight
    - Union-Find ensures we never create a cycle (only unite different components)

    Why Union-Find?
    - Efficiently checks if two vertices are in the same component: O(α(n)) ≈ O(1)
    - Efficiently merges two components: O(α(n)) ≈ O(1)
    - Without it, cycle detection would be O(V) per edge → O(VE) total

    Args:
        n: Number of vertices (labeled 0 to n-1)
        edges: List of edges as (weight, u, v) tuples

    Returns:
        (total_weight, mst_edges) tuple where:
        - total_weight: Sum of weights in the MST
        - mst_edges: List of edges in the MST as (weight, u, v) tuples
    """
    # Sort edges by weight (ascending order)
    # pair is compared by first element by default in Python
    edges.sort()

    # Initialize Union-Find for n vertices
    uf = UnionFind(n)

    # Total weight of MST
    total_weight = 0

    # Edges in the MST
    mst_edges = []

    # Process each edge in order of increasing weight
    for weight, u, v in edges:
        # If u and v are not in the same component (adding this edge won't create a cycle)
        if not uf.isSame(u, v):
            # Add this edge to MST
            total_weight += weight
            mst_edges.append((weight, u, v))

            # Unite the two components
            uf.unite(u, v)

    return total_weight, mst_edges


def kruskal_simple(n: int, edges: list[tuple[int, int, int]]) -> int:
    """
    Simplified version that only returns the total weight of MST.

    Args:
        n: Number of vertices
        edges: List of edges as (weight, u, v) tuples

    Returns:
        Total weight of the Minimum Spanning Tree
    """
    edges.sort()
    uf = UnionFind(n)
    total_weight = 0

    for weight, u, v in edges:
        if not uf.isSame(u, v):
            total_weight += weight
            uf.unite(u, v)

    return total_weight