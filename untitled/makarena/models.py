from django.db import models


# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField()
    email = models.CharField(default="", max_length=128)
    photo = models.ImageField(null=True)


class Fund(models.Model):

    sum_of_founds = models.DecimalField(max_digits=20, decimal_places=4)

    def sum(self):
        return self.sum_of_founds


class Category(models.Model):

    CATEGORIES = {
        (0, 'Unexpected'),
        (1, 'Car'),
        (2, 'Shopping'),
        (3, 'Hobbies'),
        (4, 'Technologies'),
        (5, 'Family'),
        (6, 'Education'),
        (7, 'House')
    }
    category = models.CharField(max_length=128, default=0, choices=CATEGORIES)


class Income(models.Model):

    date = models.DateField()
    value = models.FloatField()
    sender = models.CharField(max_length=50)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    description = models.TextField(default="")

    def __str__(self):
        return self.date_value_sender()

    def date_value_sender(self):
        return str(self.date) + str(self.value) + str(self.sender)


class Expense(models.Model):

    date = models.DateField()
    value = models.FloatField()
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    description = models.TextField(default="")

    def __str__(self):
        return self.date_value()

    def date_value(self):
        return str(self.date) + str(self.value)
