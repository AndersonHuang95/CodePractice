import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = []
        n = len(nums)
        for i in range(k):
            heapq.heappush(pq, nums[i])
            
        for i in range(k, n):
            heapq.heappush(pq, nums[i])
            heapq.heappop(pq)
        ans = heapq.heappop(pq)
        return ans
        
def main():
    x = [2, 3, 1, 5, 6, 4]
    sol = Solution()
    print(sol.findKthLargest(x, 2))

if __name__ == main():
    main()