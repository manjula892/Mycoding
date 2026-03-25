import random
name1=input("enter player 1 name")
name2=input("enter player 2 name")
d1=random.randint(1,25)
d2=random.randint(1,25)
s1=25
s2=25
while True:
    g=int(input("enter your guess"))
    s1=s1-1
    if(d1==g):
        break
    elif(d1<g):
      print("your guess is more")
    else:
        print("your guess is less")
        
while True:
    g=int(input("enter your guess"))
    s2=s2-1
    if(d1==g):
        break
    elif(d2<g):
      print("your guess is more")
    else:
        print("your guess is less")
if(s1>s2):
    print("{} is winner".format(name1))
elif(s1<s2):
    print("{} is winner".format(name2)) 
else:
    print(I is drwa)