class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            sorted_list = self.insert_sorted(sorted_list, current)
            current = next_node

        self.head = sorted_list

    def insert_sorted(self, sorted_list, node):
        if not sorted_list or node.value <= sorted_list.value:
            node.next = sorted_list
            return node
        else:
            current = sorted_list
            while current.next and current.next.value < node.value:
                current = current.next
            node.next = current.next
            current.next = node
        return sorted_list

    def merge_sorted_lists(self, list1, list2):
        dummy = Node(0)
        tail = dummy

        while list1 and list2:
            if list1.value <= list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        self.head = dummy.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Приклади використання класу LinkedList
ll_01 = LinkedList()
ll_01.append(-6)
ll_01.append(26)
ll_01.append(12.5)
ll_01.append(14)

print("Перший список:")
ll_01.print_list()

ll_01.reverse()
print("Перший реверсований список:")
ll_01.print_list()

ll_01.insertion_sort()
print("Перший відсортований список:")
ll_01.print_list()

ll_02 = LinkedList()
ll_02.append(5)
ll_02.append(1488)
ll_02.append(122.3)
ll_02.append(20)
ll_02.append(-11)
ll_02.insertion_sort()

print("Другий список:")
ll_02.print_list()

print("Другий відсортований список:")
ll_02.print_list()

ll_merged = LinkedList()
ll_merged.merge_sorted_lists(ll_01.head, ll_02.head)
print("Об'єднаний відсортований список:")
ll_merged.print_list()
