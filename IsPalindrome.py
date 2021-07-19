class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            xlist = list(map(int,str(x)))
            reversedlist=[]
            for i in reversed(range(len(xlist))):
                reversedlist.append(xlist[i])
            print(xlist)
            print(reversedlist)
            for j in range(len(xlist)):
                if xlist[j] != reversedlist[j]:
                    return False
            return True




s = Solution()
print(s.isPalindrome(11))
