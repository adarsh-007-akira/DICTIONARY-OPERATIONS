num=int(input("No. Of elemnts in dictionary :\n"))
dictionary={}
x=[]
y=[]
for i in range(num):
    a=input(f"Enter the Key {i+1} :\t")
    b=input(f"Enter the Number of Values for {a} :\t")
    x.append(a)
    d=[]
    for i in range(int(b)):
        c=(input(f"\tEnter the element number {i+1} for {a} :\t"))
        d.append(c)
    y.append(d)
for i in range(len(x)):
    dictionary[x[i]]=y[i]
print(dictionary)