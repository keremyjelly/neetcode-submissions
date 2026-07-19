class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        for i in range(len(nums)):
            tmp = prod[i]
            prod = list(map(lambda x: x * nums[i], prod))
            prod[i] = tmp
        return prod
