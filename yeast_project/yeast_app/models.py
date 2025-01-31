from django.db import models

class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()

class YeastBatch(models.Model):
    molasses_amount = models.FloatField()
    grain_starch_amount = models.FloatField()
    potato_starch_amount = models.FloatField()
    water = models.FloatField()
    nutrients_vitamins = models.FloatField()
    emulsifiers = models.FloatField()
    purity = models.FloatField()

