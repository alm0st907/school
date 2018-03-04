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
    for keys in keylist:#loop accesses each key within a day
        daykey = dict[keys].keys()
        for subkeys in daykey: #access the values by key within a day
            day = dict[keys]
            val = day[subkeys]
            if subkeys not in studied: #add to the dictionary if it doesnt exist
                studied.update({subkeys:val})
                #print("key not in")
            else: #update the value if the key exists already
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

def addDictN(week_list):
    #print("ignore this")
    #reduce the list down to the seven days of week
    #call addDict on that reduced dictionary
    
    #we can use addDict to get the individual results of a week
    # add the results from each week?

    #w1 = addDict(week_list[0])
    #w2 = addDict(week_list[1])
    #print("Week 1 times: " + str(w1))
    #print("week 2 times :" + str(w2))
    #k1 = w1.keys()
    #k2 = w2.keys()
    #for keys in k1,k2:
    #   print("keys"+str(keys))
    final = {} #dictionary for the results
    #for keys in k1:
    #    final.update({keys:w1[keys]})
    for entry in week_list:
        week_res = addDict(entry)
        temp_keys = week_res.keys()
        #print(week_res)
        #print(temp_keys)
        for key in temp_keys:
            if key not in final:
                final.update({key:week_res[key]})
            else:
                final[key] += week_res[key]
        #for key,value in entry.items():
        #   print(key, value)
    return final

def testaddDictN(result):
    if result == {'355': 16, '360': 24, '451': 6}:
        print("test pass")
    else:
        print("test fail")
        

def main():
    add_dict_test = {'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2,'360':3}, 'Thu':{'355':3,'451':2,'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1,'451':3,'360':1}}
    result = addDict(add_dict_test)
    print("addDict Result = " + str(result))
    testaddDict(result)

    addDictN_testval = [{'Mon':{'355':2,'360':2},'Tue':{'451':2,'360':3},'Thu':{'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1}}, {'Tue':{'360':2},'Wed':{'355':2},'Fri':{'360':3, '355':1}}, {'Mon':{'360':5},'Wed':{'451':4},'Thu':{'355':3},'Fri':{'360':6}, 'Sun':{'355':5}}]
    result = addDictN(addDictN_testval)
    print("addDictN Result = " + str(result))
    testaddDictN(result)

if __name__ == "__main__":
    main()