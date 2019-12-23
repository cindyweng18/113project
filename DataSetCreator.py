#!/usr/bin/env python
# coding: utf-8

# In[1]:


def variant(arr,sentryPos):
    changed = 0
    new_H = arr.copy();
    for i in range(len(new_H)):
        if(changed == 0 and int(new_H[i]) == 1 and i>sentryPos):
            new_H[i] = 0
            changed = changed+1
    return new_H


# In[2]:


def printList(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (j+1)%3 != 0:
                print(arr[i][j],end = " ")
            else:
                print(arr[i][j],end = " ")
                print()
        print("-----")


# In[3]:


def variant_list(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                test = variant(arr[i],j)
                arr.append(test)
    return arr


# In[4]:


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


# In[5]:


def addVariants(arr):
    remove_duplicates(arr)
    arr = variant_list(arr)
    remove_duplicates(arr)
    return arr


# In[6]:


goodH = [[1,0,1,1,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,1,1,1,0,1],[1,0,1,1,1,1,1,1,1,1,0,1],[1,0,0,1,1,1,1,0,1,1,0,1],[1,0,0,1,0,0,1,1,1,1,0,1],[1,0,0,1,1,1,1,1,1,1,0,1]]


# In[7]:


listOfH = goodH.copy()


# In[8]:


while len(listOfH)<300:
    listOfH = addVariants(listOfH)


# In[9]:


goodL = [[1,0,0,1,0,0,1,0,0,1,1,1],[1,0,0,1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0,1,1,1],[1,0,0,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,0,1,0,1,1,1,1],[0,1,0,0,1,0,0,1,1,1,1,1],[0,0,1,0,0,1,0,0,1,0,0,1],[0,1,1,0,0,1,0,0,1,0,0,1],[1,0,0,1,0,0,1,1,1,1,1,1],[0,1,0,0,1,0,1,1,0,1,1,0],[0,1,0,0,1,0,1,1,1,1,1,1],[0,0,0,0,0,0,1,0,0,1,1,1],[0,1,1,0,1,1,0,1,1,0,1,1]]


# In[10]:


listOfL = goodL.copy()


# In[11]:


while len(listOfL)<300:
    listOfL = addVariants(listOfL)


# In[12]:


trainingSet = []
testingSet = []
for i in range(200):
    trainingSet.append(listOfH[i]) #first 200 in text file will be H the following 200 will be L
for i in range(200):
    trainingSet.append(listOfL[i])
for i in range(201,301): 
    testingSet.append(listOfH[i])
for i in range(201,301):
    testingSet.append(listOfL[i])    


# In[13]:


with open("data_set.txt","a+") as dataSet:
    for i in range(len(trainingSet)):
        for j in range(len(trainingSet[i])):
            dataSet.write(str(trainingSet[i][j]))
        dataSet.write("\n")
    for i in range(len(testingSet)):
        for j in range(len(testingSet[i])):
            dataSet.write(str(trainingSet[i][j]))
        dataSet.write("\n")
    dataSet.close


# In[15]:


with open("data_set.txt","r") as dataSet:
    print(dataSet.read())
    dataSet.close()

