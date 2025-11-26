def median_of_medians(a, k):
    """
    Median of Medians アルゴリズム
    k番目に小さい要素を 最悪ケースでも O(N) で求める

    通常のクイック選択は最悪 O(N^2) だが、このアルゴリズムは
    「良いピボット」を選ぶことで O(N) を保証する

    アルゴリズムの流れ:
    1. 配列を5要素ずつのグループに分割
    2. 各グループの中央値を求める
    3. 中央値たちの中央値を求める（これがピボット）
    4. ピボットで配列を3分割してクイック選択

    なぜ O(N) なのか:
    - ピボットは全体の約30%の要素より大きく、約30%より小さい
    - つまり、次の再帰では最大70%の要素しか残らない
    - T(N) = T(N/5) + T(7N/10) + O(N) = O(N)

    Args:
        a: 配列（元の配列は変更されない）
        k: 何番目か (1-indexed, 1 <= k <= len(a))

    Returns:
        k番目に小さい値

    例:
        a = [5, 3, 8, 1, 9, 2, 7]
        median_of_medians(a, 3) -> 3
        # ソート後 [1, 2, 3, 5, 7, 8, 9] の3番目
    """

    def find_median(arr):
        """
        5要素以下の配列の中央値を求める

        小さい配列なので単純にソートして中央値を返す
        O(1) 時間（要素数が定数なので）

        Args:
            arr: 5要素以下の配列

        Returns:
            中央値
        """
        arr.sort()
        return arr[len(arr) // 2]

    def select(arr, k):
        """
        k番目に小さい要素を求める (再帰的実装)

        Args:
            arr: 対象配列
            k: 何番目か (1-indexed)

        Returns:
            k番目に小さい値
        """
        n = len(arr)

        # === ベースケース: 要素が少ない場合はソート ===
        # 5要素以下ならソートして直接k番目を返す
        # O(1) 時間（要素数が定数なので）
        if n <= 5:
            arr.sort()
            return arr[k - 1]  # k は1-indexed なので -1

        # === ステップ1: 5要素ずつのグループに分割し、各中央値を求める ===
        # 例: [1,2,3,4,5,6,7,8,9,10,11,12,13] を
        #     [1,2,3,4,5], [6,7,8,9,10], [11,12,13] に分割
        #     各グループの中央値: [3, 8, 12]
        medians = []
        for i in range(0, n, 5):  # 0, 5, 10, 15, ... と進む
            group = arr[i : i + 5]  # 5要素ずつ切り出し（最後は5未満でもOK）
            medians.append(find_median(group))

        # この時点で medians には各グループの中央値が入っている
        # medians の長さは約 N/5

        # === ステップ2: 中央値たちの中央値を求める (再帰) ===
        # medians の中央値を求めるために、自分自身を再帰呼び出し
        # これが「良いピボット」となる
        # T(N/5) の時間
        pivot = select(medians, len(medians) // 2 + 1)

        # なぜこのピボットが良いのか:
        # - 少なくとも半分のグループの中央値より大きい
        # - つまり、全体の約30%の要素より確実に大きい
        # - 同様に約30%の要素より確実に小さい
        # → 次の再帰で要素数が最大70%に減る

        # === ステップ3: ピボットで3つのグループに分割 ===
        # クイック選択と同じ分割処理
        # O(N) 時間（全要素を1回走査）
        left = [x for x in arr if x < pivot]      # ピボットより小さい
        middle = [x for x in arr if x == pivot]   # ピボットと等しい
        right = [x for x in arr if x > pivot]     # ピボットより大きい

        # 例: arr = [5,3,8,1,9,2,7], pivot = 5
        #     left = [3,1,2], middle = [5], right = [8,9,7]

        # === ステップ4: k番目がどのグループにあるか判定 ===
        # left, middle, right のどこにk番目があるかを調べる

        if k <= len(left):
            # k番目は left グループにある
            # 例: k=2 で len(left)=3 なら、left の中の2番目
            return select(left, k)

        elif k <= len(left) + len(middle):
            # k番目は middle グループにある（ピボット自身）
            # 例: k=4 で len(left)=3, len(middle)=1 なら、
            #     left に3個、middle に1個で合計4個
            #     つまりピボットが4番目
            return pivot

        else:
            # k番目は right グループにある
            # left と middle をスキップした位置を探す
            # 例: k=6 で len(left)=3, len(middle)=1 なら、
            #     right の中の 6-3-1=2番目
            return select(right, k - len(left) - len(middle))

    # メイン処理: select を呼び出す
    return select(a, k)
