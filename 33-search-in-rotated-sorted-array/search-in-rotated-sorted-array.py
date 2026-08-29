class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        rot = bisect_left(nums, True, key=lambda n: n <= nums[-1])
        
        l=0
        r=n - 1

        while l <= r:
            mid = (l + r) // 2
            real = (mid + rot) % n

            if nums[real] == target:
                return real
                
            if nums[real] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1