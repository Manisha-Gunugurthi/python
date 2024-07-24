s="Selena#34@gmail.com"
dig=0
upp=0
low=0
sp=0
for i in s:
    if i.isdigit():
        dig+=1
    elif i.isupper():
        upp+=1
    elif i.islower():
        low+=1
    elif i=="@" or i=="_" or i=="#":
        sp+=1
    elif len(s) and dig>0 and upp>0 and low>0 and sp>0 and dig+upp+low+sp>8:
        print("valid")
    else:
       print("invalid")
    
        
