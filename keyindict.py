a=input().split()
b=input().split()
d=len(a)
e=len(b)
if d!=e:
    print("Invalid")
else:
    c=input()
    mydict=dict(zip(a,b))
    if c in mydict:
        print(mydict)
        print("Exist")
    else:
        print("NOT EXIST")