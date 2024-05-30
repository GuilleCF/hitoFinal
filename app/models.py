from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comuna(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, related_name="comunas", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class User(AbstractUser):

    TIPO_USUARIO_CHOICES = [
        ("arrendatario", "Arrendatario"),
        ("arrendador", "Arrendador")
    ]
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Change 'custom_user_set' to whatever you prefer
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set_permissions',  # Change 'custom_user_set_permissions' to whatever you prefer
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    rut = models.CharField(max_length=10, unique=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    tipo_usuario = models.CharField(max_length=50, choices=TIPO_USUARIO_CHOICES, null=False, blank=False)

    def __str__(self):
        return f'{self.name} {self.last_name}'
    
class Property(models.Model):

    TYPE_CHOICES = [
        ("departamento", "Departamento"),
        ("casa", "Casa"),
        ("oficina", "Oficina"),
        ("local", "Local")
    ]
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    m2_build = models.FloatField(null=False, blank=False)
    m2_land = models.FloatField(null=False, blank=False)
    n_parking = models.IntegerField(null=False, blank=False)
    n_rooms = models.IntegerField(null=False, blank=False)
    n_bathrooms = models.IntegerField(null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    comuna = models.CharField(max_length=50, null=False, blank=False)
    type_property = models.CharField(max_length=50, choices=TYPE_CHOICES, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")

    def __str__(self):
        return self.name
    
class Solicitude(models.Model):

    STATUS_CHOICES = [
        ("pendiente", "Pendiente"),
        ("aceptada", "Aceptada"), 
        ("rechazada", "Rechazada")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="solicitudes")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="solicitudes")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Solicitud de {self.user.name} por {self.user.last_name} para {self.property.name}'



