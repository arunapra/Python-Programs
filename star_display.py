stri="*"
space=" "
print(stri)
for i in range(1,4):
    stri=stri+space
    print(stri+"*")
space="  "
for k in range(1,3):
    #for l in range(k+1,1,-1):
        
    stri=stri.replace(space," ")
    print(stri+"*")
stri="*"
print(stri)
