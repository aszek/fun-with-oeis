from oeis import OEIS

o = OEIS(None)

names = [
'Warszawa',
'Krakow',
'Lodz',
'Wroclaw',
'Poznan',
'Gdansk',
'Szczecin',
'Bydgoszcz',
'Lublin',
'Katowice',
'Bialystok',
'Gdynia',
'Czestochowa',
'Radom',
'Sosnowiec',
'Torun',
'Kielce',
'Rzeszow',
'Gliwice',
'Zabrze',
'Olsztyn',
'Bielsko',
'Bytom',
'Zielona',
'Rybnik',
'Ruda',
'Tychy',
'Opole',
'Gorzow',
'Dabrowa',
'Plock',
'Elblag',
'Walbrzych',
'Tarnow',
'Chorzow',
'Koszalin',
'Kalisz',
'Legnica',
]

stat = []

for name in names:
	res = o.count(name)
	print name, res
	if res > 0:
		stat.append((name, res))
	o.pause()

stat.sort(key = lambda x: -x[1])

import matplotlib.pyplot as plt
plt.bar(range(len(stat)), [_[1] for _ in stat], align='center')
plt.xticks(range(len(stat)), [_[0] for _ in stat])
plt.show()