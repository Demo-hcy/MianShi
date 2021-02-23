# 给定一个整数数组 nums 和一个整数目标值 target，
# 请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]。

# 双层循环暴力求解
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#
#
# if __name__ == '__main__':
#     # Solution.twoSum([2, 7, 8, 11], 9)
#     solution=Solution()
#     print(solution.twoSum([2,7,11,15],9))



# 字典法求解
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i in range(len(nums)):
            _dict[nums[i]] = i

        for i in range(len(nums)):
            j = _dict.get(target - nums[i])
            if j is not None and i != j:
                return [i, j]

if __name__ == '__main__':
    solution=Solution()
    print(solution.twoSum([2,7,11,15],9))