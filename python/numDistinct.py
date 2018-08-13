class Solution:
    def numDistinct(self, s, t):
        """
        Example: 

        Input: S = "babgbag", T = "bag"
        Output: 5
        Explanation:

        As shown below, there are 5 ways you can generate "bag" from S.
        (The caret symbol ^ means the chosen letters)

        babgbag
        ^^ ^
        babgbag
        ^^    ^
        babgbag
        ^    ^^
        babgbag
          ^  ^^
        babgbag
            ^^^
        
        Let's start by doing some elementary analysis. Say we wanted to solve this problem naively.
        We need a subsequence of s to compare to t. Consider t's length to be m and s's length to be
        n. Then the number of subsequences we potentially need to compare is bounded by 
        n choose m, which is factorial in nature. Of course, the number is less, since with 
        a subsequence, each subsequent letter after choosing the first must come after, so some
        combinations are not strictly valid. 

        A factorial-time algorithm doesn't sound appealing. How can we do better? We can, by using dynamic programming
    
            ""  b   a   b   g   b   a   g
        ""  1   1   1   1   1   1   1   1 

        b   0   1   1   2   2   3   3   3

        a   0   0   1   1   1   1   4   4   

        g   0   0   0   0   1   1   1   5       
        
        Build a table as follows: 
        check if j >= i and if t[i] == s[j] then for table[0.. i - 1, j - 1], sum nonzero, set to new table[i][j], else table[i][j - 1]
        j >= i: the given string must be longer than the target string
        t[j] == s[i]: a match occurs

        Two cases: 
        1. two conditions above hold -> match means we add to the running count of matching subsequences (carried over from the cell immediately adjacent, left)
        to the number of matching subsequences that the given string matched with the target string, minus the current character for both. 
        2. one of the two conditions breaks -> we carry over from the cell adjacent, left, since no new matches occurred. 

        Such a solution is O(N^2) space with O(N^2) time. 
        
        Args:
            s (string): given string to dissect subsequences 
            t (string): target string
        Returns:
            int: number of occurrences of target string as subseqeuence of given string
        """

        # Store occurrences of letters
        # table = {}
        # for idx, char in enumerate(s): 
        #     if char not in table: 
        #         table[char] = []
        #     table[char].append(idx)

        # candidates = [[]]
        # for char in t: 
        #     if char not in table: return 0
        #     new_candidates = []
        #     for cand in candidates: 
        #         if not cand: 
        #             new_candidates = [[idx] for idx in table[char]]
        #             break
        #         for idx in table[char]: 
        #             if cand and idx > cand[-1]: new_candidates.append([idx])
        #     candidates = new_candidates

        # return len(candidates)

        n, m = len(s), len(t)
        table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # --- base case: empty string can be found once in any given string ---
        for j in range(n + 1): 
            table[0][j] = 1

        for i in range(1, m + 1): 
            for j in range(1, n + 1): 
                if j >= i and s[j - 1] == t[i - 1]:
                    table[i][j] = table[i][j - 1] + table[i - 1][j - 1]
                else: 
                    table[i][j] = table[i][j - 1]
        return table[-1][-1]


sol = Solution()
print(sol.numDistinct("aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe", "bddabdcae"))

        