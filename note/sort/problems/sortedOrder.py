def insertionSort(nums, x):
    N = len(nums)

    for i in range(1, N):
        insertValue = nums[i]

        position = i
        while position > 0 and insertValue < nums[position - 1]:
            nums[position] = nums[position - 1]
            position -= 1

        nums[position] = insertValue

    for i in range(N):
        if nums[i] == x:
            return i + 1

    return -1


nums = [4, 7, 1, 3, 6, 8]

print(insertionSort(nums, 7))
