final_array = []
def CARDS():
    n = int(input())
    chef_cards,morty_Cards = [],[]
    chef_score,morty_score = 0,0
    for i in range(n):
        card = list(map(int,input().split()))
        chef_card = sum(list(map(int,str(card[0]))))
        morty_Card = sum(list(map(int,str(card[1]))))
        if chef_card > morty_Card:
            chef_score = chef_score + 1
        elif chef_card < morty_Card:
            morty_score = morty_score + 1
        else:
            chef_score = chef_score + 1
            morty_score = morty_score + 1

    if chef_score > morty_score:
        final_array.append([0,chef_score])
    elif  chef_score < morty_score:
        final_array.append([1,morty_score])
    else:
        final_array.append([2,chef_score])



T = int(input())
final_array = []
for i in range(T):
    CARDS()
for i in range(len(final_array)):
    print(final_array[i][0], final_array[i][1] )
