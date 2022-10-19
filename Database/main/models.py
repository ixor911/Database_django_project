from django.db import models
import pandas as pd


class Type(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField('name', max_length=30)
    regexValidator = models.CharField('RegexValidator', max_length=50)


# class Column(models):
#    name = models.CharField('Name', max_length=30)
#    type = models.ForeignKey(Type, on_delete=models.CASCADE)


# class Row(models):
#    name = pd.


class Table(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField('Name', max_length=30)
    data = pd.DataFrame()


class Database(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField('Name', max_length=30)

    tables = models.ManyToManyField(Table, blank=True)
