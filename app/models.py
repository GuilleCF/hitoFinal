from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):

    TIPO_USUARIO_CHOICES = [("arrendatario", "Arrendatario"), ("arrendador", "Arrendador")]
    rut = models.CharField(max_length="10", unique=True, null=False, blank=False)
    name = models.CharField(max_length="50", null=False, blank=False)
    last_name = models.CharField(max_length="50", null=False, blank=False)
    address = models.CharField(max_length="100", null=False, blank=False)
    phone = models.CharField(max_length="12", null=False, blank=False)
    tipo_usuario = models.CharField(max_length=50, choices=TIPO_USUARIO_CHOICES, null=False, blank=False)
    
class Property(models.Model):

    TYPE_CHOICES = [("departamento", "Departamento"), ("casa", "Casa"), ("oficina", "Oficina"), ("local", "Local")]
    name = models.CharField(max_length="50")
    description = models.TextField(null=True, blank=True)
    m2_build = models.FloatField(null=False, blank=False)
    m2_land = models.FloatField(null=False, blank=False)
    n_parking = models.IntegerField(null=False, blank=False)
    n_rooms = models.IntegerField(null=False, blank=False)
    n_bathrooms = models.IntegerField(null=False, blank=False)
    address = models.CharField(max_length="100", null=False, blank=False)
    comuna = models.CharField(max_length="50", null=False, blank=False)
    type_property = models.CharField(max_length=50, choices=TYPE_CHOICES, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    




