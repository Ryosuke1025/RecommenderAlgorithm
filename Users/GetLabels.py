import csv

def getLabels() :
    # CSVファイルを開く
    filename = 'Users/Ratings.csv'

    # ユーザーごとの回答を格納するリスト
    user1_answers = []
    user2_answers = []
    user3_answers = []

    # ユーザーごとのラベルを格納するリスト
    user1_labels = []
    user2_labels = []
    user3_labels = []

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # ヘッダー行をスキップ

        # 各ユーザーの行を読み込む
        user1_answers = next(reader)[1:]    
        user2_answers = next(reader)[1:]  
        user3_answers = next(reader)[1:] 

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
    
    for index, answer in enumerate(user3_answers):
        if answer == '行きたい':
            user3_labels.append(1)
        else:
            user3_labels.append(0)
            
    return user1_labels, user2_labels, user3_labels
