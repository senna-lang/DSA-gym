"""
挿入ソート (Insertion Sort) の実装

配列の各要素を、既にソート済みの部分に適切な位置に挿入していくアルゴリズム

時間計算量:
- 最良: O(N) (既にソート済みの場合)
- 平均: O(N^2)
- 最悪: O(N^2) (逆順の場合)

空間計算量: O(1) (in-placeソート)

特徴:
- 安定ソート (同じ値の順序が保たれる)
- 小さなデータや部分的にソート済みのデータに効率的
- オンラインアルゴリズム (データを順次受け取りながらソート可能)
"""


def insertion_sort(nums: list[int]) -> list[int]:
    """
    配列numsを挿入ソートでソートする (in-place)

    アルゴリズム:
    1. 配列の2番目の要素から順に処理
    2. 現在の要素insertValueを取り出す
    3. insertValueを挿入する適切な場所を、左側のソート済み部分から探す
    4. insertValueより大きい要素を1つ右にずらす
    5. 適切な位置にinsertValueを挿入

    Args:
        nums: ソートする配列
    """
    N = len(nums)

    # i番目の要素を適切な位置に挿入
    for i in range(1, N):
        insertValue = nums[i]  # 挿入したい値

        # insertValueを挿入する適切な場所positionを探す
        position = i
        while position > 0 and nums[position - 1] > insertValue:
            # insertValueより大きいものは1つ後ろに移す
            nums[position] = nums[position - 1]
            position -= 1

        # 最後にposition番目にinsertValueをもってくる
        nums[position] = insertValue

    return nums
