with open('abc.txt','r') as myfile:
    count=0
    for i in myfile.readlines():
        u=lambda s:s.upper()
        u(i)
        l=i.split()
        k=len(l)
        count+=k