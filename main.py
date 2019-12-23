# Names:
# Cindy Weng Zhu
# Mumtahid Akash
# Hope Dunner
# Zarif Choudhury
# Sajid Mahmud
# Michal Moryosef

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


J = []
array_H_1 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_2 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_3 = [0,  0,  0,  0,  0,  0,  0,  0]
array_H_4 = [0,  0,  0,  0,  0,  0,  0,  0]
allTs = [array_H_1, array_H_2, array_H_3, array_H_4]

# Trainings sets for Letter H
# I need to know how to pull the arrays you guys created from the data set.
# I guess you could help me link them to the code?
for i in 200:  # Correct me: this should run through 200 training sets of H
    random.shuffle(J)
    J1 = tuple(J[0:3])
    J2 = tuple(J[3:6])
    J3 = tuple(J[6:9])
    J4 = tuple(J[9:12])
    print(J1, J2, J3, J4)
    S1 = create_s(J1, i) # Correct me: this sends to the function the actual H array from the data set
    S2 = create_s(J2, i)
    S3 = create_s(J3, i)
    S4 = create_s(J4, i)
    print(S1, S2, S3, S4)
    allSs = [S1, S2, S3, S4]
    for i in allSs: # loop incrementing all T_H arrays
        match_found (allSs[i], allTs[i])
    for i in range (len(allTs)): # prints all of T's after the incrementation
        print("\t", " ", allTs[i], "\t")

array_L_1 = [0,  0,  0,  0,  0,  0,  0,  0]
array_L_2 = [0,  0,  0,  0,  0,  0,  0,  0]
array_L_3 = [0,  0,  0,  0,  0,  0,  0,  0]
array_L_4 = [0,  0,  0,  0,  0,  0,  0,  0]
allLs = [array_L_1, array_L_2, array_L_3, array_L_4]
# Trainings sets for Letter L
# same thing here guys,
# I need to know how to pull the arrays you created from the data set.
# I guess you could help me link them to the code?
for i in 200:  # Correct me: this should run through 200 training sets of L
    random.shuffle(J)
    J1 = tuple(J[0:3])
    J2 = tuple(J[3:6])
    J3 = tuple(J[6:9])
    J4 = tuple(J[9:12])
    print(J1, J2, J3, J4)
    S1 = create_s(J1, i) # Correct me: this sends to the function the actual L array from the data set
    S2 = create_s(J2, i)
    S3 = create_s(J3, i)
    S4 = create_s(J4, i)
    print(S1, S2, S3, S4)
    allSs = [S1, S2, S3, S4]
    for i in allSs: # loop incrementing all T_H arrays
        match_found (allSs[i], allTs[i])
    for i in range (len(allTs)): # prints all of T's after the incrementation
        print("\t", " ", allTs[i], "\t")
