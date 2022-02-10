from xml.dom.minidom import Document
from django.shortcuts import redirect, render
from database.models import recipeClasses, ingredientClasses, times, recipes, ingredients, recipe_ingredients, tools, recipe_tools, menu, grocery, shopping

def indexPageView(request) :
    ingredient_data = ingredients.objects.all()
    menu_data = menu.objects.all()

    mainq = "select r.recipe_id, r.recipename, r.image from recipes r, recipeclasses rc where rc.rc_id = r.rclassid_id and rc.rc_id = 1 order by r.recipename"
    sideq = "select r.recipe_id, r.recipename, r.image from recipes r, recipeclasses rc where rc.rc_id = r.rclassid_id and rc.rc_id = 4 order by r.recipename"
    dessertq = "select r.recipe_id, r.recipename, r.image from recipes r, recipeclasses rc where rc.rc_id = r.rclassid_id and rc.rc_id = 5 order by r.recipename"

    main_data = recipes.objects.raw(mainq)
    side_data = recipes.objects.raw(sideq)
    dessert_data = recipes.objects.raw(dessertq)

    list = []
    for recipe in menu_data :
        list.append(recipe.recipeid)

    context = {
        "main" : main_data,
        "side" : side_data,
        "dessert" : dessert_data,
        "ingredients" : ingredient_data,
        "menu" : list
    }

    # return render(request, 'database/index.html', context)
    return redirect('../home')

def homePageView(request) :
    ingredient_data = ingredients.objects.all()
    menu_data = menu.objects.all()

    mainq = "select r.recipe_id, r.recipename, r.image from recipes r, recipeclasses rc where rc.rc_id = r.rclassid_id and rc.rc_id = 1 order by r.recipename"
    sideq = "select r.recipe_id, r.recipename, r.image from recipes r, recipeclasses rc where rc.rc_id = r.rclassid_id and rc.rc_id = 4 order by r.recipename"
    dessertq = "select r.recipe_id, r.recipename, r.image from recipes r, recipeclasses rc where rc.rc_id = r.rclassid_id and rc.rc_id = 5 order by r.recipename"

    main_data = recipes.objects.raw(mainq)
    side_data = recipes.objects.raw(sideq)
    dessert_data = recipes.objects.raw(dessertq)

    list = []
    for recipe in menu_data :
        list.append(recipe.recipeid)

    context = {
        "main" : main_data,
        "side" : side_data,
        "dessert" : dessert_data,
        "ingredients" : ingredient_data,
        "menu" : list
    }

    return render(request, 'database/index.html', context)
    # return redirect('/index')

def recipeSearchPageView(request) :
    if request.method == 'POST':
        menu_data = menu.objects.all()

        ingredient_data = ingredients.objects.all()
        data = recipes.objects.all()

        ingredient = request.POST['ingredient']
        ingredient2 = request.POST['ingredient2']
        ingredient3 = request.POST['ingredient3']
        name_contains = request.POST['name_contains']
        egg = 0

        if name_contains != '' :
            data = data.filter(recipename__icontains=name_contains)

        # first field only
        if (ingredient != '') & (ingredient2 == '') & (ingredient3 == '') :
            i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname = '"
            i_sql += ingredient + "'"

            i_recipe = recipes.objects.raw(i_sql)
            list = []

            for id in i_recipe :
                list.append(id.recipe_id)

            data = data.filter(recipe_id__in=list)

        # second only
        if (ingredient == '') & (ingredient2 != '') & (ingredient3 == '') :
            i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname = '"
            i_sql += ingredient2 + "'"

            i_recipe = recipes.objects.raw(i_sql)
            list = []

            for id in i_recipe :
                list.append(id.recipe_id)

            data = data.filter(recipe_id__in=list)

        # third only
        if (ingredient == '') & (ingredient2 == '') & (ingredient3 != '') :
            i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname = '"
            i_sql += ingredient3 + "'"

            i_recipe = recipes.objects.raw(i_sql)
            list = []

            for id in i_recipe :
                list.append(id.recipe_id)

            data = data.filter(recipe_id__in=list)

        # one and two
        if (ingredient != '') & (ingredient2 != '') & (ingredient3 == '') :
            i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname in ('"
            i_sql += ingredient + "', '"
            i_sql += ingredient2 + "') group by r.recipe_id having count(*) = 2"

            i_recipe = recipes.objects.raw(i_sql)
            list = []

            for id in i_recipe :
                list.append(id.recipe_id)

            data = data.filter(recipe_id__in=list)   

        # one and three
        if (ingredient != '') & (ingredient2 == '') & (ingredient3 != '') :
            i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname in ('"
            i_sql += ingredient + "', '"
            i_sql += ingredient3 + "') group by r.recipe_id having count(*) = 2"

            i_recipe = recipes.objects.raw(i_sql)
            list = []

            for id in i_recipe :
                list.append(id.recipe_id)

            data = data.filter(recipe_id__in=list) 

        # two and three
        if (ingredient == '') & (ingredient2 != '') & (ingredient3 != '') :
            i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname in ('"
            i_sql += ingredient2 + "', '"
            i_sql += ingredient3 + "') group by r.recipe_id having count(*) = 2"

            i_recipe = recipes.objects.raw(i_sql)
            list = []

            for id in i_recipe :
                list.append(id.recipe_id)

            data = data.filter(recipe_id__in=list)

        # all three
        if (ingredient != '') & (ingredient2 != '') & (ingredient3 != '') :
            i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname in ('"
            i_sql += ingredient + "', '"
            i_sql += ingredient2 + "', '"
            i_sql += ingredient3 + "') group by r.recipe_id having count(*) = 3"

            i_recipe = recipes.objects.raw(i_sql)
            list = []

            for id in i_recipe :
                list.append(id.recipe_id)

            data = data.filter(recipe_id__in=list)     

        #easter egg
        if (name_contains == "Abbey") or (name_contains== "abbey") :
            egg = 1

        data = data.order_by('recipename')
        main_data = data.filter(rclassid=1)
        side_data = data.filter(rclassid=4)
        dessert_data = data.filter(rclassid=5)

        list = []
        for recipe in menu_data :
            list.append(recipe.recipeid)

        context = {
            "main" : main_data,
            "side" : side_data,
            "dessert" : dessert_data,
            "ingredients" : ingredient_data,
            "ingredient" : ingredient,
            "ingredient3" : ingredient3,
            "ingredient2" : ingredient2,
            "name" : name_contains,
            "egg" : egg,
            "menu":list
        }

        return render(request, 'database/index.html', context)

    else :
        return redirect('../')

def recipeDisplayPageView(request, recipeID) :
    recipe_data = recipes.objects.get(recipe_id = recipeID)
    menu_data = menu.objects.all()

    query = "select i.i_id, i.iname, i.icost, i.iclassid_id, ri.measurement from ingredients i, recipe_ingredients ri where i.i_id = ri.iid_id and ri.recipeid_id = "
    query += recipeID

    tquery = "select t.time_id, t.length, t.attribute from times t, recipes r where t.time_id = r.cooktimeid_id and r.recipe_id = "
    tquery += recipeID

    toolq = "select t.tool_id, t.toolname from tools t, recipes r, recipe_tools rt where t.tool_id = rt.toolid_id and r.recipe_id = rt.recipeid_id and r.recipe_id = "
    toolq += recipeID

    ingredient_data = ingredients.objects.raw(query)
    time_data = times.objects.raw(tquery)
    tool_data = tools.objects.raw(toolq)

    list = []
    for recipe in menu_data :
        list.append(recipe.recipeid)

    context = {
        "recipe" : recipe_data,
        "ingredients" : ingredient_data,
        "time" : time_data,
        "tools" : tool_data,
        "menu" : list
    }

    return render(request, 'database/recipedisplay.html', context)

def menuPageView(request) :
    menuq = "select m.menu_ID, r.recipe_id, r.recipename, r.image from recipes r, menu m where m.recipeid_id = r.recipe_id"

    menu_data = recipes.objects.raw(menuq)

    context = {
        "menu" : menu_data
    }

    return render(request, 'database/menu.html', context)

def groceryPageView(request) :
    groceryq = "select g.grocery_id, r.recipe_id, ri.measurement, i.iname, r.recipename from ingredients i, recipe_ingredients ri, grocery g, recipes r where i.i_id = ri.iid_id and g.iid_id = ri.ri_id and r.recipe_id = ri.recipeid_id order by i.iname"

    grocery_data = grocery.objects.raw(groceryq)
    shopping_data = shopping.objects.all()

    context = {
        "grocery" : grocery_data,
        "shopping" : shopping_data
    }

    return render(request, 'database/grocery.html', context)

def shoppingAddView(request) :
    if request.method == 'POST':
        new_item = shopping()

        new_item.itemname = request.POST.get('item')
        new_item.quantity = request.POST.get('amount')

        if request.POST.get('item') != '' :
            new_item.save()

    return redirect('../grocery/')

def shoppingDeleteView(request, itemID) :
    item = shopping.objects.get(shopping_id = itemID)
    item.delete()

    return redirect('../grocery/')

def groceryDeleteView(request, itemID) :
    item = grocery.objects.get(grocery_id = itemID)
    item.delete()

    return redirect('../grocery/')

def groceryDeleteAllView(request) :
    for item in grocery.objects.all() :
        item.delete()
    for item in shopping.objects.all() :
        item.delete()

    return redirect('../grocery/')

def menuDeleteAllView(request) :
    for item in grocery.objects.all() :
        item.delete()
    for item in menu.objects.all() :
        item.delete()

    return redirect('../menu/')

def menuItemDeleteView(request, menuID, recipeID) :
    item = menu.objects.get(menu_id = menuID)
    item.delete()

    ri_data = recipe_ingredients.objects.filter(recipeid_id=recipeID)
    grocery_data = grocery.objects.all()
    list = []
    for item in ri_data :
        list.append(item.ri_id)

    for item in grocery_data :
        if item.iid_id in list :
            item.delete()

    return redirect('../../menu/')

def menuItemDeleteHomeView(request, recipeID) :
    if request.method == 'POST' :
        item = menu.objects.get(recipeid_id = recipeID)
        item.delete()

        ri_data = recipe_ingredients.objects.filter(recipeid_id=recipeID)
        grocery_data = grocery.objects.all()
        list = []
        for item in ri_data :
            list.append(item.ri_id)

        for item in grocery_data :
            if item.iid_id in list :
                item.delete()

        menu_data = menu.objects.all()

        ingredient_data = ingredients.objects.all()
        data = recipes.objects.all()

        ingredient = request.POST['ingredient_2']
        ingredient2 = request.POST['ingredient2_2']
        ingredient3 = request.POST['ingredient3_2']
        name_contains = request.POST['name_contains_2']
        egg = 0

        if name_contains != '' :
            data = data.filter(recipename__icontains=name_contains)

        # first field only
        if (ingredient != '') & (ingredient2 == '') & (ingredient3 == '') :
            i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname = '"
            i_sql += ingredient + "'"

            i_recipe = recipes.objects.raw(i_sql)
            list = []

            for id in i_recipe :
                list.append(id.recipe_id)

            data = data.filter(recipe_id__in=list)

        # second only
        if (ingredient == '') & (ingredient2 != '') & (ingredient3 == '') :
            i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname = '"
            i_sql += ingredient2 + "'"

            i_recipe = recipes.objects.raw(i_sql)
            list = []

            for id in i_recipe :
                list.append(id.recipe_id)

            data = data.filter(recipe_id__in=list)

        # third only
        if (ingredient == '') & (ingredient2 == '') & (ingredient3 != '') :
            i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname = '"
            i_sql += ingredient3 + "'"

            i_recipe = recipes.objects.raw(i_sql)
            list = []

            for id in i_recipe :
                list.append(id.recipe_id)

            data = data.filter(recipe_id__in=list)

        # one and two
        if (ingredient != '') & (ingredient2 != '') & (ingredient3 == '') :
            i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname in ('"
            i_sql += ingredient + "', '"
            i_sql += ingredient2 + "') group by r.recipe_id having count(*) = 2"

            i_recipe = recipes.objects.raw(i_sql)
            list = []

            for id in i_recipe :
                list.append(id.recipe_id)

            data = data.filter(recipe_id__in=list)   

        # one and three
        if (ingredient != '') & (ingredient2 == '') & (ingredient3 != '') :
            i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname in ('"
            i_sql += ingredient + "', '"
            i_sql += ingredient3 + "') group by r.recipe_id having count(*) = 2"

            i_recipe = recipes.objects.raw(i_sql)
            list = []

            for id in i_recipe :
                list.append(id.recipe_id)

            data = data.filter(recipe_id__in=list) 

        # two and three
        if (ingredient == '') & (ingredient2 != '') & (ingredient3 != '') :
            i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname in ('"
            i_sql += ingredient2 + "', '"
            i_sql += ingredient3 + "') group by r.recipe_id having count(*) = 2"

            i_recipe = recipes.objects.raw(i_sql)
            list = []

            for id in i_recipe :
                list.append(id.recipe_id)

            data = data.filter(recipe_id__in=list)

        # all three
        if (ingredient != '') & (ingredient2 != '') & (ingredient3 != '') :
            i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname in ('"
            i_sql += ingredient + "', '"
            i_sql += ingredient2 + "', '"
            i_sql += ingredient3 + "') group by r.recipe_id having count(*) = 3"

            i_recipe = recipes.objects.raw(i_sql)
            list = []

            for id in i_recipe :
                list.append(id.recipe_id)

            data = data.filter(recipe_id__in=list)     

        #easter egg
        if (name_contains == "Abbey") or (name_contains== "abbey") :
            egg = 1

        data = data.order_by('recipename')
        main_data = data.filter(rclassid=1)
        side_data = data.filter(rclassid=4)
        dessert_data = data.filter(rclassid=5)

        list = []
        for recipe in menu_data :
            list.append(recipe.recipeid)

        context = {
            "main" : main_data,
            "side" : side_data,
            "dessert" : dessert_data,
            "ingredients" : ingredient_data,
            "ingredient" : ingredient,
            "ingredient3" : ingredient3,
            "ingredient2" : ingredient2,
            "name" : name_contains,
            "egg" : egg,
            "menu":list
        }

        return render(request, 'database/index.html', context)

    else :
        return redirect('../')

def menuItemDeleteRecipeView(request, recipeID) :
    item = menu.objects.get(recipeid_id = recipeID)
    item.delete()

    ri_data = recipe_ingredients.objects.filter(recipeid_id=recipeID)
    grocery_data = grocery.objects.all()
    list = []
    for item in ri_data :
        list.append(item.ri_id)

    for item in grocery_data :
        if item.iid_id in list :
            item.delete()

    url = '../../recipedisplay/' + recipeID
    return redirect(url)

def menuItemAddView(request, recipeID) :
    list = []
    for item in menu.objects.all() :
        list.append(item.recipeid)

    if recipeID in list :
        return redirect('../')

    else:
        if request.method=="POST" :
            new_item = menu()
            new_item.recipeid_id = recipeID
            new_item.save()

            ri_data = recipe_ingredients.objects.filter(recipeid_id=recipeID)

            for item in ri_data :
                new_item = grocery()
                new_item.iid_id = item.ri_id
                new_item.save()

            menu_data = menu.objects.all()

            ingredient_data = ingredients.objects.all()
            data = recipes.objects.all()

            ingredient = request.POST['ingredient_2']
            ingredient2 = request.POST['ingredient2_2']
            ingredient3 = request.POST['ingredient3_2']
            name_contains = request.POST['name_contains_2']
            egg = 0

            if name_contains != '' :
                data = data.filter(recipename__icontains=name_contains)

            # first field only
            if (ingredient != '') & (ingredient2 == '') & (ingredient3 == '') :
                i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname = '"
                i_sql += ingredient + "'"

                i_recipe = recipes.objects.raw(i_sql)
                list = []

                for id in i_recipe :
                    list.append(id.recipe_id)

                data = data.filter(recipe_id__in=list)

            # second only
            if (ingredient == '') & (ingredient2 != '') & (ingredient3 == '') :
                i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname = '"
                i_sql += ingredient2 + "'"

                i_recipe = recipes.objects.raw(i_sql)
                list = []

                for id in i_recipe :
                    list.append(id.recipe_id)

                data = data.filter(recipe_id__in=list)

            # third only
            if (ingredient == '') & (ingredient2 == '') & (ingredient3 != '') :
                i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname = '"
                i_sql += ingredient3 + "'"

                i_recipe = recipes.objects.raw(i_sql)
                list = []

                for id in i_recipe :
                    list.append(id.recipe_id)

                data = data.filter(recipe_id__in=list)

            # one and two
            if (ingredient != '') & (ingredient2 != '') & (ingredient3 == '') :
                i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname in ('"
                i_sql += ingredient + "', '"
                i_sql += ingredient2 + "') group by r.recipe_id having count(*) = 2"

                i_recipe = recipes.objects.raw(i_sql)
                list = []

                for id in i_recipe :
                    list.append(id.recipe_id)

                data = data.filter(recipe_id__in=list)   

            # one and three
            if (ingredient != '') & (ingredient2 == '') & (ingredient3 != '') :
                i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname in ('"
                i_sql += ingredient + "', '"
                i_sql += ingredient3 + "') group by r.recipe_id having count(*) = 2"

                i_recipe = recipes.objects.raw(i_sql)
                list = []

                for id in i_recipe :
                    list.append(id.recipe_id)

                data = data.filter(recipe_id__in=list) 

            # two and three
            if (ingredient == '') & (ingredient2 != '') & (ingredient3 != '') :
                i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname in ('"
                i_sql += ingredient2 + "', '"
                i_sql += ingredient3 + "') group by r.recipe_id having count(*) = 2"

                i_recipe = recipes.objects.raw(i_sql)
                list = []

                for id in i_recipe :
                    list.append(id.recipe_id)

                data = data.filter(recipe_id__in=list)

            # all three
            if (ingredient != '') & (ingredient2 != '') & (ingredient3 != '') :
                i_sql = "select r.recipe_id from recipes r, recipe_ingredients ri, ingredients i where ri.recipeid_id = r.recipe_id and ri.iid_id = i.i_id and i.iname in ('"
                i_sql += ingredient + "', '"
                i_sql += ingredient2 + "', '"
                i_sql += ingredient3 + "') group by r.recipe_id having count(*) = 3"

                i_recipe = recipes.objects.raw(i_sql)
                list = []

                for id in i_recipe :
                    list.append(id.recipe_id)

                data = data.filter(recipe_id__in=list)     

            #easter egg
            if (name_contains == "Abbey") or (name_contains== "abbey") :
                egg = 1

            data = data.order_by('recipename')
            main_data = data.filter(rclassid=1)
            side_data = data.filter(rclassid=4)
            dessert_data = data.filter(rclassid=5)

            list = []
            for recipe in menu_data :
                list.append(recipe.recipeid)

            context = {
                "main" : main_data,
                "side" : side_data,
                "dessert" : dessert_data,
                "ingredients" : ingredient_data,
                "ingredient" : ingredient,
                "ingredient3" : ingredient3,
                "ingredient2" : ingredient2,
                "name" : name_contains,
                "egg" : egg,
                "menu":list
            }

            return render(request, 'database/index.html', context)

        else :
            return redirect('../')

def menuItemAddRecipeView(request, recipeID) :
    list = []
    for item in menu.objects.all() :
        list.append(item.recipeid)

    if recipeID in list :
        2+2

    else :
        new_item = menu()
        new_item.recipeid_id = recipeID
        new_item.save()

        ri_data = recipe_ingredients.objects.filter(recipeid_id=recipeID)

        for item in ri_data :
            new_item = grocery()
            new_item.iid_id = item.ri_id
            new_item.save()

    url = '../../recipedisplay/' + recipeID
    return redirect(url)