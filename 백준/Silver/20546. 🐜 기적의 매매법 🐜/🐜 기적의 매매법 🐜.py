import sys
input = sys.stdin.readline

money = int(input())    # 처음 가지는 돈
stock = list(map(int, input().split()))     # 1/1 ~ 1/14 주가

# 준현이는 주식을 살 수 있을 때 전량 구입한다.
def jun():
    final = 0
    for idx, j in enumerate(stock):
        if j <= money:
            mon = money // j
            final += (stock[-1] - stock[idx]) * mon
            break
    return money + final

# 성민이는 다음날 가격이 하락할 때 전량 구입한다.
def sung():
    remains = money     # 남은 현금
    stock_list = []
    for i in range(3, 14):
        if stock[i] < stock[i-1] < stock[i-2] < stock[i-3] and remains >= stock[i]:    # 3일 연속 하락하면 전량 매수
            mon = remains // stock[i]
            remains -= stock[i] * mon
            stock_list.append((mon, stock[i]))
        elif stock[i] > stock[i-1] > stock[i-2] > stock[i-3] or i == 13:   # 3일 연속 상승하면 전량 매도
            while stock_list:
                x, y = stock_list.pop()
                remains += stock[i] * x
    return remains

jun_final = jun()
sung_final = sung()

if jun_final > sung_final:
    print("BNP")
elif jun_final < sung_final:
    print("TIMING")
else:
    print("SAMESAME")