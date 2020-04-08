# Counting Elements
# https://leetcode.com/submissions/detail/321425877/

from typing import List
import array

class Solution:
    def countElements(self, arr: List[int]) -> int:
        a = array.array('H', [0 for _ in range(1002)])
        for i in arr:
          a[i] += 1
        total = 0
        i = 0
        while i < 1001:
            offset = 0
            '''
            if a[i] < a[i + 1]:
                offset = a[i]
            else:
                offset = a[i + 1]
            total += offset
            '''
            if a[i + 1] > 0:
                total += a[i]
            i += 1
        return total


if __name__ == '__main__':
    obj = Solution()
    #data = [1,2,3]
    #data = [1,1,3,3,5,5,7,7]
    #data = [1,3,2,3,5,0]
    #data = [1,1,2,2]
    data = [1,1,2]
    result = obj.countElements(data)
    print(result)
