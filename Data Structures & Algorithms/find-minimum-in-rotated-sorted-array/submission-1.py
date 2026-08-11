class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            
            mid = (l + r) // 2
            print(l,r,mid)

            if nums[mid] < nums[r]:
                r = mid 
            else:
                l = mid + 1
        print(l,r,mid)        
        return nums[l]