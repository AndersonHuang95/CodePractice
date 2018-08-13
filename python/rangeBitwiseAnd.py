#!/usr/bin/env python3

class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans, seen = 0, False
        for i in range(31, -1, -1):
            if (m >> i) & (n >> i) == 1:
                ans += (1 << i)
                seen = True
            elif seen:
                break 
        return ans
    
    def rangeBitwiseAnd2(self, m, n):
        ans = m 
        for i in range(m, n + 1): 
            ans &= i
        return ans

def main():
    sol = Solution()
    print(sol.rangeBitwiseAnd(5, 7))
    assert sol.rangeBitwiseAnd2(5, 7) == 4

if __name__ == '__main__':
    main()
