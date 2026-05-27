class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for st in strs:
            count = [0] * 26
            for s in st:
                count[ord(s) - ord('a')] += 1
            sorted_st = tuple(count)
            if sorted_st in seen:
                seen[sorted_st].append(st)
            else:
                seen[sorted_st] = [st]
        return list(seen.values())