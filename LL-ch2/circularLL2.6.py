import LL
#given a circularly linked list return the beginning of the loop

myLL = LL.LinkedList(6)
for i in range(1,5):
    myLL.push(i)
myLL.push(myLL.returnHead())
myLL.push(7)

def circle(myLL):
    fast = myLL.returnHead()
    slow = myLL.returnHead()

    while slow != fast:
        slow = slow.nextNode
        fast = fast.nextNode.nextNode
    #cycle is found
    
    fast = myLL.returnHead()
    length = 0

    while fast != slow:
        fast = fast.next
        length += 1
    #length of cycle is found

    fast = myLL.returnHead()
    slow = myLL.returnHead()
    c = 0
    #go length of cycles
    while c < length:
        fast = myLL.nextNode
        c += 1 
    #circle until they match up
    while fast != slow:
        fast = fast.nextNode
        slow = slow.nextNode
    return fast.value

print(circle(myLL))
