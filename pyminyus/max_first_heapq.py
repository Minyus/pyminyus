import heapq as hq


class MaxFirstHeapQ:
    def __init__(self):
        self.ls = []

    def push(self, importance, item):
        hq.heappush(self.ls, (-importance, item))

    def pop(self):
        _, item = hq.heappop(self.ls)
        return item

    def __len__(self):
        return len(self.ls)


if __name__ == "__main__":
    q = MaxFirstHeapQ()
    q.push(10, "a")
    q.push(100, "b")
    while len(q):
        print(q.pop())
