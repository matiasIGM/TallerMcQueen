from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name="Id de Categoria")
    nombreCategoria = models.CharField(max_length=50,verbose_name="Nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6,primary_key=True,verbose_name="Patente")
    marca = models.CharField(max_length=20,verbose_name="Marca Vehiculo")
    modelo = models.CharField(max_length=20,null= True,blank=True,verbose_name="Modelo")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.patente

class Usuarios(models.Model):
    idUsuario =models.CharField(max_length=20, primary_key=True, verbose_name="Id de Usuario" )
    nombre = models.CharField(max_length=30, verbose_name="nombre del usuario" )
    apellido = models.CharField(max_length=30, verbose_name="apellido del usuario" )
    email = models.CharField(max_length=40, verbose_name="email del usuario" )
    contraseña = models.CharField(max_length=20, verbose_name="contraseña del usuario" )

    def __str__(self):
        return self.idUsuario
    
class Carrusel(models.Model): 
    idCarrusel = models.CharField(max_length=20, primary_key=True, verbose_name="Id Carrusel" )
    enlaceImagen = models.CharField(max_length=50, verbose_name="Enlace de imagen" )
    titulo = models.CharField(max_length=30, verbose_name="Titulo del slide" )
    descripcion = models.CharField(max_length=150, verbose_name="Descripcion del slide" )
    clase = models.CharField(max_length=30, verbose_name="clase del slide" )



    def __str__(self):
        return self.idCarrusel


class Mecanicos(models.Model): 
    idMecanico = models.CharField(max_length=20, primary_key=True, verbose_name="Id de Usuario")
    nombreMecanico = models.CharField(max_length=20, verbose_name="Nombre del mecanico")
    apellidoMecanico = models.CharField(max_length=20, verbose_name="Apellido del mecanico")
    experiencia = models.IntegerField(null=True, verbose_name="Experiencia del mecanico")
    edad = models.IntegerField(verbose_name="Edad del mecanico")
    especialidad = models.CharField(max_length=40, verbose_name="Especialidad del mecanico")
    imagenMecanico = models.CharField(max_length=40, verbose_name="Imagen del mecanico")

    def __str__(self):
        return self.idMecanico





   
   