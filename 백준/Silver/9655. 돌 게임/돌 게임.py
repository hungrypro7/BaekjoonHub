n = int(input())
players = []
while n != 0:
    if n >= 3:
        n -= 3
        if (not players) or players[-1] == 'CY':
            players.append('SK')
        else:
            players.append('CY')
    else:
        n -= 1
        if (not players) or players[-1] == 'CY':
            players.append('SK')
        else:
            players.append('CY')
print(players[-1])