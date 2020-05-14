'''
heapq 모듈: 이진트리 기반의 최소 힙(min heap) 자료구조를 제공함. 일반적인 리스트를 최소 힙처럼 쓸 수 있다.
* min heap => 모든 노드는 자식 노드보다 작거나 같다.
* heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]
* index 0(root)에 최솟값이 위치함
* 원소들을 항상 정렬된 상태로 추가/삭제 가능
    * heap = []
    * 원소 추가: heapq.heappush(heap, element)  # O(logN)
    * 원소 삭제 (가장 작은 원소를 삭제함): heapq.heappop(heap)
    * 최솟값 seek: heap[0]  # 주의: heap[1]은 두번째로 작은 값이 아님. heappop()으로 최솟값을 삭제하고 heap[0]으로 얻어야 함.
* 리스트를 힙으로 변환: heap.heapify(heap)  # O(N)

* 최대 힙으로 바꾸기: 힙의 원소를 (우선순위, 값)으로 설정하기 -> 0번째 인덱스인 우선순위를 기준으로 최소 힙이 구성됨
* K번째 최소/최댓값 구하기: 힙에 모두 push -> K번 pop (K번째 최솟값)
* 힙 정렬: 힙에 모두 push -> 힙에서 차례로 pop하고 리스트에 append
'''

import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while scoville[0] < K:
        #print(s)
        if len(scoville) == 1:
            return -1
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        heapq.heappush(scoville, s1 + s2*2)
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
print(solution([1, 2, 3, 3], 4))  # 1
print(solution([1, 2, 3, 3], 10))  # 3
