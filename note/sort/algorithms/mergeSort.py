"""
マージソート (Merge Sort) の実装

配列を再帰的に分割し、マージしながらソートする分割統治法のアルゴリズム

時間計算量:
- 最良: O(N log N)
- 平均: O(N log N)
- 最悪: O(N log N)

空間計算量: O(N) (補助配列が必要)

特徴:
- 安定ソート (同じ値の順序が保たれる)
- 外部ソートに適している
- 並列化が容易
- 常にO(N log N)の性能を保証
"""


def merge_sort(a: list[int], left: int = None, right: int = None) -> None:
    """
    配列aを区間[left, right)に対してマージソートでソートする

    注意: 入力配列aを直接変更しますが、O(N)の補助配列bufが必要です
    （厳密な意味でのin-place（O(1)空間）ではありません）

    この実装の特徴:
    - 右側の配列を逆順にコピーすることで番兵を不要にする巧妙なテクニック
    - 両端から中央に向かってマージするため、境界チェックが簡単
    - 入力配列を直接変更（新しい配列を返さない）
    - 核心：ソート済みの配列を再帰的に先頭同士を比較すると必ず最小値が得られる

    アルゴリズム:
    1. 区間を左半分[left, mid)と右半分[mid, right)に分割
    2. 左半分を再帰的にソート
    3. 右半分を再帰的にソート
    4. 2つのソート済み配列をマージ

    Args:
        a: ソートする配列
        left: ソート範囲の左端 (デフォルト: 0)
        right: ソート範囲の右端(含まない) (デフォルト: len(a))

    例:
        a = [5, 2, 8, 1, 9, 3]
        merge_sort(a, 0, 6) → a = [1, 2, 3, 5, 8, 9]
    """
    # デフォルト引数の処理
    # merge_sort(a) と呼ばれた場合、配列全体をソート
    if left is None:
        left = 0
    if right is None:
        right = len(a)

    # ベースケース: 区間の長さが1以下ならソート済み
    # 例: [5] または [] はソート不要
    if right - left <= 1:
        return

    # === 分割フェーズ ===
    # 区間を中央で半分に分割
    # オーバーフロー対策で (left + right) // 2 ではなく left + (right - left) // 2
    mid = left + (right - left) // 2

    # 左半分[left, mid)を再帰的にソート
    # 例: [5, 2, 8] のうち [5, 2] を処理
    merge_sort(a, left, mid)

    # 右半分[mid, right)を再帰的にソート
    # 例: [5, 2, 8] のうち [8] を処理
    merge_sort(a, mid, right)

    # === 結合フェーズ ===
    # ここから先は、左右がそれぞれソート済みの状態
    # 例: a[left:mid] = [2, 5], a[mid:right] = [8]

    # 【重要なトリック】右側を逆順にコピーして番兵を作る
    # buf = [左側の要素 (正順)] + [右側の要素 (逆順)]
    # 例: left=0, mid=2, right=3 の場合
    #     a = [2, 5, 8] → buf = [2, 5, 8]
    #                            ↑正順  ↑逆順
    buf = []

    # 左側を正順でコピー
    # 例: [2, 5] → buf = [2, 5]
    for i in range(left, mid):
        buf.append(a[i])

    # 右側を逆順でコピー（これが番兵の役割を果たす）
    # 例: [8] → buf = [2, 5, 8]
    # もし右側が[6, 7, 8]なら buf = [2, 5, 8, 7, 6]
    for i in range(right - 1, mid - 1, -1):
        buf.append(a[i])

    # マージ処理: 両端から中央に向かって進む
    # index_left: 左端から右へ進む
    # index_right: 右端から左へ進む
    index_left = 0  # bufの左端
    index_right = len(buf) - 1  # bufの右端

    # 例: buf = [2, 5, 8]
    #           ↑       ↑
    #      index_left  index_right

    # 元の配列aの[left, right)区間を順に埋めていく
    for i in range(left, right):
        # 左側の要素 <= 右側の要素 なら左から取る
        if buf[index_left] <= buf[index_right]:
            a[i] = buf[index_left]
            index_left += 1  # 左端を右に進める
        # 右側の要素 < 左側の要素 なら右から取る
        else:
            a[i] = buf[index_right]
            index_right -= 1  # 右端を左に進める

    # 【なぜこのトリックが有効か】
    # 通常のマージでは「どちらかの配列が尽きたか」のチェックが必要
    # しかし、右側を逆順にすることで:
    # - 左側が尽きる → 右側の残り（大きい値）が自動的に選ばれる
    # - 右側が尽きる → 左側の残り（小さい値）が自動的に選ばれる
    # つまり、境界チェック不要で常に正しい要素が選ばれる！


def merge_sort_simple(a: list[int]) -> list[int]:
    """
    マージソートのシンプルな実装（新しいリストを返す）

    分割統治法の典型例:
    1. 分割 (Divide): 配列を半分に分ける
    2. 統治 (Conquer): 各部分を再帰的にソート
    3. 結合 (Combine): 2つのソート済み配列をマージ

    Args:
        a: ソートする配列

    Returns:
        ソート済みの新しい配列

    例:
        入力: [5, 2, 8, 1]
        ステップ1: [5, 2] と [8, 1] に分割
        ステップ2: [5, 2] → [2, 5], [8, 1] → [1, 8] に再帰的にソート
        ステップ3: [2, 5] と [1, 8] をマージ → [1, 2, 5, 8]
    """
    # ベースケース: 要素数が1以下ならそのまま返す
    # 長さ0または1の配列は既にソート済み
    if len(a) <= 1:
        return a.copy()

    # === 分割フェーズ ===
    # 配列を中央で2つに分割
    mid = len(a) // 2

    # 左半分 [0, mid) を再帰的にソート
    # 例: [5, 2, 8, 1] なら [5, 2] を処理
    left = merge_sort_simple(a[:mid])

    # 右半分 [mid, len(a)) を再帰的にソート
    # 例: [5, 2, 8, 1] なら [8, 1] を処理
    right = merge_sort_simple(a[mid:])

    # === 結合フェーズ ===
    # 2つのソート済み配列をマージして1つのソート済み配列を作る
    result = []  # マージ結果を格納
    i = 0  # leftの現在位置
    j = 0  # rightの現在位置

    # 両方の配列に要素が残っている間、小さい方を選んで追加
    # 例: left=[2, 5], right=[1, 8] の場合
    #   1回目: 1 < 2 → result=[1], j=1
    #   2回目: 2 < 8 → result=[1, 2], i=1
    #   3回目: 5 < 8 → result=[1, 2, 5], i=2
    while i < len(left) and j < len(right):
        # 左側の要素が小さいまたは等しい場合
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        # 右側の要素が小さい場合
        else:
            result.append(right[j])
            j += 1

    # どちらかの配列が尽きたら、残りの要素を全て追加
    # （残っている配列は既にソート済みなので、そのまま追加できる）
    # 例: left=[5] が残っている場合 → result=[1, 2, 5]
    result.extend(left[i:])
    result.extend(right[j:])

    return result
