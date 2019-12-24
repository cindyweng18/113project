# In[1]:


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

#def printList(arr):
#    for i in range(len(arr)):
#        for j in range(len(arr[i])):
#            if (j+1)%3 != 0:
#                print(arr[i][j],end = " ")
#            else:
#                print(arr[i][j],end = " ")
#                print()
#        print("-----")

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
    if total_sumH > total_sumL:
        predicted_class = "H"
    elif total_sumH < total_sumL:
        predicted_class = "L"
    else:
        predicted_class = "H"
    return predicted_class
    
def correct_class(actual_letter,predicted_letter):
    if actual_letter == predicted_letter:
        return "True"
    elif actual_letter != predicted_letter:
        return "False"

def pred_H_wrong(Si, TLs, n, d = 0.5):
  sum = 0
  decnum = bin_2_num(Si)
  sum = sum + TLs[decnum] - (d*n)
  return sum

def pred_L_wrong(Si, THs, n, d = 0.5):
  sum = 0
  decnum = bin_2_num(Si)
  sum = sum + THs[decnum] - (d*n)
  return sum


    
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

with open("training_set.txt","w") as ds:
    for i in range(len(trainingSet)):
        for j in range(len(trainingSet[i])):
            ds.write(str(trainingSet[i][j]))
        if i < 200:
            ds.write(" H\n")
        else:
            ds.write(" L\n")
    ds.close()

with open("testing_set.txt","w") as dst:
    for i in range(len(testingSet)):
        for j in range(len(testingSet[i])):
            dst.write(str(testingSet[i][j]))
        if i < 100:
            dst.write(" H\n")
        else:
            dst.write(" L\n")
    dst.close()


# In[2]:


my_file = open ("training_set.txt", "r")
newShuffledArray = []
while True:
    a = my_file.readline()
    a = a.replace("\r", "").replace("\n", "")
    if a ==  "":
        break
    newShuffledArray.append(a)
my_file.close()
#print (newArray)
newShuffledArray = random.sample (newShuffledArray, len(newShuffledArray))
#print (newShuffledArray)

    
J = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
random.shuffle(J)
J1 = tuple(J[0:3])
J2 = tuple(J[3:6])
J3 = tuple(J[6:9])
J4 = tuple(J[9:12])
#print(J1, J2, J3, J4)

array_H_1 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_2 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_3 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_4 = [0,  0,  0,  0,  0,  0,  0,  0]
allTs = [array_H_1, array_H_2, array_H_3, array_H_4]

# Trainings sets for Letter H

#for just testing the incrementing value

trainingofH=[]
for i in range (200):
    trainingofH.append(listOfH[i])
    
trainingofL=[]
for i in range (200):
    trainingofL.append(listOfL[i])
    
for i in trainingofH:  # should run through 200 training sets of H

    S1 = create_s(J1, i) # Correct me: this sends to the function the actual H array from the data set
    S1 = create_s(J1, i) # Fix me: this sends to the function the actual H array from the data set
    S2 = create_s(J2, i)
    S3 = create_s(J3, i)
    S4 = create_s(J4, i)
    #print(S1, S2, S3, S4)
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
    #print(S1, S2, S3, S4)
    allSs = [S1, S2, S3, S4]

                                                                                                                     
    match_found (allSs[0], allLs[0])
    match_found (allSs[1], allLs[1])
    match_found (allSs[2], allLs[2])
    match_found (allSs[3], allLs[3])
        
for i in range (len(allLs)): # prints all of L's after the incrementation
    print("\t", " this is for L ", allLs[i], "\t")

j = 0
x = []
printTimes = 0
for i in newShuffledArray:
    S1 = create_s(J1, i)
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
    actual_letter = newShuffledArray[j][13]
    b = correct_class(actual_letter, predicted_letter)
    print(newShuffledArray[j][0:12], "Actual Class:", actual_letter, "Predicted Class:", predicted_letter, b)
    j += 1
    if b == "True":
        x.append(1)
        printTimes +=1
    elif b == "False":
        x.append(0)
        printTimes +=1
average = np.mean(x)
print(average)
print(printTimes)


# In[ ]:


print("=================================================================================================================================Testing Set Below===============================================================================================================================================")


# In[3]:


# this is for creating a temporary merged array and a shuffled array for the testing set
my_file = open ("testing_set.txt", "r")
newShuffledArray = []
while True:
    a = my_file.readline()
    a = a.replace("\r", "").replace("\n", "")
    if a ==  "":
        break
    newShuffledArray.append(a)
my_file.close()
#print (newArray)
newShuffledArray = random.sample (newShuffledArray, len(newShuffledArray))
#print (newShuffledArray)

J = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
random.shuffle(J)
J1 = tuple(J[0:3])
J2 = tuple(J[3:6])
J3 = tuple(J[6:9])
J4 = tuple(J[9:12])
#print(J1, J2, J3, J4)

array_H_1 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_2 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_3 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_4 = [0,  0,  0,  0,  0,  0,  0,  0]
allTs = [array_H_1, array_H_2, array_H_3, array_H_4]

# Trainings sets for Letter H

#for just testing the incrementing value

trainingofH=[]
for i in range (200):
    trainingofH.append(listOfH[i])
    
trainingofL=[]
for i in range (200):
    trainingofL.append(listOfL[i])
    
for i in trainingofH:  # should run through 200 training sets of H

    S1 = create_s(J1, i) # Correct me: this sends to the function the actual H array from the data set
    S1 = create_s(J1, i) # Fix me: this sends to the function the actual H array from the data set
    S2 = create_s(J2, i)
    S3 = create_s(J3, i)
    S4 = create_s(J4, i)
    #print(S1, S2, S3, S4)
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
    #print(S1, S2, S3, S4)
    allSs = [S1, S2, S3, S4]

                                                                                                                     
    match_found (allSs[0], allLs[0])
    match_found (allSs[1], allLs[1])
    match_found (allSs[2], allLs[2])
    match_found (allSs[3], allLs[3])
        
for i in range (len(allLs)): # prints all of L's after the incrementation
    print("\t", " this is for L ", allLs[i], "\t")

j = 0
x = []
printTimes = 0
for i in newShuffledArray:
    S1 = create_s(J1, i)
    S1 = create_s(J1, i)
    S2 = create_s(J2, i)
    S3 = create_s(J3, i)
    S4 = create_s(J4, i)
    print(S1, S2, S3, S4)
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
    
    print(total_sumH, total_sumL)
    predicted_letter = predict_class(total_sumH, total_sumL)
    actual_letter = newShuffledArray[j][13]
    b = correct_class(actual_letter, predicted_letter)
    if predicted_letter == "H":
      while b == "False":
        n = 1
        sumWH1 = pred_H_wrong(allSt[0], allLs[0], n)
        sumWH2 = pred_H_wrong(allSt[1], allLs[1], n)
        sumWH3 = pred_H_wrong(allSt[2], allLs[2], n)
        sumWH4 = pred_H_wrong(allSt[3], allLs[3], n)
        total_sumWH = sumWH1 + sumWH2 + sumWH3 + sumWH4
        print(total_sumWH, total_sumL)
        predicted_letter = predict_class(total_sumWH, total_sumL)
        b = correct_class(actual_letter, predicted_letter)
        n += 1
    elif predicted_letter == "L":
      if b == False:
        n = 1
        sumWL1 = pred_L_wrong(allSt[0], allTs[0], n)
        sumWL2 = pred_L_wrong(allSt[1], allTs[1], n)
        sumWL3 = pred_L_wrong(allSt[2], allTs[2], n)
        sumWL4 = pred_L_wrong(allSt[3], allTs[3], n)
        total_sumL = sumWL1 + sumWL2 + sumWL3 + sumWL4
        predicted_letter = predict_class(total_sumL, total_sumH)
        b = correct_class(actual_letter, predicted_letter)
        n += 1
    print(newShuffledArray[j][0:12], "Actual Class:", actual_letter, "Predicted Class:", predicted_letter, b)
    j += 1
    if b == "True":
        x.append(1)
    elif b == "False":
        x.append(0)
average = np.mean(x)
print(average*100, "% accuracy", sep = "")
