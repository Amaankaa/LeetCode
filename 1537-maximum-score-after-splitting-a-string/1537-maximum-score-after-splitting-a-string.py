class Solution:
    def maxScore(self, s: str) -> int:
        # Count total number of 1s in the string
        total_ones = s.count('1')
        
        left_zeros = 0
        current_ones_encountered = 0
        max_score = 0
        
        # Traverse the string, stopping at the second-to-last character
        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zeros += 1
            else:
                current_ones_encountered += 1
            
            # Calculate the right ones
            right_ones = total_ones - current_ones_encountered
            # Calculate the score for this split
            current_score = left_zeros + right_ones
            # Update the max score
            max_score = max(max_score, current_score)
        
        return max_score
