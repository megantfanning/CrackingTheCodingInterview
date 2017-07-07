import LL
#a linked list contains a number with two places, the ones place is the first item in the list, the 10s place the second 6->1->7 ->3->1->2 716+213
#let us assume we know that both numbers are in the hundreds place 

myLL = LL.LinkedList(6)
for i in range(7,9):
    myLL.push(i)
for i in range(1,4):
    myLL.push(i)

def sumReverse(aLL):
    count = 0
    # move fast pointer ahead
    fast = aLL.returnHead()
    while fast.nextNode != None and count < 3 :
        fast = fast.nextNode
        #print(currentNode.value)
        count += 1
    slow = aLL.returnHead()
    #create new LL
    answer = LL.LinkedList(0)
    overflow = False

    while fast != None:
        if overflow:
            print("overflow")
            new = slow.value + fast.value +1
            overflow = False
        else:
            new = slow.value + fast.value
        #handle overflow
        if new > 9:
            print(new)
            #handle overflow addition
            new = new-10
            overflow = True
        answer.push(new)
        slow =slow.nextNode
        fast =fast.nextNode
    if overflow:
        print("overflow")
        answer.push(1)
        overflow = False

    return answer

#follow up what if the numbers are stored in standard order 6->1->7 ->3->1->2 617+312

def sum(myLL):
    count = 0
    # move fast pointer ahead
    fast = aLL.returnHead()
    while fast.nextNode != None and count < 3 :
        fast = fast.nextNode
        #print(currentNode.value)
        count += 1
    slow = aLL.returnHead()
    #create new LL
    answer = LL.LinkedList(0)
    count = 0

    while fast != None:
        count +=1
        new = slow.value + fast.value
        #handle overflow
        if new > 9:
            print(new)
            #handle overflow addition
            new = new-10
            overflow = count
        answer.push(new)
        slow =slow.nextNode
        fast =fast.nextNode
    #percolate overflow values up the stack
    while overflow:
        print("overflow")
        new = answer[overflow] + 1
        if new > 9:
            overflow = True

    return answer

#myLL.print()
answer = sumReverse(myLL)
answer.print()
answer = sum(myLL)
print("answer:")
answer.print()

