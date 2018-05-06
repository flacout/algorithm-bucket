# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        #self.elems = []
        # Array of list
        self.A = [ [] for i in range(bucket_count)]


    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        # simply apply the modulo of m
        return ans % self.bucket_count

    #def write_search_result(self, was_found):
    #    print('yes' if was_found else 'no')
    #def write_chain(self, chain):
    #    print(' '.join(chain))

    def process_query(self, query):
        if query.type == "check":
            l = self.A[query.ind]
            if len(l) == 0: print()
            else : print (' '.join(l))
            #self.write_chain(cur for cur in reversed(self.elems)
            #            if self._hash_func(cur) == query.ind)

        elif query.type == "find": self.find(query)

        elif query.type == "add": self.add(query)
            
        elif query.type == "del":
            i = self._hash_func(query.s)
            try : self.A[i].remove(query.s)
            except : pass

        '''
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)'''

    def find(self, query):
        i = self._hash_func(query.s)
        l= self.A[i]
        for it in l:
            if it==query.s : 
                print('yes')
                return
        print('no')  

    def add(self, query):
        i = self._hash_func(query.s)
        l= self.A[i]
        for it in l:
            if it==query.s : 
                return
        self.A[i].insert(0,query.s)               


    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

    def read_query(self):
        return Query(input().split())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
