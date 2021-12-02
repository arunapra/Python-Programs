s=input("Enter the string:")
s=s.lower()
flag =True
for i in range(97,123):
    cstr = chr(i)
    if cstr not in s:
        flag =False
        break
if(flag):
    print("pangram")
else:
    print("not pangram")
