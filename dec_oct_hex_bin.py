def print_formatted(number):
    # your code goes here
    leng=len(bin(n)[2:])
    s=""
    for j in range(leng):
        s+=" "
    for i in range(1,n+1):
        print(str(i).rjust(leng,' '),oct(i)[2:].rjust(leng,' '),hex(i)[2:].upper().rjust(leng,' '),bin(i)[2:].rjust(leng,' '),sep=" ")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
