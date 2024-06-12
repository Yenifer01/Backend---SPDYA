from django.db import models

# Create your models here.
class Alimentos(models.Model):
    id_alimento = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    nombre= models.CharField(max_length=100)
    grupo= models.CharField(max_length=10)
    energia_kcal = models.IntegerField(default=0)
    energia_kj = models.IntegerField(default=0)
    agua_g = models.DecimalField(max_digits=6,decimal_places=2)
    proteinas_totales_g = models.DecimalField(max_digits=6,decimal_places=2)
    proteinas_vegetales_g = models.DecimalField(max_digits=6,decimal_places=2)
    proteinas_animal = models.DecimalField(max_digits=6,decimal_places=2)
    grasa_total_g = models.DecimalField(max_digits=6,decimal_places=2)
    carbohidratos_totales_g = models.DecimalField(max_digits=6,decimal_places=2)
    carbohidratos_disponibles_g= models.DecimalField(max_digits=6,decimal_places=2)
    fibra_dietaria_g = models.DecimalField(max_digits=6,decimal_places=2)
    cenizas_g = models.DecimalField(max_digits=6,decimal_places=2)
    calcio_mg = models.IntegerField(default=0)
    fosforo_mg = models.IntegerField(default=0)
    zinc_mg = models.DecimalField(max_digits=6,decimal_places=2)
    hierro_mg = models.DecimalField(max_digits=6,decimal_places=2)
    caroteno_equivalentes_totales_ug =models.IntegerField(default=0)
    vitaminaA_equivalentes_totales_ug =models.IntegerField(default=0)
    tiamina_mg = models.DecimalField(max_digits=6,decimal_places=2)
    riboflavina_mg = models.DecimalField(max_digits=6,decimal_places=2)
    niacina_mg = models.DecimalField(max_digits=6,decimal_places=2)
    vitaminaC_mg = models.DecimalField(max_digits=6,decimal_places=2)
    acido_folico_ug = models.IntegerField(default=0)
    sodio_mg = models.IntegerField(default=0)
    potasio_mg = models.IntegerField(default=0)
    def __str__(self):
            return self.nombre
    
    class Meta:
        verbose_name_plural = "Alimentos"