class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        res = 0
        costs.sort(key = lambda cost:cost[0] - cost[1])
        for costa, costb in costs:
            if n:
                res += costa
                n -= 1
            else:
                res += costb
        return res