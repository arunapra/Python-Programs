def minion_game(string):
    # your code goes here
    vowel = ["A","E","I","O","U"]
    Kevin = 0
    Stuart = 0
    for i in range(len(string)):
        if string[i] in vowel:
            Kevin+=len(string)-i
        else:
            Stuart+=len(string)-i
    if (Kevin==Stuart):
        print("Draw")
    elif (Stuart>Kevin):
        print("Stuart",Stuart)
    else:
        print("Kevin",Kevin)
               

if __name__ == '__main__':
    s = input()
    minion_game(s)
