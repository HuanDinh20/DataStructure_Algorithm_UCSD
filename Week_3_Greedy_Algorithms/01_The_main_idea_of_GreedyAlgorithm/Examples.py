"""
A greedy algorithm builds a solution piece by piece and at each step, chooses the most profitable piece.
This is best illustrated with examples.

    Our first example is the Largest Concatenate Problem: given a sequence of single-digit numbers, find the largest number
that can be obtained by concatenating these numbers. For example, for the input sequence (2,3,9,2,2)(2,3,9,2,2), the
output is the number 9332293322. It is easy to come up with an algorithm for this problem. Clearly, the largest
single-digit number should be selected as the first digit of the concatenate. Afterward, we face essentially the same
problem: concatenate the remaining numbers to get as large number as possible.

************** Pseudocode *****************

LAGESTCONCATENATE (Numbers)

result = []
while Numbers is not empty:
    maxNumber = largest among Numbers
    append maxNumber to result
    remove maxNumber from Numbers

return result




    Our second example is the Money Change Problem: given a non-negative integer moneymoney, find the minimum number of
coins with denominations 1, 5, and 10 that changes money. For example, the minimum number of coins needed to change
money = 28money=28 is 6: 28 = 10+10+5+1+1+128=10+10+5+1+1+1. This representation of 2828 already suggests an algorithm.
We take a coin cc with the largest denomination that does not exceed moneymoney. Afterward, we face essentially the
same problem: change (money − c)(money−c) with the minimum number of coins.


************** Pseudocode *****************

CHANGE(money, Denominator):
number  = 0
While money > 0:
    maxCoin <- largest among Denominator that does not exceed money
    money <- money - maxCoin
    numberCoins <- numCoins + 1
return numCoins

"""


def LargestConcatenateNumber(numbers):
    results = ''
    numbers = list(numbers)
    while numbers is not len(numbers) > 1:
        maxNumber = max(numbers)
        results = results + str(maxNumber)
        numbers.remove(maxNumber)
    return results


number = (2,3,9,2,2)
print(LargestConcatenateNumber(number))
