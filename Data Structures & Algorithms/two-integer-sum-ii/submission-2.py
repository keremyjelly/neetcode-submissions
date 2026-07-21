class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = [ (i + 1, j + 1) for i in range(len(numbers)) for j in range(i, len(numbers)) if numbers[i] + numbers[j] == target ]
        return list(res[0])