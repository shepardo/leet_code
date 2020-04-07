
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = 0
        while True:
            while i < len(nums) and nums[i] != 0:
                i += 1
            while j < len(nums) and nums[j] == 0:
                j += 1
            if i >= len(nums) or j >= len(nums):
                break
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                j += 1

if __name__ == '__main__':
    obj = Solution()
    #data = [0,1,0,3,12]
    #data = [1,0]
    data = [1,0,1]
    obj.moveZeroes(data)
    print('[{0}]'.format(','.join(map(lambda x: str(x), data))))
