from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)  # Чтобы поле индексировалось и поиск шёл быстрее
    times_cooked = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    products = models.ManyToManyField(Product, through='RecipeProduct')

    def __str__(self):
        return self.name


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.IntegerField()

    class Meta:
        unique_together = ('recipe', 'product')  # Уникальность в полях recipe и product
