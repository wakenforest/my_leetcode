# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        newNode=ListNode(0)
        ansNode=newNode
        flag=-1
        while l1 or l2 or flag:
            if flag!=-1:
                newNode.next=ListNode(0)
                newNode=newNode.next
            else:
                flag=0
            if l1 and l2:
                sum=l1.val+l2.val
                l1=l1.next
                l2=l2.next
            elif l1:
                sum=l1.val
                l1=l1.next
            elif l2:
                sum=l2.val
                l2=l2.next
            else:
                sum=0
            newNode.val=(sum+1)%10 if flag==1 else sum%10
            flag=1 if sum+flag>9 else 0 
        return ansNode


def stringToListNode(input):
    import json
    # Generate list from the input
    # numbers = json.loads(input)
    numbers = input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    list1=[2,4,3]
    list2=[5,6,4]
    l1=stringToListNode(list1)
    l2=stringToListNode(list2)
    s=Solution()
    ansNode=s.addTwoNumbers(l1,l2)
    print("input:")
    print(list1)
    print(list2)
    print("output:")
    print( listNodeToString(ansNode) )

if __name__ == '__main__':
    main()