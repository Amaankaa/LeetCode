class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dict_.keys():
                return [i, dict_[difference]]
            dict_[nums[i]] = i