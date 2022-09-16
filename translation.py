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
shops["shop_name_en"] = shops["shop_name"].replace(shops_english, regex=True)

# Translate items names - dictionary was build with a python script
print("Items translation...")
items["item_name_en"] = items["item_name"].map(items_english)

# export data to csv
print("Exporting Data...")
items.to_csv("data/items_en.csv")
shops.to_csv("data/shops_en.csv")
categories.to_csv("data/item_categories_en.csv")
