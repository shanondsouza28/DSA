class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceHeap =[]

        for x,y in points:
            distance = (x**2) + (y**2)
            distanceHeap.append([distance,x,y])

        heapq.heapify(distanceHeap)
        result =[]

        while k >0:
            distance,x,y =heapq.heappop(distanceHeap)
            result.append([x,y])
            k -=1
        return result

        