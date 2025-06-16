
input()
minutos = list(map(int, input().split()))

ultimo = 0
for minuto in minutos:
    if minuto - ultimo > 15:
        print(ultimo + 15)
        break
    ultimo = minuto
else:
    print(90)

