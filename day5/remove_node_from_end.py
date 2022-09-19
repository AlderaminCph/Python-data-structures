"""
Given the head of a linked list,
remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""


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


def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy_node = Node(0)
    dummy_node.next = head
    left_pointer = dummy_node
    right_pointer = head

    while n > 0 and right_pointer:
        right_pointer = right_pointer.next
        n -= 1

    while right_pointer:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    # delete nth node:
    left_pointer.next = left_pointer.next.next

    # delete dummy_node
    return dummy_node.next
