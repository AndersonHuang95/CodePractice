class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        Let's think through this problem. We are given some constraints which make our error checking much easier. 
        Off the bat, we can think of a naive solution that runs in O(n^2). Consider every node as a starting point, 
        and traverse the array until we arrive back at the original starting point. If at any point we do not have
        enough gas to continue, we try the next index. 
        
        The question becomes can we do any better? 
        
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, supply, extra = 0, 0, 0
        i = 0
        while i < len(gas):
            print(i, supply, extra)
            supply = supply + gas[i] - cost[i]
            # --- if we can't reach the next node, start a new search from next node --- 
            if supply < 0: 
                extra += supply 
                supply = 0 
                start = i + 1
            i += 1
        print(supply, extra)
        return start if (supply + extra) >= 0 else -1

sol = Solution()
print(sol.canCompleteCircuit([1,2,3,4,3,2,4,1,5,3,2,4], [1,1,1,3,2,4,3,6,7,4,3,1]))