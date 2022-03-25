"""
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.



Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
"""


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        loc_cost = []
        length = len(costs)
        min_cost = 0

        for i in range(length):
            loc_cost.append((costs[i][1] - costs[i][0], i))

        loc_cost = sorted(loc_cost, reverse=True)

        for i in range(length):
            index = loc_cost[i][1]
            if i < length / 2:
                min_cost += costs[index][0]
            else:
                min_cost += costs[index][1]

        return min_cost

"""
Success
Details
Runtime: 55 ms, faster than 59.04% of Python3 online submissions for Two City Scheduling.
Memory Usage: 13.9 MB, less than 82.59% of Python3 online submissions for Two City Scheduling.
"""
