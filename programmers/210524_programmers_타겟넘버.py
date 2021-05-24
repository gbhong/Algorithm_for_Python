class target_num(object):
    def __init__(self):
        self.answer = 0
        self.numbers = None
        self.target = None

    def pwrset_sum(self, k, idx):
        print(k, idx)
        if idx == len(self.numbers):
            if k == self.target:
                self.answer += 1
            return

        for i in range(idx, len(self.numbers)):
            self.pwrset_sum(k + self.numbers[i], idx + 1)
            self.pwrset_sum(k - self.numbers[i], idx + 1)

    def solution(self, numbers, target):
        self.numbers = numbers
        self.target = target
        self.pwrset_sum(k=0, idx=0)
        return self.answer

print(target_num().solution(numbers=[1,1], target=2))