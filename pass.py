import random # for random obviously
import subprocess #for clipboard also apparently XD
#alan k john

caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
specials = ['#','(',')','?','[',']','`','~',',',';',':','$','%','^','&','*','=','+','/','*','-','?','!','@']
numbs = ['1','2','3','4','5','6','7','8','9','0']

#numbs = list(range(0,10))                          #does the same thing


splespce = caps + small + specials + numbs



#print(*splespce, sep='')                           #to print it continuously



# initialising passw

passw = []

i=0

for b in range(1,17):                               #cuz we want 16 digits
#    print(b)
    a = random.choice(splespce)                     #pulls a random element from the list
#    print(a)
    passw.insert(i,a)                               #can also try .append to simple add to the end
    i=i+1                                           # i did it this way because i didnt understand how python for loops worked yet

#print(*passw, sep='')                              #if you want to see the list


# list to string                                    #to convert the list into a string

str = ""

for j in passw:
    str += j                                        # short hand for str=str+j

#  to clipboard


data = str                                          #not necessary you can just type str instead of data below
subprocess.run("clip", universal_newlines=True, input=data)         #to push the string into the clip board so now try ctrl+v to paste it anywhere



