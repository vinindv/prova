Contagem = 0
Cont1 = 0 #Contagem Facebook
Cont2 = 0 #Contagem Instagram
Cont3 = 0 #Contagem Twitter
IdadeMaior1 = 0 #Pessoa mais velha que prefere facebook
IdadeMaior2 = 0 #Pessoa mais velha que prefere instagram 
IdadeMaior3 = 0 #pessoa mais velha que prefere twitter
IdadeMenor1 = 100 #Pessoa mais nova que prefere facebook
IdadeMenor2 = 100 #Pessoa mais nova que prefere instagram  
IdadeMenor3 = 100 #Pessoa mais nova que prefere twitter
ContM1 = 0
ContM2 = 0
ContM3 = 0
ContF1 = 0
ContF2 = 0
ContF3 = 0


while True:
    Contagem = Contagem + 1
    rede  = int(input("Qual rede voce prefere?(1-Facebook,2-Instagram,3-Twitter)"))
    Idade = int(input("Qual sua idade?"))
    Sexo = (input("Qual seu Sexo?(M-Masculino, F-Feminino)"))
    Refazer = input("Deseja refazer o formulário? (S , N)")

    if rede == 1:
        Cont1 = Cont1 + 1
    elif rede == 2:
        Cont2 = Cont2 + 1
    elif rede == 3:
        Cont3 = Cont3 + 1

    if rede == 1 and Idade > IdadeMaior1:
        IdadeMaior1 = Idade
    if rede == 2 and Idade > IdadeMaior2:
        IdadeMaior2 = Idade
    if rede == 3 and Idade > IdadeMaior1:
        IdadeMaior3 = Idade

    if rede == 1 and Idade < IdadeMenor1:
        IdadeMenor1 = Idade
    if rede == 2 and Idade < IdadeMenor2:
        IdadeMenor2 = Idade
    if rede == 3 and Idade < IdadeMenor3:
        IdadeMenor3 = Idade

    if Sexo == "M" and rede == 1:
        ContM1 = ContM1 + 1
    if Sexo == "M" and rede == 2:
        ContM2 = ContM2 + 1
    if Sexo == "M" and rede == 3:
        ContM3 = ContM3 + 1

    if Sexo == "F" and rede == 1:
        ContF1 = ContF1 + 1
    if Sexo == "F" and rede == 2:
        ContF2 = ContF2 + 1
    if Sexo == "F" and rede == 3:
        ContF3 = ContF3 + 1

    if Refazer == "N":
        break

if IdadeMenor1 == 1000:
    IdadeMenor1 = 0
if IdadeMenor2 == 1000:
    IdadeMenor2 = 0
if IdadeMenor3 == 1000:
    IdadeMenor3 = 0
# 1-
print("Total de respondentes foi de:",Contagem)
# 2-
Pergunta2 = (Cont1/Contagem) * 100
print(Pergunta2,"% das pessoas preferem facebook")
# 3-
Pergunta3 = (Cont2/Contagem) * 100
print(Pergunta3, "% das pessoas preferem instagram")
# 4-
Pergunta4 = (Cont3/Contagem) * 100
print(Pergunta4,"% das pessoas preferem twitter")
# 5-
print("Idade da pessoa mais velha que preferiu Facebook foi de:",IdadeMaior1," Anos")
# 6-
print("Idade da pessoa mais velha que preferiu Instagram foi de:",IdadeMaior2," Anos")
# 7-
print("Idade da pessoa mais velha que preferiu Twitter foi de:",IdadeMaior3," Anos")
# 8-
print("Idade da pessoa mais nova que prefiriu Facebook foi de:" ,IdadeMenor1 ," Anos")
# 9-
print("Idade da pessoa mais nova que prefiriu Instagram foi de:" ,IdadeMenor2 ," Anos")
# 10-
print("Idade da pessoa mais nova que prefiriu Twitter foi de:" ,IdadeMenor3 ," Anos")
# 11,13,15-
print("Quantidade de homens que escolheram Facebook:",ContM1," ,Instagram:",ContM2," e Twitter:",ContM3)
# 12,14,16-
print("Quantidade de mulheres que escolheram Facebook:",ContF1," ,Instagram:",ContF2," e Twitter:",ContF3)
