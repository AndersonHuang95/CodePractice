class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ans = ""
        if self.is_palindrome(s):
            return s
        for i in range(1, n):
            candidate = s[i:][::-1] + s
            if self.is_palindrome(candidate):
                ans = candidate
        return ans
    
    def is_palindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right: 
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

def main():
    s = "abcd"
    sol = Solution()
    assert sol.shortestPalindrome("aacecaaa") == "aaacecaaa"

if __name__ == '__main__':
    main()
