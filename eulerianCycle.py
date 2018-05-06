# python3

class Euler:
    def __init__(self):
      self.V=0
      self.E=0
      self.graph = []
      self.edges = []
      self._cycle = []

    def makeGraph(self):
      self.V, self.E = map(int, input().split())
      self.graph = [ [[],[]] for v in range(self.V)]
      self.edges = [ 0 for e in range(self.E)]

      for index_e in range(self.E):
        v, u = map(int, input().split())
        self.graph[v-1][0].append(index_e)
        self.graph[u-1][1].append(index_e)
        self.edges[index_e] = (v-1, u-1)

    def hasEulerian(self):
      for v in range(self.V):
        if len(self.graph[v][0]) != len(self.graph[v][1]):
          return 0
      return 1

    def findCycle(self, v, cycle):
      #first use v=0
      while len(self.graph[v][0]) !=0:
        nextEdge = self.graph[v][0].pop()
        cycle.append(self.edges[nextEdge])
        v = self.edges[nextEdge][1]


    def updateCycle(self):
      newCycle=[]
      index = 0
      #find next vertex origin
      for  i,e in enumerate(self._cycle):
        if len(self.graph[e[0]][0]) !=0:
          ori_v = e[0]
          index = i
          break
      # update cycle
      for e in self._cycle[index:]:
        newCycle.append(e)
      for e in self._cycle[:index]:
        newCycle.append(e)

      # continue newcyle
      self.findCycle(ori_v, newCycle)
      return newCycle
  


if __name__ == '__main__':
  euler = Euler()
  euler.makeGraph()
  #print(euler.graph)
  #print(euler.edges)
  valid = euler.hasEulerian()
  if valid == 0:
    print(0)
    exit()
  else:
    print(1)

  euler.findCycle(0, euler._cycle)
  #print(euler._cycle)
  while len(euler._cycle) != euler.E:
    euler._cycle = euler.updateCycle()
    #print(euler._cycle)
  for i in euler._cycle:
    print(i[0]+1, end=' ')
  
