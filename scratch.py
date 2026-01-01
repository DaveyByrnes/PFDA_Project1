import json
import pandas as pd
from pathlib import Path 

raw_path = Path("data/raw/default-cards-20251222100856.json")

with open(raw_path, encoding="utf-8") as f:
    cards = json.load(f)

len(cards)

war_cards = [card for card in cards if card.get("set_code") == "war"]

len(war_cards)
df = pd.DataFrame(war_cards)
df.head()