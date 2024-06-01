from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Contact)

    def __str__(self):
        return self.name


class MarketingPorCorreo(models.Model):
    cuerpoDelCorreo = models.TextField()
    tipoCorreo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipoCorreo

class MarketingPorCorreoPersonal(MarketingPorCorreo):
    emailDeDestino = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.emailDeDestino.email} - {self.tipoCorreo}"


