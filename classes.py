class Roupas:
    tipo = "comercio"

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def description(self):
        return f"A marca da roupa é {self.marca} e o modelo é uma {self.modelo}"

class Aula:
    tipo = "universidade"
  
    def __init__(self,materia, sala):
      self.materia = materia
      self.sala =  sala
    def description(self):
      return f"A aula será de {self.materia} e será na sala {self.sala}"

class Carne:
    tipo: "carne"

    def __init__(self, corte, valor):
      self.corte = corte
      self.valor = valor
    def description(self):
      return f"O valor da {self.corte} é {self.valor} R$ o quilo"
      
