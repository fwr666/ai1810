import random
L = []
for _ in range(30):
	a = random.randint(1,2000)
	L.append(a)
print(L)
i = 1
while i < len(L):
	a = L[i]
	if L[i]<L[i-1]:
		L[i],L[i-1] = L[i-1],L[i]


	i += 1
print(L)
