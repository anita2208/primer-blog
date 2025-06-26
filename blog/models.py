from django.conf import settings
from django.db import models
from django.utils import timezone
class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    hora_creacion = models.DateTimeField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Fotografía(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=200, default='ejemplo: Buenos Aires, Argentina')
    fallecimiento = models.DateField(blank=True, null=True)
    edad = models.IntegerField(default='ejemplo 30, o edad de fallecimiento')
    nacionalidad = models.CharField(max_length=100, default='ejemplo: Argentina')
    ocupación = models.CharField(max_length=100,default='ejemplo: Fotógrafo, Artista, etc.')
    nombre_artístico = models.CharField(max_length=200)
    tipo_de_fotografía_o_movimiento = models.CharField(max_length=200)
    estilo = models.CharField(max_length=200, default='por ejemplos, retratos,paisajes,etc.')
    características = models.TextField()
    tecnicas = models.TextField()
    exposiciones = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    hora_creacion = models.DateTimeField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='imagenes_publicaciones/', null=True, blank=True)
    nombre_imagen = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.nombre
