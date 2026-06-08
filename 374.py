# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
import random

l, r = 1, 2**31 - 1

rand_num = random.randint(l, r)


def guess(num):
    if rand_num == num:
        return 0
    elif rand_num > num:
        return -1
    elif rand_num < num:
        return 1


class Solution:
    def guessNumber(self, n):
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                r = mid - 1
            else:
                l = mid + 1
