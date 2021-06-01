import heapq
def solution(operations):
    answer = []
    heap = []
    max_heap = []
    for i in operations:
        a, b = i.split()
        if a == 'I':
            b = int(b)
            heapq.heappush(heap, b)
            heapq.heappush(max_heap, (-1*b, b))
        else : 
            if len(heap) > 0:
                if b == '1':
                    heap.remove(heapq.heappop(max_heap)[1])
                else:
                    heapq.heappop(heap)
            else:
                pass
    if heap : 
        answer = [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    else : 
        answer = [0,0]
    return answer
