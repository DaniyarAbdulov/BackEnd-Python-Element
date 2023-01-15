from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField(max_length=250, default=0)
    description = models.TextField(blank=True)
    amount = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f'{self.category}: {self.name}'


