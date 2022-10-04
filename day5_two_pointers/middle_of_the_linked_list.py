"""
Given the head of a singly linked list,
return the middle node of the linked list.

If there are two middle nodes, return
the second middle node.

Example 1:

>>> middleNode([1,2,3,4,5])
[3, 4, 5]
Explanation: The middle node of the list is node 3.

Example 2:

>>> middleNode([1,2,3,4,5,6])
[4, 5, 6]
Explanation: Since the list has
two middle nodes with values 3 and 4, we return the second one.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, val):
        self.val = val  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Print the linked list
    def printList(self):
        node = self.head
        while node:
            print(str(node.val) + "->", end="")
            node = node.next
        print("NULL")


def middleNode(head):
    """
    Solution idea: two iterators
    fast and slow.
    fast increments by two
    slow increments by one

    :type head: ListNode
    :rtype: ListNode
    """
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
