#Q.NO.1

l=[]
for a in range(10):
    integer= int(input("enter nos.: "))
    l.append(integer)
print(l)
for b in l:
    print(b)

#Q.NO.2

while True:
    print("I Love You ❤")

#Q.NO.3

m=[]
elements = int(input("enter total no elements of list: "))
for c in range(elements):
    element=int(input("enter elements: "))
    m.append(element)
print(m)
n=[]
for d in m:
    e=d**2
    n.append(e)
print(n)

#Q.NO.4

integers=[]
decimals = []
strings = []
lists = ["rakesh", "2", "4", "5.5", "kumar", "9.8"]
for f in lists:
    if f.isalpha():
        strings.append(f)
    elif f.isdigit():
        integers.append(int(f))
    else:
        decimals.append(float(f))
print(decimals)
print(integers)
print(strings)

#Q.NO.5

even =[]
odd = []
for g in range(1,101):
    if g%2==0:
        even.append(g)
    else:
        odd.append(g)
print(even)
print(odd)

#Q.NO.6

for h in range(1,5):
    print("*"*h)

#Q.NO.7

dict1 = {}
elements = int(input("enter no of elements: "))
for i in range(elements):
    key = input("enter key: ")
    value = input("enter value: ")
    dict1[key]=value
print(dict1)
for key in dict1:
    print(key)


#Q.NO.8

l=  []
a = int(input("enter total no of elements: "))
for b in range(a):
    elements = input("enter element: ")
    l.append(elements)
c = input("enter elemnts to be search: ")
for d in l:
    if c==d:
        l.remove(c)
print(l)
