class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        finallist = []
        intervals.sort()
        current0 = intervals[0][0]
        current1 = intervals[0][1]
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= current1:
                if intervals[i][1] > current1:
                    current1 = intervals[i][1]
            else:
                finallist.append([current0, current1])
                current0 = intervals[i][0]
                current1 = intervals[i][1]
            i += 1
        finallist.append([current0, current1])
        return finallist

            