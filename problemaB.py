while True:
    n = int(input())
    if n == 0:
        break

    maior = -1
    sala = -1
    
    for i in range(n):
        pontos = int(input())
        if pontos > maior:
            maior = pontos
            sala = i + 1
    print(sala)


