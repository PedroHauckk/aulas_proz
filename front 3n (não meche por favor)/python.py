nprimos = [2]
nescolhidos = []
y = int(input("Até qual número deseja saber se é primo? "))
x = 2
while x != y:
	x = x + 1
	nescolhidos.append(x)
for i in range(len(nescolhidos)):
	for e in range(len(nprimos)):
		if nescolhidos[i] != nprimos[e] or 7**0.5 > nprimos[e]:
			if nescolhidos[i] % nprimos[e] != 0:
				if nescolhidos[i] in nprimos:
					continue
				else: 
					nprimos.append(nescolhidos[i])
					continue
			else:
				if nescolhidos[i] in nprimos:
					nprimos.remove(nescolhidos[i])
				else:
					pass
				break
		else:
			pass
		break
print(nprimos)
print("Existem",len(nprimos),"números primos de 0 a até", y)
