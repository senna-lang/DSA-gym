"""
code 13.5: 二部グラフ判定

問題: グラフ G が二部グラフかどうかを判定する

二部グラフとは:
- 頂点を2つのグループに分けられる
- 同じグループ内の頂点同士は辺で結ばれていない
- 異なるグループ間にのみ辺がある

判定方法:
- DFSで各頂点に色(0 or 1)を塗る
- 隣接する頂点には異なる色を塗る
- 矛盾が生じたら二部グラフではない
"""

from typing import List


def is_bipartite(graph: List[List[int]]) -> bool:
    """
    グラフが二部グラフかどうかを判定

    Args:
        graph: 隣接リスト表現のグラフ（無向グラフ）

    Returns:
        True: 二部グラフである
        False: 二部グラフではない

    例:
        # 二部グラフの例
        graph = [
            [1, 3],  # 0 -- 1, 3
            [0, 2],  # 1 -- 0, 2
            [1, 3],  # 2 -- 1, 3
            [0, 2],  # 3 -- 0, 2
        ]
        # グループA: {0, 2}, グループB: {1, 3}
        is_bipartite(graph) -> True

        # 二部グラフでない例（三角形）
        graph = [
            [1, 2],  # 0 -- 1, 2
            [0, 2],  # 1 -- 0, 2
            [0, 1],  # 2 -- 0, 1
        ]
        is_bipartite(graph) -> False
    """
    N = len(graph)
    color = [-1] * N  # -1: 未訪問, 0: 色0, 1: 色1

    def dfs(v: int, cur: int = 0) -> bool:
        """
        深さ優先探索で二部グラフ判定

        Args:
            v: 現在の頂点
            cur: 現在の頂点に塗る色 (0 or 1)

        Returns:
            True: 矛盾なく塗れた
            False: 矛盾が発生（二部グラフではない）
        """
        # v に色 cur を塗る
        color[v] = cur

        # v の隣接頂点を探索
        for next_v in graph[v]:
            # 隣接頂点がすでに色確定していた場合
            if color[next_v] != -1:
                # 同じ色が隣接した場合は二部グラフではない
                if color[next_v] == cur:
                    return False

                # 色が確定した場合には探索しない
                continue

            # 隣接頂点の色を変えて、再帰的に探索
            # 1 - curとすることで色を交互に指定可能
            # false が返ってきたら false を返す
            if not dfs(next_v, 1 - cur):
                return False

        return True

    # 探索
    # 各連結成分について探索する必要がある
    for v in range(N):
        # v が探索済みの場合は探索しない
        if color[v] != -1:
            continue

        # v を始点として探索（色0から開始）
        if not dfs(v):
            return False

    return True
