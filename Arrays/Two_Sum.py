'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''

class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dic:
                return [dic[diff],i]
            dic[nums[i]] = i 
        return -1

s = Solution()
nums = list(map(int, input().split()))
target = int(input())
print(s.twoSum(nums, target))