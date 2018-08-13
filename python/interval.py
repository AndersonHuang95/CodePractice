#!/usr/bin/env python3

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        Pseudocode: 
        Possibly preprocess badly-formatted intervals, e.g. (5, -1), 
        those intervals in reverse order
		Sort the intervals by (start, end) -> this simplifies comparisons 
		Create new list to hold modified intervals
		Pairwise compare adjacent intervals and merge according to the rules:
			(As <= Bs) and (Ae < Be) and (Ae) => merge into (As, Be)
			(As <= Bs) and (Ae >= Be) => merge into (As, Ae)
			otherwise, add (Bs, Be)
		Return answer array 
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ### Preprocessing would go here ###
        intervals.sort(key=lambda x: (x.start, x.end))
        ans = []
        ### pairwise compare ###
        for interval in intervals: 
        	if not ans: ans.append(interval); continue
        	A, B = ans[-1], interval
        	if A.start <= B.start and A.end < B.end and A.end >= B.start:
        		A.end = B.end
        	elif A.start <= B.start and A.end >= B.end:
        		A.end = A.end 
        	else:
        		ans.append(B)
        return ans

    def insert(self, intervals, newInterval): 
        # find the rightful place for newInterval
        for i in range(len(intervals)): 
            if newInterval.start <= intervals[i].start and newInterval.end <= intervals[i].end:
                break
        intervals.insert(i, newInterval)
        return self.merge(intervals)




        
