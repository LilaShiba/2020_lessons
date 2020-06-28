import random

class WeightRandom:
    def __init__(self, weights):
        self.nums = []
        current_sum = 0
        for w in weights:
            current_sum += w 
            self.nums.append(current_sum)
        self.sum = current_sum
        print(self.nums)
    
    def randomPick(self):
        randomNum = self.sum * random.random()
        lo,hi = 0, len(self.nums)

        while lo < hi:
            mid = lo + (hi-lo)//2

            if randomNum > self.nums[mid]:
                lo = mid + 1
            else:
                hi = mid

        print(f" random num {randomNum}: idx {lo}: value {self.nums[lo]}") 
        return lo
        



r1 =  WeightRandom([1,3,4])
r1.randomPick()
