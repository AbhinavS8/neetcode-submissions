"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key = lambda x: x.start)

        ends = []
        
        for i in intervals:

            
            
            heapq.heappush(ends,i.end)

            if ends[0]<=i.start:
                heapq.heappop(ends)
        
        return len(ends)

        