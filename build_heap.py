# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]

  # my implementation
  def siftDown(self, i, size):
    minIndex = i
    left = 2*i+1
    if left<= size and self._data[left] < self._data[minIndex]:
      minIndex = left
    right = 2*i+2
    if right<= size and self._data[right] < self._data[minIndex]:
      minIndex = right

    if i!=minIndex:
      self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
      self._swaps.append((i,minIndex))
      self.siftDown(minIndex, size)

  # my implementation
  def makeHeap(self):
    size = len(self._data)-1
    i=len(self._data)//2
    while i>=0:
      self.siftDown(i, size)
      i-=1




  def Solve(self):
    self.ReadData()
    #self.GenerateSwaps()
    self.makeHeap()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
