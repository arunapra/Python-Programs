st=input("Enter any string:")
rev=""
for i in st:
    print(i)
    rev=i+rev
if st==rev:
    print(st,"is a palindrome string")
else:
    print(rev,"is not a palindrome string")
