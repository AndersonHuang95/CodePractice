from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """Finds majority element
        
        A anive solution can use a hash map to store the results. We go through the hash map and find the 
        maximum item with a count. This is similar to using a counter.

        However, we are given an extra piece of information: namely that the majority element always appears more than
        floor(n/2) times or more. For example, in a list of 9 elements, the majority element is guaranteed
        to appear more than floor(9/2) = 4 times. With this extra piece of information, we may be able make use of more
        info.

        :type nums: List[int]
        :rtype: int
        """
        # table = defaultdict(int)
        # for num in nums: 
        #     table[num] += 1

        # ans = (-1, 0)
        # for key in table: 
        #     if table[key] > ans[1]:
        #         ans = (key, table[key])

        # return ans[0]

        mode, count = -1, 0
        for num in nums: 
            if count == 0:
                count += 1
                mode = num
            elif num == mode: 
                count += 1
            else: 
                count -= 1
        return mode

def main():
    sol = Solution()
    print(sol.majorityElement([3,2,3]))
    print(sol.majorityElement([2,2,1,1,1,2,2]))


if __name__ == '__main__':
    main()