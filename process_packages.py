# python3
import sys

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head==self.tail

    def pushFront(self, val):
        if self.size==0 :
            n = Node(val)
            self.head = n
            self.tail = n
            self.size +=1
        else :
            n = Node(val)
            n.next = self.head
            self.head.prev = n
            self.head = n
            self.size +=1

    def popBack(self):
        if self.size==0 : return
        elif self.size==1 : 
            return_value = self.tail.value
            self.size -=1
            self.tail=None
            self.head=None
            return return_value
        else :
            return_value = self.tail.value
            cancel = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            cancel.prev = None
            self.size -=1
            return return_value

    def top(self):
        return self.tail.value

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        # write your code here
        return Response(False, -1)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)
'''
if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)'''
'''
q = Queue()
q.pushFront(5)
q.pushFront(10)
q.pushFront(15)
while q.size!=0 :
    print(q.popBack())
'''
input = sys.stdin.read()

S, n, *data = map(int, input.strip().split())
arrival = list(data[::2])
process= list(data[1::2])
buffer = Queue()
result = [0]*n


time=arrival[0]
i=0
timeToPop = 100000
processing = False

while i<len(arrival) or buffer.size!=0:
    '''
    # pass packets with no processing time
    while buffer.size!=0 and buffer.top()[1]==0 :
        #print("in while")
        ind, t = buffer.popBack()
        result[ind] = time'''

    while True:
        # start packet processing.
        if buffer.size!=0 and processing==False:
            ind, t = buffer.top()
            result[ind] = time
            timeToPop = time + t
            processing = True
            #print("timeToPop", timeToPop)

        # stop processing
        if time == timeToPop and processing==True:
            #print ("pop")
            buffer.popBack()
            processing=False
            continue
        break


    # place packet in queue if there is space    
    if i<len(arrival) and arrival[i] <= time: 
        if buffer.size<S : 
            buffer.pushFront((i,process[i]))
            i+=1
        else : 
            result[i] = -1
            i+=1 

    # if there is no packet arriving at this time process next in queue
    #else: time +=1
    else : 
        if i<len(arrival) and processing==True : time = min(arrival[i], timeToPop)
        elif processing==True : time = timeToPop
        else: time +=1
    #print ("time", time)

'''
while i<=len(arrival):
    # empty queue after processing all packets
    if i==len(arrival):
        while buffer.size!=0:
            ind, t = buffer.popBack()
            result[ind] = time
            time +=t
        break

    # pass packets with no processing time
    if buffer.size!=0 and buffer.top()[1]==0 :
        ind, t = buffer.popBack()
        result[ind] = time

    # place packet in queue if there is space    
    if arrival[i] == time: 
        if buffer.size<S : 
            buffer.pushFront((i,process[i]))
            i+=1
        else : 
            result[i] = -1
            i+=1

    elif arrival[i] < time:
        result[i] = -1
        i+=1

    # if there is no packet arriving at this time process next in queue
    else:
        if buffer.size>0 :
            ind, t = buffer.popBack()
            result[ind] = time
            time +=t
        else : time+=1'''

for i in result:
    print(i)
