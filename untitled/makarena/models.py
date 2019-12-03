from django.db import models


# Create your models here.
class Expenditure(models.Model):

    value = models.FloatField()
    date = models.DateField()
    category = models.CharField(max_length = 50)


class Meta:
    db_table = "Wallet"
