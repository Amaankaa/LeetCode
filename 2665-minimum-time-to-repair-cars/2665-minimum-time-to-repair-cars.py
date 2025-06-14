class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, ranks[0] * cars * cars
        res = -1

        while l <= r:
            m = (l + r)//2
            repaired = 0

            for rank in ranks:
                repaired += int(sqrt(m/rank))
            
            if repaired >= cars:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res