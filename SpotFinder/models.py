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


