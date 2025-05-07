from django.db import models

class Lista(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    PRIORIDAD_CHOICES = (
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    )

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    fecha_limite = models.DateField(null=True, blank=True)
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='media')
    lista = models.ForeignKey(Lista, related_name='tareas', on_delete=models.CASCADE)

    etiquetas = models.ManyToManyField(Etiqueta, through='TareaEtiqueta', related_name='tareas')

    def __str__(self):
        return self.titulo

class TareaEtiqueta(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tarea', 'etiqueta')