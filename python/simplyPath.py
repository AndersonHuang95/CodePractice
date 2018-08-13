class Solution:
    def simplifyPath(self, path):
        """
        Sounds like a stack will be very useful in this scenario. 

        We simply split on the forward slashes. We can do this manually with string parsing
        or we can use the built-in split() method in python with a delimiter. 

		Example: "/a/./b/../../c/"

        :type path: str
        :rtype: str
        """
        stack = path.split('/')
        ans = []
        for s in stack: 
        	if s == '..' and ans: 
        		ans.pop()
        	elif s == '..' or s == '.' or s == '':
        		pass
        	else: 
        		ans.append(s)
        return '/' + '/'.join(ans)

sol = Solution()
print(sol.simplifyPath("/a/./b/../../c/"))
        