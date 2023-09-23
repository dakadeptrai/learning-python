from final import LinkedList,Node
import copy
danhBa = ['Bao', 'Tra', 'Anh', 'Cuong', 'Cu', 'Ao',  'Cao', 'Hung', 'Duat', 'Uyen', 'Khoa', 'Dung', 'Duc',  'Danh', 'Anh', 'Ao'] 
danhball = LinkedList()
'''danhball.head = Node(danhBa[0])
danhball.tail = danhball.head
for z in danhBa[1:]:
    danhball.append(z)
danhball.printLinkedList()'''
for name in danhBa:
    danhball.append(name)
danhball.printLinkedList()
lenLL = danhball.len()
lenArr = len(danhBa)
def insertionsortll(ll:LinkedList):
    ll_copy = copy.deepcopy(ll)
    for i in range(1,lenLL):
        key = ll_copy.index(i).data
        j = i-1
        while j >= 0 and ll_copy.index(j).data > key:
            ll_copy.index(j+1).data = ll_copy.index(j).data
            j -=1
        ll_copy.index(j+1).data=key
    return ll_copy
def insertionSort(arr):
    arr_copy = arr.copy()
    for i in range(1, lenArr):
        key = arr_copy[i]
        j = i-1
        while j >= 0 and arr_copy[j] > key:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy 
#sorrt = insertionsort(danhball)
#sorrt.printLinkedList()
insertionsortll(danhball).printLinkedList()
def list2ll(l: list):
    ll = LinkedList()
    ll.head = ll.tail = Node(l[0])
    for item in l[1:]:
        ll.append(item)
    return ll
testset = danhBa
def stressTestsort(arr:list,methodlist,methodll):
    ll = list2ll(arr)
    arrsort = methodlist(arr)
    llsort = methodll(ll)
    node = llsort.head
    for i in range(len(arrsort)):
        if(node.data != arrsort[i]):
            print('wrong at' + str(i))
            return
        print('past')
        node = node.next
danhball = list2ll(danhBa)
stressTestsort(testset,insertionSort,insertionsortll)