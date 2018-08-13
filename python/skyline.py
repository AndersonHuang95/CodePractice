import heapq
from collections import defaultdict, OrderedDict

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        # critical points maps from building -> [left end, right end]
        critical_points = defaultdict(list)
        for building in buildings:
            critical_points[building[0]] += [building]
            critical_points[building[1]] += [building]
        
        critical_points = OrderedDict(sorted(critical_points.items(), key=lambda x: x[0]))
        
        # use heapq to hold heights
        ans, pq = [], []
        for critical_point, building in critical_points.items():
            for building in critical_points[critical_point]:
                if critical_point == building[0]:
                    heapq.heappush(pq, -building[2])
                # right edge of rect
                else:
                    pq.remove(-building[2])
                    heapq.heapify(pq)

            if len(pq) == 0:
                ans.append([critical_point, 0])
            else:
                height = -pq[0]
                if not ans or ans[-1][1] != height:
                    ans.append([critical_point, height])
        return ans

        # --- O(N^2) solution follows ---
        # for critical_point in critical_points:
        #     for building in buildings:
        #         if critical_point[0] >= building[0] and critical_point[0] < building[1]:
        #             critical_point[1] = max(critical_point[1], building[2])
        
        # ans = []
        # # remove duplicate horizontal lines
        # for critical_point in critical_points:
        #     if not ans: 
        #         ans.append(critical_point)
        #         continue
        #     last = ans[-1]
        #     if last[1] != critical_point[1]:
        #         ans.append(critical_point)      
        # return ans
        
def main():
    x = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    y = [[0,2,3],[2,5,3]]
    sol = Solution()
    print(sol.getSkyline(y))

if __name__ == "__main__":
    main()