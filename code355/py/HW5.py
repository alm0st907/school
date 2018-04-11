#Garrett Rudisill
#CptS 355 HW4 part 1 & 2
#WSU ID 11461816
#PostScript interpreter part 1 in python 3.6
#tested on both linux and windows

#opstack portion
opstack = []

def opPop():
    #pop a item off stack if its not empty
    if len(opstack) > 0:
        return opstack.pop()
    else:
        print("Op stack is empty")

def opPush(val):
    #push things to the stack
    #functions error check, so we dont need to check whats pushed
    opstack.append(val)

#dictionary stack
#-----------------------
dictstack = []

def dictPop():
    #pop from dictionary if there is an item inside
    if len(dictstack) > 0:
        return dictstack.pop()
    else:
        print("Dict stack is empty")

def dictPush(d):
    #append to dictstack
    dictstack.append(d)

def define(name,val):
    if name[0] =='/':#check for / character symbolizing a var def
        name = name[1:]#rem /
        if dictstack == []:#if dictionary stack empty
            d = {}
            d[name] = val
            dictstack.append(d) #append new dict with val to dictstack
        else:
            (dictstack[-1])[name]=val #update if not empty
    else:
        print("variable not defined")

#check this
def lookup(name):
    operable_dict = reversed(dictstack) #if more than one dict, ensure from top of stack to bottom
    for d in operable_dict:
        if name in d:
            return d[name]
    else:
        return None

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
        #type checking
        if isinstance(op1,(int,float)) and isinstance(op2,(int,float)):
            opstack.append(op1+op2)
        else:
            print("Invalid inputs")
    except:
        print("not enough args")

def sub():
    try:
        op1 = opPop()
        op2 = opPop()
        #type checking
        if isinstance(op1,(int,float)) and isinstance(op2,(int,float)):
            opstack.append(op2-op1)
        else:
            print("Invalid inputs")
    except:
        print("not enough args")

def mul():
    try:
        op1 = opPop()
        op2 = opPop()
        #type checking
        if isinstance(op1,(int,float)) and isinstance(op2,(int,float)):
            opstack.append(op2*op1)
        else:
            print("Invalid inputs")
    except:
        print("not enough args")

def div():
    try:
        op1 = opPop()
        op2 = opPop()
        if op2 == 0:
            print("div by 0 error")
            return
        elif op1 == 0 and op2 == 0:
            print("div by 0 error")
            return
        elif op1 == 0:
            opstack.append(0)
            return
        else:
            pass
        #type checking
        if isinstance(op1,(int,float)) and isinstance(op2,(int,float)):
                opstack.append(op2/op1)
        else:
            print("invalid inputs")
    except:
        print("not enough args")

def mod():
    try:
        op1 = opPop()
        op2 = opPop()
        #type checking
        #mods are probably int only?
        if isinstance(op1,int) and isinstance(op2,int):
            opstack.append(op2%op1)
        else:
            print("invalid ops")
    except:
        print("not enough args")


#array ops
#---------
#length
#get

def length():
    temp = opPop()
    if isinstance(temp, list): #check for array before len call
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
    #works, could be more efficient, but I dont really care

def exch():
    op1 = opPop()
    op2 = opPop()
    if op1 == None or op2 == None:
        print("cant exchange some with none")
        return
    opstack.append(op1)
    opstack.append(op2)
    #ol' reddit switcheroo

def pop():
    _ = opPop()
    #trash a op

def clear():
    opstack.clear()
    #nuclear launch @ stack detected

def copy():
    try:#how many items to copy
        numItems = int(opPop()) #cast to an int if possible
    except:
        print("Item is null/unsucessfully converted to int")
        return
    if numItems > len(opstack) or numItems < 0:
        print("negative items or attempting to copy nonexistent items")
        return
    else:
        #operation execution
        i = 0
        temp = []
        operableStack = list(reversed(opstack))
        #reversed for easy linear traversal
        while i < numItems: #iterate for i number of items
            #get num items
            temp.append(operableStack[i])
            i+=1            
        for val in temp:#appened all the values that need to be copied
            opstack.append(val)
        

    

def roll():
    if len(opstack) <=2 : #stack 2 short
        print("not enough args, cant roll")
        return
    rolls = opPop() # num of rolls
    items = opPop() # num of items to be rolled
    if not isinstance(rolls,int) or not isinstance(items,int): #datatype check
        print("invalid args")
        return
    elif items < 0:
        print("invalid index")
        return
    elif items <2:
        return #no change to stack
    
    else: #actually perform op
        if rolls >=0 : #roll data to bottom from top
            items = -items +1 #index correction
            for count in range(rolls):
                val = opPop()
                opstack[items:items-1]=[val]
        else:
            #roll data to top from bottom
            items = -items
            rolls = -rolls
            for count in range(rolls):
                val = opPop()
                opstack[items:items-1]=[val]

#print le stack
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

#push a dict to dictstack
def begin():
    temp = opPop()
    if isinstance(temp, dict):
        dictPush(temp)
    else:
        print("not a dictionary")

#pop off dictstact
def end():
    if dictstack != None:
        dictPop()
    else:
        print("dict empty, nothing to pop from end")

#define stuff
def psDef():
    val = opPop()
    name = opPop()
    define(name,val)

#-----------------------------------#
#part 2 work

import re #for regex handling

#given function that uses regex for parsing the passed in code
def tokenize(s):
    retValue = re.findall(r"-?\d*\.\d*|/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z09_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)
    #r before quotes removes the pylint errors thrown in vs code linting   
    #I added -?\d*\.\d*| to the regex for +- float parsing as well.  
    return retValue


#flexible way to groupmatch
def groupMatching(it, left,right):
    result = [] #the inner code from parsing
    for thing in it:
        if thing == right: 
            return result
            #return on hitting right bracket

        elif thing == left :
            result.append(groupMatching(it,left,right))
            #we found a sublist, make another call
        elif thing != ' ': #append what isnt a space
            result.append(thing)
        else:
            return False #unmatched braces

#breaking the tokens down
def parse(tokens):
    tok_list = iter(tokens) #makes into iterable list
    parsed_list = [] #list of parsed code
    for token in tok_list: #iterate through each token
        if isinstance(token, list): #array
            parsed_list.append(parse(token)) #append a code array
        elif token[0] == '{': #code arrays and such
            group = groupMatching(tok_list,'{','}')
            if group: 
                parsed_list.append(parse(group))
            #if our groupmatching doesnt return false, recursively parse and append from that list
        elif token[0] == '[':
            sub_it = iter(token[1:]) if len(token) > 1  else tok_list
            group = groupMatching( sub_it, '[',']')
            if group: 
                parsed_list.append(parse(group))
        elif (token[0].isdigit() or (token[0]=='-' and token[1].isdigit())):#checks for a number, and a potential negative sign
            #check for pos/neg floats
            if token.find('.') != -1 or (token.find('-') and token.find('.') != -1): 
                #we check for a "." or "-" and a period which denotes a pos/neg float
                token=float(token)
            else:#otherwise this is an int
                token = int(token)
            parsed_list.append(token)#append the token after doing castings
        else:
            parsed_list.append(token) #string
    return parsed_list

#for loop implementation
def forLoop():
    codeArr = opPop() #code array
    final = opPop() #final condition
    incr = opPop() #increment
    init = opPop()#starting point
    if(isinstance((final and incr and init), (int)) and isinstance(codeArr, list)):
        if (final > init and incr < 0) or (init > final and incr > 0) or incr == 0:
            print("Infinite loop/out of bounds ya dingus")
            #error checking for infinite loop/out of bounds
            return
        else:
            if incr>0: final+=1 #final value manipulation allowed in positive increments
            else: final-=1 #for negative indexing
            for index in range(init, final, incr):#increment throught the range
                opPush(index) #push the index to stack
                interpret(codeArr) #apply code array
    else:
        print("You have an invalid argument")
        
#recursive code interpreter that handles our parsed code
def interpret(code):
    for token in code:                  
        if isinstance(token, str):
            #if token is a string, its a name, a lookup, or an op
            if token[0]=='/':
                #slash denotes var name to be defined
                opPush(token)
            elif token in PsOps:
                #if token is a valid function from the dict, we call it
                PsOps[token]()
            else:
                lookup_val = lookup(token)#try a lookup if name lacks "/"
                if lookup_val != None:
                    if isinstance(lookup_val, list):
                        #detected a code array, so we recursively call the interpreter on it
                        interpret(lookup_val)
                    else:
                        opPush(lookup_val)
                else:
                    print("undefined variable")#if none is returned, that var isnt found
        else:            #ints, floats, and lists just get pushed to opstack
            opPush(token)
    return

def interpreter(original_code):#all in one call to run interpreter. Pass in the ps code and let it rip
    interpret(parse(tokenize(original_code)))

def testParse():
    # Test cases
    tokens = parse(tokenize("/square {dup mul} def 1 square 2 square 3 square add add"))
    if tokens != ['/square', ['dup', 'mul'], 'def', 1, 'square', 2, 'square', 3, 'square', 'add', 'add']:
        return False

    tokens = parse(tokenize("/n 5 def 1 n -1 1 {mul} for"))
    if tokens != ['/n', 5, 'def', 1, 'n', -1, 1, ['mul'], 'for']:
        return False

    tokens = parse(tokenize("/sum { -1 0 {add} for } def 0 [1 2 3 4] length sum 2 mul [1 2 3 4] {2 mul} forall add add add stack"))
    if tokens != ['/sum', [-1, 0, ['add'], 'for'], 'def', 0, [1, 2, 3, 4], 'length', 'sum', 2, 'mul', [1, 2, 3, 4], [2, 'mul'], 'forall', 'add', 'add', 'add', 'stack']:
        return False

    return True

def testInterpreter():
    #good input test from pdf
    interpreter("/fact {0 dict begin /n exch def 1 n -1 1 {mul} for end} def [1 2 3 4 5] dup 4 get pop length fact stack")
    if opPop() != 120:
        return False
    clear()
    dictstack.clear()
    #clears just in case before code runs

    #testing pad ps code coming in, doesnt evaluate to a number and should return None when oppop()
    interpreter("/sum { -1 0 {add} for} def 0 [1 2 3 4] length sum 2 mul [1 2 3 4] 2 get add add add stack")
    if opPop() != None:
        return False    
    
    clear()
    dictstack.clear()
    #some random ps i wrote
    interpreter(" /thing 4 def [1 2 5 6] 3 get thing mul stack")
    if opPop() != 24 :
        return False
    
    clear()
    dictstack.clear()
    return True



#dictionary of operations we can call in the interpreter

PsOps = {"add": add, "sub": sub, "div": div, "mul": mul, "mod": mod, "length": length, "get": get, "pop": pop, "dup": dup, "exch": exch, "roll": roll, "copy": copy, "clear": clear, "stack": stack, "def": psDef, "dict": psDict, "begin": begin, "end": end, "for": forLoop}


if __name__ == '__main__':
    testing = True
    if testing == True:
        print("\nRunning tests. Change testing @ line 435 to false to disable \n")
        print("Parsing testing",testParse(),"\n")
        print("interpreter testing/output :", testInterpreter(),"\n\ntests complete\n")
    else:
        print("running any code after line 441.")

        

    
    