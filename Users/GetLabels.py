import csv

def getLabels() :
    # CSVファイルを開く
    filename = 'Users/Labels.csv'

    # ユーザーごとの回答を格納するリスト
    user1_answers = []
    user2_answers = []

    # ユーザーごとのラベルを格納するリスト
    user1_labels = []
    user2_labels = []

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # ヘッダー行をスキップ

        # 各ユーザーの行を読み込む
        user1_answers = next(reader)[1:]  # ユーザー1の回答 (最初の要素はユーザー名なのでスキップ)        
        user2_answers = next(reader)[1:]  # ユーザー2の回答

    for index, answer in enumerate(user1_answers):
        if answer == '行きたい':
            user1_labels.append(1)
        else:
            user1_labels.append(0)

    for index, answer in enumerate(user2_answers):
        if answer == '行きたい':
            user2_labels.append(1)
        else:
            user2_labels.append(0)

    print(user1_labels)
    
    return user1_labels, user2_labels

getLabels()