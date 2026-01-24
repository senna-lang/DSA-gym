# O(n)
# https://leetcode.com/problems/can-place-flowers/submissions/1892134042
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        N = len(flowerbed)

        for i in range(N):
            if flowerbed[i] == 0:
                left = i == 0 or flowerbed[i - 1] == 0
                right = i == N - 1 or flowerbed[i + 1] == 0

                if left and right:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n
