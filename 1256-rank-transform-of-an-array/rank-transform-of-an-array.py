class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = list(sorted(set(arr)))
        rank_dict = {}
        i = 1
        for x in sorted_arr:
            rank_dict[x] = i
            i+=1
        return [rank_dict[x] for x in arr]
        