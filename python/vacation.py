#!/usr/bin/env python3

class Solution:
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]] - N x N matrix (adjacency matrix)
        :type days: List[List[int]] - N x K matrix (shows maximum vacation days for each city, for each week)
        :rtype: int
        """
        cities = len(days)
        weeks = len(days[0]) if days else 0
        table = [0 for _ in range(cities)]
        # return self.dfs(flights, days, cities, weeks, 0, 0, table)
        for week in range(weeks - 1, -1, -1):
            next_table = [0 for _ in range(cities)]
            for city in range(cities):
                next_table[city] = table[city] + days[city][week]
                for next_city in range(cities):
                    if flights[city][next_city] == 1:
                        next_table[city] = max(next_table[city], table[next_city] + days[next_city][week])
            table = next_table
        return table[0]


    def dfs(self, flights, days, cities, weeks, city_no, week_no, table):
        if week_no == weeks:
            return 0
        if table[city_no][week_no] != float("-inf"):
            return table[city_no][week_no]
        ans = 0
        for i in range(len(flights)):
            if i == city_no or flights[city_no][i] == 1:
                vacation_days = days[i][week_no] + self.dfs(flights, days, cities, weeks, i, week_no + 1, table)
                ans = max(ans, vacation_days)
        table[city_no][week_no] = ans
        return ans

def main():
    flights = [[0,1,1],[1,0,1],[1,1,0]]
    days = [[1,3,1],[6,0,3],[3,3,3]]
    flights2 = [[0,0,0],[0,0,0],[0,0,0]]
    days2 = [[1,1,1],[7,7,7],[7,7,7]]
    sol = Solution()
    print(sol.maxVacationDays(flights2, days2))

if __name__ == '__main__':
    main()