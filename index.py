#Desafio Classificador de nível de Herói

nomeDoHeroi = input("Qual é o nome do Herói? ")
quantdXpHeroi = int (input("Que nível está o Herói? "))

if quantdXpHeroi <= 1000:
    print("O Herói" ,nomeDoHeroi, "está no nível de: Ferro")
elif quantdXpHeroi >= 1001 and quantdXpHeroi <= 2000: 
    print("O Herói" ,nomeDoHeroi, "está no nível de: Bronze")
elif quantdXpHeroi >= 2001 and quantdXpHeroi <= 5000:
    print("O Herói" ,nomeDoHeroi, "está no nível de: Prata")
elif quantdXpHeroi >= 5001 and quantdXpHeroi <= 7000:
    print("O Herói" ,nomeDoHeroi, "está no nível de: Ouro")
elif quantdXpHeroi >= 7001 and quantdXpHeroi <= 8000:
    print("O Herói" ,nomeDoHeroi, "está no nível de: Platina")
elif quantdXpHeroi >=  8001 and quantdXpHeroi <= 9000:
    print("O Herói" ,nomeDoHeroi, "está no nível de: Ascendente")
elif quantdXpHeroi >= 9001 and quantdXpHeroi <= 10000:
    print("O Herói" ,nomeDoHeroi, "está no nível de: Imortal")
else: 
    print("Seu Herói está no nível de: Radiante")




