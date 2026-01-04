from django.db import models

class DrinkCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(
        DrinkCategory,
        on_delete=models.CASCADE,
        related_name="drinks"
    )
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
