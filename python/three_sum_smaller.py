from collections import defaultdict

class Solution:
    def threeSumSmaller(self, nums, target):
        """
        Modify our search and leverage sorting to increase our runtime performance.
        We fix an element each time, and modify the target by decrementing it by the
        value of the element. Then we check two numbers in the portion of the list
        to the right of said element, and check that thse two elements, b and c, sum
        to less than (target - a), where a is the fixed element.

        So, instead of solving

        a + b + c < target

        We solve 

        b + c < target - a

        A special case arises that doesn't come up in normal three-sum. Namely, there
        are scenarios where we should move the left pointer backwards. This occurs because
        we are not only solving for equality.
    
        Check duplicates later.

        Sorting takes O(n log n) time, while looping takes O(n^2) time.

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        ans = []
        nums.sort()
        for idx in range(n - 2):
            current = nums[idx]
            new_target = target - current
            left = idx + 1, n - 1
            while left < right:
                if nums[left] + nums[right] < new_target:
                    ans += right - left
                    left += 1
                else: 
                    right -= 1
        return ans

    def brute_force(self, nums, target):
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    print(i, j, k)
                    if nums[i] + nums[j] + nums[k] < target:
                        ans += 1
        return ans

def main():
    a = [-2, 0, 1, 3]
    b = [-5, -3, 2, 10, 11]
    sol = Solution()
    print(sol.brute_force(a, 2))

if __name__ == "__main__":
    main()