"""
code 13.6: トポロジカルソート (Topological Sort)

問題: 有向非巡回グラフ (DAG: Directed Acyclic Graph) のトポロジカルソートを求める

トポロジカルソートとは:
- DAGの頂点を一列に並べる
- 辺 u → v がある場合、u は v よりも前に並ぶ
- 依存関係の解決、タスクの実行順序などに使える

実装方法:
- DFSで各頂点の探索完了順（v-out）を記録
- 完了順の逆順がトポロジカルソート順

計算量: O(V + E)
"""


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
