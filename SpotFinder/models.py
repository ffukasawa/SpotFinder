from django.db import models

class carro (models.Model):
    
        modelo = models.CharField (max_length=100),
        marca = models.CharField (max_length=100),
        ano = models.IntegerField(), 
        placa = models.CharField (max_length=7),
        codigovenda = models.IntegerField()

        def __iter__(self):
             return f"{self.modelo} - {self.marca} - {self.ano} - {self.placa} - {self.codigovenda}"

class Rua(models.Model):
      numVagas = models.IntegerField()

      def __iter__(self):
             return f"{self.numVagas}"


class Pessoa (models.Model):
    nome=models.CharField(max_length=120),
    telefone=models.IntegerField(max_length=11),
    email=models.CharField(max_length=100)
    def _iter_(self):
        return f"{self.nome}-{self.telefone}-{self.email}"

        
class Vaga (models.Model):
    localizacao=models.CharField(max_length=100),
    id=models.CharField(max_length=30),
    tamanho=models.CharField(max_length=10),
    def _iter_(self):
        return f"{self.localizacao}-{self.id}-{self.tamanho}"
