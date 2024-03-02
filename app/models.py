from django.db import models

# Create your models here.
class Evento(models.Model):
    """ Modelo de la tabla eventos"""
    id= models.AutoField(primary_key=True) #Campo autoincremental, llave primaria y clave foránea a
    nombre = models.CharField(max_length=100, verbose_name="Nombre") # Campo para el nombre del evento
    imagen = models.ImageField(upload_to="imagenes/", verbose_name="Imagen", null=True)  # Campo para subir
    descripcion = models.TextField(verbose_name="Descripcion", null=True)              # Campo para descripcion larga
    
    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Descripcion: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        
    class Meta:
        db_table = 'evento'
       
       