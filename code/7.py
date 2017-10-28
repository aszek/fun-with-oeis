from oeis import OEIS
import json

def compute():
    o = OEIS(None, 12)

    names = [
    'prime',
    'graph',
    'automorphism',
    'group',
    'space',
    'code',
    'elliptic',
    'algorithm',
    'distribution',
    'probability',
    'differential',
    'stochastic',
    'poset',
    'invariant',
    'automatic',
    'metric',
    'binary',
    'field',
    'fraction',
    'operator',
    'norm',
    'set',
    'cardinality',
    'modulo',
    'quantum',
    'convex',
    'manifold',
    'variety',
    'category',
    'process',
    'extension',
    'equivalence',
    'algebraic',
    'topology',
    'kernel',
    'approximation'
    ]

    stat = []

    for name in names:
        res = o.count(name)
        print name, res
        if res > 0:
            stat.append((name, res))
        o.pause()

    stat.sort(key = lambda x: x[1])

    with open('../artifacts/7.json', 'w') as outfile:
        json.dump(stat, outfile)

def plot():
    with open('../artifacts/7.json', 'r') as infile:
        stat = json.load(infile)

    import matplotlib.pyplot as plt
    plt.barh(range(len(stat)), [_[1] for _ in stat], align='center')
    plt.yticks(range(len(stat)), [_[0] for _ in stat])
    plt.show()

#compute()
plot()