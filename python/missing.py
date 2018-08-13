class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ans = []
        nums.insert(0, lower - 1)
        nums.append(upper + 1)
        idx = 1
        while idx < len(nums):
            diff = nums[idx] - nums[idx - 1]
            start, end = "", ""

            if diff == 2: 
                start = str(nums[idx - 1] + 1)
            elif diff > 2:
                start = str(nums[idx - 1] + 1)
                end = str(nums[idx] - 1)
            
            current = ""
            if start: current += start
            if end: current += ("->" + end)
            if current: ans.append(current)

            idx += 1
        return ans

def main():
    a = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    sol = Solution()
    print(sol.findMissingRanges(a, lower, upper))

if __name__ == "__main__":
    main()