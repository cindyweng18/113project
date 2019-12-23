# Names:
# Cindy Weng Zhu
# Mumtahid Akash
# Hope Dunner
# Zarif Choudhury
# Sajid Mahmud
# Michal Moryosef

import random

def bin2Numconv(userlist):
    numeral =((int(userlist[0]))*4) + ((int(userlist[1]))*2) + ((int(userlist[2]))*1) 
    return numeral

# Cindy's part: Create smaller set of lists 
def create_S(small_tuple, original_list):
    S = []
    for i in small_tuple:
        S.append(original_list[i-1])
    return S

RH = [1,0,1,1,1,1,1,0,1,1,0,1] # indexes start from 1 instead of 0
J = [1,2,3,4,5,6,7,8,9,10,11,12] #indexes
random.shuffle(J)
J1 = tuple(J[0:3])
J2 = tuple(J[3:6])
J3 = tuple(J[6:9])
J4 = tuple(J[9:12])
print(J1,J2,J3,J4)
S1 = create_S(J1,RH)
S2 = create_S(J2,RH)
S3 = create_S(J3,RH)
S4 = create_S(J4,RH)
print(S1,S2,S3,S4)




# DELETE this if this is not what we are supposed to do
#Training the machine


T_1H = [0,  0,  0,  0,  0,  0,  0,  0]
T_2H = [0,  0,  0,  0,  0,  0,  0,  0]
T_3H = [0,  0,  0,  0,  0,  0,  0,  0]
T_4H = [0,  0,  0,  0,  0,  0,  0,  0]

allTs = [T_1H, T_2H, T_3H, T_4H]
allSs = [S1, S2, S3, S4]
def matchFound (Ti, Si): # this is just to increment those 7 boxes in machine learning part
    decimalNum = bin2Numconv(Si)
    Ti[decimalNum] += 1

print ("\n\nindex:  0  1  2  3  4  5  6  7")
for i in range (len(allTs)): # loop to repeat incrementing all T arrays
    matchFound(allTs[i], allSs[i])
    print ("\t"," ",allTs[i],"\t")
