class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        for i in range(2**n):
            binary = bin(i)[2:].zfill(n)
            is_valid = True
            for j in range(len(binary) - 1):
                if binary[j] == '0' and binary[j + 1] == '0':
                    is_valid = False
                    break
            if is_valid:
                res.append(binary)
        
        return res
