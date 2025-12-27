"""
code 14.2 ベルマン・フォード法の実装

負の重みを持つ辺があるグラフでも最短経路を求められるアルゴリズム
負閉路（negative cycle）の検出も可能

計算量: O(V * E)
- V: 頂点数
- E: 辺数
"""

# 無限大を表す値
INF = float("inf")


class Edge:
    """辺を表すクラス（重み付き有向辺）"""

    def __init__(self, to: int, weight: int):
        self.to = to  # 隣接頂点番号
        self.weight = weight  # 重み

    def __repr__(self):
        return f"Edge(to={self.to}, w={self.weight})"


# 重み付きグラフを表す型
Graph = list[list[Edge]]


def chmin(a: list[float], index: int, b: float) -> bool:
    """
    緩和処理を実施する関数
    a[index] を min(a[index], b) で更新し、更新されたら True を返す

    Args:
        a: 更新対象の配列
        index: 更新する要素のインデックス
        b: 比較する値

    Returns:
        更新が発生したら True、そうでなければ False
    """
    if a[index] > b:
        a[index] = b
        return True
    return False


def bellmanFord(graph: Graph, start: int) -> tuple[list[float], bool]:
    """
    ベルマン・フォード法で単一始点最短経路を求める

    アルゴリズムの流れ:
    1. dist[start] = 0, その他は INF で初期化
    2. N-1 回、全ての辺について緩和処理を実行
       - 緩和: dist[to] = min(dist[to], dist[from] + weight)
    3. N 回目に更新が発生したら負閉路が存在

    なぜ N-1 回？
    - 最短経路は高々 N-1 本の辺を使う（同じ頂点を2回訪れない）
    - N-1 回の反復で全ての最短経路が確定する
    - N 回目に更新が起きる = 負閉路で距離が無限に減少可能

    Args:
        graph: 重み付き有向グラフ（隣接リスト表現）
        start: 始点

    Returns:
        (dist, has_negative_cycle) のタプル
        - dist: 各頂点への最短距離（負閉路がある場合は無意味）
        - has_negative_cycle: 負閉路が存在するか
    """
    N = len(graph)

    # 距離配列を初期化
    dist = [INF] * N
    dist[start] = 0

    # 負閉路の有無
    has_negative_cycle = False

    # 最大でN 回の反復
    for iter_count in range(N):
        update = False  # この反復で更新が発生したかを記録

        # 全ての頂点について
        for v in range(N):
            # dist[v] = INF のときは頂点 v からの緩和を行わない
            # （まだ始点から到達できていない）
            # ここでスキップされてもstartから到達可能であれば２週目以降で処理される
            if dist[v] == INF:
                continue

            # 頂点 v から出る全ての辺について緩和処理
            for edge in graph[v]:
                # 緩和処理を行い、更新されたら update を True にする
                # ここでdistを更新することでINFの頂点が到達可能として更新されることがあり、その場合次のiter_countで処理される
                if chmin(dist, edge.to, dist[v] + edge.weight):
                    update = True

        # 更新が行われなかったら、すでに最短路が求められている
        if not update:
            break

        # N 回目の反復で更新が行われたならば、負閉路をもつ
        if iter_count == N - 1 and update:
            has_negative_cycle = True

    return dist, has_negative_cycle
