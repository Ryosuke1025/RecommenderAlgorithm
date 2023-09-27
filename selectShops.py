import json
import random

# JSONファイルから店舗情報を読み込む
with open('shops.json', 'r', encoding='utf-8') as f:
    shops = json.load(f)

# 各種情報を管理するセットとリストを初期化
chosen_genres = set()
chosen_budgets = set()
chosen_shops = set()  # 選ばれた店舗の名前を記録するセット
selected_shops = []  # 選ばれた店舗を保存するリスト

# 価格帯が空文字列でない店舗、ジャンルが"その他グルメ"でない店舗のみを処理対象にする
shops = [shop for shop in shops if shop["価格帯"] != "" and shop["ジャンル名"] != "その他グルメ"]

# 最初に全てのジャンルを1つずつ選ぶ
for shop in shops:
    genre = shop["ジャンル名"]
    shop_name = shop["店の名前"]

    if shop_name not in chosen_shops and genre not in chosen_genres:
        chosen_genres.add(genre)
        chosen_shops.add(shop_name)
        selected_shops.append(shop)

# すでに選択されているジャンルの後に、まだ選ばれていない価格帯を選ぶ
for shop in shops:
    budget = shop["価格帯"]
    shop_name = shop["店の名前"]

    if shop_name not in chosen_shops and budget not in chosen_budgets:
        chosen_budgets.add(budget)
        chosen_shops.add(shop_name)
        selected_shops.append(shop)

# 各ジャンルで選ばれた店舗の数を管理する辞書を初期化
chosen_genres_counts = {genre: 0 for genre in chosen_genres}

# 全てのジャンルをもう一つずつ選ぶ
for shop in shops:
    genre = shop["ジャンル名"]
    shop_name = shop["店の名前"]

    # 選択されたジャンルであり、まだ選ばれていない店舗であれば選ぶ
    # ただし、そのジャンルで既に2つの店舗が選ばれている場合はスキップする
    if genre in chosen_genres and shop_name not in chosen_shops and chosen_genres_counts[genre] < 2:
        chosen_genres_counts[genre] += 1
        chosen_shops.add(shop_name)
        selected_shops.append(shop)

# 各価格帯で選ばれた店舗の数を管理する辞書を初期化
chosen_budgets_counts = {budget: 0 for budget in chosen_budgets}

# 全ての価格帯をもう一つずつ選ぶ
for shop in shops:
    budget = shop["価格帯"]
    shop_name = shop["店の名前"]

    # 選択された価格帯であり、まだ選ばれていない店舗であれば選ぶ
    # ただし、その価格帯で既に1つの店舗が選ばれている場合はスキップする
    if budget in chosen_budgets and shop_name not in chosen_shops and chosen_budgets_counts[budget] < 1:
        chosen_budgets_counts[budget] += 1
        chosen_shops.add(shop_name)
        selected_shops.append(shop)

# 残りはランダムで
while len(selected_shops) < 100:
    shop = random.choice(shops)
    shop_name = shop["店の名前"]

    # すでに選ばれている店舗は除外
    if shop_name not in chosen_shops:
        chosen_shops.add(shop_name)
        selected_shops.append(shop)

# 選択した店舗をJSON形式でファイルに出力
with open('selected_shops.json', 'w', encoding='utf-8') as f:
    json.dump(selected_shops, f, ensure_ascii=False, indent=4)
    