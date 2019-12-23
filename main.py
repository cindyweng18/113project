# Names:
# Cindy Weng Zhu
# Mumtahid Akash
#
#
#
#
import random

def bin2Numconv(a):
    b =((int(a[0]))*4) + ((int(a[1]))*2) + ((int(a[2]))*1) 
    return b

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
