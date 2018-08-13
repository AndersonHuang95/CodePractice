#!/usr/bin/env python3

def binary_search(nums, target):
	start, end = 0, len(nums)
	while start < end: 
		mid = (start + end) // 2
		if nums[mid] > target: end = mid
		elif nums[mid] < target: start = mid + 1
		else: return mid
	return -1 

x = [0, 1, 2, 3, 4, 5]
print(binary_search(x, 0))
print(binary_search(x, 1)) 
print(binary_search(x, 2)) 
print(binary_search(x, 3)) 
print(binary_search(x, 4)) 
print(binary_search(x, 5)) 
print(binary_search(x, 6)) 