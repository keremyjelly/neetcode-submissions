class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = collections.defaultdict(list)
        for s in strs:
            counts[tuple(sorted(s))].append(s)
        return list(counts.values())