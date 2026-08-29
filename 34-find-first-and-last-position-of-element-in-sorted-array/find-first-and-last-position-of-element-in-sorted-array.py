class Solution:
    def lowerbound(self,nums,target):
        n= len(nums)
        l=0
        r=n-1
        ans=n

        while l<=r:
            mid= (l+r)//2

            if nums[mid]>=target:
                ans=mid
                r=mid-1
            else:
                #right shift
                l=mid+1
        
        return ans
    def upperbound(self,nums,target):
        n= len(nums)
        l=0
        r=n-1
        ans=n

        while l<=r:
            mid= (l+r)//2

            if nums[mid]>target:
                ans=mid
                r=mid-1
            else:
                #right shift
                l=mid+1
        
        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb=self.lowerbound(nums,target)
        ub=self.upperbound(nums,target)

        if lb==ub:
            #not prsent
            return [-1,-1]
        else:
            return [lb,ub-1]
        
