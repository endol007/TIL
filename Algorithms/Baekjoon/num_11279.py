import heapq, sys

t = int(sys.stdin.readline())
max_heap = []
for i in range(t):
    n = int(sys.stdin.readline())
    if n:heapq.heappush(max_heap, -n)
    else:print(-heapq.heappop(max_heap)if max_heap else 0)



# import sys
#
# t = int(sys.stdin.readline())
#
#
# class Maxheap:
#     def __init__(self):
#         self.items = [None]
#
#     def insert(self, value):
#         self.items.append(value)
#         cur_index = len(self.items) -1
#
#         while cur_index > 1:
#             parent_index = cur_index //2
#             if self.items[parent_index] < self.items[cur_index]:
#                 self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
#                 cur_index = parent_index
#             else:
#                 break
#
#     def delete(self):
#         self.items[1], self.items[-1] = self.items[-1], self.items[1]
#         prev_max = self.items.pop()
#         cur_index = 1
#
#         while cur_index <= len(self.items) - 1:
#             left_child_index = cur_index * 2
#             right_child_index = cur_index * 2 + 1
#             max_index = cur_index
#
#             if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
#                 max_index = left_child_index
#
#             if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
#                 max_index = right_child_index
#
#             if max_index == cur_index:
#                 break
#
#             self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
#             cur_index = max_index
#
#         return prev_max
#
# max_heap = Maxheap()
# for i in range(t):
#     h = int(sys.stdin.readline())
#     if h == 0:
#         if len(max_heap.items) == 1:
#             print(0)
#         elif max_heap is not None:
#             print(max_heap.delete())
#     else:
#         max_heap.insert(h)
