#garrett rudisill
#HW3 CptS 355

#problem 1 - dictionaries

#add dict should get the total hours studied per class
def addDict(dict):
    keylist = dict.keys()#get all the keys from input dictionary
    #these keys are the days of the week
    #for keys in keylist:
    #   print("DoW Key: "+ keys)
    #for keys in keylist:
    #    print("Day: " + str(keys) +"; Day Contents: " + str(dict[keys]))
    studied = {}
    for keys in keylist:#loop accesses each value within a day
        daykey = dict[keys].keys()
        for subkeys in daykey:
            day = dict[keys]
            val = day[subkeys]
            if subkeys not in studied:
                studied.update({subkeys:val})
                #print("key not in")
            else:
                #print("key in")
                studied[subkeys] += val
            #print(str(day)+str(val))
        #print(daykey)
    #print(studied)
    #sums[c] = sums.get(c,0)+val
    #for k, v in dict.items():print (k,v)
    return studied

#function to test output of the result
def testaddDict(result):
        if result == {'355': 8, '451': 8, '360': 9}:
            print("test pass")
        else:
            print("test fail")


def main():
    testdict = {'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2,'360':3}, 'Thu':{'355':3,'451':2,'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1,'451':3,'360':1}}
    result = addDict(testdict)
    print("addDict Result = " + str(result))
    testaddDict(result)

if __name__ == "__main__":
    main()