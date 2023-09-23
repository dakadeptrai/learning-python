x = int(input())
list = [1,3,5,7,9]
def tktt():
    global x
    for i in range(len(list)):
        if x == list[i]:
            return i
    return -1
def recursion(list,tar,start = 0):
    if start >= len(list):
        return print(-1)
    if list[start] == tar:
        return print(start)
    else:
        recursion(list,tar,start + 1)
recursion(list,x)
