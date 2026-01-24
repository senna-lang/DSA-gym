# O(n)
class MySolution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        N = len(nums)
        res = [0] * N

        l = 1
        for i in range(N):
            res[i] = l
            l *= nums[i]

        r = 1
        for i in range(N - 1, -1, -1):
            res[i] *= r
            r *= nums[i]

        return res
