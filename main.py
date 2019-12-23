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
array_H_1 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_2 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_3 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_4 = [0,  0,  0,  0,  0,  0,  0,  0]
allTs = [array_H_1, array_H_2, array_H_3, array_H_4]

# Trainings sets for Letter H
# I need to know how to pull the arrays you guys created from the data set.
# I guess you could help me link them to the code?
for i in 200:  # Fix me: this should run through 200 training sets of H
    random.shuffle(J)
    J1 = tuple(J[0:3])
    J2 = tuple(J[3:6])
    J3 = tuple(J[6:9])
    J4 = tuple(J[9:12])
    print(J1, J2, J3, J4)
    S1 = create_s(J1, i) # Fix me: this sends to the function the actual H array from the data set
    S2 = create_s(J2, i)
    S3 = create_s(J3, i)
    S4 = create_s(J4, i)
    print(S1, S2, S3, S4)
    allSs = [S1, S2, S3, S4]
    for j in allTs: # loop incrementing all T_H arrays
        for i in allSs: # loop running through all S tuples
            match_found (allSs[i], allTs[j])
    for i in range (len(allTs)): # prints all of T's after the incrementation
        print("\t", " ", allTs[i], "\t")

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
array_L_1 = [0,  0,  0,  0,  0,  0,  0,  0]
array_L_2 = [0,  0,  0,  0,  0,  0,  0,  0]
array_L_3 = [0,  0,  0,  0,  0,  0,  0,  0]
array_L_4 = [0,  0,  0,  0,  0,  0,  0,  0]
allLs = [array_L_1, array_L_2, array_L_3, array_L_4]
# Trainings sets for Letter L
# same thing here guys,
# I need to know how to pull the arrays you created from the data set.
# I guess you could help me link them to the code?
for i in 200:  # fix me: this should run through 200 training sets of L
    random.shuffle(J)
    L1 = tuple(L[0:3])
    L2 = tuple(L[3:6])
    L3 = tuple(L[6:9])
    L4 = tuple(L[9:12])
    print(L1, L2, L3, L4)
    S1 = create_s(L1, i) # Fix me: this sends to the function the actual L array from the data set
    S2 = create_s(L2, i)
    S3 = create_s(L3, i)
    S4 = create_s(L4, i)
    print(S1, S2, S3, S4)
    allSs = [S1, S2, S3, S4]
for j in allLs: # loop incrementing all T_L arrays
    for i in allSs: # loop running through all S tuples
        match_found (allSs[i], allLs[j])
    for i in range (len(allLs)): # prints all of T's after the incrementation
        print("\t", " ", allLs[i], "\t")

# Testing 100 sets of H

# Summing up all 4 H arrays created with the corresponding indexes for comparison
H_sum = [0,  0,  0,  0,  0,  0,  0,  0]
for j in H_sum:
    for i in allTs: #allTs = [array_H_1, array_H_2, array_H_3, array_H_4]
        for k in allTs[i]:
            H_sum[j] += allTs[k]
# at this point all 4 H arrays are updated in one Sum_H array with their corresponding indexes.

# # Summing up all 4 L arrays created with the corresponding indexes for comparison
L_sum = [0,  0,  0,  0,  0,  0,  0,  0]
for j in L_sum:
    for i in allLs: #allLs = [array_L_1, array_L_2, array_L_3, array_L_4]
        for k in allLs[i]:
            H_sum[j] += allLs[k]

# at this point all 4 L arrays are updated in one Sum_H array with their corresponding indexes.

# now, we break each testing array to Js and Ss like we did for the training array

count_H =0
count_L=0
for i in 200: # fix me: this should pull 100 H training sets + 100 L training sets
    random.shuffle(J)
    J1 = tuple(J[0:3])
    J2 = tuple(J[3:6])
    J3 = tuple(J[6:9])
    J4 = tuple(J[9:12])
    print(J1, J2, J3, J4)
    S1 = create_s(J1, i)  # Fix me: this sends to the function the actual H/L array from the data set
    S2 = create_s(J2, i)
    S3 = create_s(J3, i)
    S4 = create_s(J4, i)
    print(S1, S2, S3, S4)
    allSs = [S1, S2, S3, S4]
    #starting to compare each tuple of testing array to the sums of L and H in its corresponding index
    for i in allSs:  # loop running through all S tuples
        decimal_num = bin_2_num(allSs[i])
        if  H_sum[decimal_num] > L_sum[decimal_num]:
            count_H +=1
        elif H_sum[decimal_num] < L_sum[decimal_num]:
            count_L += 1
    if count_H > count_L:
        print("Image number " i , "in the testing set is the H letter") #fix me: i is an actual array from the testing data set
    elif count_H < count_L:
        print("Image number " i , "in the testing set is the L letter") #fix me: i is an actual array from the testing data set

#STILL NEED TO DO THE ACCURACY PART- CHECKING IF OUR ANALYSIS IS CORRECT OR NOT
