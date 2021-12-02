def swap_case(s):
    swap_str=""
    for i in range(len(s)):
        if s[i].islower():
            swap_str=swap_str+s[i].upper()
        else:
            swap_str=swap_str+s[i].lower()
    return swap_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
