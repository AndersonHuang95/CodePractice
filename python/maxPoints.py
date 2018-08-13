# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        """
        Use slope to track lines

        Time: O(n^2)
        Space: O(n)
        :type points: List[Point]
        :rtype: int
        """
        if not points: return 0
        if len(points) <= 2: return len(points)

        n = len(points)
        ans = 0
        for i in range(n):
            duplicates = 0
            # Map times slope has been seen
            table = defaultdict(int)
            for j in range(i + 1, n):
                # Calculate slope
                if points[j].x > points[i].x:
                    rise = points[j].y - points[i].y
                    run = points[j].x - points[i].x
                else:
                    rise = points[i].y - points[j].y
                    run = points[i].x - points[j].x

                # Find duplicate points
                if not rise and not run:
                    duplicates += 1

                # Add abs value of slope (slope depends on which point comes first) to map
                # We must account for lines parallel to x-axis (0 slope) and y-axis(infinite slope)
                # Because these are special cases, we store a tuple to help us differentiate
                slope = self.getSlope(rise, run)
                if slope not in table:
                    table[slope] = 0

                if not slope:
                    table[(slope, points[i].y)] += 1
                elif slope == float("inf"):
                    table[(slope, points[i].x)] += 1
                else:
                    table[(slope, 1)] += 1
            current = 0
            # duplicates are on the same line, and we add 1 to account for the original point in question
            for slope, times in table.items():
                current = max(current, duplicates + 1 + times)
            ans = max(current, ans)
        return ans

    def getSlope(self, rise, run):
        """Returns normalized slope
        """
        return rise / run if run else float("inf")

def main():
    a = Point(0, 0)
    b = Point(1, 1)
    c = Point(2, 2)
    d = Point(3, 3)
    points = [a, b, c, d]

    sol = Solution()
    print(sol.maxPoints(points))

if __name__ == '__main__':
    main()
