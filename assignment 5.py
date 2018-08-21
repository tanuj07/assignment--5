#Question 1
y=int(input("enter year"))
if y%4==0:
    if y%100==0:
        if y%400==0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")

#Question 2
l=int(input("enter length"))
b=int(input("enter breadth"))
if l==b:
    print("it is square")
else:
    print("it is rectangle")

#Question 3
a=int(input("enter first age"))
b=int(input("enter second age"))
c=int(input("enter third age"))
if a>b and a>c:
    print("a is oldest")
elif b>c and b>a:
    print("b is oldest")
else:
    print("c is oldest")
if a<b and a<c:
    print("a is youngest")
elif b<c and b<a:
    print("b is youngest")
else:
    print("c is youngest")

#Question 4
age=int(input("enter age"))
sex=input("enter sex")
st=input("enter marital status")
if age<20 and age>60:
    if sex=='male' or sex=='female':
        print("error")
else:
    if sex=='female':
        print("u will work in urban areas only")
    else:
        if age>20 and age<40:
            print("u may work anywhere")
        else:
            print("u will work in urban areas only")

#Question 5
q=int(input("enter quantity"))
q=q*100
if q>1000:
    q=q-(q*0.1)
print("total cost: ",q)

#Question 6
a=[]
for i in range(0,10):
    n=int(input(" "))
    a.append(n)
print(a)

#Question 7
a=0
while a==0:
    print("hello")

#Question 8
a=[]
b=[]
for i in range(0,5):
    n=int(input(""))
    a.append(n)
    b.append(n*n)
print(a)
print(b)

#Question 9
a=['tanuj',14,18,7.9]
ints=[]
strs=[]
floats=[]
for i in range(0,4):
    if isinstance(a[i],int):
        ints.append(a[i])
    elif isinstance(a[i],str):
        strs.append(a[i])
    else:
        floats.append(a[i])
print(ints)
print(strs)
print(floats)

#Question 10
a=[]
for i in range(1,101):
    flag=0
    if i==2:
        a.append(i)
    else:
        for j in range(2,i):
            if i%j==0:
                flag=1
                break;
            else:
                flag=0
        if flag==0:
            a.append(i)
a.remove(1)
print(a)

#Question 11
for i in range(0,4):
    for j in range(0,i+1):
        print("*",end='')
    print("\r")

#Question 12
a=[]
for i in range(0,6):
    n=int(input(""))
    a.append(n)
n=int(input("enter no. u want to delete"))
a.remove(n)
print(a)