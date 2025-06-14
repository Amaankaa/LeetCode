class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        max_val = int(s)
        min_val = int(s)

        # Try all remappings for max
        for d1 in set(s):
            for d2 in '9876543210':
                remapped = s.replace(d1, d2)
                max_val = max(max_val, int(remapped))

        # Try all remappings for min
        for d1 in set(s):
            for d2 in '0123456789':
                remapped = s.replace(d1, d2)
                min_val = min(min_val, int(remapped))

        return max_val - min_val
