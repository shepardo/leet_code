# Single Number
# https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3283/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        acc = 0
        for i in range(len(nums)):
            acc = acc ^ nums[i]
        return acc
