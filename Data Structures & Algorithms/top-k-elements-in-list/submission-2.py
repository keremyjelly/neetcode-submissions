class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        buckets = [ [] for i in range(len(nums) + 1) ]

        for num, freq in counts.items():
            buckets[freq].append(num)
        
        res = []
        for f in range(len(buckets) - 1, 0, -1):
            for item in buckets[f]:
                res.append(item)
                if len(res) == k:
                    return res
        return res