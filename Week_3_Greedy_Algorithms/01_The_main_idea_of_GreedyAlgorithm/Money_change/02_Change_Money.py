import numpy as np


def change(money, denominations):
    if money == 0:
        return 0

    denominations = np.array(denominations)
    maxCoin = denominations[denominations <= money].max()
    return 1 + change(money - maxCoin, denominations)


denominations = [1, 5, 10]
print(change(28, denominations))


def changeMoney(money):
    numCoin = 0
    while money > 0:
        if money >= 10:
            money = money - 10
            numCoin += 1
        elif money >= 5:

            money = money - 5
            numCoin += 1
        else:

            money = money - 1
            numCoin += 1
    return numCoin


print("other change money: ", changeMoney(28))


def third_way_chane(money):
    return money // 10 + (money % 10) // 5 + money % 5


print("third_way_chane: ", third_way_chane(28))
