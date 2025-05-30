class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        res = 0
        for freq, val in cnt.items():
            group_size = freq + 1
            groups_needed = ceil(val/group_size)
            res += groups_needed * group_size
        return res