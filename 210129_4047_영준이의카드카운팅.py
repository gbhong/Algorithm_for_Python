import sys
sys.stdin = open("/Users/gibonghong/Downloads/sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    _cards = input()
    cards = []
    for i in range(len(_cards)//3):
        cards.append(_cards[3*i:3*(i+1)])
    cards_dict = {'S':[], 'D':[], 'H':[], 'C':[]}

    a=0
    for card in cards:
        if card[1:] not in cards_dict[card[0]]:
            cards_dict[card[0]].append(card[1:])
            a+=1

    answer = []
    if a == len(cards):
        for c in 'SDHC':
            answer.append(str(13-len(cards_dict[c])))
        print('#{} {}'.format(tc, ' '.join(answer)))
    else:
        print(f'#{tc} ERROR')


