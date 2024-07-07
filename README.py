# Reverse
Reversing words of a string
s = input("Enter string :")
num = len(s)
l = list(s)
# Remove spaces from back of given string

a = True
while a:
    if l[num - 1] == ' ' :
        del l[num-1]
        num = num -1 
    else:
        a = False
#insert a space at last
l.append(' ')
# Remove spaces from starting of given string  
def rem_space_start(list):     
    a = True
    while a:
        if list[0] == ' ' :
            del list[0] 
        else:
            a = False

rem_space_start(l)                            
b = True
li=[]
string = ''
while b:
    if len(l) == 1 and l[0] == ' ' :
        break
    
    rem_space_start(l)
    for i in range(len(l)):
        if l[i] ==' ' :
            del l[0:i]            
            break
        else :
            string = string + l[i]           
    li.append(string)
    string = ''            
            
            

    if len(l) == 0  :
        b = False

list_new = li[ : :-1] 
final_string = ''                          
for k in list_new:
    final_string = final_string + k + ' '   

print(final_string)
