class MySolution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        left = 0
        i = 0
        while left < N:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
            else:
                i += 1
            
            left += 1


class AdvanceSolution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                #  If the current element is non-zero, 
                # swap it with the element at index left. This effectively moves non-zero elements towards the beginning of the list.
                nums[right], nums[left] = nums[left], nums[right]
                #  Increment the left pointer to mark the next position where a non-zero element should be moved.
                left += 1
        