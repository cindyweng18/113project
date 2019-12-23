#!/usr/bin/env python
# coding: utf-8

# In[1]:


def h_variant(arr,sentryPos):
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


def h_variant_list(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                test = h_variant(arr[i],j)
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
                j-= 1
            else:
                j += 1
        i += 1


# In[6]:


def listAddBack(arr,arr2):
    for i in range(len(arr)):
        arr2.append(arr[i])


# In[7]:


def addVariants(arr):
    remove_duplicates(arr)
    arr = h_variant_list(arr)
    remove_duplicates(arr)
    return arr


# In[8]:


listOfH = []
goodH = [[1,0,1,1,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,1,1,1,0,1],[1,0,1,1,1,1,1,1,1,1,0,1],[1,0,0,1,1,1,1,0,1,1,0,1],[1,0,0,1,0,0,1,1,1,1,0,1],[1,0,0,1,1,1,1,1,1,1,0,1]]


# In[9]:


listOfH = goodH.copy()


# In[12]:


listOfH = addVariants(listOfH)
listOfH = addVariants(listOfH)
listOfH = addVariants(listOfH)


# In[13]:


len(listOfH)


# In[15]:


remove_duplicates(listOfH)
len(listOfH)


# In[16]:


printList(listOfH)


# In[ ]:


#remove_duplicates(listOfH)
#len(listOfH)


# In[ ]:


#remove_duplicates(listOfH)
#var2 = listOfH.copy()


# In[ ]:


#for i in range(len(var1)):
#   listOfH.remove(var1[i])


# In[ ]:




