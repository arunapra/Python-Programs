''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
 ND_list = list(map(int,input().split()))
 N = ND_list[0]
 D = ND_list[1]
 temp = list(map(int,input().split()))
 nday = nshoechange = 0
 shoe=1
 for i in range(N):
    if(temp[i]<0):
        if(shoe==1):
            shoe = 2
            nday+=1
            nshoechange+=1
        else:
            nday+=1
    else:
        if(shoe==2):
            nshoechange+=1
            shoe = 1

 if(nday<=D):
     print(nshoechange)
 else:
     print("NOT POSSIBLE")


main()