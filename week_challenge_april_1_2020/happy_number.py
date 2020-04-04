# https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3284/

class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        total = 0
        while True:
            while n != 0:
                total += (n % 10) ** 2
                n = n // 10
            if total == 1:
                return True
            elif d.get(total) != None:
                return False
            else:
                d[total] = 1
                print(total)
                n = total
                total = 0

        return True

if __name__ == '__main__':
    obj = Solution()
    print(obj.isHappy(19))
