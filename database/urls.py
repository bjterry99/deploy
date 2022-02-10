from django.urls import path
from .views import indexPageView, recipeDisplayPageView, recipeSearchPageView, menuPageView, groceryPageView, shoppingAddView, menuItemAddView, menuItemAddRecipeView
from .views import shoppingDeleteView, groceryDeleteView, groceryDeleteAllView, menuDeleteAllView, menuItemDeleteView, menuItemDeleteHomeView, menuItemDeleteRecipeView, homePageView

urlpatterns = [
    path("recipedisplay/<recipeID>", recipeDisplayPageView, name="recipedisplay"),
    path("index/", recipeSearchPageView, name="recipesearch"),
    path("menu/", menuPageView, name="menu"),
    path("grocery/", groceryPageView, name="grocery"),
    path("groceryadd/", shoppingAddView, name="shoppingadd"),
    path("shoppingdelete/<itemID>", shoppingDeleteView, name="shoppingdelete"),
    path("grocerydelete/<itemID>", groceryDeleteView, name="grocerydelete"),
    path("grocerydeleteall/", groceryDeleteAllView, name="grocerydeleteall"),
    path("menudelete/", menuDeleteAllView, name="menudelete"),
    path("menuitemdelete/<menuID>/<recipeID>", menuItemDeleteView, name="menuitemdelete"),
    path("menuitemdeletehome/<recipeID>", menuItemDeleteHomeView, name="menuitemdeletehome"),
    path("menuitemdeleterecipe/<recipeID>", menuItemDeleteRecipeView, name="menuitemdeleterecipe"),
    path("menuitemadd/<recipeID>", menuItemAddView, name="menuitemadd"),
    path("menuitemaddrecipe/<recipeID>", menuItemAddRecipeView, name="menuitemaddrecipe"),
    path("home/", homePageView, name="home"),
    path("", indexPageView, name="index")
]