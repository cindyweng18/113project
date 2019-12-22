# Names:
# Cindy Weng Zhu
#
#
#
#
#

#Create a function to write more variations of H and L? or separate functions for H and L
def variations():


#The "good" H
with open("datasets.txt","w") as file:
    file.write("101111101101")

#Separates each 0 and 1 into a single element of ONE list
with open("datasets.txt","r") as file:
    line = file.readline()
    print(line)
    bits = list(line)
    print(str(bits))
