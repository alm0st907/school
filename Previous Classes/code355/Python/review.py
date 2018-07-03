#review.py
x = 0
def add(a):
    global x
    x = a+x
    return x
def sumAll (L):
    if not L:
        return 0
    else:
        return L[0] + sumAll(L[1:])
def grow (c):
    return sumAll (range (c, c +2))
def outer (f):
    def inner (g, y):
        return f(y)+g(y)
    return inner
#page 2   
class Stream(object):
    def __init__(self, first, compute_rest, empty= False):
        self.first = first
        self._compute_rest = compute_rest
        self.empty = empty
        self._rest = None
        self._computed = False
    @property
    def rest(self):
        assert not self.empty, 'Empty streams have no rest.'
        if not self._computed:
            self._rest = self._compute_rest()
            self._computed = True
        return self._rest
empty_stream = Stream(None, None, True)

def stream_mystery(fn, n, s1):
    def compute_rest():
        return stream_mystery(fn, n, s1)
    t = n
    temp = 0
    while (t > 0):
        temp = fn(temp,s1.first)
        s1 = s1.rest
        t -= 1
    return Stream(temp, compute_rest)

def make_integer_stream(first=1):
    def compute_rest():
        return make_integer_stream(first+1)
    return Stream(first, compute_rest)
S2 = stream_mystery(lambda x,y: x+y, 2, make_integer_stream(1))

def make_one_stream(): 
    def compute_rest(): 
        return make_one_stream() 
    return Stream(1, compute_rest)

def aroundL(L):
    temp = []
    for item in L:
        temp.append((item-1,item+1))
    for item in temp:
        print(item)

def aroundL2(L):
    temp = [(item-1,item+1)for item in L]
    for item in temp:
        print(item)

def wordCount(L):
    temp = {}
    for item in L:
        temp[item]= 1+(temp.get(item,0))
    print(temp)
    
  
if __name__ == "__main__":
    L = [1,2,3,4,5]
    #for each item in list, number plus next number(not of list)
    # 1+2, 2+3, 3+4, 4+5, 5+6
    print(list(map(grow,L)))
    
    #sum of list up to current iteration
    L = [1,2,3,4,5]
    print(list(map(add,L)))

    x = 1
    #adds add + grow
    print(outer (add) (grow,5))
    #add global x =1 and 5
    #grow is sum of input plus next number

    x = 2
                #add return 4, add returns 6, add together for total 10
    print(outer (add) (add,x))

    print(S2.first, S2.rest.first, S2.rest.rest.first, S2.rest.rest.rest.first)
    
    aroundL([1,2,3])
    aroundL2([1,2,3])
    
    wordCount(["yes","yes","no","maybe","probably"])

    S3 = stream_mystery(lambda x,y: x+y, 3, make_one_stream())
    print(S3.first,S3.rest.first,S3.rest.rest.first, S3.rest.rest.rest.first)
