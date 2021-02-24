# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。
# 12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # value = 0
        # for i in range(len(s)-1,-1,-1):
        #     if  i == len(s)-1 or dict[s[i]] >= dict[s[i + 1]]:
        #         value += dict[s[i]]
        #     else:
        #         value -= dict[s[i]]
        # return value


        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        high=0                              #标记目前遇到的字典中最大的罗马数字
        answer=0                            #最终的答案
        for c in s[::-1]:                   #以反转的顺序来遍历字典
            if dic[c]>=high:                #遍历的罗马值<=最大罗马值就相加。
                answer+=dic[c]
                high=dic[c]                 #替换当前遇到的最大值
            else:
                answer-=dic[c]
        return answer
if __name__ == '__main__':
    solution =Solution()
    print(solution.romanToInt("III"))
    print(solution.romanToInt("IV"))
    print(solution.romanToInt("IX"))
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))
