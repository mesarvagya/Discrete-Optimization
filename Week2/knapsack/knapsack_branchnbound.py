# http://www.geeksforgeeks.org/branch-and-bound-set-2-implementation-of-01-knapsack/
# https://github.com/tegarwicaksono/knapsack/blob/master/solver_alt.py

from queue import Queue
from collections import deque
class Node:
    def __init__(self):
        self.level = None
        self.profit = None
        self.bound = None
        self.weight = None
        self.contains = []

    def __str__(self):
        return "Level: %s Profit: %s Bound: %s Weight: %s" % (self.level, self.profit, self.bound, self.weight)


def bound(node, n, W, items):
    if(node.weight >= W):
        return 0

    profit_bound = int(node.profit)
    j = node.level + 1
    totweight = int(node.weight)

    while ((j < n) and (totweight + items[j].weight) <= W):
        totweight += items[j].weight
        profit_bound += items[j].value
        j += 1

    if(j < n):
        profit_bound += (W - totweight) * items[j].value / float(items[j].weight)

    return profit_bound

Q = deque([])

def KnapSackBranchNBound(weight, items, total_items):
    items = sorted(items, key=lambda x: x.value/float(x.weight), reverse=True)

    u = Node()

    u.level = -1
    u.profit = 0
    u.weight = 0

    Q.append(u)
    maxProfit = 0
    bestItems = []

    while (len(Q) != 0):

        u = Q[0]
        Q.popleft()
        v = Node()

        if u.level == -1:
            v.level = 0

        if u.level == total_items - 1:
            continue

        v.level = u.level + 1
        v.weight = u.weight + items[v.level].weight
        v.profit = u.profit + items[v.level].value
        v.contains = list(u.contains)
        v.contains.append(items[v.level].index)

        if (v.weight <= weight and v.profit > maxProfit):
            maxProfit = v.profit
            bestItems = v.contains

        v.bound = bound(v, total_items, weight, items)
        if (v.bound > maxProfit):
            # print v
            Q.append(v)

        v = Node()
        v.level = u.level + 1
        v.weight = u.weight
        v.profit = u.profit
        v.contains = list(u.contains)

        v.bound = bound(v, total_items, weight, items)
        if (v.bound > maxProfit):
            # print v
            Q.append(v)

    taken = [0] * len(items)
    for i in xrange(len(bestItems)):
        taken[bestItems[i]] = 1

    return maxProfit, taken

def get_solution(optimal_value, taken):
    output_data = None
    output_data = str(optimal_value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

if __name__ == "__main__":
    from collections import namedtuple
    Item = namedtuple("Item", ['index', 'value', 'weight'])
    input_data = open("./data/test").read()
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    print "running from main"
    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), float(parts[1])))
    kbb = KnapSackBranchNBound(capacity, items, item_count)
    print kbb

