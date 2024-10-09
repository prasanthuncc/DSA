from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def insert_at_end(self, data: int):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = node

    def insert_at_beginning(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            p = self.head
            node.next = p
            self.head = node

    def insert_at_position(self, data, pos):
        node = Node(data)
        if self.head is None:
            self.head = node
        elif pos == 0:
            self.insert_at_beginning(data)
        else:
            p = self.head
            for i in range(1, pos - 1):
                if p.next:
                    p = p.next
                else:
                    return self.insert_at_end(data)
            node.next = p.next
            p.next = node

    def reversal(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def check_loop(self):
        first = second = self.head
        while first and second.next:
            first = first.next
            second = second.next.next
            if first and second and first == second:
                return True
        return False

    def traverse(self):
        p = self.head
        while p:
            if p.next:
                print(p.data, end=" -> ")
            else:
                print(p.data)
            p = p.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(9)
    ll.insert_at_beginning(8)
    ll.insert_at_position(20, 20)
    ll.insert_at_position(21, 10)
    ll.insert_at_position(21, 6)
    ll.traverse()
    ll.reversal()
    ll.traverse()
    print(ll.check_loop())
