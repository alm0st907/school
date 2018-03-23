#Garrett Rudisill
#CptS 355 HW4 part 1

#opstack portion
opstack = []

def opPop():
    if len(opstack) > 0:
        return opstack.pop()
    else:
        print("Op stack is empty")

def opPush(val):
    #probably more to be done here
    #use isinstance or type() to check for a type for error checking push

    opstack.append(val)

#dictionary stack
#-----------------------
dictstack = []

def dictPop():
    if len(dictstack) > 0:
        return dictstack.pop()
    else:
        print("Dict stack is empty")

def dictPush(d):
    #use isinstance or type() to check for a type for error checking push
    dictstack.append(d)

def define(name,val):
    try:
        top = dictstack[-1]
        top[name]=val
    except:
        pass

#check this
def lookup(name):
    operable_dict = reversed(dictstack)
    for d in operable_dict:
        if name in d:
            return d[name]
    else:
        print("Name is not defined")

#we gon shoot at ops
#-----
#add
#sub 
#mul
#div
#mod
def add():
    try:
        op1 = opPop()
        op2 = opPop()
        opstack.append(op1+op2)
    except:
        print("not enough args")

def sub():
    try:
        op1 = opPop()
        op2 = opPop()
        opstack.append(op2-op1)
    except:
        print("not enough args")

def mul():
    try:
        op1 = opPop()
        op2 = opPop()
        opstack.append(op1*op2)
    except:
        pass

def div():
    try:
        op1 = opPop()
        op2 = opPop()
        if op2 != 0:
            opstack.append(op2/op1)
        else:
            print("div by 0 error")
    except:
        print("not enough args")

def mod():
    try:
        op1 = opPop()
        op2 = opPop()
        opstack.append(op2%op1)
    except:
        print("not enough args")


#array ops
#---------
#length
#get

def length():
    temp = opPop()
    if isinstance(temp, list):
        opPush(len(temp))
    else:
        print("type error")

def get():
    ar_ind = opPop()
    arr = opPop()
    if isinstance(arr, list):
        try:
            opPush(arr[ar_ind])
        except:
            print("out of index error")
    else:
        print("type error - not array")

    
#stack manip ops
#--------
#dup, exch, pop, roll , copy, clear, stack

def dup():
    op1 = opPop()
    opstack.append(op1)
    opstack.append(op1)

def exch():
    op1 = opPop()
    op2 = opPop()
    opstack.append(op1)
    opstack.append(op2)

def pop():
    trash = opPop()
    #trash a op

def clear():
    opstack.clear()

def copy():
    try:#how many items to copy
        numItems = int(opPop())
    except:
        print("Item is null/unsucessfully converted to int")
    if numItems > len(opstack) or numItems < 0:
        print("negative items or attempting to copy nonexistent items")
    else:
        #operation execution
        i = 0
        temp = []
        operableStack = list(reversed(opstack))
        while i < numItems: 
            #get num items
            temp.append(operableStack[i])
            i+=1            
        for val in temp:
            opstack.append(val)
        

    
#not finished
def roll(post_position, vals):
    i = 0
    val_list = []
    while i < vals:
        val_list=opstack[i]
    for ent in val_list:
        opstack.insert(post_position,ent)
    i=0
    while i<vals:
        temp =opPop()
 
def stack():
    printable = reversed(opstack)
    for ent in printable:
        print(ent)

#dick manip ops
#------
#psDict, begin, end, psDef
def psDict():
    if opPop() != None:
        opPush({})
    else:
        print("operation not completed")

def begin():
    temp = opPop()
    if isinstance(temp, dict):
        dictPush(temp)
    else:
        print("not a dictionary")
def end():
    if dictstack != None:
        dictPop()
    else:
        print("dict empty, nothing to pop from end")

def psDef():
    val = opPop()
    name = opPop()
    if isinstance(name,str) and isinstance(val,(int,list)):
        if dictstack == None:
            dictPush({})
        define(name,lookup(val))
    
    elif isinstance(name,str) and isinstance(val,str):
        if dictstack == None:
            dictPush({})
        define(name,lookup(val))    
    else:
        print("type error")
#------- Part 1 TEST CASES--------------
def testDefine():
    define("/n1", 4)
    if lookup("n1") != 4:
        return False
    return True

def testLookup():
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True

#Arithmatic operator tests
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True

def testSub():
    opPush(10)
    opPush(4.5)
    sub()
    if opPop() != 5.5:
        return False
    return True

def testMul():
    opPush(2)
    opPush(4.5)
    mul()
    if opPop() != 9:
        return False
    return True

def testDiv():
    opPush(10)
    opPush(4)
    div()
    if opPop() != 2.5:
        return False
    return True

def testMod():
    opPush(10)
    opPush(3)
    mod()
    if opPop() != 1:
        return False
    return True

#Array operator tests
def testLength():
    opPush([1,2,3,4,5])
    length()
    if opPop() != 5:
        return False
    return True

def testGet():
    opPush([1,2,3,4,5])
    opPush(4)
    get()
    if opPop() != 5:
        return False
    return True

#stack manipulation functions
def testDup():
    opPush(10)
    dup()
    if opPop()!=opPop():
        return False
    return True

def testExch():
    opPush(10)
    opPush("/x")
    exch()
    if opPop()!=10 and opPop()!="/x":
        return False
    return True

def testPop():
    l1 = len(opstack)
    opPush(10)
    pop()
    l2= len(opstack)
    if l1!=l2:
        return False
    return True

def testRoll():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(4)
    opPush(-2)
    #roll()
    if opPop()!=3 and opPop()!=2 and opPop()!=5 and opPop()!=4 and opPop()!=1:
        return False
    return True

def testCopy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if opPop()!=5 and opPop()!=4 and opPop()!=5 and opPop()!=4 and opPop()!=3 and opPop()!=2:
        return False
    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack)!=0:
        return False
    return True

#dictionary stack operators
def testDict():
    opPush(1)
    psDict()
    if opPop()!={}:
        return False
    return True

def testBeginEnd():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x")!=3:
        return False
    return True

def testpsDef():
    opPush("/x")
    opPush(10)
    psDef()
    if lookup("x")!=10:
        return False
    return True

def testpsDef2():
    opPush("/x")
    opPush(10)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("x")!=10:
        end()
        return False
    end()
    return True


def main_part1():
    testCases = [('define',testDefine),('lookup',testLookup),('add', testAdd), ('sub', testSub),('mul', testMul),('div', testDiv),  ('mod', testMod), \
                ('length', testLength),('get', testGet), ('dup', testDup), ('exch', testExch), ('pop', testPop), ('roll', testRoll), ('copy', testCopy), \
                ('clear', testClear), ('dict', testDict), ('begin', testBeginEnd), ('psDef', testpsDef), ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('All part-1 tests OK')

if __name__ == '__main__':
    #main_part1()
    #math ops tested and good
    #print(testAdd())
    #print(testSub())
    #print(testMul())
    #print(testDiv())
    #print(testMod())

    #print(testLength())
    #print(testGet())