# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""


# 示例 1：
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"

# 示例 2：
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
from typing import List


class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) ->str:
        global tmp
        result  = ""
        """
        :type strs: List[str]
        :rtype: str
        """
        for tmp in zip(*strs):
            if len(set(tmp)) == 1:
                result += tmp[0]
            else:
                break
        return result

if __name__ == '__main__':
    solution = Solution()
    print("示例1：",solution.longestCommonPrefix(["flower","flow","flight"]))
    print("示例2：", solution.longestCommonPrefix(["dog","racecar","car"]))
    #