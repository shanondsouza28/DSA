class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)


        while k > 0:
            largestKth = heapq.heappop(nums)#log n 
            k -= 1
        return largestKth * -1