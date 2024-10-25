s=int(input("size:"))
dic={}
for i in range(s):
	key=input("key:")
	dic[key]=int(input("value:"))
sum=sum(dic.values())
print(f"Sum:{sum}")
print(dic)