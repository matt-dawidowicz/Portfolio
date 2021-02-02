#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #used to put the data into tables, but you can use an alternative package
import pickle #used to serialize the dictionaries and load it in the graphing script
import math #used to find null points and skip over them


# In[2]:


xls = pd.ExcelFile("SFMdata.xlsx") #loads the file from Excel
xls1 = xls.parse(0) #
xls2 = xls.parse(1)
xls3 = xls.parse(2)
xls1["Organization:ID"] = xls1.index
xls2["ID"] = xls2.index
xls1 = xls1.drop(['Unnamed: 66', 'Unnamed: 67', 'Unnamed: 68', 'Unnamed: 69', 'Unnamed: 70', 'Unnamed: 71', 'Unnamed: 72', 'Unnamed: 73', 'Unnamed: 74', 'Unnamed: 75'], 1)
xls2 = xls2.drop(['Unnamed: 35', 'Unnamed: 36'], 1)


# In[8]:


get_ipython().run_line_magic('reload_ext', 'line_profiler')
def all_indices(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices

#The above function finds all the indices of the table that match to create the dictionary; originally used a nested for loop,
#but it was extremely inefficient, with an exponentially increasing runtime


def relationship (typ, inp1, inp2):
    dictionary = {} #start with empty dictionary
    num = int(typ)
    column = int(inp1) #index of the column to be the dictionary entry
    column2 = int(inp2) #index of the column that will fill the list in each dictionary entry
    if num == 1:
        asd = xls1 #picks table of organizations
    elif num == 2:
        asd = xls2 #picks table of people
    elif num == 3:
        asd = xls3 #picks table of events
    else:
        return ("First number is invalid.") #error message if input incorrect
    a = asd.iloc[:,column].tolist() #the above function only works with lists, not pandas series
    b = asd.iloc[:,column2].tolist()
    for i in range(len(a)): #goes through every entry in the column
        ert = list() #start with a blank list
        part1 = a[i] #start with the one you want to match
        if type(part1) == float:
                    if math.isnan(part1): #if null, skip it and go back to the beginning of the loop
                        continue
        relev = all_indices(part1,a) #finds the indices where Part 1 matches with other rows
        for r in relev: #list of all the matching indices with the second column
            if type(b[r]) == float:
                if math.isnan(b[r]): #if null, skip and go back to the rest of the indices
                    continue
                else:
                    ert.append(b[r]) #add it to the list
            if type(b[r]) != float and pd.isnull(b[r]):
                continue
            else:
                ert.append(b[r])
        dictionary[part1] = ert #add the complete list to the dictionary entry
    return dictionary #after all the loops, the completed dictionary is returned

get_ipython().run_line_magic('lprun', '-f all_indices')


# In[4]:


result = relationship(1,1,56)
f = open("dicts", "wb")
pickle.dump(result, f)
f.close()
resultfirstdate = relationship(1,1,62)
f = open("dictsfirstdate", "wb")
pickle.dump(resultfirstdate, f)
f.close()
resultlastdate = relationship(1,1,62)
f = open("dictslastdate", "wb")
pickle.dump(resultlastdate, f)
f.close()
resultpeople1 = relationship(2,8,1)
f = open("dictspeople1", "wb")
pickle.dump(resultpeople1, f)
f.close()
resultpeople2 = relationship(2,1,8)
f = open("dictspeople2", "wb")
pickle.dump(resultpeople2, f)
f.close()
resultpeople3 = relationship(2,1,11)
f = open("dictspeople3", "wb")
pickle.dump(resultpeople3, f)
f.close()
resultlocation = relationship(1,1,44)
f = open("dictslocation", "wb")
pickle.dump(resultlocation, f)
f.close()
resultrank = relationship(1,1,44)
f = open("dictslocation", "wb")
pickle.dump(resultlocation, f)
f.close()
resultorg = relationship(1,56,1)
f = open("dictsorg", "wb")
pickle.dump(resultorg, f)
f.close()
resultclass = relationship(1,1,7)
f = open("dictsclass", "wb")
pickle.dump(resultclass, f)
f.close()
#Various relationships found between

