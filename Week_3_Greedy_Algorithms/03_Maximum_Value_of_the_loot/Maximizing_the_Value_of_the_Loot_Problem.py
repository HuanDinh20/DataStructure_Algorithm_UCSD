"""
        Maximizing the Value of the Loot Problem
**  Find the maximum value of items that fit into the backpack

********************    Input:
W: The capability of the backpack
(w1, ... wn): the weights
(c1, ... cn): the cost
n: number of compounds

********************    Output:
The Maximum amount of items that fit into the backpack of the given capacity:
i.e., the maximum value of c1f1 + ...cnfn such that
w1f1 + ........ + wnfn <= W
and 0 <= fi <= 1 for all i
fi is the fraction of the i-th item take to the backpack


example:
A thief breaks into a spice shop and finds four pounds of saffron, three pounds of vanilla, and five pounds of cinnamon.
His backpack fits at most nine pounds, therefore he cannot take everything. Assuming that the prices of saffron,
vanilla, and cinnamon are $5000, $200, and $10 per pound , respectively, what is the most valuable loot in this case?
If the thief takes u_1 pounds of saffron, u_2 pounds of vanilla, and u_3 pounds of cinnamon, the total value of the loot
is
5000u1 + 200u2 + 10u3
The thief would like to maximize the value of this expression subject to the following constraints:
u1 <= 4
u2 <= 3
u3 <= 5

u1 + u2 + u3 <=9
"""

import sys


def get_optimal_value(capa , wei , cost):

    if capa == 0 or len(wei) == 0:
        return 0

    m = cost.index(max(cost))
    amount = min([wei[m], capa])
    value = cost[m] * amount / wei[m]

    wei.remove(wei[m])
    cost.remove(cost[m])
    return value + get_optimal_value(capa, wei, cost)


if __name__ == "__main__":
    data = list([int(i) for i in input().split()])
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

