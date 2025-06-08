class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        remainder = n % 4
        val = n//4
        if remainder:
            return False
        else:
            return self.isPowerOfFour(val)
            