class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for st in strs:
            count = [0] * 26
            for s in st:
                count[ord(s) - ord('a')] += 1
            dic_key = tuple(count)
            if dic_key in seen:
                seen[dic_key].append(st)
            else:
                seen[dic_key] = [st]
        return list(seen.values())