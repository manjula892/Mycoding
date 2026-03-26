a=input("enter any password: ")
up=0
sm=0
dg=0
sp=0
if(len(a)>7):
    for i in a:
        if i.isupper():
            up=up+1
        elif i.islower():
            sm=sm+1
        elif i.isdigit():  
            dg=dg+1
        else:
            sp=sp+1
    if(up>0and sm>0and dg>0and sp>0):
        print("strong password")
    else:
        print("weak password")
else:
    print("invalid")