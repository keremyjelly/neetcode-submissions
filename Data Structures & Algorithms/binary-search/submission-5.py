import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        return (idx if idx < len(nums) and nums[idx] == target else -1)
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     mid = l + (r - l) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return -1