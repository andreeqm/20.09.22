a=int(input("a= "))
m=int(input("m= "))
#a
def suma(x,y):
    s=0
    s=x+y
    return s
print("Suma nr este:",suma(a,m))
#b
def produs(x,y):
    p=1
    p=x*y
    return p
print("Produsul nr este:",produs(a,m))
#c
def med_aritmetic(x,y):
    ma=1
    ma=(a+m)/2
    return ma 
print("Media aritmetica a nr este:",med_aritmetic(a,m))
#d
def cmmdc(x,y):
    while x!=y:
        if x>y: x=x-y
        else: y=y-x
    return x
print("Cel mai mare divizor comun a nr este:",cmmdc(a,m))
#e
def cmmmc(x,y):
    w=x*y//cmmdc(x,y)
    return w
print("Cel mai mic multipu comun a nr este:",cmmmc(a,m))
#f
def min(x,y):
    if x<y:
        minimum=x
        return minimum
    if y<x:
        minimum=y
        return minimum
print("Numarul minim este:",min(a,m))
#g
def max(x,y):
    if x>y:
        maximum=x
        return maximum
    if y>x:
        maximum=y
        return maximum
print("Numarul maxim este:",max(a,m))
#h
def suma():
    a=int(input("a= "))
    b=int(input("b= "))
    c=a+b
    print(a,"+",b,"=",c)
c=suma()
#i
def produs():
    a=int(input("a= "))
    b=int(input("b= "))
    c=a*b
    print(a,"*",b,"=",c)
c=produs()
#j
def toti_div(x,y):
    div=[]
    for i in range(1,min(x,y)+1):
        if x%i==y%i==0:
            div.append(i)
    return div
print("Toti divizorii comuni ai nr sunt:",toti_div(a,m))
#k
mult=[]
def mult_5(a,m):
    z=a*m
    for i in range(5):
        mult.append(z)
        z=z*2
mult_5(a,m)
print("Multiplii comuni ai nr sunt:",mult,sep=" ")
#l
x=list(map(int, str(a)))
y=list(map(int, str(m)))
def cifre_comune(x,y):
    return set(x).intersection(y)
print("Cifrele care se contin in ambele numere sunt:",cifre_comune(x,y))
#m
s=[]
def cif_1nr_nu_2nr(a,m):
    for element in a:
        if element not in m:
            s.append(element)
    return s
print("Cifrele care sunt in primul nr si nu sunt in al doilea nr este:",cif_1nr_nu_2nr(a,m))
#n
def Prietene(a):
    b=[]
    for i in range(1,a+1):
        if a%i==0:
            b.append(i)
    return(len(b))
if Prietene(a)==Prietene(m):
    print("PRIETENE")
else:
    print("NU SUNT PRIETENE")
    


