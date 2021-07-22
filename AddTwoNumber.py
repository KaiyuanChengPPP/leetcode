class Node:
    def __init__(self,val=0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def insertBegin(self,data):
        node = Node(data)


    def insertEnd(self,data):
        node = Node(data,self.headval)
        if self.headval is None:
            self.headval = node
            return
        last = self.headval
        while (last.next):
            last = last.next
        last.next = Node(data,None)
    def solution(self,l1: Node,l2: Node):
        prev = Node()
        temp = prev
        carry = 0
        while (l1 or l2):
            l1data = l1.val if l1 != None else 0
            l2data = l2.val if l2 != None else 0
            sum = l1data + l2data + carry
            if (sum >= 10):
                sum = sum // 10
                carry = 1
            else:
                carry = 0
            temp = Node(sum)
            if self.headval is None:
                self.headval = temp
            else:
                prev.next = temp

            prev = temp

            if (l1 is not None):
                l1 = l1.next
            if (l2 is not None):
                l2 = l2.next
        if (carry > 0):
            temp.next = Node(carry)



    def print(self,listnode):
        if listnode is None:
            print("linked list is empty")
            return
        itr = listnode
        while itr:
            print(itr.val)
            itr = itr.next



llist1 = LinkedList()
llist2 = LinkedList()
llist3 = LinkedList()
l1 = llist1.insertBegin(10)
for i in range(9,0,-1):
    llist1.insertBegin(i)
for i in range(7):
    llist2.insertBegin(i)
llist1.print(llist1)

# llist3.solution(llist1,llist2)
# llist3.print()