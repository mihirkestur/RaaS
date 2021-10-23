import pandas as pd
def get_recipes(ingredients):
    recipes = []
    df = pd.read_csv("recipes.csv")
    for index, row in df.iterrows():
        count = 0
        for i in ingredients:
            if(i in str(row["ingredients"])):
                count+=1
        if(count):
            recipes.append([count ,row])
    recipes = sorted(recipes, key=lambda x: x[0])
    recipes = recipes[::-1]
    return [i[1] for i in recipes]