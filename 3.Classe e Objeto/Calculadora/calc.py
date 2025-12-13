class Calculadora:
    def soma(self, a, b):
        self.a =a
        self.b = b
        resultado = self.a + self.b
        print(f"O resultado da soma é: {resultado}")
    
    def subtracao(self, a, b):
        self.a =a
        self.b = b
        resultado = self.a - self.b
        print(f"O resultado da subtração é: {resultado}")
        
    def multiplicacao(self, a, b):
        self.a =a
        self.b = b
        resultado = self.a * self.b
        print(f"O resultado da multiplicação é: {resultado}")
        
    def divisao(self, a, b):
        self.a =a
        self.b = b
        if self.b != 0:
            resultado = self.a / self.b
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")