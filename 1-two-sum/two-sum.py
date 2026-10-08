class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict= {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in dict:
                return [dict[rem], i]

            dict[nums[i]] = i