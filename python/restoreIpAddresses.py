class Solution:
    def restoreIpAddresses(self, s):
        """
        We should try to chunk in 1, 2, 3 digit increments. We only add 
        to the list of return strings if we arrive at the end of string
        :type s: str
        :rtype: List[str]
        """
     	ans = []
     	self.recurse(self, s, ans)
     	return ans
        


        