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
    counter = {value: key for key, value in Counter(list(skus)).items()}
    print(counter)

if __name__ == '__main__':
    checkout('ABCA')



