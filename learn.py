distancia_terra_marte = float(input())
velocidade_nave = float(input())
autonomia_combustivel = float(input())

tempo_viagem = distancia_terra_marte / (velocidade_nave * 3600)
combustivel_necessario = tempo_viagem * 500
margem_seguranca = autonomia_combustivel - tempo_viagem
if tempo_viagem < autonomia_combustivel:
    print("abortar")
else:
    print("marcha")


