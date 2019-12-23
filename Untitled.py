#!/usr/bin/env python
# coding: utf-8

# In[1]:


listOfH = []
goodH = [[1,0,1,1,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,1,1,1,0,1],[1,0,1,1,1,1,1,1,1,1,0,1],[1,0,0,1,1,1,1,0,1,1,0,1],[1,0,0,1,0,0,1,1,1,1,0,1],[1,0,0,1,1,1,1,1,1,1,0,1]]


# In[2]:


for i in range(len(goodH)):
    for j in range(len(goodH[i])):
        if (j+1)%3 != 0:
            print(goodH[i][j],end = " ")
        else:
            print(goodH[i][j],end = " ")
            print()
    print("-----")


# In[3]:


def h_variant(arr,sentryPos):
    changed = 0
    new_H = arr.copy();
    for i in range(len(new_H)):
        if(changed == 0 and int(new_H[i]) == 1 and i>sentryPos):
            new_H[i] = 0
            changed = changed+1
    return new_H


# In[5]:


testList = []
for i in range(len(goodH)):
    for j in range(len(goodH[i])):
        if goodH[i][j] == 1:
            test = h_variant(goodH[i],j)
            listOfH.append(test)


# In[8]:


for i in range(len(listOfH)):
    for j in range(len(listOfH[i])):
        if (j+1)%3 != 0:
            print(listOfH[i][j],end = " ")
        else:
            print(listOfH[i][j],end = " ")
            print()
    print("-----")


# In[7]:


len(listOfH)




# Takes a list parameter and returns a list without any duplicates
def remove_duplicates (userList):
    userListLength = int (len (userList))
    i = 0
    i = int (i)
    while i < userListLength:
        j = 0
        j = int (j)
        while j < userListLength:
            if userList[i] == userList[j] and i != j:
                userList [i] = userList [userListLength - 1]
                userList.pop()
                userListLength -= 1
                i-= 1
            else:
                j += 1
        i += 1
    return userList
