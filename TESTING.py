#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Names:
#Sajid Mahmud
#Mumtahid Akash
#Michal Moryosef
#Zarif Choudhury
#Hope
#Cindy

import random
import numpy as np

random.seed(84)

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

def create_s(small_tuple, original_list):
    S = []
    for i in small_tuple:
        S.append(original_list[i-1])
    return S

def bin_2_num(a):
    b =((int(a[0]))*4) + ((int(a[1]))*2) + ((int(a[2]))*1)
    return b

def match_found(Si, Ti): # this is incrementing those 7 boxes in machine learning part
    decimal_num = bin_2_num(Si)
    Ti[decimal_num] += 1

def add_sumH(Si, THs):
    sum = 0;
    decnumH = bin_2_num(Si)
    sum += THs[decnumH]
    return sum

def add_sumL(Si, TLs):
    sum = 0;
    decnumL = bin_2_num(Si)
    sum += TLs[decnumL]
    return sum

def predict_class(total_sumH,total_sumL):
    predicted_class = ""
    if total_sumH >= total_sumL:
        predicted_class = "H"
    elif total_sumH <= total_sumL:
        predicted_class = "L"
    else:
        predicted_class = "H"
    return predicted_class
    
def correct_class(actual_letter,predicted_letter):
    if actual_letter == predicted_letter:
        return "True"
    elif actual_letter != predicted_letter:
        return "False"

# Dataset creation # 
goodH = [[1,0,1,1,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,1,1,1,0,1],[1,0,1,1,1,1,1,1,1,1,0,1],[1,0,0,1,1,1,1,0,1,1,0,1],[1,0,0,1,0,0,1,1,1,1,0,1],[1,0,0,1,1,1,1,1,1,1,0,1]]

listOfH = goodH.copy()

while len(listOfH)<300:
    listOfH = addVariants(listOfH)

#goodL = [[1,0,0,1,0,0,1,0,0,1,1,1],[1,0,0,1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0,1,1,1],[1,0,0,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,0,1,0,1,1,1,1],[0,1,0,0,1,0,0,1,1,1,1,1],[0,0,1,0,0,1,0,0,1,0,0,1],[0,1,1,0,0,1,0,0,1,0,0,1],[1,0,0,1,0,0,1,1,1,1,1,1],[0,1,0,0,1,0,1,1,0,1,1,0],[0,1,0,0,1,0,1,1,1,1,1,1],[0,0,0,0,0,0,1,0,0,1,1,1],[0,1,1,0,1,1,0,1,1,0,1,1]]

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

#with open("data_set.txt","r") as dataSet:
#    print(dataSet.read())
#    dataSet.close()


# Create testing set #
my_file = open ("data_set.txt", "r")
newShuffledArrayTesting = []
newShuffledArrayTraining = []
i = 0
while True:
    if i < 400:
        a = my_file.readline()
        a = a.replace("\r", "").replace("\n", "")
        if a ==  "":
            break
        newShuffledArrayTraining.append(a)
        i += 1
    else:
        a = my_file.readline()
        a = a.replace("\r", "").replace("\n", "")
        if a ==  "":
            break
        newShuffledArrayTesting.append(a)
my_file.close()


# In[2]:


#print (newArray)
newShuffledArrayTesting = random.sample (newShuffledArrayTesting, len(newShuffledArrayTesting))
newShuffledArrayTraining = random.sample(newShuffledArrayTraining, len(newShuffledArrayTraining))
#print (newShuffledArray)

# Training Section #
J = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
random.shuffle(J)
J1 = tuple(J[0:3])
J2 = tuple(J[3:6])
J3 = tuple(J[6:9])
J4 = tuple(J[9:12])
#print(J1, J2, J3, J4)
# TH's
array_H_1 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_2 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_3 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_4 = [0,  0,  0,  0,  0,  0,  0,  0]
allTs = [array_H_1, array_H_2, array_H_3, array_H_4]

trainingofH=[]
for i in range (200):
    trainingofH.append(newShuffledArrayTraining[i])
    
trainingofL=[]
for i in range (200):
    trainingofL.append(newShuffledArrayTraining[i])
    
# S sets
for i in trainingofH:

    S1 = create_s(J1, i) 
    S2 = create_s(J2, i)
    S3 = create_s(J3, i)
    S4 = create_s(J4, i)
    #print(S1, S2, S3, S4)
    allSs = [S1, S2, S3, S4]           

    match_found (allSs[0], allTs[0])
    match_found (allSs[1], allTs[1])
    match_found (allSs[2], allTs[2])
    match_found (allSs[3], allTs[3])  
    
for i in range (len(allTs)):
    print("\t", " this is for H ", allTs[i], "\t")
# TLs
array_L_1 = [0,  0,  0,  0,  0,  0,  0,  0]
array_L_2 = [0,  0,  0,  0,  0,  0,  0,  0]
array_L_3 = [0,  0,  0,  0,  0,  0,  0,  0]
array_L_4 = [0,  0,  0,  0,  0,  0,  0,  0]
allLs = [array_L_1, array_L_2, array_L_3, array_L_4]


for i in trainingofL:  

    S1 = create_s(J1, i) 
    S2 = create_s(J2, i)
    S3 = create_s(J3, i)
    S4 = create_s(J4, i)
    #print(S1, S2, S3, S4)
    allSs = [S1, S2, S3, S4]                                                                                                       
    match_found (allSs[0], allLs[0])
    match_found (allSs[1], allLs[1])
    match_found (allSs[2], allLs[2])
    match_found (allSs[3], allLs[3])
        
for i in range (len(allLs)): 
    print("\t", " this is for L ", allLs[i], "\t")

# Testing Section #
j = 0
x = []
for i in newShuffledArrayTesting:
    S1 = create_s(J1, i)
    S2 = create_s(J2, i)
    S3 = create_s(J3, i)
    S4 = create_s(J4, i)
    #print(S1, S2, S3, S4)
    allSt = [S1, S2, S3, S4]

    total_sumH = 0;
    sumH1 = add_sumH(allSt[0], allTs[0])
    sumH2 = add_sumH(allSt[1], allTs[1])
    sumH3 = add_sumH(allSt[2], allTs[2])
    sumH4 = add_sumH(allSt[3], allTs[3])
    total_sumH = sumH1 + sumH2 + sumH3 + sumH4

    total_sumL = 0;
    sumL1 = add_sumL(allSt[0], allLs[0])
    sumL2 = add_sumL(allSt[1], allLs[1])
    sumL3 = add_sumL(allSt[2], allLs[2])
    sumL4 = add_sumL(allSt[3], allLs[3])
    total_sumL = sumL1 + sumL2 + sumL3 + sumL4
    
#    print(total_sumH, total_sumL)
    predicted_letter = predict_class(total_sumH, total_sumL)
    actual_letter = newShuffledArrayTesting[j][13]
    b = correct_class(actual_letter, predicted_letter)
    print(newShuffledArrayTesting[j][0:12], "Predicted Class:", predicted_letter, "Actual Class:", actual_letter,b)
    j += 1
    # Accuracy 
    if b == "True":
        x.append(1)
    elif b == "False":
        x.append(0)
average = np.mean(x)
print(average*100, "% accuracy")


# In[ ]:




