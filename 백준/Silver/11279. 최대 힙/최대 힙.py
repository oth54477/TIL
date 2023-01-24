import sys

def heap_push(item):
    heap.append(item)
    child = len(heap) - 1
    parent = child // 2

    while parent > 0 and heap[parent] < heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2

def heap_pop():
    if len(heap) <= 2:
        return heap.pop()

    item = heap[1]
    heap[1] = heap.pop()
    parent = 1
    child = parent * 2

    while child < len(heap):
        if child + 1 < len(heap) and heap[child] < heap[child+1]:
            child+=1
        if heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            child = parent * 2
        else:
            break
    return item





input = sys.stdin.readline

heap = [0]
n = int(input().strip())
for _ in range(n):
    x = int(input().strip())
    if x != 0:
        heap_push(x)
    else:
        if len(heap) == 1:
            print(0)
        else:
            print(heap_pop())