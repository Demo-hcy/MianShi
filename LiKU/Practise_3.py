# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # 方法一：
        # return str(x) == str(x)[::-1]

        # 方法二：
        # 定义一个变量存储x的值
        prev_x = x
        # 定义一个变量存储x倒序后的值
        inve_x = 0
        # 当prev_x大于0的时候循环，这里筛选负数
        while prev_x > 0:
            # inve_x*10加上prev_x和10取余的数
            inve_x = inve_x * 10 + (prev_x % 10)
            # prev_x整除10
            prev_x = prev_x // 10
        return inve_x == x


if __name__ == '__main__':
    s = Solution()
    palindrome_bool = s.isPalindrome(121)
    print(palindrome_bool)