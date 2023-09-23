# Định nghĩa Node: gồm dữ liệu(data) và con trỏ (next)
class Node:
    # Khởi tạo object Node (Constructor)
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

# Định nghĩa danh sách liên kết đơn (singly linked-list) với 1 node đầu tiên (head)
class LinkedList:
    def __init__(self):  
        self.head = None
        self.tail = None

    def printLinkedList(self):
        '''Duyet danh sach Linked-list'''
        head = self.head
        print("Linked list: ")
        while head != None: # head != tail
            print(head.data, end = '->')
            head = head.next
        print(end ='\n')

    def len(self):
        '''hien thuc ham len() xuat ra so luong phan tu trong LL'''
        count = 0
        head = self.head
        while head != None: # head != tail
            count += 1
            head = head.next
        return count
        
    def index(self, id):
        '''In ra phan tu thu <id> '''
        head = self.head
        while head != None and id>0: # head != tail
            id -= 1
            head = head.next
        return head

    def insert(self, id, data):
        '''Chen phan tu thu <id> chua <data> '''
        newNode = Node(data)
        if id == 0: # first id
            temp = self.head
            self.head = newNode
            self.head.next = temp
        elif id >= self.len()-1 or id < 0: # last id
            self.tail.next = newNode
            self.tail = self.tail.next
        else: # middle id
            prevNode = self.index(id = id - 1)
            temp = prevNode.next
            prevNode.next = newNode
            newNode.next = temp

    def remove(self,id):
        """ remove data by index"""
        if id == 0:
            tmp=self.head.next
            del self.head
            self.head=tmp
            return True
        
        elif id == (self.len() - 1):
            tmp2 = self.index(self.len() - 2)
            tmp2.next = None
            self.tail = tmp2

        # else:     # xóa tại vị trí cuối cùng trong linkedList
        #     tmp3 = self.index(id-1) 
        #     tmp4=tmp3.next
        #     tmp3.next=tmp4.next
        #     del tmp4

        elif id >= self.len()-1 or id<0:
            return False
        
        else:
            tmp3 = self.index(id-1)
            tmp4=tmp3.next
            tmp3.next=tmp4.next
            del tmp4 
            return True
        
        # else:     # xóa tại vị trí cuối cùng trong linkedList
        #     tmp3 = self.index(id-1) 
        #     tmp4=tmp3.next
        #     tmp3.next=tmp4.next
        #     del tmp4

    # def append(self, data): # def push_back()
    #     newNode = Node(data)
    #     if self.head == None:
    #         self.head = newNode
    #         self.tail = newNode
    #         return 
    #     self.tail.next = Node(data)
    #     self.tail = self.tail.next

    def append(self,data):
        """
        TH1: nếu danh sách rỗng: gán top bằng newData
        TH2: nếu danh sách không rỗng: tới vị trí cuối trong danh sách : thêm data
        """
        newNode = Node(data)    
        if self.head == None:
            self.head = newNode
            return
        newData = self.head
        while newData.next: 
            newData = newData.next
        newData.next = newNode


# ll = LinkedList()
# ll.append("4")
# ll.append("5")
# ll.append("6")
# ll.remove(2)
# ll.printLinkedList()
