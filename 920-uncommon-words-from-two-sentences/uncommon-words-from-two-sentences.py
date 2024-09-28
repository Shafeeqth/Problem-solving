class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        my_dict = {}
        arrS1 = s1.split(" ")
        arrS2 = s2.split(" ")
        for x in arrS1:
            my_dict[x] = my_dict[x] + 1 if x in my_dict else 1
        for x in arrS2:
            my_dict[x] = my_dict[x] + 1 if x in my_dict else 1
        return [x for x, y in my_dict.items() if y == 1]
