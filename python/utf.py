#!/usr/bin/env python3

class Solution:
    OFFSET = 8
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        idx = 0
        n = len(data)
        while idx < n:
            leading_ones = self.numLeadingOnes(data[idx])
            if leading_ones == 1 or leading_ones > 4:
                return False

            idx += 1
            if not leading_ones:
                continue

            cont = leading_ones - 1
            while idx < n and cont > 0: 
                if self.isContinuationCharacter(data[idx]):
                    cont -= 1
                    idx += 1
                else:
                    return False
            if cont: 
                return False
        return True

    
    def isContinuationCharacter(self, byte):
        return (byte >> (self.OFFSET - 2)) == 2
    
    def numLeadingOnes(self, byte):
        ans = 0
        for i in range(self.OFFSET - 1, -1, -1):
            if (byte >> i) & 1 == 1:
                ans += 1
            else:
                break
        return ans

def main():
    t1 = [197, 130, 1]
    t2 = [235, 140, 4]

    sol = Solution()
    print(sol.validUtf8(t1))
    print(sol.validUtf8(t2))

if __name__ == '__main__':
    main()