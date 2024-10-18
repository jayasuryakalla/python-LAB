s=input()
flag = 0
for z in s:
    if('a' in z or 'A' in z or 'e' in z or 'E' in z or 'i' in z or 'I' in z or 'o' in z or 'O' in z or 'u' in z or 'U' in z):
        flag+=1
print("no.of vowels:",flag)