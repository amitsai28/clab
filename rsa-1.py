from decimal import Decimal
def gcd(a,b):
  if(b==0):
    return a
  else:
   return gcd(b,a%b)

p=int(input("enter the first prime no"))
q=int(input("enter the second prime no"))
n=p*q;
t=(p-1)*(q-1)

gcd_list = []
for e in range(2,t):
   if(gcd(e,t)==1):
      gcd_list.append(e)

print(gcd_list)
e= int(input("enter the no from the above list"))
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

d= modinv(e,t)              
print("public key",(e,n))
print("private key",(d,n))      
m=int(input("enter the input message"))
ctt=pow(m,e)
ctt=ctt%n

dtt=m
dtt=pow(ctt,d)
dtt=dtt%n

print("the encyrpted text"+ str(ctt) +" "+"the decrypted text"+ str(dtt)+" ")
    
  