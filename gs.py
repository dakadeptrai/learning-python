class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printDataLinkedList(self):
        """"""
        tamp = self.head
        while tamp != None:
            print(tamp.data,end="->")
            tamp = tamp.next  # trỏ tới node kế tiếp

    def indexLinkedList(self,index): # 2  => index > 0
        """"""
        tamp = self.head
        while tamp != None and index > 0: # tamp != None and index
            index -= 1   # index = index - 1
            tamp = tamp.next
        print(tamp.data)

    def append(self, data): 
        newNode = Node(data)  # tạo ra 1 Node mới 
        if self.head == None:  # TH1: LinkedList đang rỗng 
            self.head = newNode
            self.tail = newNode
            return 
        # TH2: LinkedList có giá trị
        self.tail.next = newNode # tail.next sẽ không còn là rỗng mà được gán             # giá trị bằng newNode
        self.tail = self.tail.next # cập nhật lại giá trị cho tail

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
        return head #->node

    def removeHead(self):
        temp = self.head.next
        del self.head
        self.head = temp

    def removeTail(self):
        # Node tại vị trí có index = len - 2 
        temp = self.index(self.len() - 2)
        print("temp", temp.data)
        temp.next = None
        del self.tail
        self.tail = temp

    def remove(self, id):
        if id == 0: 
            tmp=self.head.next
            del self.head
            self.head=tmp

        elif id >= self.len()-1 or id<0:  
            print("id: ",id)
            tmp2=self.index(self.len()-2)
            del tmp2.next
            tmp2.next=None
            self.tail = tmp2

        else:     
            
            print("id_2: ",id)
            tmp3 = self.index(id-1)
            tmp4=tmp3.next 
            tmp3.next=tmp4.next 
            del tmp4

def remove_2(ll, id):
    if id == 0: 
        tmp=ll.head.next
        del ll.head
        ll.head=tmp

    elif id >= ll.len()-1 or id<0:  
        print("id: ",id)
        tmp2=ll.index(ll.len()-2)
        del tmp2.next
        tmp2.next=None
        ll.tail = tmp2

    else:     
        
        print("id_2: ",id)
        tmp3 = ll.index(id-1)
        tmp4=tmp3.next 
        tmp3.next=tmp4.next 
        del tmp4

def index2(LL, it):
    '''In ra phan tu thu <id> '''
    id = 0
    head = LL.head
    while head != None: 
        if head.data == it:
            break
        id += 1
        head = head.next
    if id >= LL.len():
        print(it)
        return -1
    return id #->node

# node_1 -> node_2 -> node_3 -> node_4 (tail)
# 4 -> 5 -> 6 -> 1
link1 = LinkedList()
link1.append(1)
link1.append(2)
link1.append(3)
link1.append(4)
# link1.removeHead()
# link1.remove(-4)
print(index2(link1, 3))
link1.printDataLinkedList()