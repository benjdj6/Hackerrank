def insert(self, head, data):
    if not head:
        head = Node(data)
    else:
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)
    return head
