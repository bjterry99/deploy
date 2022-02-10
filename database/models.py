from django.db import models

class recipeClasses(models.Model) :
    rc_id = models.AutoField(primary_key=True)
    classname = models.CharField(max_length=20, default="default", verbose_name="Recipe Class Name")

    class Meta:
        db_table = 'recipeclasses'

    def __str__(self) :
        return (self.classname)

class ingredientClasses(models.Model) :
    ic_id = models.AutoField(primary_key=True)
    iclassname = models.CharField(max_length=20, default="default", verbose_name="Ingredient Class Name")

    class Meta:
        db_table = 'ingredientclasses'

    def __str__(self) :
        return (self.iclassname)

class times(models.Model) :
    time_id = models.AutoField(primary_key=True)
    length = models.FloatField(default=0.00)
    attribute = models.CharField(max_length=10)

    class Meta:
        db_table = 'times'

    def __str__(self) :
        return (str(self.length) + ' ' + str(self.attribute))

class recipes(models.Model) :
    recipe_id = models.AutoField(primary_key=True)
    recipename = models.CharField(max_length=30)
    instructions = models.CharField(max_length=3000)
    image = models.ImageField(upload_to = 'photos', default="photos/none.png", blank=True)
    rclassid = models.ForeignKey(recipeClasses, default = "", blank=True, verbose_name="Recipe-Class ID", related_name = 'rClassID', on_delete=models.DO_NOTHING, to_field='rc_id')
    cooktimeid = models.ForeignKey(times, blank=True, default = "", verbose_name="Cook Time ID", related_name = 'cookTimeID', on_delete=models.DO_NOTHING, to_field='time_id')

    class Meta:
        db_table = 'recipes'

    def __str__(self) :
        return (self.recipename)

class ingredients(models.Model) :
    i_id = models.AutoField(primary_key=True)
    iname = models.CharField(max_length=30, default="default", verbose_name="Ingredient Name")
    icost = models.FloatField(default=0.00, blank=True, verbose_name="Cost")
    iclassid = models.ForeignKey(ingredientClasses, default = "", blank=True, verbose_name="Ingredient-Class ID", related_name = 'iClassID', on_delete=models.DO_NOTHING, to_field='ic_id')

    class Meta:
        db_table = 'ingredients'

    def __str__(self) :
        return (self.iname)

class recipe_ingredients(models.Model) :
    ri_id = models.AutoField(primary_key=True)
    iid = models.ForeignKey(ingredients, models.DO_NOTHING, default="default", verbose_name="Ingredient")
    recipeid = models.ForeignKey(recipes, models.DO_NOTHING, default="default", verbose_name="Recipe")
    measurement = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'recipe_ingredients'
        #unique_together = (('recipes', 'ingredients'),)

    def __str__(self) :
        return (str(self.recipeid) + ' - ' + str(self.iid))

class tools(models.Model) :
    tool_id = models.AutoField(primary_key=True)
    toolname = models.CharField(max_length=20)

    class Meta:
        db_table = 'tools'

    def __str__(self) :
        return (self.toolname)

class recipe_tools(models.Model) :
    rt_id = models.AutoField(primary_key=True)
    toolid = models.ForeignKey(tools, models.DO_NOTHING, default="default", verbose_name="Tool Name")
    recipeid = models.ForeignKey(recipes, models.DO_NOTHING, default="default", verbose_name="Recipe Name")

    class Meta:
        db_table = 'recipe_tools'
        #unique_together = (('recipes', 'tools'),)

    def __str__(self) :
        return (str(self.recipeid) + ' - ' + str(self.toolid))

class menu(models.Model) :
    menu_id = models.AutoField(primary_key=True)
    recipeid = models.ForeignKey(recipes, blank=True, default = "", verbose_name="Recipe ID", related_name = 'recipeID', on_delete=models.DO_NOTHING, to_field='recipe_id')

    class Meta:
        db_table = 'menu'

    def __str__(self) :
        return (str(self.recipeid))

class grocery(models.Model) :
    grocery_id = models.AutoField(primary_key=True)
    iid = models.ForeignKey(recipe_ingredients, blank=True, default = "", verbose_name="Ingredient ID", related_name = 'iID', on_delete=models.DO_NOTHING, to_field='ri_id')

    class Meta:
        db_table = 'grocery'

    def __str__(self) :
        return (str(self.iid))

class shopping(models.Model) :
    shopping_id = models.AutoField(primary_key=True)
    itemname = models.CharField(max_length=100, default="default", verbose_name="Item Name")
    quantity = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'shopping'

    def __str__(self) :
        return (self.itemname)
