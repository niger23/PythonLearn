sp = []
for i in range(3):
    sp1=[]
    for j in range(3):
        sp1.append(i + j)
    sp.append(sp1)

for i in range(len(sp)):
    print(sp[i])

sp.insert(0,[8,9])
print("------")

sp.remove([8,9])
a=sp.pop(-1)

print(a)
print("одномерный список")
print(a[::-1])
a=a + [15,11,99]
print(a)
print(a[2:5])

book={}

book['Миша'] = 69505906
book['Саша'] = [56576857, 856748578]

print(book)

if 'Саша' in book:
    print("Yes")
else:
    print("No")

for x,y in book.items():
    print(x,y)

for x in book.values():
    print(x)
for y in book.keys():
    print(y)
    