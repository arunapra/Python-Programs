if __name__ == '__main__':
    scores=[]
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        records.append([name,score])
    num=len(records)
    score_desc=list((sorted(scores)))
    mini=score_desc[0]
    names=[]
    for i in range(num):
        if score_desc[i]!=mini:
            second_grade=score_desc[i]
            for j in range(num):
                if records[j][1]==second_grade:
                    names.append(records[j][0])
            break
    print("\n".join(sorted(names)))

