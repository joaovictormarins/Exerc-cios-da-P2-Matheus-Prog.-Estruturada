#16. Filtrar Palavras de uma Lista

time = ["Real Madrid" ,"Barcelona","Atlético de Madrid", "Sevilla", "Valencia","Inglaterra","Manchester United","Manchester City"]

letra = str(input("Qual a letra desejada ? ")) .upper()
if letra:
    filtrar = list(filter(lambda time: time.startswith(letra), time))
    print (filtrar)
else:
    print ("Digite uma letra para funcionar")