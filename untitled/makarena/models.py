from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField()
    email = models.CharField(default="", max_length=128)
    photo = models.ImageField(blank=True, null=True)


class Category(models.Model):
    category_name = models.CharField(primary_key=True, max_length=50, default="")

    def __str__(self):
        return str(self.category_name)


class Income(models.Model):
    date = models.DateField()
    value = models.FloatField()
    sender = models.CharField(max_length=50)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(default="")

    def __str__(self):
        return self.date_value_sender()

    def date_value_sender(self):
        return str(self.date) + str(self.value) + str(self.sender)


class Expense(models.Model):
    date = models.DateField()
    value = models.FloatField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(default="")

    def __str__(self):
        return self.date_value()

    def date_value(self):
        return str(self.date) + str(self.value)


class Fund(models.Model):
    sum_of_founds = models.FloatField()

    def sum(self):
        return self.sum_of_founds


class Balance(models.Model):
    money_balance = models.FloatField()

    # TODO: zaimplementować sum_income - sum_expense
    # TODO: zaimplementować sumowanie dodanych incomów i osobno expensów
