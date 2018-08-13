class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(s): 
            n = len(s)
            for i in range(len(s) // 2):
                if s[i] != s[n - i - 1]: return False
            return True
        
        def recurse(s, ans, cand):
            if not s: 
                print(len(cand) - 1)
                ans.append(cand)
                return 
            for i in range(len(s) - 1, -1, -1): 
                # -- partition here ---
                current = s[:i + 1]
                if is_palindrome(current):
                    recurse(s[i + 1:], ans, cand + [current])
                    
        ans, cand = [], []
        recurse(s, ans, cand)
        return ans 

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        def recurse(s, ans, cand):
            if not s:
                ans[0] = min(ans[0], len(cand) - 1)
                print(cand)
            for i in range(len(s)): 
                # -- partition here ---
                current = s[:i + 1]
                if current[:] == current[::-1]:
                    recurse(s[i + 1:], ans, cand + [current])
        ans, cand = [float("inf")], []
        recurse(s, ans, cand)
        return ans[0]

sol = Solution()
print(sol.partition("aba"))
print(sol.minCut("aaabaa"))
