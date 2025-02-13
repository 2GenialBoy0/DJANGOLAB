from django.db import models

from django.db import models

class Tipo(models.Model):
    TIPOS_PROYECTO = [
        ('Desarrollo Web', 'Desarrollo Web'),
        ('Aplicación Móvil', 'Aplicación Móvil'),
        ('Software Empresarial', 'Software Empresarial'),
        ('IA & Machine Learning', 'IA & Machine Learning'),
        ('Ciberseguridad', 'Ciberseguridad'),
    ]

    nombre = models.CharField(max_length=100, choices=TIPOS_PROYECTO, default='Desarrollo Web')

    def __str__(self):
        return self.nombre


class Herramienta(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='herramientas/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Detalle(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    herramienta = models.ForeignKey(Herramienta, on_delete=models.CASCADE)
