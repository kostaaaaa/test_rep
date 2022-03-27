shopping_list = ['milk', 'meat', 'lemon', 'beer', 'whiskey', 'vodka', 'cola']
new_list = list(filter(lambda prod: len(prod) == 4, shopping_list))
print(new_list)