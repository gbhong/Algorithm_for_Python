class circular_queue(object):
    def __init__(self, q_size):
        self.queue = list(range(1, q_size+1))

    def slide_left(self):
        tgt = self.queue[0]
        self.queue.pop(0)
        self.queue.append(tgt)

    def slide_right(self):
        tgt = self.queue[-1]
        self.queue[1:] = self.queue[:-1]
        self.queue[0] = tgt

    def cnt_slide(self, targets:list):
        cnt = 0
        for t in targets:
            if self.queue[0] == t:
                self.queue.pop(0)
            else:
                if self.queue.index(t) <= len(self.queue)//2:
                    while self.queue[0] != t:
                        self.slide_left()
                        cnt += 1
                    self.queue.pop(0)
                else:
                    while self.queue[0] != t:
                        self.slide_right()
                        cnt += 1
                    self.queue.pop(0)
        return cnt

N, M = map(int, input().split())
targets = list(map(int, input().split()))

circular_queue = circular_queue(q_size=N)
print(circular_queue.cnt_slide(targets=targets))