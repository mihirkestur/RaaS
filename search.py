import pandas as pd
def get_recipes(ingredients):
    recipes = []
    df = pd.read_csv("recipes.csv")
    for index, row in df.iterrows():
        for i in ingredients:
            if(i in str(row["ingredients"])):
                recipes.append(row)
    return recipes
