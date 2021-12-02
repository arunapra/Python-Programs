if __name__ == '__main__':
    n = int(input())
    phone_book = {}
    for _ in range(n):
        name, phone_num = input().split()
        phone_book[name] = phone_num
    while True:
        try:
            query=str(input())
            phnum=phone_book.get(query)
            if phnum!=None:
                print(query,"=",phnum,sep="")
            else:
                print("Not found")
        except:
            break
