# Middle of the Linked List
# https://leetcode.com/submissions/detail/321790561/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        current = head
        cnt = 0
        while current != None:
            cnt += 1
            current = current.next

        cnt = (cnt // 2) + 1
        current = head
        for i in range(cnt):
            prev = current
            current = current.next

        return prev

if __name__ == '__main__':
    head = ListNode(0)
    current = head
    for i in range(1,5,1):
        newNode = ListNode(i)
        current.next = newNode
        newNode.next = None
        current = newNode

    obj = Solution()
    head = obj.middleNode(head)

    current = head
    while current != None:
        print(current.val)
        current = current.next
