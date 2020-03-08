def cakes(recipe, available):
    n_cakes = 0
    while True:
        for k in recipe.keys():
            if k in available:
                available[k] = available[k] - recipe[k]
                if available[k] < 0:
                    return n_cakes
            else:
                return n_cakes
        n_cakes += 1


recipe2 = {"flour": 500, "sugar": 200, "eggs": 1}
available2 = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe2, available2))

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe, available))