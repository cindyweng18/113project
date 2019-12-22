# Names:
# Cindy Weng Zhu
#
#
#
#
#
import random #allows us to use randint(0,1) -> function that randomly returns a 0 or 1

#Create a function to write more variations of H and L? or separate functions for H and L
def create_h():
    good_h = ['1','0','1','1','1','1','1','0','1','1','0','1']
    for i in range(12):
        good_h[i] = str(random.randint(0,1))
    return good_h

def list_to_string(lst):
    newstr = ""
    for i in lst:
        newstr = newstr + i
    return newstr
            
                
with open("datasets.txt","w") as file:
    for i in range(50):
        eich = create_h()
        file.write(list_to_string(eich))
    

#Separates each 0 and 1 into a single element of ONE list
with open("datasets.txt","r") as file:
    line = file.readlines()
    print(line)
#    bits = list(line)
#    print(str(bits))
