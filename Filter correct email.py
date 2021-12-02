def fun(s):
    flag=False
    d=s.find(".")
    if(d==-1):
        return flag
    k=0
    for n in range(d+1,len(s)):
        k+=1
        if (ord(s[n]) in range(65,91) or ord(s[n]) in range(97,123)):
            if(k<=3):
                continue
        return flag
    r=s.find("@")
    if(r==0) or (r==-1):
        return flag
    for i in range(r):
        if(ord(s[i]) in range(65,91) or ord(s[i]) in range(97,123) or ord(s[i]) in range(48,58) or s[i]=="-" or s[i]=="_"):
            continue
        return flag
    for j in range(r+1,d):
        if(ord(s[j]) in range(65,91) or ord(s[j]) in range(97,123) or ord(s[j]) in range(48,58)):
            continue
        return flag
    return True    
             
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
