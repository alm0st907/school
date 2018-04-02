#Garrett Rudisill
#CptS 355 HW4 part 1
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
     retValue = re.findall("-?\d+\.\d|/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z09_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)
     #retValue = re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z09_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)
     
     return retValue


#flexible way to groupmatch
#i know it works because parsing worked fine
def groupMatching(it, left,right):
    result = []
    for thing in it:
        if thing == right:
            return result
            #stuff is matched up

        elif thing == left :
            result.append(groupMatching(it,left,right))
            #we found a sublist
        elif thing != ' ':
            result.append(thing)
        else:
            return False

#NEED TO TEST
def parse(tokens):
    print(tokens)
    tok_list = iter(tokens) #makes into iterable list
    parsed_list = []
    for token in tok_list:
        if isinstance(token, list):
            parsed_list.append(parse(token))
        elif token[0] == '{':
            group = groupMatching(tok_list,'{','}')
            if group: parsed_list.append(parse(group))
            #if our groupmatching doesnt return false, recursively parse and append from that list
        elif token[0] == '[':
            sub_it = iter(token[1:]) if len(token) > 1  else tok_list
            group = groupMatching( sub_it, '[',']')
            if group: 
                parsed_list.append(parse(group))
        elif (token[0].isdigit() or (token[0]=='-' and token[1].isdigit())):#checks for a number
            #check for pos/neg floats
            if token.find('.') != -1 or (token.find('-') and token.find('.') != -1): 
                token=float(token)
            else:#otherwise this is an int
                token = int(token)
            parsed_list.append(token)
        else:parsed_list.append(token) #string
    return parsed_list

def testParse():
    # Test cases, handles +- ints and floats, code arrays, etc
    tokens = parse(tokenize("/square {dup mul} def -1.1 square 2 square -3 square add add"))
    if tokens == ['/square', ['dup', 'mul'], 'def', -1.1, 'square', 2, 'square', -3, 'square', 'add', 'add']:
        print("\ntokens are "+str(tokens))
        return True
               
    else:
        return False
        

#need to handle a 
def forLoop():
    code_ar = opPop()
    final = opPop()
    incr = opPop()
    init = opPop()
    if isinstance((code_ar and final and incr), int) and isinstance(init, list): #type check our oppops
        if incr < 0 :
            final -= 1
        else:
            final += 1
        for index in range (final,incr):
            opPush(index)
            print("INTERPRET CALL MISSING IN FORLOOP")
        
    else:
        print("missing arg for loop")


#def forall():
#    pass
def safe_ex(token):
    if token in PsOps:#see if function in dictionary
        try:
            PsOps[token]() #executes function from dictionary
        except:
            print("some error or something")

def interpret(code):
    #this takes in the parsed code to start operating on
    pass


#dictionary of operations we can call in the interpreter
#not sure if i need for all alongside for
PsOps = {"add": add, "sub": sub, "div": div, "mul": mul, "mod": mod, "length": length, "get": get, "pop": pop, "dup": dup, "exch": exch, "roll": roll, "copy": copy, "clear": clear, "stack": stack, "def": psDef, "dict": psDict, "begin": begin, "end": end, "for": forLoop}

#need to implement the for loop/for all loop
#implement interpreter function


if __name__ == '__main__':
    print("not finished lols")
    opPush(3)
    opPush(4)
    safe_ex("sub")
    print(opPop())