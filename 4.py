num=int(input("No. Of elemnts in dictionary :\n"))
dictionary={}
x=[]
y=[]
for i in range(num):
    a=input(f"Enter the Key {i+1} :\t")
    b=int(input(f"Enter the Value {a} :\t"))
    x.append(a)
    y.append(b)
for i in range(len(x)):
    dictionary[x[i]]=y[i]
vals=dictionary.values()
print(sum(vals))
