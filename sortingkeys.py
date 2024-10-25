n = int(input())
my_dict = {}
my_dict1 = {}
for _ in range(n):
	key=int(input())
	value=input()
	my_dict1[key]=value
my_dict=dict(sorted(my_dict1.items()))
print(my_dict)