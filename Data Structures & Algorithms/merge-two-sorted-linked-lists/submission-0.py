# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode(0)
        head = list3
        Arr1 = list1
        Arr2 = list2
        while Arr1 and Arr2:
            if Arr1.val <= Arr2.val:
                list3.next = Arr1
                Arr1 = Arr1.next
                list3 = list3.next
            else:
                list3.next = Arr2
                Arr2 = Arr2.next
                list3 = list3.next

        if Arr1:
            list3.next = Arr1
        if Arr2:
            list3.next = Arr2
        return head.next
