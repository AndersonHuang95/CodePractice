class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}
        left, ans = 0, 0
        for right, char in enumerate(s):
            if len(table) <= 2: 
                table[char] = right
            if len(table) > 2:
                # find left-most index
                leftmost = len(s)
                for entry in table:
                    leftmost = min(leftmost, table[entry])
                table.pop(s[leftmost])
                left = leftmost + 1
            print(right, left)
            ans = max(ans, right - left + 1)      
        return ans

def main():
    x = "eceba"
    sol = Solution()
    print(sol.lengthOfLongestSubstringTwoDistinct(x))

if __name__ == "__main__":
    main()