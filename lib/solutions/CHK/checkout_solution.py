from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

PRICE_TABLE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

OFFERS = {
    ('A', 3): 130,
    ('B', 2): 45
}

def checkout(skus):
    total = 0
    counter = Counter(skus)
    for key in counter.keys():
        if counter[key] == 1:
            total += PRICE_TABLE[key]
        elif (key, counter[key]) in OFFERS:
            total += OFFERS[key, counter[key]]
    return total

if __name__ == '__main__':
    print(checkout('ABCA'))




