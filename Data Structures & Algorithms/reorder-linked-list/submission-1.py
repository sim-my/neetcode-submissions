# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMiddle(self,head):
        if not head: return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


    
    def reverse_list(self,head):
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


    
    def merge_alternate(self,first, second):
        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next


    

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        middle = self.findMiddle(head)
        second = middle.next
        middle.next = None

        second = self.reverse_list(second)
        self.merge_alternate(head, second)
