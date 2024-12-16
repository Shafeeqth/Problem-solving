import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        pq = []
        for x in range(len(nums)):
            heapq.heappush(pq, (nums[x], x))
        
        heapq.heapify(pq)

        print(pq)
        
        while k:
            k -= 1
            heapq.heapreplace(pq, (pq[0][0] * multiplier, pq[0][1]))
        
        for x in pq:
            nums[x[1]] = x[0] # place the priority queue values to currect positions
        
        return nums
        