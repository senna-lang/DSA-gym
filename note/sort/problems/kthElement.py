import heapq


def kthElement(nums, k):
    N = len(nums)
    """
    O(N log N) でk番目に小さい値を追跡
    """
    # Pythonのheapqは最小ヒープなので、最大ヒープは値を反転
    max_heap = []  # k個の最小値を保持（最大ヒープ）
    min_heap = []  # 残りの要素（最小ヒープ）
    result = []

    for i in range(N):
        # 最大ヒープに追加（値を反転）
        heapq.heappush(max_heap, -nums[i])

        # 最大ヒープのサイズがkを超えたら、最大値を最小ヒープへ
        if len(max_heap) > k:
            largest = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, largest)

        # k個以上挿入されたら結果を記録
        if i >= k - 1:
            # 最大ヒープのトップ = k番目に小さい値
            result.append(-max_heap[0])

    return result
