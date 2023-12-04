from django.contrib import admin
from .models import Allergies, Ingredients, IngredientsPairs, Recipes, Profiles

admin.site.register(Allergies)
admin.site.register(Ingredients)
admin.site.register(IngredientsPairs)
admin.site.register(Recipes)
admin.site.register(Profiles)