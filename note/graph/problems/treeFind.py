"""
code 13.7 & 13.8 & 13.9: 根なし木の走査と深さ計算、部分木のサイズ

問題: 根なし木を根付き木として扱い、各頂点の深さと部分木のサイズを求める

根なし木とは:
- 閉路のない連結グラフ
- N個の頂点とN-1個の辺を持つ
- 任意の2頂点間に経路が1つだけ存在

根付き木にする:
- 特定の頂点（通常は頂点0）を根とする
- 根からの各頂点への距離（深さ）を求める
- 親子関係が定まる

計算量: O(V + E) = O(N)（木なのでE = N-1）
"""


def dfs_tree_basic(graph: list[list[int]], root: int = 0) -> list[bool]:
    """
    code 13.7: 根なし木の走査の基本形

    木の探索で親方向への逆流を防ぐ方法

    Args:
        graph: 隣接リスト表現の木（無向グラフ）
        root: 根とする頂点（デフォルト: 0）

    Returns:
        訪問済み配列（全てTrueになる）

    注意:
        - p（親頂点）を引数で渡すことで、親方向への探索を防ぐ
        - 根のときは p = -1（親なし）
    """
    N = len(graph)
    seen = [False] * N

    def dfs(v: int, p: int = -1) -> None:
        """
        木の探索（親を記憶する版）

        Args:
            v: 現在探索中の頂点
            p: vの親（vが根のとき p = -1）

        処理:
            1. vを訪問済みにする
            2. vの各子頂点cについて:
               - c == p なら親方向なのでスキップ
               - それ以外は子頂点なので再帰的に探索
        """
        seen[v] = True

        for c in graph[v]:
            # 探索が親方向へ逆流するのを防ぐ
            if c == p:
                continue

            # c は v の子頂点を動く。このとき c の親は v となる
            dfs(c, v)

    # 根から探索開始
    dfs(root)

    return seen


def dfs_tree_depth(graph: list[list[int]], root: int = 0) -> list[int]:
    """
    code 13.8: 根なし木を根付き木としたときの各頂点の深さを求める
    
    Args:
        graph: 隣接リスト表現の木（無向グラフ）
        root: 根とする頂点（デフォルト: 0）
    
    Returns:
        depth: 各頂点の深さ（根からの距離）
    
    例:
        # 木の構造:
        #     0
        #    / \
        #   1   2
        #  /
        # 3
        graph = [
            [1, 2],  # 0 -- 1, 2
            [0, 3],  # 1 -- 0, 3
            [0],     # 2 -- 0
            [1]      # 3 -- 1
        ]
        depth = dfs_tree_depth(graph, 0)
        # depth = [0, 1, 1, 2]
        #          0の深さ=0, 1の深さ=1, 2の深さ=1, 3の深さ=2
    """
    N = len(graph)
    depth = [-1] * N  # -1: 未訪問

    def dfs(v: int, p: int = -1, d: int = 0) -> None:
        """
        深さ優先探索で各頂点の深さを記録

        Args:
            v: 現在の頂点
            p: vの親（根のとき -1）
            d: vの深さ（根からの距離）

        処理:
            1. depth[v] = d を記録
            2. vの各子頂点cについて:
               - c == p なら親なのでスキップ
               - dfs(c, v, d+1) で深さを1増やして子頂点へ
        """
        # d: 頂点 v の深さ（v が根のとき d = 0）
        depth[v] = d

        for c in graph[v]:
            # 探索が親方向へ逆流するのを防ぐ
            if c == p:
                continue

            # d を 1 増やして子頂点へ
            dfs(c, v, d + 1)

    # 根から探索開始（深さ0）
    dfs(root, -1, 0)

    return depth


def dfs_tree_subtree_size(graph: list[list[int]], root: int = 0) -> list[int]:
    """
    code 13.9: 根なし木を根付き木にしたときの、各頂点の深さや部分木サイズを求める

    部分木のサイズとは:
    - 頂点vを根とする部分木に含まれる頂点数
    - v自身 + vの全ての子孫の数
    - 葉ノードの部分木サイズは1（自分自身のみ）

    Args:
        graph: 隣接リスト表現の木（無向グラフ）
        root: 根とする頂点（デフォルト: 0）

    Returns:
        subtree_size: 各頂点を根とする部分木のサイズ

    例:
        # 木の構造:
        #     0
        #    / \
        #   1   2
        #  /
        # 3
        graph = [
            [1, 2],  # 0 -- 1, 2
            [0, 3],  # 1 -- 0, 3
            [0],     # 2 -- 0
            [1]      # 3 -- 1
        ]
        subtree_size = dfs_tree_subtree_size(graph, 0)
        # subtree_size = [4, 2, 1, 1]
        #   頂点0の部分木: {0,1,2,3} サイズ=4
        #   頂点1の部分木: {1,3}     サイズ=2
        #   頂点2の部分木: {2}       サイズ=1（葉）
        #   頂点3の部分木: {3}       サイズ=1（葉）
    """
    N = len(graph)
    depth = [-1] * N
    subtree_size = [0] * N

    def dfs(v: int, p: int = -1, d: int = 0) -> int:
        """
        深さ優先探索で各頂点の深さと部分木サイズを記録

        Args:
            v: 現在の頂点
            p: vの親（根のとき -1）
            d: vの深さ（根からの距離）

        Returns:
            vを根とする部分木のサイズ

        処理の流れ:
            1. depth[v] = d を記録
            2. 各子頂点について再帰的に部分木サイズを求める
            3. subtree_size[v] = 1（自分自身） + 全ての子の部分木サイズの合計
        """
        # 深さを記録
        depth[v] = d

        # 帰りがけに、部分木サイズを求める
        # まず自分自身をカウント
        subtree_size[v] = 1  # 自分自身

        for c in graph[v]:
            # 探索が親方向へ逆流するのを防ぐ
            if c == p:
                continue

            # 子頂点を根とする部分木のサイズを加算する
            # dfs(c)は「cを根とする部分木のサイズ」を返す
            subtree_size[v] += dfs(c, v, d + 1)

        # vを根とする部分木のサイズを返す
        return subtree_size[v]

    # 根から探索開始
    dfs(root, -1, 0)

    return subtree_size


graph1 = [
    [1, 2],  # 0 -- 1, 2
    [0, 3],  # 1 -- 0, 3
    [0],  # 2 -- 0
    [1],  # 3 -- 1
]

print(dfs_tree_subtree_size(graph1, 0))
