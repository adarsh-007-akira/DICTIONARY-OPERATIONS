num=int(input("No. Of elemnts in dictionary :\n"))
dictionary={}
x=[]
y=[]
for i in range(num):
    a=input(f"Enter the Key {i+1} :\t")
    b=input(f"Enter the Value {a} :\t")
    x.append(a)
    y.append(b)
for i in range(len(x)):
    dictionary[x[i]]=y[i]
for i in sorted(dictionary.keys()):
    print(f"\n{i} : {dictionary[i]}\n")