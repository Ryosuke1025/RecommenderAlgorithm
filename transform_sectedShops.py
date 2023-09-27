import json
import pandas as pd

# 価格帯を順序エンコーディングする関数
def price_to_ordinal(price_range):
    try:
        if price_range:
            limits = price_range.replace('円', '').split('～')
            lower_limit = int(limits[0]) if limits[0] else None
            upper_limit = int(limits[1]) if limits[1] else None
            
            if lower_limit:
                if lower_limit <= 1000:
                    return 0
                elif lower_limit <= 3000:
                    return 0.25
                elif lower_limit <= 5000:
                    return 0.5
                elif lower_limit <= 10000:
                    return 0.75
                else:
                    return 1
            elif upper_limit:
                if upper_limit <= 1000:
                    return 0
                elif upper_limit <= 3000:
                    return 0.25
                elif upper_limit <= 5000:
                    return 0.5
                elif upper_limit <= 10000:
                    return 0.75
                else:
                    return 1
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"Error with price_range: '{price_range}', error: {e}")
        return None

def format_features(row):
    features = [row['価格帯']]
    for genre in genres:
        features.append(row[genre])
    return ", ".join(map(str, features))

# ファイルを読み込む
with open('selected_shops.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# pandas DataFrameへ変換
df = pd.DataFrame(data)

# ジャンルをワンホットエンコーディング
genres = ['中華', '居酒屋', 'ダイニングバー・バル', '和食', 'お好み焼き・もんじゃ', '韓国料理', "イタリアン・フレンチ", '焼肉・ホルモン', '洋食', 'カフェ・スイーツ', 'アジア・エスニック料理', '創作料理', 'バー・カクテル', '各国料理', 'カラオケ・パーティ', 'ラーメン']
for genre in genres:
    df[genre] = df['ジャンル名'].apply(lambda x: 1 if x == genre else 0)
df.drop('ジャンル名', axis=1, inplace=True)

# 価格帯を順序エンコーディング
df['価格帯'] = df['価格帯'].apply(price_to_ordinal)

# 新たなfeatures列を作成
df['features'] = df.apply(format_features, axis=1)

# 不要な列を削除
df.drop(['価格帯'] + genres, axis=1, inplace=True)

# 新たなjsonファイルに保存
with open('restaurants.json', 'w', encoding='utf-8') as f:
    json.dump(df.to_dict('records'), f, ensure_ascii=False, indent=4)