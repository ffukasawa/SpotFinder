from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.IntegerField(max_length=11),
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    placa = models.CharField(max_length=10)
    codigo_venda = models.CharField(max_length=50, blank=True, null=True)
    proprietario = models.ForeignKey(
        Pessoa, on_delete=models.SET_NULL, null=True, blank=True, related_name='carros'
    )

    def __str__(self):
        return f"{self.modelo} - {self.placa}"


class Rua(models.Model):
    nome = models.CharField(max_length=100)
    num_vagas = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    localizacao = models.CharField(max_length=100)
    id_vaga = models.CharField(max_length=30)
    tamanho = models.CharField(max_length=10)
    rua = models.ForeignKey(Rua, on_delete=models.CASCADE, related_name='vagas')

    def __str__(self):
        return f"Vaga {self.id_vaga} - {self.localizacao}"


class Estacionamento(models.Model):
    carro = models.OneToOneField(Carro, on_delete=models.CASCADE, related_name='estacionamento', null=True, blank=True)
    vaga = models.OneToOneField(Vaga, on_delete=models.CASCADE, related_name='estacionamento', null=True, blank=True)
    hora = models.TimeField()
    data = models.DateField()

    def __str__(self):
        return f"Carro: {self.carro}, Vaga: {self.vaga}, Data: {self.data}, Hora: {self.hora}"
