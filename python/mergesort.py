#!usr/bin/env python3

def mergesort(nums, left, right):
    if left >= right:
        return
    mid = left + (right - left) // 2
    mergesort(nums, left, mid)
    mergesort(nums, mid + 1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    first = nums[left:mid + 1]
    second = nums[mid + 1:right + 1]
    i, j = 0, 0
    k = left

    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            nums[k] = first[i]
            i += 1
        else:
            nums[k] = second[j]
            j += 1
        k += 1

    while i < len(first):
        nums[k] = first[i]
        i += 1
        k += 1

    while j < len(second):
        nums[k] = second[j]
        j += 1
        k += 1

def main():
    arr = [5, 2, 3, 7, 1, 4, 9, 8, 6, 10, 11, -1, -5, -2, -3, -4]
    mergesort(arr, 0, len(arr))
    print(arr)

if __name__ == "__main__":
    main()