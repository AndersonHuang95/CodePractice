class Solution(object):
    def candy(self, ratings):
        """
        If we are giving each child at least one candy, we are guaranteed to give at least N candies out. 
        Now we need to make sure to give extra candies only if the rating is greater than the neighbors.
        Two special cases arise: start of array, end of array 
        
        In a monotonically increasing sequence, there must be increasing candies (+1); once this sequence is
        broken, we can go back to giving one candy. 
        
        This applies to a forward pass and a backward pass in the algorithm. When doing a backward pass, 
        we must take care to take the max of whats already there, and adding 1 to the amount of candies
        at the original index. 
        """
        n = len(ratings)
        candies = [1 for _ in range(n)]
        
        # --- forward pass ---
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]: 
                candies[i] = candies[i - 1] + 1
                
        # --- backward pass ---
        for i in range(n - 1, 0, -1): 
            if ratings[i - 1] > ratings[i]: 
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)
                
        # --- summing all candies ---
        return sum(candies)

sol = Solution()
print(sol.candy([1, 0, 2]))