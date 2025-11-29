"""
code 13.4: s-t パスがあるかどうかを深さ優先探索を用いて判定

問題: グラフ G において、頂点 s から頂点 t へのパスが存在するか判定する
"""

from typing import List


def has_path(graph: List[List[int]], s: int, t: int) -> bool:
    """
    頂点 s から頂点 t へのパスが存在するか判定（内部関数版）

    Pythonらしい実装:
    - グローバル変数を使わず、内部関数で seen を共有
    - 外側の関数のスコープから seen を参照できる（クロージャ）

    Args:
        graph: 隣接リスト表現のグラフ
        s: 始点
        t: 終点

    Returns:
        True: パスが存在する
        False: パスが存在しない

    例:
        graph = [
            [1, 2],  # 0 -> 1, 2
            [3],     # 1 -> 3
            [3],     # 2 -> 3
            []       # 3 -> なし
        ]
        has_path(graph, 0, 3) -> True  # 0->1->3 というパスがある
        has_path(graph, 3, 0) -> False # 3から0へのパスはない
    """
    N = len(graph)
    seen = [False] * N

    def dfs(v: int) -> None:
        """
        深さ優先探索（内部関数）

        外側の関数の seen を直接参照できる

        Args:
            v: 現在の頂点
        """
        # v を訪問済にする
        seen[v] = True

        # v から行ける各頂点 next_v について
        for next_v in graph[v]:
            # next_v が探索済ならば探索しない
            if seen[next_v]:
                continue

            # 再帰的に探索
            dfs(next_v)

    # 頂点 s をスタートとした探索
    dfs(s)

    # t にたどり着けるかどうか
    return seen[t]
