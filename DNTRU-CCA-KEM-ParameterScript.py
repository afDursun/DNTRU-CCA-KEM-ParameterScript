import  math
from decimal import Decimal

my_list = []
narray = []
darray = []
twin_list = []

def message_security(N,d):
    a = math.factorial(N)
    b = math.pow((math.factorial(d)),2)
    c = math.factorial(N - 2*d)
    d = math.sqrt(a / ( Decimal(b) * Decimal(c)) )
    return math.log2( d )


def key_security(N,d):
    a = math.factorial(N)
    b = (math.factorial(d))
    c = math.factorial(d-1)
    d = math.factorial(N - 2*d + 1)
    e = math.sqrt( Decimal(a) / ( Decimal(b) * Decimal(c) * Decimal(d)) )
    return math.log2(e)

def is_prime(n):
   for i in range(2, n):
      if n % i == 0:
         return False
   return True

def generate_twins(start, end):
   for i in range(start, end):
      j = i + 2
      if(is_prime(i) and is_prime(j)):
        twin_list.append(i)
         


def foo(d):
    q1 = ( d * 40 ) - 18
    return q1

def bar(q1):
    return math.floor( (q1 + 18) / 40 ) 


def is_twin_prime(num):
    if is_prime(num) == False:
        return False
    
    if is_prime(num - 2) == True:
        return True
    
    if is_prime(num + 2) == True:
        return True
    
    return False

    
 
def findNd(targetSecurity,defaultN):
    for N in range(defaultN+1):
        for d in range( math.floor(defaultN / 3) ):
            try:
                if math.floor(key_security(N,d)) <= targetSecurity+1 and math.floor(key_security(N,d)) >= targetSecurity-1:
                    if N == defaultN:
                        return N,d
            except:
                a=5    
 
def takeClosest(num,collection):
   return min(collection,key=lambda x:abs(x-num))

def generateQ1(d,defaultQ):
   q = foo(d)
   generate_twins(q,defaultQ)
   q1 = takeClosest(defaultQ,twin_list)
   return q1

def findPkSize(n,q1,q2):
    return math.floor((n * (math.log2(q1) + math.log2(q2)) ) / 8)

def findSkSize(n,p,q1):
    return math.floor((2* n * (math.log2(p) + math.log2(q1))  ) / 8)

def findCtSize(q1,q2,n):
    return math.floor((n * (math.log2(q1) + math.log2(q2) + math.log2(2))) / 8)


targetSecurityList = [128 , 192 , 256] 
defaultNList = [509, 677, 821]
defaultQList = [2048, 2048, 4096]            
defaultP = 3

for i in range(len(targetSecurityList)):
    nVar , dVar = findNd(targetSecurityList[i] , defaultNList[i])
    q1 = generateQ1(dVar, defaultQList[i])
    q2 = q1+2
    pkSize = findPkSize(nVar,q1,q2)
    skSize = findSkSize(nVar,defaultP,q1)
    ctSize = findCtSize(q1,q2,nVar)
    ms = message_security(nVar, dVar)
    print("Target Security: " + str(targetSecurityList[i]) + " Message Security:" + str(math.floor(ms)) + " N:" + str(nVar) 
    + " Q1: "+str(q1) + " Q2: "+str(q2) + " d: "+str(dVar) + 
    " PK: "+str(pkSize) + " SK: "+str(skSize)  + " CT: "+str(ctSize))
    
