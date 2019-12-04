from django.db import models


# Create your models here.
class User(models.Model):

    value = models.FloatField()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField()


class Funds(models.Model):

    sum_of_founds = models.FloatField()


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
    category = models.IntegerField(default=0, choices=CATEGORIES)


class Income(models.Model):

    date = models.DateField()
    value = models.FloatField()
    sender = models.CharField(max_length=50)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)


class Expense(models.Model):

    date = models.DateField()
    value = models.FloatField()
    recipient = models.CharField(max_length=50)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
