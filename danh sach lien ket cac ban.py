class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def search(self, target):
        current = self.head
        index = 0

        while current is not None:
            if current.data == target:
                return index
            current = current.next
            index += 1

        return -1

    def reverse_print(self):
        self._reverse_print_helper(self.head)

    def _reverse_print_helper(self, node):
        if node is None:
            return
        self._reverse_print_helper(node.next)
        print(node.data)

# Tạo danh sách liên kết
danhBa = LinkedList()
danhBa.append('Bao')
danhBa.append('Anh')
danhBa.append('Cuong')
danhBa.append('Cu')
danhBa.append('Ao')
danhBa.append('Cao')
danhBa.append('Hung')
danhBa.append('Duat')
danhBa.append('Uyen')
danhBa.append('Khoa')
danhBa.append('Dung')
danhBa.append('Duc')
danhBa.append('Danh')
danhBa.append('Anh')
danhBa.append('Ao')

# Tìm tên trong danh bạ
ten = input("Nhập tên người cần tìm: ")
vi_tri = danhBa.search(ten)
if vi_tri != -1:
    print("Tên", ten, "được tìm thấy tại vị trí", vi_tri)
else:
    print("Tên", ten, "không có trong danh bạ.")

# In ra màn hình thứ tự đảo ngược
print("Thứ tự đảo ngược:")
danhBa.reverse_print()