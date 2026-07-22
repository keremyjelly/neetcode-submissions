class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for l in s:
                idx = ord(l) - ord('a')
                count[idx] += 1
            res[str(count)].append(s)
        return list(res.values())
