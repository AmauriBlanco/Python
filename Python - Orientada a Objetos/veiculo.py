class Veiculo():
    """Essa é a classe carro. Esta classe é utilizada para instaciar novos carros em nosso programa"""
    def __init__(self, cor,  tipo_combustivel, potencia):
        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0
        self.is_ligado = False
        self.velocidade = 0
    def __del__(self):
        print("O objeto foi removido da memória! ")

    def abastecer(self, qtd_combustivel):
        """ O método abastecer recebe como parâmetro a quantidade de combustível e incrementa no atributo qtd_combustivel no objeto carro"""
        self.qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.is_ligado:
            print("O veículo ja está ligado")
        else:
            self.is_ligado = True
            print("O veículo foi ligado!")

    def desligar(self):
        if self.is_ligado == False:
            print("O veículo ja está desligado")
        else:
            self.is_ligado = False

    def acelerar(self, velocidade=10):
        if self.is_ligado:
            self.velocidade += velocidade
        else:
            print("O veículo precisa estar ligado !")