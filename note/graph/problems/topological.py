"""
code 13.6 & 問題13.5: トポロジカルソート (Topological Sort)

問題: 有向非巡回グラフ (DAG: Directed Acyclic Graph) のトポロジカルソートを求める

トポロジカルソートとは:
- DAGの頂点を一列に並べる
- 辺 u → v がある場合、u は v よりも前に並ぶ
- 依存関係の解決、タスクの実行順序などに使える

実装方法:
1. DFS版（code 13.6）: 各頂点の探索完了順（v-out）を記録し、逆順にする
2. BFS版（問題13.5 - Kahn's Algorithm）: 入次数が0の頂点から順に処理（閉路検出可能）

計算量: O(V + E)
"""

from collections import deque


def topological_sort(graph: list[list[int]]) -> list[int]:
    """
    トポロジカルソートを求める（内部関数版）

    Args:
        graph: 隣接リスト表現の有向グラフ（DAGである必要がある）

    Returns:
        トポロジカルソート順の頂点リスト

    例:
        # DAGの例（依存関係グラフ）
        # 0 → 1 → 3
        # ↓   ↓
        # 2 → 3
        graph = [
            [1, 2],  # 0 → 1, 2
            [3],     # 1 → 3
            [3],     # 2 → 3
            []       # 3 → なし
        ]
        topological_sort(graph) -> [0, 2, 1, 3] または [0, 1, 2, 3]
        # どちらも正しいトポロジカルソート順

    注意:
        - グラフが閉路を含む場合、結果は正しくない
        - 閉路検出は別途実装が必要
    """
    N = len(graph)
    seen = [False] * N
    order = []  # トポロジカルソート順（逆順）

    def dfs(v: int) -> None:
        """
        深さ優先探索でトポロジカルソート順を記録

        Args:
            v: 現在の頂点

        処理の流れ:
        1. v を訪問済みにする
        2. v から行ける全ての頂点を再帰的に探索
        3. v の探索が完了したら order に追加（v-out を記録）
        """
        # v を訪問済にする
        seen[v] = True

        # v から行ける各頂点を探索
        for next_v in graph[v]:
            # すでに訪問済みならば探索しない
            if seen[next_v]:
                continue

            # 再帰的に探索
            dfs(next_v)

        # v-out を記録する
        # v から行ける全ての頂点の探索が完了した後に記録
        # これは帰りがけの処理でforで展開されて深さの行き止まりに達したら深いところから順番にこの処理をして帰ってくる
        order.append(v)

    # 全頂点について探索
    # 連結でないグラフにも対応
    for v in range(N):
        # v が探索済みの場合は探索しない
        if seen[v]:
            continue

        # v を始点として探索
        dfs(v)

    # order は「探索完了順」なので逆順にする
    # 完了順の逆順 = トポロジカルソート順
    order.reverse()

    return order


def topological_sort_bfs(graph: list[list[int]]) -> list[int]:
    """
    問題13.5: トポロジカルソートを幅優先探索で実装（Kahn's Algorithm）

    Args:
        graph: 隣接リスト表現の有向グラフ（DAGである必要がある）

    Returns:
        トポロジカルソート順の頂点リスト

    アルゴリズム（Kahn's Algorithm）:
        1. 各頂点の入次数（入ってくる辺の数）を計算
        2. 入次数が0の頂点（依存なし）をキューに追加
        3. キューから頂点を取り出し、結果に追加
        4. その頂点から出る辺を削除（隣接頂点の入次数を-1）
        5. 入次数が0になった頂点をキューに追加
        6. キューが空になるまで繰り返す

    例:
        # DAGの例
        # 0 → 1 → 3
        # ↓   ↓
        # 2 → 3
        graph = [
            [1, 2],  # 0 → 1, 2
            [3],     # 1 → 3
            [3],     # 2 → 3
            []       # 3 → なし
        ]

        入次数: [0, 1, 1, 2]
        - 頂点0: 入次数0 → 最初にキューへ
        - 頂点0処理 → 頂点1,2の入次数-1 → [0, 0, 2]
        - 頂点1,2処理 → 頂点3の入次数-1-1 → [0]
        - 頂点3処理 → 完了

        結果: [0, 1, 2, 3] または [0, 2, 1, 3]

    注意:
        - DAGでない場合（閉路がある場合）、結果の長さ < N になる
        - これを利用して閉路検出も可能
    """
    N = len(graph)
    inDegree = [0] * N  # 各頂点の入次数

    # 入次数を計算
    for v in range(N):
        for next_v in graph[v]:
            inDegree[next_v] += 1

    # 入次数が0の頂点をキューに追加
    queue = deque()
    for v in range(N):
        if inDegree[v] == 0:
            queue.append(v)

    # トポロジカルソート順
    result = []

    # BFS
    while queue:
        v = queue.popleft()
        result.append(v)

        # vから出る辺を削除（隣接頂点の入次数を減らす）
        for next_v in graph[v]:
            inDegree[next_v] -= 1

            # 入次数が0になったらキューに追加
            if inDegree[next_v] == 0:
                queue.append(next_v)

    # DAGでない場合（閉路がある場合）は len(result) < N
    return result


def has_cycle(graph: list[list[int]]) -> bool:
    """
    有向グラフが閉路を持つかどうかを判定

    トポロジカルソートBFS版を利用:
    - DAG（閉路なし）ならトポロジカルソート可能
    - 閉路があるとトポロジカルソートできない（一部の頂点が処理できない）

    Args:
        graph: 隣接リスト表現の有向グラフ

    Returns:
        閉路があればTrue、なければFalse

    例:
        # DAG（閉路なし）
        graph = [[1], [2], []]  # 0 → 1 → 2
        has_cycle(graph) -> False

        # 閉路あり
        graph = [[1], [2], [0]]  # 0 → 1 → 2 → 0
        has_cycle(graph) -> True
    """
    N = len(graph)
    result = topological_sort_bfs(graph)

    # トポロジカルソートで全頂点を処理できなければ閉路あり
    return len(result) < N

