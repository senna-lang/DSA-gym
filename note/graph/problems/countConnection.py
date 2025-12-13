"""
問題 13.1: 連結成分の個数を数える

問題:
無向グラフ G = (V, E) が与えられたとき、連結成分の個数を求める

連結成分とは:
- グラフを構成する「繋がっている部分」のこと
- 同じ連結成分内の任意の2頂点間には経路が存在する
- 異なる連結成分間には経路が存在しない

解法:
1. DFS版: 未訪問の頂点からDFSを開始するたびにカウント+1
2. BFS版: 未訪問の頂点からBFSを開始するたびにカウント+1

計算量: O(V + E)
"""

from collections import deque


def count_connected_components_dfs(graph: list[list[int]]) -> int:
    """
    連結成分の個数を数える（DFS版）

    Args:
        graph: 隣接リスト表現の無向グラフ

    Returns:
        連結成分の個数

    例:
        # グラフ: 0--1  2--3  4
        #        (成分1) (成分2) (成分3)
        graph = [
            [1],     # 0 -- 1
            [0],     # 1 -- 0
            [3],     # 2 -- 3
            [2],     # 3 -- 2
            []       # 4 (孤立)
        ]
        count_connected_components_dfs(graph) -> 3
    """
    N = len(graph)
    seen = [False] * N
    count = 0

    def dfs(v: int) -> None:
        """
        深さ優先探索で連結成分を探索

        Args:
            v: 現在の頂点
        """
        seen[v] = True

        for next_v in graph[v]:
            if seen[next_v]:
                continue
            dfs(next_v)

    # 全頂点について探索
    for v in range(N):
        # v が未訪問なら、新しい連結成分を発見
        if not seen[v]:
            dfs(v)  # この連結成分全体を探索
            count += 1  # 連結成分カウントを増やす

    return count


def count_connected_components_bfs(graph: list[list[int]]) -> int:
    """
    連結成分の個数を数える（BFS版）

    Args:
        graph: 隣接リスト表現の無向グラフ

    Returns:
        連結成分の個数

    アルゴリズム:
        1. 全頂点について順番にチェック
        2. 未訪問の頂点vを見つけたら:
           - vを始点としてBFSを実行
           - この連結成分全体を訪問済みにする
           - カウント+1
        3. 全頂点をチェックし終えたらカウントを返す
    """
    N = len(graph)
    seen = [False] * N
    count = 0

    # 全頂点について探索
    for start in range(N):
        # start が未訪問なら、新しい連結成分を発見
        if seen[start]:
            continue

        # BFSでこの連結成分全体を探索
        queue = deque([start])
        seen[start] = True

        while queue:
            v = queue.popleft()

            for next_v in graph[v]:
                if seen[next_v]:
                    continue
                seen[next_v] = True
                queue.append(next_v)

        # この連結成分の探索完了
        count += 1

    return count


def get_connected_components(graph: list[list[int]]) -> list[list[int]]:
    """
    各連結成分に含まれる頂点のリストを返す

    Args:
        graph: 隣接リスト表現の無向グラフ

    Returns:
        各連結成分に含まれる頂点のリスト

    例:
        # グラフ: 0--1  2--3  4
        graph = [[1], [0], [3], [2], []]
        get_connected_components(graph)
        -> [[0, 1], [2, 3], [4]]
    """
    N = len(graph)
    seen = [False] * N
    components = []

    def dfs(v: int, component: list[int]) -> None:
        """
        DFSで連結成分を探索し、頂点をcomponentに追加
        """
        seen[v] = True
        component.append(v)

        for next_v in graph[v]:
            if seen[next_v]:
                continue
            dfs(next_v, component)

    # 全頂点について探索
    for v in range(N):
        if not seen[v]:
            component = []
            dfs(v, component)
            components.append(component)

    return components

