class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set=set(nums)
        longest=0
        for num in new_set:
            if num-1 not in new_set:
                length=1
                while num+length in new_set:
                    length+=1
            
                longest=max(longest,length)
        return longest