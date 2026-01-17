"""
Code 16.1: Ford-Fulkerson Algorithm (Maximum Flow)

Finds the maximum flow in a flow network from source to sink.
Uses depth-first search (DFS) to find augmenting paths in the residual graph.

Complexity:
- Time: O(F * E) where F is the maximum flow value and E is the number of edges
  - Each augmenting path takes O(E) time to find using DFS
  - In the worst case, each path increases flow by 1, requiring F iterations
- Space: O(V + E) for the graph representation and DFS recursion

Characteristics:
- Works on directed graphs with edge capacities
- Finds maximum flow from source s to sink t
- Uses residual graph concept (remaining capacity on each edge)
- Each iteration finds an augmenting path and pushes flow along it
- Terminates when no augmenting path exists (max-flow min-cut theorem)

Comparison with other max flow algorithms:
- Edmonds-Karp (BFS-based Ford-Fulkerson): O(V * E²), better worst-case
- Dinic's Algorithm: O(V² * E), faster for dense graphs
- Push-Relabel: O(V² * E) or O(V³), good for dense graphs

When to use Ford-Fulkerson:
- Graph has integer capacities (guarantees integer flows)
- Maximum flow value is relatively small
- Simple implementation needed
- Graph is sparse

Note: This implementation assumes integer capacities for guaranteed termination.
For real-valued capacities, use Edmonds-Karp (BFS-based) to guarantee O(V*E²).
"""

from typing import List


class Edge:
    """
    Represents a directed edge in the flow network.

    Attributes:
        rev: Index of the reverse edge in the adjacency list of 'to'
        from_: Source vertex
        to: Destination vertex
        cap: Remaining capacity (residual capacity)
    """

    def __init__(self, rev: int, from_: int, to: int, cap: int):
        self.rev = rev
        self.from_ = from_
        self.to = to
        self.cap = cap


class Graph:
    """
    Graph representation using adjacency list for flow networks.

    For each edge (u, v) with capacity c, we store:
    - Forward edge: (u -> v) with capacity c
    - Backward edge: (v -> u) with capacity 0 (for flow cancellation)

    This allows us to easily update residual capacities when pushing flow.
    """

    def __init__(self, n: int):
        """
        Initialize graph with n vertices.

        Args:
            n: Number of vertices (labeled 0 to n-1)
        """
        self.n = n
        self.list: List[List[Edge]] = [[] for _ in range(n)]

    def size(self) -> int:
        """Return the number of vertices."""
        return self.n

    def __getitem__(self, i: int) -> List[Edge]:
        """Access adjacency list of vertex i using G[i] syntax."""
        return self.list[i]

    def addedge(self, from_: int, to: int, cap: int) -> None:
        """
        Add a directed edge from 'from_' to 'to' with capacity 'cap'.
        Also creates a reverse edge with capacity 0 for flow cancellation.

        Why do we need reverse edges?
        - In the residual graph, if we push flow f along edge (u, v),
          we can later "cancel" up to f units of that flow
        - This is represented by adding capacity f to the reverse edge (v, u)
        - Allows the algorithm to "undo" suboptimal flow decisions

        Args:
            from_: Source vertex
            to: Destination vertex
            cap: Edge capacity
        """
        # Index of the reverse edge that will be added to 'to'
        fromrev = len(self.list[from_])
        # Index of the reverse edge that will be added to 'from_'
        torev = len(self.list[to])

        # Add forward edge: from_ -> to with capacity cap
        self.list[from_].append(Edge(torev, from_, to, cap))
        # Add reverse edge: to -> from_ with capacity 0
        self.list[to].append(Edge(fromrev, to, from_, 0))

    def redge(self, e: Edge) -> Edge:
        """
        Get the reverse edge of edge e.

        Args:
            e: An edge in the graph

        Returns:
            The reverse edge of e
        """
        return self.list[e.to][e.rev]

    def run_flow(self, e: Edge, f: int) -> None:
        """
        Push flow f along edge e and update residual capacities.

        When we push flow f along edge (u, v):
        1. Decrease forward edge capacity by f
        2. Increase reverse edge capacity by f (allow flow cancellation)

        Args:
            e: Edge to push flow along
            f: Amount of flow to push
        """
        e.cap -= f  # Reduce remaining capacity on forward edge
        self.redge(e).cap += f  # Increase capacity on reverse edge


class FordFulkerson:
    """
    Ford-Fulkerson algorithm for computing maximum flow.

    Algorithm overview:
    1. Start with zero flow on all edges
    2. While there exists an augmenting path from s to t in residual graph:
       a. Find an augmenting path using DFS
       b. Determine bottleneck capacity (minimum capacity along path)
       c. Push flow equal to bottleneck along the path
       d. Update residual capacities
    3. Return total flow pushed from s to t
    """

    INF = 1 << 30  # Infinity constant for flow calculations

    def __init__(self):
        """Initialize Ford-Fulkerson solver."""
        self.seen: List[bool] = []

    def fodfis(self, G: Graph, v: int, t: int, f: int) -> int:
        """
        Find an augmenting path from v to t using DFS (depth-first search).

        Algorithm flow:
        1. If reached sink t, return the flow f (base case)
        2. Mark current vertex v as visited
        3. For each outgoing edge e from v:
           - Skip if already visited or no remaining capacity
           - Recursively search for path from e.to to t
           - If path found, push flow and return
        4. If no path found, return 0

        Why does DFS work here?
        - We need to find ANY path from s to t in the residual graph
        - DFS explores paths deeply, finding an augmenting path if one exists
        - The returned value is the minimum capacity along the found path

        Args:
            G: Flow network graph
            v: Current vertex in DFS
            t: Sink vertex (target)
            f: Minimum capacity along the path from s to v

        Returns:
            Bottleneck capacity of the augmenting path (0 if no path found)
        """
        # Base case: reached the sink
        if v == t:
            return f

        # Mark current vertex as visited
        self.seen[v] = True

        # Try all outgoing edges from v
        for e in G[v]:
            # Skip if destination already visited
            if self.seen[e.to]:
                continue

            # Skip if edge has no remaining capacity
            if e.cap == 0:
                continue

            # Recursively search for path from e.to to t
            # The flow is limited by min(current_f, edge_capacity)
            flow = self.fodfis(G, e.to, t, min(f, e.cap))

            # If augmenting path found (flow > 0)
            if flow > 0:
                # Push flow along this edge
                G.run_flow(e, flow)
                # Return the bottleneck capacity
                return flow

        # No augmenting path found from this vertex
        return 0

    def solve(self, G: Graph, s: int, t: int) -> int:
        """
        Compute maximum flow from source s to sink t.

        Algorithm flow:
        1. Initialize total flow to 0
        2. Repeat until no augmenting path exists:
           a. Reset visited array
           b. Find augmenting path and its bottleneck capacity using DFS
           c. If path found (flow > 0), add flow to result
        3. Return total maximum flow

        Why does this work? (Max-Flow Min-Cut Theorem)
        - The algorithm terminates when no augmenting path exists
        - At termination, the flow is maximum because:
          * No more flow can be pushed from s to t
          * The set of visited vertices in the last iteration forms a min-cut

        Args:
            G: Flow network graph
            s: Source vertex
            t: Sink vertex

        Returns:
            Maximum flow value from s to t
        """
        res = 0

        # Continue until no augmenting path exists
        while True:
            # Reset visited array for new DFS iteration
            self.seen = [False] * G.size()

            # Find augmenting path and get its bottleneck capacity
            flow = self.fodfis(G, s, t, self.INF)

            # No augmenting path found, algorithm terminates
            if flow == 0:
                return res

            # Add bottleneck flow to total
            res += flow