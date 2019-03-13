# coding=utf-8

"""
Given a string of numbers and operators,
return all possible results from computing
all the different possible ways to group numbers and
operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
"""


# class Solution:
#     def diffWaysToCompute(self, input, low, high):
#         res = []
#         if low == high:
#             res.append(int(input[low]))
#             return res
#         if low == high - 2:
#             num = self.evel_(int(input[low]), input[low+1], int(input[low+2]))
#             res.append(num)
#             return res
#         for i in range(low+1, high, 2):
#             l = self.diffWaysToCompute(input, low, i-1)
#             r = self.diffWaysToCompute(input, i+1, high)
#             for s1 in range(len(l)):
#                 for s2 in range(len(r)):
#                     val = self.evel_(l[s1], input[i], r[s2])
#                     res.append(val)
#         return res
#
#     def evel_(self, a, op, b):
#         if op == '+': return a + b
#         if op == '-': return a - b
#         if op == '*': return a * b

class Solution:
    def diffWaysToCompute(self, input):
        res = []
        if len(input) == 1:
            res.append(int(input[0]))
            return res
        if len(input) == 2:
            res.append(int(input[0:]))
            return res
        for i in range(0, len(input)):
            if input[i] == '-' or input[i] == '*' or input[i] == '+':
                l = self.diffWaysToCompute(input[0:i])
                r = self.diffWaysToCompute(input[i+1:])
                for s1 in l:
                    for s2 in r:
                        val = self.evel_(s1, input[i], s2)
                        res.append(val)
        return res

    def evel_(self, a, op, b):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b


if __name__ == '__main__':
    a = Solution()
    f = "2*3-4*5"
    g = "2*3"
    c = "1+50"
    print(a.diffWaysToCompute(c))