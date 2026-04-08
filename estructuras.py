class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def print_histogram(self):
        current = self.head
        while current:
            print("█" * current.value)
            current = current.next
        
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next  
        return result

    def update_from_list(self, arr):
        current = self.head
        i = 0
        while current and i < len(arr):
            current.value = arr[i]
            current = current.next
            i += 1