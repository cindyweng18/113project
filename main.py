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
        if i < 200:
            dataSet.write(" H\n")
        else:
            dataSet.write(" L\n")
    for i in range(len(testingSet)):
        for j in range(len(testingSet[i])):
            dataSet.write(str(trainingSet[i][j]))
        if i < 100:
            dataSet.write(" H\n")
        else:
            dataSet.write(" L\n")
    dataSet.close


# In[14]:


with open("data_set.txt","r") as dataSet:
    print(dataSet.read())
    dataSet.close()


# In[15]:


len(trainingSet)


# In[17]:


len(testingSet)


# In[ ]:

import random
# Michal and Akash Code

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
    
J = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
random.shuffle(J)
J1 = tuple(J[0:3])
J2 = tuple(J[3:6])
J3 = tuple(J[6:9])
J4 = tuple(J[9:12])
print(J1, J2, J3, J4)

array_H_1 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_2 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_3 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_4 = [0,  0,  0,  0,  0,  0,  0,  0]
allTs = [array_H_1, array_H_2, array_H_3, array_H_4]

# Trainings sets for Letter H

#for just testing the incrementing value

trainingofH=[]
for i in range (200):
    fiveofH.append(listOfH[i])
    
trainingofL=[]    
for i in range (200):
    trainingofL.append(listOfL[i])
    
for i in trainingofH:  # should run through 200 training sets of H

    S1 = create_s(J1, i) # Correct me: this sends to the function the actual H array from the data set
    S1 = create_s(J1, i) # Fix me: this sends to the function the actual H array from the data set
    S2 = create_s(J2, i)
    S3 = create_s(J3, i)
    S4 = create_s(J4, i)
    print(S1, S2, S3, S4)
    allSs = [S1, S2, S3, S4]
                                                                                                                    
    match_found (allSs[0], allTs[0])                                                                                                                    
    match_found (allSs[1], allTs[1])                                                                                                                    
    match_found (allSs[2], allTs[2])                                                                                                                    
    match_found (allSs[3], allTs[3])
   
for i in range (len(allTs)): # prints all of T's after the incrementation
    print("\t", " this is for H ", allTs[i], "\t")

array_L_1 = [0,  0,  0,  0,  0,  0,  0,  0]
array_L_2 = [0,  0,  0,  0,  0,  0,  0,  0]
array_L_3 = [0,  0,  0,  0,  0,  0,  0,  0]
array_L_4 = [0,  0,  0,  0,  0,  0,  0,  0]
allLs = [array_L_1, array_L_2, array_L_3, array_L_4]
# Trainings sets for Letter L


for i in trainingofL:  # should run through 200 training sets of L


    S1 = create_s(J1, i) # Fix me: this sends to the function the actual L array from the data set
    S2 = create_s(J2, i)
    S3 = create_s(J3, i)
    S4 = create_s(J4, i)
    print(S1, S2, S3, S4)
    allSs = [S1, S2, S3, S4]

                                                                                                                     
    match_found (allSs[0], allLs[0])                                                                                                                    
    match_found (allSs[1], allLs[1])                                                                                                                    
    match_found (allSs[2], allLs[2])                                                                                                                    
    match_found (allSs[3], allLs[3])
        
for i in range (len(allLs)): # prints all of L's after the incrementation
    print("\t", " this is for L ", allLs[i], "\t")

