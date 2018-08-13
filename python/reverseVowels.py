class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        stack = []
        for char in s:
            if char in vowels:
                stack.append(char)

        ans = ''
        for char in s:
            if char in vowels:
                ans += stack.pop()
            else:
                ans += char

        return ans

def main():
    a = 'hello'
    b = 'leetcode'
    c = 'aA'
    sol = Solution()
    print(sol.reverseVowels(a))
    print(sol.reverseVowels(b))
    print(sol.reverseVowels(c))

if __name__ == '__main__':
    main()