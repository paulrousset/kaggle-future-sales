"""Translate item names with Google Translator and build mapping file."""
from googletrans import Translator
import time

# we will use nordvpn to rotate IP to avoid google API requests limits
from nordvpn_switcher import initialize_VPN, rotate_VPN, terminate_VPN
import json


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


# Initializing dictionary
items_english = {}

# Initializing VPN settings
initialize_VPN(save=1)

# add countries to the settings
settings = json.load("settings_nordvpn.txt")
settings["settings"] = [
    "belgium",
    "netherlands",
    "germany",
    "spain",
    "france",
    "United_States",
    "Canada",
    "Brazil",
    "Argentina",
    "Mexico",
    "Chile",
    "Costa_Rica",
    "Australia",
]

start_time = time.time()
print("Building Name Dictionary...")

# listing all item names
to_translate = items.item_name.to_list()

# split list into chunks
name_chunks = chunks(to_translate, 300)

# Loop through each chunk with a different IP
count = 0
for chunk in name_chunks:
    start_time = time.time()
    count += 1
    # changing IP
    rotate_VPN(settings)
    # initializing translator
    translator = Translator()
    # Looping through the chunk names
    for name in chunk:
        if not items_english.get(name):
            # translate word and save in the dictionary
            items_english[name] = translator.translate(name).text
            time.sleep(0.3)
    print("chunk {}: runtime{} seconds".format(count, time.time() - start_time))

print(
    "Name Dictionary processed in {} minutes ---".format(
        (time.time() - start_time) / 60
    )
)

terminate_VPN

# save dictionary as json
with open("data/items_english.json", "w") as f:
    json.dump(items_english, f)
