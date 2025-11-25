def minEnergyDrink(shops: list[tuple[int, int]], M: int):
    totalCost = 0
    remaining = M

    shops.sort(key=lambda x: x[0])

    for p, s in shops:
        buy = min(remaining, s)
        totalCost += p * buy
        remaining -= buy

        if remaining == 0:
            break

    return totalCost
