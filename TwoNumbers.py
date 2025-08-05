from typing import Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def PrintLinkedList(node: Optional[ListNode]):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

class Solution(object):
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        current_node = head
        carry = 0
        
        p1 = l1
        p2 = l2
        
        while p1 is not None or p2 is not None or carry != 0:
            val1 = p1.val if p1 is not None else 0
            val2 = p2.val if p2 is not None else 0
            
            sum = val1 + val2 + carry
            
            carry = sum // 10
            digit = sum % 10
            
            current_node.next = ListNode(digit)
            current_node = current_node.next
            
            if p1 is not None:
                p1 = p1.next
            if p2 is not None:
                p2 = p2.next
        
        return head.next
    
def CreateLinkedList(array):
    head = ListNode(array[0])
    current = head
    for num in array[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

solution = Solution()
l1 = CreateLinkedList([2, 4, 3])
l2 = CreateLinkedList([5, 6, 4])

result = solution.addTwoNumbers(l1, l2)

print(PrintLinkedList(result))