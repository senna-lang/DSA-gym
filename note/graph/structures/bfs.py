"""
グラフ探索の実装 - BFS (Breadth First Search: 幅優先探索)

code 13.1 のPython実装
"""

from collections import deque
from typing import List


def bfs(graph: List[List[int]], s: int) -> List[bool]:
    """
    グラフ G において、頂点 s を始点とした探索を行う (BFS)

    BFS (幅優先探索):
    - キュー (queue) を使う
    - 始点に近い頂点から順に探索
    - 最短経路問題に使える

    計算量: O(V + E)
    - V: 頂点数
    - E: 辺の数

    Args:
        graph: 隣接リスト表現のグラフ
               graph[v] = 頂点v から行ける頂点のリスト
        s: 始点

    Returns:
        seen: 各頂点が訪問済みかどうか
              seen[v] = True なら頂点v は始点sから到達可能

    例:
        graph = [
            [1, 2],    # 0 -> 1, 2
            [0, 3],    # 1 -> 0, 3
            [0, 3],    # 2 -> 0, 3
            [1, 2]     # 3 -> 1, 2
        ]
        bfs(graph, 0) -> [True, True, True, True]
        # 頂点0から全ての頂点に到達可能
    """
    N = len(graph)

    # グラフ探索のためのデータ構造
    # 全頂点を「未訪問」に初期化する
    seen = [False] * N

    # キュー (BFSでは queue、DFSでは stack を使う)
    todo = deque()

    # 初期条件
    # s は探索済みとする
    seen[s] = True

    # todo は s のみを含む状態となる
    todo.append(s)

    # todo が空になるまで探索を行う
    while todo:
        # todo から頂点を取り出す
        v = todo.popleft()

        # v からたどれる頂点をすべて調べる
        for x in graph[v]:
            # すでに発見済みの頂点は探索しない
            if seen[x]:
                continue

            # 新たな頂点 x を探索済みとして todo に挿入
            seen[x] = True
            todo.append(x)

    return seen


def bfs_shortest_path(graph: List[List[int]], s: int) -> List[int]:
    """
    幅優先探索で最短路を求める (code 13.3)

    入力: グラフ G と、探索の始点 s
    出力: s から各頂点への最短路長を表す配列

    Args:
        graph: 隣接リスト表現のグラフ
        s: 始点

    Returns:
        dist: 各頂点への最短距離
              dist[v] = 始点sから頂点vまでの最短距離
              到達不可能な場合は -1

    例:
        graph = [
            [1, 2],    # 0 -> 1, 2
            [3],       # 1 -> 3
            [3],       # 2 -> 3
            []         # 3 -> なし
        ]
        bfs_shortest_path(graph, 0) -> [0, 1, 1, 2]
        # 0->0: 0, 0->1: 1, 0->2: 1, 0->3: 2
    """
    N = len(graph)

    # 全頂点を「未訪問」に初期化
    dist = [-1] * N

    # キュー
    que = deque()

    # 初期条件（頂点 0 を初期頂点とする）
    dist[0] = 0

    # 0 を橙色頂点にする
    que.append(0)

    # BFS 開始（キューが空になるまで探索を行う）
    while que:
        # キューから先頭頂点を取り出す
        v = que.popleft()

        # v からたどれる頂点をすべて調べる
        for x in graph[v]:
            # すでに発見済みの頂点は探索しない
            if dist[x] != -1:
                continue

            # 新たな頂点 x について距離情報を記録してキューに挿入
            dist[x] = dist[v] + 1
            que.append(x)

    return dist

