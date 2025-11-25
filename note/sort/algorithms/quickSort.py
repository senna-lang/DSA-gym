"""
クイックソート (Quick Sort) の実装

ピボットを基準に配列を分割し、再帰的にソートする分割統治法のアルゴリズム

時間計算量:
- 最良: O(N log N) (ピボットが常に中央値の場合)
- 平均: O(N log N)
- 最悪: O(N^2) (既にソート済みで、ピボットが常に最小/最大の場合)

空間計算量: O(log N) (再帰呼び出しのスタック)

特徴:
- 不安定ソート (同じ値の順序が保証されない)
- in-placeソート (追加の配列が不要)
- 実用的には最も高速なソートの1つ
- ピボットの選び方で性能が変わる
"""


def quick_sort(a: list[int], left: int = None, right: int = None) -> None:
    """
    配列aを区間[left, right)に対してクイックソートでソートする

    アルゴリズム:
    1. ピボット（基準値）を選ぶ（この実装では中央要素）
    2. ピボットより小さい要素を左に、大きい要素を右に分割
    3. ピボットを適切な位置に配置
    4. 左半分と右半分を再帰的にソート

    Args:
        a: ソートする配列
        left: ソート範囲の左端 (デフォルト: 0)
        right: ソート範囲の右端(含まない) (デフォルト: len(a))

    例:
        a = [5, 2, 8, 1, 9]
        quick_sort(a) -> a = [1, 2, 5, 8, 9]
    """
    # デフォルト引数の処理
    if left is None:
        left = 0
    if right is None:
        right = len(a)

    # ベースケース: 区間の長さが1以下ならソート済み
    if right - left <= 1:
        return

    # ピボット選択: 中央の要素をピボットとして選択
    pivot_index = (left + right) // 2
    pivot = a[pivot_index]

    # ピボットと右端を交換
    a[pivot_index], a[right - 1] = a[right - 1], a[pivot_index]

    # 分割処理
    # i: 左詰めされたpivot未満の要素の右端を表す
    i = left

    # jでループして、pivot未満のものがあったら左に詰めていく
    # iを右にずらす＝pivot未満の要素を左に詰めて蓋をしていくイメージ
    for j in range(left, right - 1):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    # pivotを適切な場所に挿入
    # 蓋とpivotを交換
    a[i], a[right - 1] = a[right - 1], a[i]

    # 再帰的にソート
    quick_sort(a, left, i)  # 左半分 (pivot未満)
    quick_sort(a, i + 1, right)  # 右半分 (pivot以上)


def quick_sort_simple(a: list[int]) -> list[int]:
    """
    クイックソートのシンプルな実装（新しいリストを返す）

    Pythonのリスト内包表記を使った読みやすい実装

    Args:
        a: ソートする配列

    Returns:
        ソート済みの新しい配列
    """
    # ベースケース
    if len(a) <= 1:
        return a.copy()

    # ピボットを選択
    pivot = a[len(a) // 2]

    # 3つに分割
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]

    # 再帰的にソートして結合
    return quick_sort_simple(left) + middle + quick_sort_simple(right)
