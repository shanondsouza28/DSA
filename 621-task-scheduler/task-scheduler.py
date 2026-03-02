class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) # prepares hasmap of all the alphabets with their count
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q=deque() # [-c,time +n] current tasks of a kind , idle time
        time = 0

        while maxHeap or q:
            time +=1
            if maxHeap:
                currCount = heapq.heappop(maxHeap) + 1
                if currCount:
                    q.append([currCount, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time

   
            


        