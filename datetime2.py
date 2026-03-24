from datetime import datetime
a=input("Enter date in YYYY-MM-DD:")
b=input("Enter date in YYYY-MM-DD:")
a1=datetime.strptime(a,"%Y-%m-%d")
b1=datetime.strptime(b,"%Y-%m-%d")
print(b1-a1)