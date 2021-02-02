#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import graphviz as vg
import random
import time
import datetime
import pickle
import sys
#!pip install git+git://github.com/pygraphviz/pygraphviz.git
print(sys.version)


# In[77]:


def load(file_name):
    f =  open(file_name,'rb')
    b = pickle.load(f)
    return b
result = load("dicts")
resultdate = load("dictsdate1")
#resultdate2 = load("dictsdate2")
resultpeople1 = load("dictspeople1")
resultpeople2 = load("dictspeople2")
resultrank = load("dictspeople3")
resultlocation = load("dictslocation")
resultorg = load("dictsorg")
resultclass = load("dictsclass")

keysorg1 = list(result.keys())
keysorg2 = list(resultorg.keys())
keyspeople = list(resultpeople2.keys())
dates1 = resultdate1.values()
#dates2 = resltdate2.values()
ranks = list(resultrank.values())
locations = resultlocation.keys()

keyspeople

for i in range(len(resultpeople2)):
    resultpeople2[keyspeople[i]] = list(set(resultpeople2[keyspeople[i]]))
for i in range(len(resultrank)):
    resultrank[keyspeople[i]] = list(set(resultrank[keyspeople[i]]))
for i in range(len(resultorg)):
    resultorg[keysorg2[i]] = list(set(resultorg[keysorg2[i]]))
for i in range(len(resultclass)):
    if keysorg1[i] in resultclass.keys():
        resultclass[keysorg1[i]] = list(set(resultclass[keysorg1[i]]))
resultclass


# In[44]:


dot = vg.Graph()
dot.engine = 'dot'
dot.attr('node', shape='circle', style = "filled", fillcolor = "red", height = "4")
def areagraph1(area):
    alreadyedges = list()
    area = str(area)
    dot.node(area)
    dot.attr('node', shape='oval', style = "filled", fillcolor = "white", height = "0.02")
    if area not in resultpeople1.keys():
        print("This is not a valid entry. Here are valid entries.")
        print(list(set(resultpeople1.keys())))
        return -1
    for j in range(len(resultpeople1[area])):
        person = resultpeople1[area][j]
        rank = resultrank[person][0]
        if len(rank) > 1:
            for r in range(len(resultrank[person])):
                if r != 0:
                    rank = rank + ", " + resultrank[person][r]
                print(rank)
        if (str(person), str(area)) not in alreadyedges:
            alreadyedges.append((str(person), str(area)))
            dot.edge(str(person), str(area), color = "red", taillabel = rank, lblstyle="above, sloped")
        
        if area in keysorg:
            member = result[area]
            if len(member) == 0:
                member = ["No information about memberships."]
        else:
            member = ["No information about memberships."]
        if area in resultdate:
            dt = resultdate[area]
            if len(dt) == 0:
                dt3 = "No Date Given"
            else:
                dt1 = dt[len(dt)-1]
                dt2 = datetime.date(dt1.year, dt1.month, dt1.day)
                dt3 = str(dt2.strftime('%B %d, %Y'))
        else:
            dt3 = "N/A"
        for r in range(len(member)):
            if (str(area), str(member[r])) not in alreadyedges:
                alreadyedges.append((str(area), str(member[r])))
                dot.edge(str(area), str(member[r]), color = "green", headlabel = "Last Confirmed: " + dt3 + ".")
        if area in locations:
            location = resultlocation[area]
            if len(location) == 0:
                location = "No location given in data."
                if (str(area), str(location)) not in alreadyedges:
                    alreadyedges.append((str(area), str(location)))
                    dot.edge(str(area), str(location), color = "blue")
            else:
                location = location[0]
                if (str(area), str(location)) not in alreadyedges:
                    alreadyedges.append((str(area), str(location)))
                    dot.edge(str(area), str(location), color = "blue", headlabel = "Location:")
        else:
                location = "No location given in data."
                if (str(area), str(location)) not in alreadyedges:
                    alreadyedges.append((str(area), str(location)))
                    dot.edge(str(area), str(location), color = "blue")
    return dot
areagraph1("1 Mechanised Division")
dot.render('Graph1.jpg', view=True)


# In[ ]:





# In[43]:


dot = vg.Graph()
dot.engine = 'dot'
dot.attr('node', shape='circle', style = "filled", fillcolor = "red", height = "4")

def areagraph2(person):
    alreadyedges = list()
    person = str(person)
    dot.node(person)
    dot.attr('node', shape='oval', style = "filled", fillcolor = "white", height = "0.02")
    if person not in resultpeople2.keys():
        print("This is not a valid entry. Here are valid entries.")
        print(list(set(resultpeople2.keys())))
        return -1
    for j in range(len(resultpeople2[person])):
        area = resultpeople2[person][j]
        if (str(person), str(area)) not in alreadyedges:
            alreadyedges.append((str(person), str(area)))
            dot.edge(str(person), str(area), color = "red")
        personarea = resultpeople1[area]
        for r in range(len(personarea)):
            personarea1 = personarea[r]
        if (str(personarea1), str(area)) not in alreadyedges and (str(area), str(personarea1)) not in alreadyedges:
            alreadyedges.append((str(personarea1), str(area)))
            dot.edge(str(personarea1), str(area), color = "purple")
        if area in locations:
                location = resultlocation[area]
                if len(location) == 0:
                    location = "No location given in data."
                    if (str(area), str(location)) not in alreadyedges:
                        alreadyedges.append((str(area), str(location)))
                        dot.edge(str(area), str(location), color = "blue")
                    else:
                        location = location[0]
                        if (str(area), str(location)) not in alreadyedges:
                            alreadyedges.append((str(area), str(location)))
                            dot.edge(str(area), str(location), color = "blue", headlabel = "Location:")
                else:
                    location = "No location given in data."
                    if (str(area), str(location)) not in alreadyedges:
                        alreadyedges.append((str(area), str(location)))
                        dot.edge(str(area), str(location), color = "blue")
    return dot
areagraph2("Garba Ayodele Wahab")
dot.render('Graph2.jpg', view=True)


# In[83]:


dot = vg.Graph()
dot.engine = 'dot'
dot.attr('node', shape='circle', style = "filled", fillcolor = "red", height = "4")

def areagraph3(org, color1):
    alreadyedges = list()
    org = str(org)
    dot.node(org)
    dot.attr('node', shape='oval', style = "filled", fillcolor = "white", height = "0.02")
    if org not in resultorg.keys():
        print("This is not a valid entry. Here are valid entries.")
        print(list(set(resultorg.keys())))
        return -1
    for j in range(len(resultorg[org])):
        area = resultorg[org][j]
        if (str(org), str(area)) not in alreadyedges:
            alreadyedges.append((str(org), str(area)))
            dot.edge(str(org), str(area), color = str(color1))
        class1 = resultclass[org]
    return dot

areagraph3("Operation BOYONA", "red")
dot.attr('node', shape='circle', style = "filled", fillcolor = "red", height = "4")
areagraph3("Operation Zaman Lafiya", "blue")
dot.attr('node', shape='circle', style = "filled", fillcolor = "red", height = "4")
areagraph3("Joint Task Force, Operation Restore Order I", "green")
dot.attr('node', shape='circle', style = "filled", fillcolor = "red", height = "4")
areagraph3("Operation Lafiya Dole", "purple")
dot.render('OperationOverlap', view=True)

