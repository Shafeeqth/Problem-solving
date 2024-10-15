class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionery = defaultdict(list)
        for x in strs:
            srtd = ''.join(sorted(x))
            dictionery[srtd].append(x)
        return dictionery.values()
       
        