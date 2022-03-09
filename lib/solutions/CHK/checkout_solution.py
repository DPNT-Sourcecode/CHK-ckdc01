from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

PRICE_TABLE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}

OFFERS = {'A': {3: 130, 5: 200},
          'B': {2: 45}}

def checkout(skus):
    total = 0
    counter = Counter(skus)
    for key in counter.keys():
        if key not in PRICE_TABLE:
            return -1
        total += PRICE_TABLE[key] * counter[key]
        if key in OFFERS:
            sorted_dict = sorted(OFFERS[key], key=OFFERS[key].get, reverse=True)

                total -= (counter[key] // relevant_promotion) * (relevant_promotion*PRICE_TABLE[key]-OFFERS[key][relevant_promotion])

    return total

if __name__ == '__main__':
    print(checkout('AAAAAAAABC'))
