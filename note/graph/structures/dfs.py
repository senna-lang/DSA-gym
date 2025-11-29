"""
グラフ探索の実装 - DFS (Depth First Search: 深さ優先探索)

BFSとの違い: queue の代わりに stack を使う
"""

from typing import List


def dfs_iterative(graph: List[List[int]], s: int) -> List[bool]:
    """
    グラフ G において、頂点 s を始点とした探索を行う (DFS - 反復版)

    DFS (深さ優先探索):
    - スタック (stack) を使う
    - 一方向に深く探索してから戻る
    - 経路探索、サイクル検出などに使える

    計算量: O(V + E)

    Args:
        graph: 隣接リスト表現のグラフ
        s: 始点

    Returns:
        seen: 各頂点が訪問済みかどうか
    """
    N = len(graph)

    # 全頂点を「未訪問」に初期化する
    seen = [False] * N

    # スタック (Pythonではリストをスタックとして使える)
    todo = []

    # 初期条件
    seen[s] = True
    todo.append(s)

    # todo が空になるまで探索を行う
    while todo:
        # スタックの末尾から取り出す (LIFO)
        v = todo.pop()

        # v からたどれる頂点をすべて調べる
        for x in graph[v]:
            # すでに発見済みの頂点は探索しない
            if seen[x]:
                continue

            # 新たな頂点 x を探索済みとして todo に挿入
            seen[x] = True
            todo.append(x)

    return seen


# グローバル変数として seen を定義（C++版に合わせる）
seen = []


def dfs_recursive(graph: List[List[int]], v: int) -> None:
    """
    再帰関数を用いる深さ優先探索 (code 13.2)

    C++版のコードをそのままPythonに移植した形式

    グラフ G において、頂点 v から探索を行う

    グローバル変数 seen を使用:
    - seen[v] = True: 頂点 v を訪問済にする
    - すでに訪問済みの頂点は探索しない

    使用方法:
        # グローバル変数 seen を初期化
        seen = [False] * N

        # 各頂点について、未訪問なら探索
        for v in range(N):
            if seen[v]:
                continue
            dfs_code_13_2(graph, v)

    Args:
        graph: 隣接リスト表現のグラフ
               graph[v] = 頂点v から行ける頂点のリスト
        v: 現在の頂点

    計算量: O(V + E)
    - V: 頂点数
    - E: 辺の数
    """
    # v を訪問済にする
    seen[v] = True

    # v から行ける各頂点 next_v について
    for next_v in graph[v]:
        # next_v が探索済ならば探索しない
        if seen[next_v]:
            continue

        # 再帰的に探索
        dfs_recursive(graph, next_v)
