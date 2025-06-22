class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        radius = 0
        heaters.sort()

        for house in houses:
            radius = max(radius, self.close_dist(house, heaters))
        return radius

    def close_dist(self, house, heaters):
        min_dist = float('inf')        
        left, right = 0, len(heaters) - 1

        while left <= right:
            mid = (left + right)//2
            min_dist = min(min_dist, abs(heaters[mid] - house))

            if heaters[mid] < house:
                left = mid + 1
            else:
                right = mid - 1
        
        return min_dist