N=int(input("Enter the total number of country stamps:"))
s=set()
for i in range(N):
    s.add(input("Enter the name of the country stamp"))
print(s)
print(len(s))
