#Garrett Rudisill
#CptS 355 HW4 part 1

#opstack portion
opstack = []

def opPop():
    return opstack.pop()

def opPush(val):
    #probably more to be done here
    #use isinstance or type() to check for a type for error checking push

    opstack.append(val)

#dictionary stack
#-----------------------
dictstack = []

def dictPop():
    return dictstack.pop()

def dictPush(d):
    #use isinstance or type() to check for a type for error checking push
    dictstack.append(d)

def define(name,val):
    if dictstack == []:
        d = {}
        d[name] = val
        dictstack.append(d)
    else:
        #push to top of dictionary of dict stack
        (dictstack[-1])[name] = val

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
    op1 = opPop()
    op2 = opPop()
    opstack.append(op1+op2)

def sub():
    op1 = opPop()
    op2 = opPop()
    opstack.append(op1-op2)

def mul():
    op1 = opPop()
    op2 = opPop()
    opstack.append(op1*op2)

def div():
    op1 = opPop()
    op2 = opPop()
    opstack.append(op1/op2)

def mod():
    op1 = opPop()
    op2 = opPop()
    opstack.append(op1%op2)


#array ops
#---------
#length
#get

#stack manip ops
#--------
#dup, exch, pop, roll , copy, clear, stack

#dick manip ops
#------
#psDict, begin, end, psDef


#testfunction
def tests():
    print("Hope your code isnt ass\n")
    pass

def main():
    mytests = True
    if mytests == True:
        print("Running my tests, set mytests at line 336 to false to disable\n")
        tests()
    else:
        print("Executing your tests")
if __name__ == "__main__":
    main()