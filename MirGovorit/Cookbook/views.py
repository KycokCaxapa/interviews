from django.shortcuts import HttpResponse, render
from django.shortcuts import get_object_or_404
from .models import *


def add_product_to_recipe(request, recipe_id, product_id, weight):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)

    RecipeProduct.objects.update_or_create(
        recipe=recipe,
        product=product,
        defaults={'weight': weight},
    )

    return HttpResponse(status=204)


def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    for rp in recipe.recipeproduct_set.all():
        rp.product.times_cooked += 1
        rp.product.save()

    return HttpResponse(status=204)


def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    recipes = Recipe.objects.exclude(
        id__in=Recipe.objects.filter(
            recipeproduct__product=product,
            recipeproduct__weight__gte=10,
        ).values_list('id', flat=True),
    )

    context = {'recipes': recipes,
               'product': product,
               }

    return render(request, 'Cookbook/recipes_without_product.html', context=context)
