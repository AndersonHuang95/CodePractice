class Solution(object):
    def titleToNumber(self, s):
        """Returns a column mapping to a number
        
        This is the opposite of the problem we experienced last time, the trickiest part is to handle
        the 1-indexing instead of 0-indexing.
        
        Let's handle 'ZY' as a example. 
        
        0. ans = 0 
        
        'ZY'
         ^--
        
        1. Get mapping for Z -> 25, add 1. ans = 0 * 26 + 26

        'ZY'
          ^--
        
        2. Get mapping for Y -> 24, add 1. ans = 26 * 26 + 25 = 676 + 25 = 701 
        
        So to account for the 1-indexing, we simply add one after we construct the mapping. We 
        can also do this in the dictionary to begin with. Either way will work.
        
        :type s: str
        :rtype: int
        """
        
        letters = [char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        nums = [num for num in range(26)]
        table = dict(zip(letters, nums))
        
        ans = 0
        for letter in s: 
            value = table[letter]
            ans = ans * 26 + value + 1
        return ans
        
def main():
    sol = Solution()
    assert sol.titleToNumber("A") == 1
    assert sol.titleToNumber("") == 0
    assert sol.titleToNumber("ZY") == 701
    assert sol.titleToNumber("ABY") == 28