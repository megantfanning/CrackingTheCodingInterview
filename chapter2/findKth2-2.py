import LL
#find the kth to last element in a singlely linked list

#initialize a LL
myLL = LL.LinkedList(1)
for i in range(1,11):
    myLL.push(i)

#traverse once  the fast counter is offset by k elements, the slow one will return the kth to last element when the fast pointer reaches the end of the list
def getkthToLast(LL,k):
    counter = 0
    fast = LL.returnHead()
    
    while counter <= k:
        fast = myLL.getNext(fast)
        counter +=1
    slow = LL.returnHead()
    while fast != None:
        fast = myLL.getNext(fast)
        slow = myLL.getNext(slow)
        #print(slow.value)
        counter += 1
    return slow.value

#run Code
print(getkthToLast(myLL,4))


