# 给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
         """
        tmp = int((str(x) if x > 0 else str(-x) + "-")[::-1])
        return tmp if -2 ** 31 < tmp < 2 ** 31 - 1 else 0


if __name__ == '__main__':
    solution =Solution()
    print(solution.reverse(123))
