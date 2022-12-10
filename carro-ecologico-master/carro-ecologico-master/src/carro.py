class Carro:

    def __init__(self):
     self.combustivel = 0
     self.passageiros = 0
     self.quilometragem = 0

    def getPassageiros(self):
     self.passageiros = 0



    def getCombustivel(self):
        self.combustivel = 0



    def getQuilometragem(self):
        self.quilometragem = 0


    def embarcar(self):

     if self.passageiros >= 0 and self.passageiros < 2:
        self.passageiros += 1
        print("Um passageiro subui")
        return True
     else:
        return False



    def desembarcar(self):
        if self.passageiros > 0 and self.passageiros <= 2:
            self.passageiros -= 1
            print("Um passageiro desceu")
            return True
        else:
            return False


    def dirigir(self, distancia):
        if self.passageiros > 0 and self.combustivel > 0:
            self.quilometragem += 1
            if self.combustivel > distancia:
                self.combustivel -= distancia
                print("Você chegou ao seu destino:")
            else:
                print("Procure o posto mais próximo você precisa abastecer ")





    def abastecer(self, quantidade):
        if self.combustivel >= 0 and self.combustivel <= 100:
            self.combustivel += quantidade
            return True
        elif self.combustivel > 100:
            print("Tanque cheio")
            return False
