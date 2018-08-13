class Solution:
    def isIsomorphic(self, s, t):
        """
        We are testing one-to-one mappings.
        Simply use a hash map that takes a letter from s and maps to t.
        We know there is no isomorphic mapping immediately when we encounter a new letter in s
        that maps to the same character in t. 
        
        Precondition: s and t are of the same length
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1, l2 = len(s), len(t)
        if l1 != l2: 
            raise ValueError("Argument strings must be of the same length.")
        
        t1, t2 = {}, {}
        for i in range(l1): 
            if s[i] in t1 and t1[s[i]] != t[i]: 
                return False
            t1[s[i]] = t[i]
            
            if t[i] in t2 and t2[t[i]] != s[i]: 
                return False
            t2[t[i]] = s[i]
               
        return True
        
def main():
    sol = Solution()
    assert sol.isIsomorphic("egg", "add") == True
    assert sol.isIsomorphic("foo", "bar") == False
    assert sol.isIsomorphic("paper", "title") == True

if __name__ == '__main__':
    main()