"""Translate item names with Google Translator."""
import pandas as pd
import json

# loading shops and categories dictionaries
from utils import categories_english, shops_english

# loading item name dictionary
with open("data/items_english.json", "r") as f:
    items_english = json.load(f)

# Load Data
items = pd.read_csv("data/items.csv")
shops = pd.read_csv("data/shops.csv")
categories = pd.read_csv("data/item_categories.csv")

# Translate category names - dictionary was built manually
print("Categories translation...")
categories["item_category_name_en"] = categories["item_category_name"].replace(
    categories_english, regex=True
)

# translate shop names - dictionary was built manually
print("Shops translation...")
shops["shop_name_en"] = shops["shop_name"].map(shops_english)
# some mappins are not working - we will correct them manually
# shops.loc[6, 'shop_name_en'] = 'Voronezh - Plekhanovskaya'
# shops.loc[23, 'shop_name_en'] = 'Moscow - Budenovskiy - A2'
# shops.loc[24, 'shop_name_en'] = 'Moscow - Budenovskiy - K7'
# shops.loc[26, 'shop_name_en'] = 'Moscow - Areal (Belyaevo)'
# shops.loc[29, 'shop_name_en'] = 'Moscow - New Age (Novokosino)'

# Translate items names - dictionary was build with a python script
print("Items translation...")
items["item_name_en"] = items["item_name"].map(items_english)

# export data to csv
print("Exporting Data...")
items.to_csv("data/items_en.csv", index=False)
shops.to_csv("data/shops_en.csv", index=False)
categories.to_csv("data/item_categories_en.csv", index=False)
