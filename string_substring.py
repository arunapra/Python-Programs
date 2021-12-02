def count_substring(string, sub_string):
    index=string.find(sub_string)
    if index==-1:
        return 0
    else:
        count=0
    while index!=-1 and index<len(string):
        count+=1
        ind=string[(index+1):].find(sub_string)
        if ind==-1:
            break
        index=index+ind+1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
