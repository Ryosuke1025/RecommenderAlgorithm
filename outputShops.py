import json
import random
from collections import Counter

# JSONファイルから店舗情報を読み込む
with open('shops.json', 'r', encoding='utf-8') as f:
    shops = json.load(f)

# ジャンルと価格帯がすでに選ばれたかどうかを記録するセット
chosen_genres = set()
chosen_budgets = set()

# 選択した店舗の名前を保存するセット
chosen_names = set()

# 選択した店舗を保存するリスト
selected_shops = []

for shop in shops:
    # ジャンルと価格帯を取得
    genre = shop["ジャンル名"]
    budget = shop["価格帯"]
    name = shop["店の名前"]

    # ジャンルが「その他グルメ」の場合、または店舗が既に選ばれている場合はスキップ
    if genre == "その他グルメ" or name in chosen_names:
        continue

    # 価格帯とジャンルがまだ選ばれていない場合、店を選択
    if (genre not in chosen_genres or budget not in chosen_budgets) and budget:
        chosen_genres.add(genre)
        chosen_budgets.add(budget)
        chosen_names.add(name)
        selected_shops.append(shop)

    # 100店舗選ばれたらループを抜ける
    if len(selected_shops) == 100:
        break

# 100店舗に満たない場合、ジャンルと価格帯が均等になるように選択
remaining = 100 - len(selected_shops)
remaining_genre_half = remaining // 2
remaining_budget_half = remaining - remaining_genre_half

genre_counter = Counter([shop["ジャンル名"] for shop in selected_shops])
budget_counter = Counter([shop["価格帯"] for shop in selected_shops])

for _ in range(remaining_genre_half):
    min_genre = min(genre_counter, key=genre_counter.get)
    for shop in shops:
        if shop["ジャンル名"] == min_genre and shop["店の名前"] not in chosen_names and budget:
            chosen_names.add(shop["店の名前"])
            selected_shops.append(shop)
            genre_counter[min_genre] += 1
            break

for _ in range(remaining_budget_half):
    min_budget = min(budget_counter, key=budget_counter.get)
    for shop in shops:
        if shop["価格帯"] == min_budget and shop["店の名前"] not in chosen_names and budget:
            chosen_names.add(shop["店の名前"])
            selected_shops.append(shop)
            budget_counter[min_budget] += 1
            break

# 選択した店舗をJSON形式でファイルに出力
with open('selected_shops.json', 'w', encoding='utf-8') as f:
    json.dump(selected_shops, f, ensure_ascii=False, indent=4)