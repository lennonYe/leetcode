# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def count(self,root):
        count = 0
        while root:
            root = root.next
            count += 1
        return count

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        nodes_num = self.count(head)
        repeat = nodes_num // k
        root = ListNode()
        root.next = head
        tmp_head = root
        node = head

        for i in range(repeat):
            for j in range(k - 1):
                next_node = node.next
                next_next_node = node.next.next

                node.next = next_next_node
                next_node.next = tmp_head.next
                tmp_head.next = next_node
                
            tmp_head = node
            node = tmp_head.next
            
        return root.next

