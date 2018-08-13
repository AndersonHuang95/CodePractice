#!/usr/bin/env python3

import random

def qs(nums):
    quicksort(nums, 0, len(nums) - 1)

def quicksort(nums, left, right):
    """Uses quicksort algorithm to order a list of numbers

    Args:
        nums (List[int]):
    Returns:
        (void):
    """
    if left >= right: 
        return
    pivot = partition(nums, left, right)
    quicksort(nums, left, pivot - 1)
    quicksort(nums, pivot + 1, right)

def partition(nums, left, right): 
    # choose a random item as the pivot, stuff it at the highest element (index: right)
    # x = random.randrange(left, right + 1)
    # nums[x], nums[right] = nums[right], nums[x]

    i = left
    for j in range(left, right):
        if nums[j] <= nums[right]: 
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[right], nums[i] = nums[i], nums[right]
    return i

def quickselect(nums, k):
    random.shuffle(nums)
    n = len(nums)
    k = n - k
    left, right = 0, n - 1
    while left < right:
        pivot = partition(nums, left, right)
        if pivot < k: 
            left = pivot + 1
        elif pivot > k:
            right = pivot - 1
        else:
            break
    return nums[pivot]

def main():
    a = [3, 7, 2, 4, 1, 6, 8, 9, 5, 3, -3, -3, -1000]
    print(quickselect(a, 2))

if __name__ == main():
    main()


