class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        val = self.doMaxSubArray(nums, 0, len(nums) - 1)
        if val == -1:
            all_neg = True
            max = -0xffffffff
            for i in range(len(nums)):
                if max < nums[i]:a
                    max = nums[i]
                if nums[i] >= 0:
                    all_neg = False
            if all_neg:
                return max
        return val

    def doMaxSubArray(self, nums: List[int], left, right) -> int:
        if left >= len(nums) or right < 0:
            return -1
        sum = 0
        total = 0
        i = left
        j = right
        while i <= right and nums[i] < 0:
            i += 1
        while j >= left and nums[j] < 0:
            j -= 1
        sum = 0
        if i > j:
            return -1
        #print('K has the range ({0}, {1})'.format(i, j + 1))
        for k in range(i, j + 1):
            sum += nums[k]
        if total < sum:
            total = sum

        total1 = self.doMaxSubArray(nums, i + 1, j)
        total2 = self.doMaxSubArray(nums, i, j - 1)

        if total1 > total2:
            if total > total1:
                return total
            else:
                return total1
        else:
            if total > total2:
                return total
            else:
                return total2
