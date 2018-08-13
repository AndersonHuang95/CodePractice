class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        idx, n = 0, len(nums)
        while idx < n:
            start, end = str(nums[idx]), ""
            j = idx + 1
            while j < n:
                if (nums[j] - nums[idx]) == (j - idx):
                    end = str(nums[j])
                    j += 1
                else:
                    break
            ans += [start + "->" + end] if end else [start]
            idx = j # guaranteed to always increase by 1 every loop
        return ans

def main():
    x = [0, 2, 5, 6, 7, 8, 9, 10, 1003]
    sol = Solution()
    assert sol.summaryRanges([]) == []
    print(sol.summaryRanges(x))

if __name__ == "__main__":
    main()