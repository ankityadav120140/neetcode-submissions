class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for st in strs:
            sorted_st = ''.join(sorted(st))
            if sorted_st in seen:
                seen[sorted_st].append(st)
            else:
                seen[sorted_st] = [st]
        ans = []
        for k,v in seen.items():
            ans.append(v)
        return ans