num_list=eval(input("Enter the list elements:"))
#num_list=list(input("Enter the list elements:"))
#num_list=list(map(int,input("Enter the list elements:").split()))

l=len(num_list)
even_count=odd_count=s=0
for i in range(l):
    s=(num_list[i])
    if(s%2==0):
        even_count+=1
    else:
        odd_count+=1
print("Number of even numbers=",even_count)
print("Number of odd numbers=",odd_count)
