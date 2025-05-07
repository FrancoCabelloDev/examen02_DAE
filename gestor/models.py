from django.db import models

class Carpeta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    carpeta = models.ForeignKey(Carpeta, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Documento(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='documentos/')
    carpeta = models.ForeignKey(Carpeta, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre
