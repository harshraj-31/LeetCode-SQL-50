class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)

        if start > end:
            return 0

        before = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

        def day_of_year(date):
            return before[int(date[:2]) - 1] + int(date[3:])

        return day_of_year(end) - day_of_year(start) + 1