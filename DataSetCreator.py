#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np

random.seed(84)
#functions for data set creation
def variant(arr,sentryPos):
    changed = 0
    new_H = arr.copy();
    for i in range(len(new_H)):
        if(changed == 0 and int(new_H[i]) == 1 and i>sentryPos):
            new_H[i] = 0
            changed = changed+1
    return new_H

def variant_list(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                test = variant(arr[i],j)
                arr.append(test)
    return arr

def remove_duplicates (userList):
    i = 0
    while i < len(userList):
        j = 1
        while j < len(userList):
            if userList[i] == userList[j] and i != j:
                userList [j] = userList [len(userList) - 1]
                userList.pop()
                j -= 1
            else:
                j += 1
        i += 1

def addVariants(arr):
    remove_duplicates(arr)
    arr = variant_list(arr)
    remove_duplicates(arr)
    return arr
# Dataset creation # 
goodH = [[1,0,1,1,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,1,1,1,0,1],[1,0,1,1,1,1,1,1,1,1,0,1],[1,0,0,1,1,1,1,0,1,1,0,1],[1,0,0,1,0,0,1,1,1,1,0,1],[1,0,0,1,1,1,1,1,1,1,0,1]]

listOfH = goodH.copy()

while len(listOfH)<300:
    listOfH = addVariants(listOfH)

goodL = [[1,0,0,1,0,0,1,0,0,1,1,1],[1,0,0,1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0,1,1,1],[1,0,0,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,0,1,0,1,1,1,1],[0,1,0,0,1,0,0,1,1,1,1,1],[1,0,0,1,0,0,1,1,1,1,1,1],[0,1,0,0,1,0,1,1,0,1,1,0],[0,1,0,0,1,0,1,1,1,1,1,1],[0,1,1,0,1,1,0,1,1,0,1,1]]

listOfL = goodL.copy()

while len(listOfL)<300:
    listOfL = addVariants(listOfL)

trainingSet = []
testingSet = []
for i in range(200):
    trainingSet.append(listOfH[i]) #first 200 in text file will be H the following 200 will be L
for i in range(101,301):
    trainingSet.append(listOfL[i])
for i in range(201,301):
    testingSet.append(listOfH[i])
for i in range(100):
    testingSet.append(listOfL[i])

with open("data_set.txt","w") as dataSet:
    for i in range(len(trainingSet)):
        for j in range(len(trainingSet[i])):
            dataSet.write(str(trainingSet[i][j]))
        if i < 200:
            dataSet.write(" H\n")
        else:
            dataSet.write(" L\n")
    for i in range(len(testingSet)):
        for j in range(len(testingSet[i])):
            dataSet.write(str(testingSet[i][j]))
        if i < 100:
            dataSet.write(" H\n")
        else:
            dataSet.write(" L\n")
    dataSet.close

