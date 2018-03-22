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
        opstack.append(op1-op2)
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
            opstack.append(op1/op2)
        else:
            print("div by 0 error")
    except:
        print("not enough args")

def mod():
    try:
        op1 = opPop()
        op2 = opPop()
        opstack.append(op1%op2)
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

def clear():
    opstack.clear()

def copy():
    # Sufficient number of operands
    if len(opstack) >= 1:
        N = opstack[-1] # Number of top values to copy

        # Check for right data type
        if type(N) is int:
            # N has to be lower than or equal to number of elements in stack
            if (N <= len(opstack)):
                # Non negative N
                if (N >= 0):
                    N = opPop() # pop N from stack
                    L = [] # Temp list
                    for index in range(-N, 0, +1): # Start at -N, stop before 0, increment
                        L.append(opstack[index]) # Append top values to temp list
                    for value in L: # For each element in temp list
                        opstack.append(value) # Push element to stack to copy top values
                # Negative N
                else:
                    return "negative" # Return error
            # N is out of range of stack
            else:
                return "range" # Return error
        # Wrong data type
        else:
            return "type" # Return error
    # Insufficient operands
    else:
        return "operand" # Return error
    
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

#testfunction
def testDefine():
    # Layer 1 of dictionaries: new entry
    dictPush({})
    define('x', 1)
    if lookup('x') != 1:
        return False
    # Layer 2 of dictionaries: new entry
    dictPush({})
    define('x', 2)
    if lookup('x') != 2:
        return False
    # Update existing entry
    define('x', 3)
    if lookup('x') != 3:
        return False
    return True

def testLookup():
    # Layer 1 of dictionaries: Defined name constant
    opPush("y")
    opPush(10)
    psDef()
    if lookup("y") != 10:
        return False
    # Layer 2 of dictionaries: Defined name constant
    dictPush() # Create new layer
    opPush("nl")
    opPush(3)
    psDef()
    if lookup("nl") != 3:
        return False
    # Layer 3 of dictionaries: Defined name constant
    dictPush() # Create new layer
    opPush("x")
    opPush(4)
    psDef()
    if lookup("x") != 4:
        return False
    # Non-defined name constant
    if lookup("xl") != None:
        return False
    # Previous layer: Define name constant
    if lookup("y") != 10:
        return False
    return True

############################# operand stack operations ########################

def testOpPush():
    # String
    # Case 1: Name constant
    opPush('/x')
    if opstack[-1] != 'x':
        return False
    # Case 2: Name
    dictPush()
    define('x', 3)
    opPush('x')
    if opstack[-1] != 3: # Defined
        return False
    # Array constant
    opPush([])
    if opstack[-1] != []:
        return False
    # Integer constant
    opPush(1)
    if opstack[-1] != 1:
        return False
    # Real constant
    opPush(1.0)
    if opstack[-1] != 1.0:
        return False
    # Dictionaries
    opPush({})
    if opstack[-1] != {}:
        return False
    return True

############################ arithmetic operators ###############################

def testAdd():
    # Test Cases
    # Test 1: Int & Int
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    # Test 2: Float & Int
    opPush(2.5)
    opPush(1)
    add()
    if opPop() != 3.5:
        return False
    # Test 3: Int & Float
    opPush(2)
    opPush(2.5)
    add()
    if opPop() != 4.5:
        return False
    # Test 4: Float & Float
    opPush(1.5)
    opPush(1.5)
    add()
    if opPop() != 3.0:
        return False

    
    return True

def testSub():
    # Test Cases
    # Test 1: Int & Int
    opPush(1)
    opPush(2)
    sub()
    if opPop() != -1:
        return False
    # Test 2: Float & Int
    opPush(1)
    opPush(2.5)
    sub()
    if opPop() != -1.5:
        return False
    # Test 3: Int & Float
    opPush(1.5)
    opPush(2)
    sub()
    if opPop() != -0.5:
        return False
    # Test 4: Float & Float
    opPush(1.5)
    opPush(1.5)
    sub()
    if opPop() != 0.0:
        return False

    # Error Test Cases
    # Test 1: Not enough operands
    opPush(1)
    if sub() != "operand":
        return False
    # Test 2: Wrong data type
    opPush(1)
    opPush([])
    if sub() != "type":
        return False
    opPush(1.0)
    opPush([])
    if sub() != "type":
        return False
    opPush([])
    opPush(1.0)
    if sub() != "type":
        return False
    opPush([])
    opPush(1.0)
    if sub() != "type":
        return False
    return True

def testMul():
    # Test Cases
    # Test 1: Int & Int
    opPush(1)
    opPush(2)
    mul()
    if opPop() != 2:
        return False
    # Test 2: Float & Int
    opPush(2.5)
    opPush(1)
    mul()
    if opPop() != 2.5:
        return False
    # Test 3: Int & Float
    opPush(1)
    opPush(2.5)
    mul()
    if opPop() != 2.5:
        return False
    # Test 4: Float & Float
    opPush(1.5)
    opPush(1.5)
    mul()
    if opPop() != 2.25:
        return False

    return True

def testDiv():
    # Test Cases
    # Test 1: Int & Int
    opPush(2)
    opPush(1)
    div()
    if opPop() != 2:
        return False
    # Test 2: Float & Int
    opPush(1)
    opPush(2.5)
    div()
    if opPop() != 0.4:
        return False
    # Test 3: Int & Float
    opPush(2.5)
    opPush(2)
    div()
    if opPop() != 1.25:
        return False
    # Test 4: Float & Float
    opPush(1.5)
    opPush(1.5)
    div()
    if opPop() != 1.0:
        return False

    # Error Test Cases
    # Test 1: Not enough operands
    opPush(1)
    if div() != "operand":
        return False
    # Test 2: Wrong data type
    opPush(1)
    opPush([])
    if div() != "type":
        return False
    opPush(1.0)
    opPush([])
    if div() != "type":
        return False
    opPush([])
    opPush(1.0)
    if div() != "type":
        return False
    opPush([])
    opPush(1.0)
    if div() != "type":
        return False
    # Test 3: denominator = 0
    opPush(2)
    opPush(0)
    if div() != "undefined":
        return False
    return True

def testMod():
    # Test Cases
    # Test 1: Int & Int
    opPush(2)
    opPush(1)
    mod()
    if opPop() != 0:
        return False
    opPush(7)
    opPush(4)
    mod()
    if opPop() != 3:
        return False

    # Error Test Cases
    # Test 1: Not enough operands
    if mod() != "operand":
        return False
    # Test 2: Wrong data type
    opPush(1)
    opPush([])
    if mod() != "type":
        return False
    opPush(1)
    opPush(1.0)
    if mod() != "type":
        return False
    opPush([])
    opPush(1)
    if mod() != "type":
        return False
    opPush(1.0)
    opPush(1)
    if mod() != "type":
        return False
    # Test 3: denominator = 0
    opPush(2)
    opPush(0)
    if mod() != "undefined":
        return False
    return True

################################ Array operators #############################

def testLength():
    # Test Cases
    # Non-empty array
    opPush([1, 2, 3, 4])
    length()
    if opPop() != 4:
        return False
    # empty array
    opPush([])
    length()
    if opPop() != 0:
        return False

    # Error Test Cases
    # Test 1: Not enough operands
    if length() != "operand":
        return False
    # Test 2: Wrong type
    opPush(1)
    if length() != "type":
        return False
    return True

def testGet():
    # Test Cases
    # Non-empty array
    opPush([1, 2, 3, 4])
    opPush(0)
    get()
    if opPop() != 1:
        return False
    opPush([1, 2, 3, 4])
    opPush(1)
    get()
    if opPop() != 2:
        return False

    # Error Test Cases
    # Test 1: Not enough operands
    if get() != "operand":
        return False
    # Test 2: Wrong type
    opPush(1.0)
    opPush([1, 2])
    if get() != "type":
        return False
    opPush(1)
    opPush(1.0)
    if get() != "type":
        return False
    # Test 3: Index not in range
    opPush([1])
    opPush(6)
    if get() != "range":
        return False
    return True

###################### Stack manipulation & print operators ####################

def testPop():
    # Test Cases
    # Non-empty stack
    opPush(1)
    opPush(2)
    pop()
    if opstack[-1] != 1:
        return False

    # Error Test Cases
    # Empty stack
    pop()
    if pop() != "empty":
        return False
    return True

def testDup():
    # Test Cases
    # Name constant
    opPush("/x")
    dup()
    if opPop() != 'x' or opPop() != 'x':
        return False
    # array constant
    opPush([])
    dup()
    if opPop() != [] or opPop() != []:
        return False
    # Integer constant
    opPush(1)
    dup()
    if opPop() != 1 or opPop() != 1:
        return False
    # Real constant
    opPush(1.0)
    dup()
    if opPop() != 1.0 or opPop() != 1.0:
        return False
    # Dictionary
    opPush({})
    dup()
    if opPop() != {} or opPop() != {}:
        return False

    # Error Test Cases
    # Empty stack
    if dup() != "empty":
        return False
    return True

def testExch():
    # Test Cases
    # Integer constant
    opPush(1)
    opPush(2)
    exch()
    if opPop() != 1 or opPop() != 2:
        return False
    # Real constant
    opPush(1.0)
    opPush(2.0)
    exch()
    if opPop() != 1.0 or opPop() != 2.0:
        return False
    # Array constant
    opPush([1])
    opPush([])
    exch()
    if opPop() != [1] or opPop() != []:
        return False
    else:
        return True





def testCopy():
    # Test Cases
    opPush(1)
    opPush(2)
    # 1 copy
    opPush(1)
    copy()
    if opPop() != 2:
        return False
    if opPop() != 2:
        return False
    # 0 copy
    opPush(2)
    opPush(0)
    copy()
    if opPop() != 2:
        return False
    if opPop() != 1:
        return False

    # Error Test Cases
    # Test 1: Not enough operands
    if copy() != "operand":
        return False
    # Test 2: Wrong type
    opPush(1.3)
    if copy() != "type":
        return False
    # Test 3: Out of range of stack
    opPush(1)
    opPush(2)
    opPush(8)
    if copy() != "range":
        return False
    opPush(-1)
    if copy() != "negative":
        return False
    return True

def testClear():
    opPush(1)
    clear()
    if opstack: # If stack has content
        return False
    return True

########################## Dictionary manipulation operators ######################

def testDef():
    # Tase Cases
    # First layer of dictionaries: new defined variable
    dictPush({})
    opPush("/x")
    opPush(3)
    psDef()
    if lookup('x') != 3:
        return False
    # Updating variable
    opPush("/x")
    opPush(4)
    psDef()
    if lookup('x') != 4:
        return False
    # Second layer of dictionaries: new defined variable
    dictPush({})
    opPush('/x')
    opPush(5)
    psDef()
    if lookup('x') != 5:
        return False

    # Error Test Cases
    # Test 1: Not enough operands
    if psDef() != "operand":
        return False
    # Test 2: Wrong type
    opPush(1)
    opPush("/string")
    if psDef() != "type":
        return False
    opPush(1)
    opPush([])
    if psDef() != "type":
        return False
    return True

def testDict():
    # Test Cases
    # Push new empty stack to op stack
    opPush(1)
    psDict()
    if opPop() != {}:
        return False

    # Test Cases
    # Test 1: Not enough operands
    if psDict() != 'operand':
        return False
    # Test 2: Wrong type
    opPush(1.3)
    if psDict() != "type":
        return False
    return True

def testBegin():
    # Test Cases
    # Non empty dictionary
    opPush({'x':4})
    begin()
    if dictstack[-1] != {'x':4}:
        return False
    # empty dictionary
    opPush({})
    begin()
    if dictstack[-1] != {}:
        return False

    # Error Test Cases
    # Test 1: Empty stack
    if begin() != "empty":
        return False
    # Test 2: Wrong type
    opPush([])
    if begin() != "type":
        return False
    return True

def testEnd():
    # Test Cases
    dictPush({})
    dictPush({})
    # Top dictionary popped, one dictionary remains
    end()
    if dictstack[-1] != {}:
        return False
    # Top dictionary popped, empty stack
    end()
    if dictstack:
        return False

    # Error Test Cases
    # Empty dict stack
    if end() != "empty":
        return False
    return True


def testRoll():
    # Test Cases
    opPush(0)
    opPush(1)
    opPush(2)
    opPush(3)
    # 3 2 roll
    opPush(3)
    opPush(2)
    roll()
    if opstack != [0, 2, 3, 1]:
        return False
    # 3 -2 roll
    opPush(3)
    opPush(-2)
    roll()
    if opstack != [0, 1, 2, 3]:
        return False
    # 0 -2 roll
    opPush(0)
    opPush(-2)
    roll()
    if opstack != [0, 1, 2, 3]:
        return False
    # 1 2 roll
    opPush(1)
    opPush(2)
    roll()
    if opstack != [0, 1, 2, 3]:
        return False
    # 2 0 roll
    opPush(2)
    opPush(0)
    roll()
    if opstack != [0, 1, 2, 3]:
        return False

    # Error Test Cases
    # Test 1: Insufficient elements on stack
    opPush(8)
    opPush(1)
    if roll() != "insufficient":
        return False
    # Test 2: Negative second operand
    opPush(-1)
    opPush(1)
    if roll() != "negative":
        return False
    # Test 3: Wrong type
    opPush([])
    opPush(1)
    if roll() != "type":
        return False
    opPush(1)
    opPush([])
    if roll() != "type":
        return False
    # Test 4: Not enough operands
    opstack.clear()
    if roll() != "operand":
        return False

    return True

#---------------------------------------------------------------------------------

#                                     Main                                       #

# Accepts a variable number of function names
# Accepts a dictionary with strings as keys and values as functions
# Tests all functions
def testAll(matchFuncs, *testNames):
    for testName in testNames:
        valid = matchFuncs[testName]() # Boolean value
        clear() # Clear operand stack
        dictstack.clear() # Clear dict stack

        # Display messages
        if valid == True:
            print(testName, "passed!")
        else:
            print(testName, "failed!")

if __name__ == '__main__':

    # Functions as high order objects
    # Dictionary of values as functions
    #matchTestFuncs = {"testDefine": testDefine, "testLookup": testLookup, "testOpPush": testOpPush, "testAdd": testAdd, "testSub": testSub, "testMul": testMul, "testDiv": testDiv, "testMod": testMod, "testLength": testMod, "testGet": testGet, "testPop": testPop, "testDup": testDup, "testExch": testExch, "testCopy": testCopy, "testClear": testClear, "testDef": testDef, "testDict": testDict, "testBegin": testBegin, "testEnd": testEnd}

    # Tests all of the functions
    #testAll(matchTestFuncs, "testDefine", "testLookup", "testOpPush", "testAdd", "testSub", "testMul", "testDiv", "testMod", "testLength", "testGet", "testPop", "testDup", "testExch", "testCopy", "testClear", "testDef", "testDict", "testBegin", "testEnd")
    opPush(1)
    opPush(2)
    add()
    opPush(4)
    opPush("str")
    mul()
    clear()
    print(testDefine())
    print(testLookup())
    print(testOpPush())
    print(testAdd())
    print(testMul())
    print(testExch())