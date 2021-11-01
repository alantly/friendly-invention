def knapsackLight(value1, weight1, value2, weight2, maxW):
    items = [(weight1, value1), (weight2, value2)]
    return knapsack(items, 0, maxW)

def knapsack(remainingItems, currentValue, maxW):
    if maxW < 0:
        return 0
    if maxW == 0:
        return currentValue
    if len(remainingItems) == 0:
        return currentValue
    topItem = remainingItems[0]
    return max(knapsack(remainingItems[1:], currentValue + topItem[1], maxW - topItem[0]), knapsack(remainingItems[1:], currentValue, maxW))
