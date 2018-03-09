#garrett rudisill
#WSU ID 11461816
#HW3 "py-ton" CptS 355
from functools import reduce
from collections import OrderedDict
import math
import sys

#problem 1 - dictionaries
#add dict should get the total hours studied per class
def addDict(dict):
    keylist = dict.keys()#get all the keys from input dictionary
    #these keys are the days of the week
    studied = {}
    for keys in keylist:#loop accesses each key within a day
        daykey = dict[keys].keys()
        for subkeys in daykey: #access the values by key within a day
            day = dict[keys]
            val = day[subkeys]
            if subkeys not in studied: #add to the dictionary if it doesnt exist
                studied.update({subkeys:val})
            else: #update the value if the key exists already
                studied[subkeys] += val
    return studied

def addDictN(week_list):
    final = {} #dictionary for the results
    if week_list == []:
        return final
    def add_subs(dict1,dict2):
        keys1=dict1.keys()
        keys2=dict2.keys()
        for key in keys2:
            if key in keys1:
                dict1[key]+=dict2[key]
            else:
                dict1.update({key:dict2[key]})
        return dict1

    mapper= reduce(add_subs,map(addDict,week_list)) 
    #final result is mapper
    return mapper

#function to test output of the result
def testaddDict():
    print()
    week = {'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2,'360':3},'Thu':{'355':3,'451':2,'360':3}, 'Fri':{'355':2},'Sun':{'355':1,'451':3,'360':1}}
    result = {'355': 8, '451': 8, '360': 9}
    week2 = {'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2,'360':3}}
    result2 = {'355': 2, '451': 3, '360': 5}
    print("addDict Test "+str(addDict(week)==result))
    print("addDict Test "+str(addDict({})=={}))
    print("addDict Test "+str(addDict(week2)==result2))

    print()

#test function for addDictN
def testaddDictN():
    log = [{'Mon':{'355':2,'360':2},'Tue':{'451':2,'360':3},'Thu':{'360':3},'Fri':{'355':2}, 'Sun':{'355':1}},{'Tue':{'360':2},'Wed':{'355':2},'Fri':{'360':3, '355':1}},{'Mon':{'360':5},'Wed':{'451':4},'Thu':{'355':3},'Fri':{'360':6},'Sun':{'355':5}}]
    result = {'355': 16, '360': 24, '451': 6}
    log2 = [{'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2,'360':3},'Thu':{'355':3,'451':2,'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1,'451':3,'360':1}}]
    result2 = {'355': 8, '451': 8, '360': 9}
    
    print("addDictN Test "+str(addDictN(log)==result))
    print("addDictN Test "+str(addDictN([])=={}))
    print("addDictN Test "+str(addDictN(log2)==result2))


    print()

#problem 2 code
#needs to be sorted then stored to a list
def charCount(st):
    #write your code here
    try:
        stats = {}
        for letter in st:
            if letter == ' ':
                pass
            elif letter not in stats:
                stats.update({letter:1})
            else:
                stats[letter] +=1
        dic_keys = stats.keys()

        result_list = []

        for keys in dic_keys:
            temp = (keys, stats[keys])
            result_list.append(temp)

        result_list.sort(key = lambda x: x[0])
        result_list.sort(key = lambda x: x[1])
        #THIS FINISHES THEsort
        return(result_list)
    except:
        return []


def charCount2(st):
    #code here
    try:
        st = st.replace(' ','')#remove whitespace
        res2 =[(let,st.count(let)) for let in st] #list comprehens
        res2.sort(key = lambda x: x[0])
        res2.sort(key = lambda x: x[1])
        res2 = list(OrderedDict.fromkeys(res2))#remove duplicates
        return(res2)
    except:
        return []

def testCharCount():
    st="Cpts355 --- Assign1"
    result = [('1', 1), ('3', 1), ('A', 1), ('C', 1), ('g', 1), ('i', 1), ('n', 1),('p', 1), ('t', 1), ('5', 2), ('-', 3), ('s', 3)]
    print("char count test " + str(charCount(st)==result))
    print("char count test " + str(charCount("")==[]))
    print("char count test " + str(charCount(" ")==[]))

    print()

def testCharCount2():
    st="Cpts355 --- Assign1"
    result = [('1', 1), ('3', 1), ('A', 1), ('C', 1), ('g', 1), ('i', 1), ('n', 1),('p', 1), ('t', 1), ('5', 2), ('-', 3), ('s', 3)]
    print("char count2 test " + str(charCount2(st)==result))
    print("char count2 test " + str(charCount2("")==[]))
    print("char count2 test " + str(charCount2(" ")==[]))

    print()
    
#problem 3
def lookupVal(lst,val):
    #code here
    #code to reverse a list, modify later to make useful
    try:
        for ent in reversed(lst):
            if val in ent.keys():
                return ent[val]
            else:
                pass
    except:
        return None
    
def lookupValTest():
    L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
    print("lookupValTest = "+str(lookupVal(L1,"x")==2))
    print("lookupValTest = "+str(lookupVal(L1,"y")==False))
    print("lookupValTest = "+str(lookupVal(L1,"z")=="found"))
    print("lookupValTest = "+str(lookupVal(L1,"t")==None))
    print("lookupValTest = "+str(lookupVal([],"t")==None))
    print()

def lookupVal2(lst,key):
    #use a subfunction to handle the jumping from index to index
    #this hanldes the non linear jumps via the given index in the dictionary
    def helper(lst, ind, key):
        if key in lst[ind][1]:# key is in one of the dictionaries
            return lst[ind][1][key]#return the value

        elif ind == lst[ind][0]: #handling cur_ind = next_ind; key!=present
            return None

        else:
            temp = lst[ind] #get next index by nab the tuple
            return helper(lst,temp[0],key) #access index by accessing first of tuple
    #run in a try block to try and handle anything sam can throw at it
    try:
        return helper(lst,(lst.__len__())-1,key)
    except:
        return None            

def lookupVal2Test():
    L2 = [(0,{"x":0,"y":True,"z":"zero"}),(0,{"x":1}),(1,{"y":False}),(1,{"x":3, "z":"three"}),(2,{})]
    print("lookupValTest2 = "+str(lookupVal2(L2,"x")==1))
    print("lookupValTest2 = "+str(lookupVal2(L2,"y")==False))
    print("lookupValTest2 = "+str(lookupVal2(L2,"z")=="zero"))
    print("lookupValTest2 = "+str(lookupVal2(L2,"t")==None))
    print("lookupValTest2 = "+str(lookupVal2([],"t")==None))
    print()

#problem 4
def funRun(d, name, args):
    try:#handles for function not in list
        function = d[name] #lambda func from dictionary
    except:
        return None
    try:
        val = function(*args)#execute and return function if possible
        return(val)
    except:#handling not enough args/bad input
        return None
def funRunTest():
    d = {"add": lambda x,y: (x+y), "concat3": lambda a,b,c:(a+","+b+","+c),"mod2": lambda n: (n % 2)}
    print("fun run test " + str(funRun(d,"concat3",["one","two","three"])=="one,two,three"))
    print("fun run test " + str(funRun(d,"mod2",[40])==0))
    print("fun run test "+ str(funRun(d,"mod3",[])==None))
    print("fun run test "+ str(funRun(d,"mod2",[])==None))
    print("fun run test "+ str(funRun([],"mod3",[])==None))
    print()
    

#problem 5
def numPaths(x, y):
    if(x <= 0 or y <=0): #stop trying to break my code plz
        return 0
    #base case to exit the loop
    if(x == 1 or y == 1):
        return 1
    #recursively iterate 
    return  numPaths(x-1, y) + numPaths(x, y-1)
 
def numberOfPathsTest():
    print("numPath tests " + str(numPaths(2,2)==2))
    print("numPath tests " + str(numPaths(3,3)==6))
    print("numPath tests " + str(numPaths(0,2)==0))
    print("numPath tests " + str(numPaths(2,0)==0))
    print("numPath tests " + str(numPaths(0,0)==0))
    print()

#problem 6
class iterSquares():
    def __init__(self):#constructor for the class
        self.square = 0
        self.pos = 0
    def __next__(self):#iterate up to the next square and return
        self.pos +=1
        self.square = self.pos*self.pos
        return self.square
    def __cur__(self):#return current square
        return self.square

def numbersToSum(iNumbers,sum):
    result=[]
    cur_sum = 0
    if iNumbers.__cur__() == 0: #making sure we start at 1
        cur_square = iNumbers.__next__()
    else: # preventing off by one on subsequent calls on same class
        cur_square = iNumbers.__cur__()
    while  cur_sum + cur_square < sum: #checking if we are at n-1 of sum
        result.append(cur_square)
        cur_sum +=cur_square
        cur_square = iNumbers.__next__()
    return result

def numbersToSumTest():
    squares = iterSquares()
    test = numbersToSum(squares,55)
    test2 = numbersToSum(squares,100)
    test3 = numbersToSum(iterSquares(),100)
    if test ==[1, 4, 9, 16] and test2 ==[25, 36] and test3 == [1,4,9,16,25,36]:
        print("numToSum tests True")
    else:
        print("numToSum pass fail")

#problem 7

class Stream(object):
    def __init__(self, first, compute_rest, empty = False):#construct
        self.first = first
        self._compute_rest = compute_rest
        self.empty = empty
        self._rest = None
        self._computed = False
    @property
    def rest(self):#rest property to call on stream objects
        assert not self.empty, 'Empty streams have no rest'
        if not self._computed:
            self._rest = self._compute_rest()
            self._computed = True
        return self._rest

def make_integer_stream(first = 1):#default construct is 1, or what is passed in
    def compute_rest():
        return make_integer_stream(first+1)#increment up
    return Stream(first, compute_rest)#return integer, call increment

def evenStream(streamObj):
    temp = streamObj.first
    if temp % 2 == 0:#check if stream obj is even
        def compute_rest():
            return evenStream(streamObj.rest)
        return Stream(temp,compute_rest)#return even and increment stream
    else:#stream obj isnt returning an even num
        while temp % 2 != 0:#loop to iterate until even
            streamObj = streamObj.rest
            temp = streamObj.first
        def compute_rest():
            return evenStream(streamObj.rest)
        return Stream(temp,compute_rest)

def streamSquares(square=1):
    if(square % math.sqrt(square) != 0):#check for a int root/square
    #this guaruntees 1, or a square is coming in for expected output
        print("stop trying to break my code dammit")
        return sys.exit("exiting due to non integer root")
    else:
        root = math.sqrt(square)#get square root of what is passed in
        root+=1#increment up for next square
        new_sqr = root* root #make the square
        new_sqr = int(new_sqr)#cast as int just to make sure
        if square == 1:#making sure that it properly increments up from 1
            def compute_rest():
                return streamSquares(4)
            return Stream(square,compute_rest)
        else:#any other number
            def compute_rest():
                return streamSquares(new_sqr)
            return Stream(square,compute_rest)

def evenStreamTest():
    sqStream = evenStream(streamSquares(9))
    lst = []
    while sqStream.first <225:
        lst.append(sqStream.first)
        sqStream = sqStream.rest
    if lst == [16, 36, 64, 100, 144, 196]:
        print("Even stream test true")
    else:
        print("even stream test failed")
    
    sqStream = evenStream(streamSquares())
    lst2 = []
    while sqStream.first <225:
        lst2.append(sqStream.first)
        sqStream = sqStream.rest
    if lst2 == [4,16, 36, 64, 100, 144, 196]:
        print("Even stream test true")
    else:
        print("even stream test failed")
        
    sqStream = evenStream(streamSquares(64))
    lst2 = []
    while sqStream.first <225:
        lst2.append(sqStream.first)
        sqStream = sqStream.rest
    if lst2 == [64, 100, 144, 196]:
        print("Even stream test true")
    else:
        print("even stream test failed")

def test_cases():
    testaddDict()
    testaddDictN()
    testCharCount()
    testCharCount2()
    lookupValTest()
    lookupVal2Test()
    funRunTest()
    numberOfPathsTest()
    numbersToSumTest()
    evenStreamTest()

#where the bullshit and black magic gets executed
def main():
    mytests = True
    if mytests == True:
        print("Running my tests, set mytests at line 336 to false to disable")
        test_cases()
    else:
        print("Executing your tests")
if __name__ == "__main__":
    main()