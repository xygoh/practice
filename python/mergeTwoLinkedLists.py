# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
# Time: O(len(l1)+len(l2))
#  No additional space

def mergeTwoLinkedLists(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    
    prev=head=None
    while l1 and l2:
        if l1.value<=l2.value: #take l1
            if prev!=None:
                prev.next=l1    
            else:
                head=l1  
            prev=l1
            l1=l1.next
            
        else: # take l2
            if prev!=None:
                prev.next=l2      
            else:
                head=l2
            prev=l2
            l2=l2.next
            
    prev.next=l1 or l2
    return head
        
