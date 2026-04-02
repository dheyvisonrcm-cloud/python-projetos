

print ("conta de energia")
resposta = input ("vamos lá? digite sim para começar e não para sair:").lower()
if resposta == "sim":
    try:
     consumo = float(input("digite a quantidade de kWh consumida:"))
     if consumo <= 0:
        print ("o consumo deve ser maior que zero")
        consumo = float(input ("digite a quantidade de kWh consumida:"))
        while True:
            if consumo <= 0:
                print ("o consumo deve ser maior que zero")
                consumo = float(input ("digite a quantidade de kWh consumida:"))
                continue
     elif consumo > 0:
        pass
    except ValueError:
        print ("entrada inválida, por favor digite um número.")
        while True:    
            try:
                consumo = float(input("digite a quantidade de kWh consumida:"))
                if consumo <= 0:
                    print ("o consumo deve ser maior que zero")
                    continue
                else:
                    break
            except ValueError:
                print ("entrada inválida, por favor digite um número.")
                continue

    conta_base = consumo * 0.6

    resposta = input("qual a sua bandeira?").lower()
    if resposta == "verde":
        print ("sua conta é: R$ ", conta_base)
    elif resposta == "amarela":
        conta_amarela = conta_base + (0.02 * consumo)
        print ("sua conta é: R$ ", conta_amarela)
    elif resposta == "vermelha":
        conta_vermelha = conta_base + (0.05 * consumo)
        print ("sua conta é: R$ ", conta_vermelha)


    else:
        resposta = input("bandeira inválida, por favor digite verde, amarela ou vermelha.")
        if resposta == "verde" or resposta == "amarela" or resposta == "vermelha":
            if resposta == "verde":
                print ("sua conta é: R$ ", conta_base)
            elif resposta == "amarela":
                conta_amarela = conta_base + (0.02 * consumo)
                print ("sua conta é: R$ ", conta_amarela)
            elif resposta == "vermelha":
                conta_vermelha = conta_base + (0.05 * consumo)
                print ("sua conta é: R$ ", conta_vermelha)
        else:
            resposta = input("gostaria de realizar um novo cálculo? digite sim para continuar ou não para sair:")
            if resposta == "sim":
                while True:
                    consumo = float(input("digite a quantidade de kWh consumida:"))
                    if consumo <= 0:
                        print ("o consumo deve ser maior que zero")
                        continue
                    else:
                        break

elif resposta == "não":
    print ("ok, adeus")
elif resposta != "sim" and resposta != "não":
    resposta = input("resposta inválida, por favor digite sim ou não:")
    if resposta == "sim":
        while True:
            consumo = float(input("digite a quantidade de kWh consumida:"))
            if consumo <= 0:
                print ("o consumo deve ser maior que zero")
                continue
            else:
                break
    elif resposta == "não":
        print ("ok, adeus")
    