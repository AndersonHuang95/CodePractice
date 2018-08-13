#!/usr/bin/env python3

class Solution():
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        if not n or not m:
            raise ValueError("Invalid text or pattern supplied")
        table = [[False] * (n + 1) for _ in range(m + 1)]
        for j in range(1, n):
            if p[j] == '*' and table[0][j - 1]:
                table[0][j + 1] = True

        for i in range(m):
            for j in range(n):
                if p[j] == '.' or p[j] == s[i]:
                    table[i + 1][j + 1] = table[i][j]
                if p[j] == '*':
                    if p[j - 1] != s[i - 1] and p[j - 1] == '.':
                        table[i + 1][j + 1] = table[i + 1][j - 1]
                    else:
                        table[i + 1][j + 1] = table[i + 1][j] or table[i + 1][j - 1] or table[i][j + 1]
        return table[-1][-1]
