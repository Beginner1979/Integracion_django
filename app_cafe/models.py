from django.db import models

class Cafe(models.Model):

    nombre  = models.CharField(max_length=200)
    rating  = models.PositiveSmallIntegerField(blank=False,null=False)
    abv     = models.FloatField(blank=True, null=True)


    def __str__(self):
        return f"El cafe: {self.nombre}, Rating {self.abv}"

    def obtner_campos_valores(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
