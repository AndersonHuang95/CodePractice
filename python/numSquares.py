import math

class Solution(object):
    _table = [0]
    def numSquares(self, n):
        """
        At first glance, a greedy solution seems like the direction to go towards. However, after some examples, 
        we see that making the locally optimal choice does not yield a globally optimal solution in the end. 
        Take 43 for example. If we simply take largest squares first, we will get 36 + 4 + 1 + 1 + 1 = 43, yielding
        5 perfect squares. The optimal solution is actually 25 + 9 + 9 = 43, yielding 3 perfect squares. 
        
        When a greedy solution fails, this usually signals that dynamic programming will be of use, as we will need
        to cache subproblems to build a globall optimal solution. 
        
        Let's assume we have a table of entries in the range [0 .. n] and we are building in a bottom-up fashion;
        in other words, we will build from small subproblems up to the larger ones. Each dynamic programming solution
        involves a recurrence relation. The relation dictates how to build a problem from existing subproblems. 
        
        For this problem, the recurrence relation is of the form
        
        table[i] = min(table[i], x + 1)
        
        where x is some expression we will have to discover. Via the earlier discussion, we can't simply make the locally
        optimal choice. For example, we can't simply choose the largest square available. Instead, we go from bottom to top.
        Each time, we go through and see if we can improve upon our solution by adding a new, larger square. Looking
        at it from this point of view, we can see that it is a lot like the knapsack problem. 
        
        Notice that for each item, we need only examine squares up to sqrt(i), since anything larger will not fit in i.
        
        Another minor optimization we can make is to notice that since 1 is the smallest square, we can initialize the 
        minimum number of squares to be i for each i > 0, and start the calculation from the least square of 4 and onward.
        
        We use O(n) space for storage. The runtime is a little harder to analyze. The outer loop runs O(n) times, but
        the inner loop runs on average O(sqrt(n)) times. Therefore our runtime is around O(n^(3/2))
        :type n: int
        :rtype: int
        """
        table = self._table
        for num in range(1, n + 1): 
            max_root = math.floor(math.sqrt(num)) + 1
            current = num
            for root in range(2, max_root):
                current = min(current, table[num - root**2] + 1)
            table.append(current)
            print(num, table)
        return table[-1]

def main():
    sol = Solution()
    print(sol.numSquares(22))

if __name__ == "__main__":
    main()