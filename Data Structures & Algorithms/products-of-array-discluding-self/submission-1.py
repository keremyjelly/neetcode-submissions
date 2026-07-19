class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        for i in range(len(nums)):
            l, r = i - 1, i + 1
            while True:
                if l >= 0:
                    prod[i] *= nums[l]
                    l -= 1
                elif r < len(nums):
                    prod[i] *= nums[r]
                    r += 1
                else:
                    break
        return prod
