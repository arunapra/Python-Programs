def secondl(t):
    maxv=max(t)
    secmax=0
    for i in t:
        if (secmax<i)and(i<maxv):
            secmax=i
    return secmax

t=eval(input("Enter the tuple elements:"))
print("Second largest value of given tuple:",secondl(t))

