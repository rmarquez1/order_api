from django.db import models

# Create your models here.
class Menu(models.Model):
    description = models.CharField(max_length=100)
    price = models.FloatField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.description + ' - ' + str(self.price)

    def __unicode__(self):
        return self.description + ' - ' + str(self.price)
