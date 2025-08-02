class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)
        total = Counter()

        for key in set(basket1 + basket2):
            total[key] = freq1[key] + freq2[key]
            if total[key] % 2 != 0:
                return -1
        
        extra1 = []
        extra2 = []

        for key in total:
            diff = freq1[key] - freq2[key]
            if diff > 0:
                extra1.extend([key] * (diff//2))
            elif diff < 0:
                extra2.extend([key] * (-diff//2))
        
        extra1.sort()
        extra2.sort(reverse=True)
        
        global_min = min(basket1 + basket2)
        total = 0

        for a, b in zip(extra1, extra2):
            total += min(min(a, b), 2 * global_min)
        return total