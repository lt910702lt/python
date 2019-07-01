import queue
'''
LifoQueue()
PriorityQueue()
'''
# q = queue.Queue()  # 线程安全的
# q.get()
# q.put()
# q.qsize()

# # LifoQueue() -- 后进先出的队列
# lfq = queue.LifoQueue()
# lfq.put(1)
# lfq.put(2)
# lfq.put(3)
# lfq.put(4)
# print(lfq.get())       # 结果是4

# PriorityQueue() -- 有优先级的队列(值越小越优先)
pq = queue.PriorityQueue()
pq.put((10, 'a'))
pq.put((15, 'b'))
pq.put((5, 'c'))
print(pq.get())     # 结果是(5, 'c')