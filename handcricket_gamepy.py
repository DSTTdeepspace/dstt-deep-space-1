import random
from random import randint
you=str(input("enter your team name: "))
opp=str(input("enter your opponent's name: "))
ind=0
aus=0
s=0
w=0
e=int(input("specify the number of overs: "))
o=e*6
for i in range(0,o+1):
  bat=random.randint(0,6)
  b=int(input("enter the number: "))
  if(b==str):
    b=int(input("enter the number again: "))
  if(b>6 or b<1):
    b=int(input("enter the number again: "))
  if(b==bat):
    s=s+1
    print(opp,":",aus,"/",s)
  else:
    aus=aus+bat
    print(opp,":",aus,"/",s)
  if(s==10 or i==o):
    print("innings end")
    break
  else:
    print("")
for i in range(0,o+1):
  ball=random.randint(0,6)
  a=int(input("enter the number: "))
  if(a==str):
    a=int(input("enter the number again: "))
  if(a>6):
    a=int(input("enter the number again: "))
  if(a==ball):
    w=w+1
    print(you,":",ind,"/",w)
  else:
    ind=ind+a
    print(you,":",ind,"/",w)
  if(w==10 or i==o):
    print(opp," wins")
    break
  elif(ind>aus):
    print(you," wins")
    break
if(o >= 300):
  for i in range(0,o+1):
    bat=random.randint(0,4)
    b=int(input("enter the number: "))
    if(b>4 or b<0):
      b=int(input("enter the number again: "))
    elif(b==str):
      b=int(input("enter the number again: "))
    elif(b==bat):
      s=s+1
      print(opp,":",aus,"/",s)
    else:
      aus=aus+bat
      print(opp,":",aus,"/",s)
    if(s==10 or i==o):
      print("innings end")
      break
    else:
      print("")
    for i in range(0,o+1):
      ball=random.randint(0,4)
      a=int(input("enter the number: "))
      if(a==str):
        a=int(input("enter the number again: "))
      elif(a>4 or a<0):
        a=int(input("enter the number again: "))
      elif(a==ball):
        w=w+1
        print(you,":",ind,"/",w)
      else:
        ind=ind+a
        print(you,":",ind,"/",w)
      if(w==10):
        print(opp," wins")
        break
      elif(ind>aus):
        print(you," wins")
        break
      else:
        print("draw")
        break
else:
  print("")

  

    
    

  
  
