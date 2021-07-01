import carro,moto

print("Uno Vermelho")
uno_vermelho = carro.Carro("vermelho", "Flex", 1.0, 4)
uno_vermelho.ligar()
uno_vermelho.abastecer(25)
print(f"A quandotidade de combustível do uno vermelhor  é: {uno_vermelho.qtd_combustivel}")
uno_vermelho.acelerar()
print(f"A valocidade atual do uno vermelhor é de {uno_vermelho.velocidade}Km/h")

moto_vermelha = moto.Moto('Vermelha', 'Gasolina',1.0,2)
moto_vermelha.ligar()
moto_vermelha.abastecer(30)
moto_vermelha.abastecer(10)
print(moto_vermelha.is_ligado)
print(moto_vermelha.qtd_combustivel)