def searchBinary(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        middle = int((start + end) / 2)
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    return -1
