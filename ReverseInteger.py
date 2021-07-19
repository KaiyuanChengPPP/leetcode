import math
class Solution:
    def reverse(self, x: int) -> int:
       y = x
       if x < 0:
           x = -x
       xlist = list(map(int, str(x)))
       result = []
       for i in reversed(range(len(xlist))):
           result.append(xlist[i])

       result = [str(integer) for integer in result]
       result = "".join(result)

       if (int(result) >= -pow(2, 31) and int(result) <= pow(2, 31) - 1 and y < 0):
           return -int(result)
       elif (int(result) >= -pow(2, 31) and int(result) <= pow(2, 31) - 1 and y > 0):
           return int(result)
       else:
           return 0



s = Solution()
print(s.reverse(-120))