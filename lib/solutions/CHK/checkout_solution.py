from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

PRICE_TABLE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

OFFERS = {'A': (3, 130), 'B': (2, 45)}

def checkout(skus):
    total = 0
    counter = Counter(skus)
    for key in counter.keys():
        if key not in PRICE_TABLE:
            return -1
        total += PRICE_TABLE[key] * counter[key]
        if key in OFFERS:
            total -= (counter[key] // OFFERS[key][0]) * (counter[key]*PRICE_TABLE[key]-OFFERS[key][1])

    return total

if __name__ == '__main__':
    print(checkout('AABC'))


