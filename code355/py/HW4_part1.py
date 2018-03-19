#Garrett Rudisill
#CptS 355 HW4 part 1

#opstack portion
opstack = []

def opPop():
    return opstack.pop()

def opPush(val):
    #probably more to be done here
    opstack.append(val)

#dictionary stack
#-----------------------
dictstack = []

def dictPop():
    return dictstack.pop()

def dictPush(d):
    dictstack.append(d)

def define(name,val):
    pass

def lookup(name):
    pass

#we gon shoot at ops
#-----
#add
#sub
#mul
#div
#mod

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