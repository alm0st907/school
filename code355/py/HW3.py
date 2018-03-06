#garrett rudisill
#HW3 CptS 355
from functools import reduce
from collections import OrderedDict
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

#function to test output of the result
def testaddDict(result):
        if result == {'355': 8, '451': 8, '360': 9}:
            print("test pass")
        else:
            print("test fail")

def addDictN(week_list):
    final = {} #dictionary for the results

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
    print(mapper)
    #final result is mapper
    return mapper

#test function for addDictN
def testaddDictN(result):
    if result == {'355': 16, '360': 24, '451': 6}:
        print("test pass")
    else:
        print("test fail")

#problem 2 code
#needs to be sorted then stored to a list
def charCount(st):
    #write your code here
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
    print(result_list)
    return(result_list)


def charCount2(st):
    #code here
    st = st.replace(' ','')#remove whitespace
    res2 =[(let,st.count(let)) for let in st]
    res2.sort(key = lambda x: x[0])
    res2.sort(key = lambda x: x[1])
    #res2= list(set(res2))
    res2 = list(OrderedDict.fromkeys(res2))#remove duplicates
    print(res2)
    return(res2)

#problem 3
def lookupVal(lst,val):
    #code here
    #code to reverse a list, modify later to make useful
    L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
    L2 = []
    while len(L1) != 0:
        L2.append(L1.pop())
    for ent in L2:          
        if val in ent.keys():
            return ent[val]
        else:
            pass
    #print(L2)

def lookupVal2(lst,val):
    print("teststatement")

#problem 4

#problem 5
def numberOfPaths(m, n):
   # If either given row number is first
   # or given column number is first
   if(m == 1 or n == 1):
        return 1
   
   # If diagonal movements are allowed
   # then the last addition
   # is required.
   return  numberOfPaths(m-1, n) + numberOfPaths(m, n-1)
 
#problem 6

#problem 7

def main():
    add_dict_test = {'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2,'360':3}, 'Thu':{'355':3,'451':2,'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1,'451':3,'360':1}}
    result = addDict(add_dict_test)
    print("addDict Result = " + str(result))
    testaddDict(result)

    addDictN_testval = [{'Mon':{'355':2,'360':2},'Tue':{'451':2,'360':3},'Thu':{'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1}}, {'Tue':{'360':2},'Wed':{'355':2},'Fri':{'360':3, '355':1}}, {'Mon':{'360':5},'Wed':{'451':4},'Thu':{'355':3},'Fri':{'360':6}, 'Sun':{'355':5}}]
    result = addDictN(addDictN_testval)
    print("addDictN Result = " + str(result))
    testaddDictN(result)

    tes1 = charCount("Cpts355 --- Assign1")
    tes2 = charCount2("Cpts355 --- Assign1")
    print(tes1 == tes2)

    val = lookupVal([{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}],"y")
    print(val)

    print(numberOfPaths(3,3))


if __name__ == "__main__":
    main()