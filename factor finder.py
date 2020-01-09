a=int(input("enter the number"))
for p in range(a,b):
  for i in range(2,p):
    if(p%i==0):
     break;
    else:
       print("the prime number is",p)
