import json
import pandas as pd

# 1. Update the path to include your subfolders
file_path = 'data/raw/LEA.json' 

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        lea_data = json.load(f)
        # 2. Use the correct variable 'lea_data' to get the cards
        cards_list = lea_data['data']['cards'] 

    all_keys = set()
    for card in cards_list:
        # Check if the 'keywords' field exists for this card
        if 'keywords' in card:
            all_keys.update(card['keywords'])

    print(f"Successfully loaded {len(cards_list)} cards.")
    print("All unique keywords in LEA set:")
    print(sorted(list(all_keys)))

except FileNotFoundError:
    print(f"Error: The file was not found at {file_path}")
    print("Check if your 'data' folder is in the same place as your scratch.py script.")

'''
cleaned_cards = []
for card in cards_list:
    cleaned_card = {
        'name': card.get('name'),
        'type': card.get('type_line'),
        'mana_cost': card.get('mana_cost'),
        'cmc': card.get('cmc'),
        'colors': card.get('colors'),
        'rarity': card.get('rarity'),
        'set_name': card.get('set_name'),
        'artist': card.get('artist'),
        'power': card.get('power'),
        'toughness': card.get('toughness'),
        'loyalty': card.get('loyalty'),
    }
    cleaned_cards.append(cleaned_card)

'''