from django.contrib import admin
from .models import recipeClasses, ingredientClasses, times, recipes, ingredients, recipe_ingredients, tools, recipe_tools, menu, grocery, shopping

# Register your models here.
admin.site.register(recipeClasses)
admin.site.register(ingredientClasses)
admin.site.register(times)
admin.site.register(recipes)
admin.site.register(ingredients)
admin.site.register(recipe_ingredients)
admin.site.register(tools)
admin.site.register(recipe_tools)
admin.site.register(menu)
admin.site.register(grocery)
admin.site.register(shopping)