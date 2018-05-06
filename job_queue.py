# python3
class Node:
    def __init__(self,threadIndex):
        self.threadIndex = threadIndex
        self.priority = 0
        
class MinHeap:
    def __init__(self, nbNodes):
        self.heap = [ Node(i) for i in range(nbNodes)]

    def top(self):
        return self.heap[0]

    def changePriority(self, time):
        self.heap[0].priority += time
        self.siftDown(0)

    def siftDown(self, i):
        size = len(self.heap)-1
        minIndex = i
        minThread = self.heap[i].threadIndex
        left = 2*i+1
        if (left<= size and self.heap[left].priority < self.heap[minIndex].priority) or (
           left<=size and self.heap[left].priority==self.heap[minIndex].priority 
                      and self.heap[left].threadIndex < minThread ):
            minIndex = left
            minThread = self.heap[left].threadIndex
        right = 2*i+2
        if (right<= size and self.heap[right].priority < self.heap[minIndex].priority):
            minIndex = right
        elif (right<=size and self.heap[right].priority==self.heap[minIndex].priority 
                        and self.heap[right].threadIndex < minThread ):
            minIndex = right
   
        if i!=minIndex:
            self.heap[i], self.heap[minIndex] = self.heap[minIndex], self.heap[i]
            self.siftDown(minIndex)

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        queue = MinHeap(self.num_workers)
        '''
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]'''
        for i in range(len(self.jobs)):
          node = queue.top()
          self.assigned_workers[i] = node.threadIndex
          self.start_times[i] = node.priority
          queue.changePriority(self.jobs[i])

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

