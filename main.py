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
    
                

#The "good" H
with open("datasets.txt","w") as file:
    create_h()
    

#Separates each 0 and 1 into a single element of ONE list
with open("datasets.txt","r") as file:
    line = file.readline()
    print(line)
    bits = list(line)
    print(str(bits))
