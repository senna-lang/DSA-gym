"""
問題 13.3: 二部グラフ判定

問題:
無向グラフ G = (V, E) が二部グラフかどうかを判定する

二部グラフとは:
- 頂点集合Vを2つのグループに分割できる
- 同じグループ内の頂点間には辺がない
- 異なるグループ間にのみ辺がある
- 例: マッチング問題、チェス盤の白黒など

判定方法:
- グラフを2色で塗り分けられるか = 二部グラフ
- 隣接する頂点は異なる色にする
- 矛盾が生じなければ二部グラフ

重要な定理:
- グラフが二部グラフ ⇔ 奇数長の閉路を持たない

計算量: O(V + E)
"""

from collections import deque


def is_bipartite_bfs(graph: list[list[int]]) -> bool:
    """
    二部グラフ判定（BFS版）- code 13.5の実装

    Args:
        graph: 隣接リスト表現の無向グラフ

    Returns:
        二部グラフならTrue、そうでなければFalse

    アルゴリズム:
        1. 各頂点に色を割り当てる（-1: 未訪問, 0: 色1, 1: 色2）
        2. 未訪問の頂点からBFSを開始
        3. 隣接頂点に現在の頂点と異なる色を割り当て
        4. すでに塗られている頂点と同じ色になろうとしたら二部グラフでない

    例:
        # 二部グラフ: 0--1
        #            |  |
        #            3--2
        graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
        is_bipartite_bfs(graph) -> True

        # 非二部グラフ（三角形）: 0--1
        #                        \ /
        #                         2
        graph = [[1, 2], [0, 2], [0, 1]]
        is_bipartite_bfs(graph) -> False
    """
    N = len(graph)
    color = [-1] * N  # -1: 未訪問, 0: 色1, 1: 色2

    # 全ての連結成分について判定（非連結グラフにも対応）
    for start in range(N):
        # すでに訪問済みならスキップ
        if color[start] != -1:
            continue

        # BFSで2色塗り分け
        queue = deque([start])
        color[start] = 0  # 最初の頂点は色0

        while queue:
            v = queue.popleft()

            for next_v in graph[v]:
                # 未訪問なら、現在の頂点と異なる色を割り当て
                if color[next_v] == -1:
                    color[next_v] = 1 - color[v]  # 色を反転 (0→1, 1→0)
                    queue.append(next_v)
                # すでに訪問済みで、同じ色なら二部グラフでない
                elif color[next_v] == color[v]:
                    return False

    # 全ての連結成分で矛盾がなければ二部グラフ
    return True