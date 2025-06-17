# 決定木を用いた飲食店推薦アルゴリズムの提案

<img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat"> <img src="https://img.shields.io/badge/License-CC%20BY%204.0-green.svg?style=flat">

<img src="https://img.shields.io/badge/-Visual%20Studio%20Code-007ACC.svg?logo=visual-studio-code&style=flat"> <img src="https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat"> <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=flat&logo=jupyter&logoColor=white">

## 🗂️ フォルダ構成

```
RecommenderAlgorithm/
├── Restaurants/               # 飲食店データ
│   ├── GetFeatures.ipynb      # API取得コード
│   ├── AllRestaurants.json    # 全飲食店情報
│   ├── RestaurantsNumber.json # 数値データ
│   ├── RestaurantsText.json   # テキストデータ
│   └── Features.json          # 特徴量データ
├── Users/                     # ユーザーデータ
│   ├── GetLabels.py           # ラベル取得スクリプト
│   └── Ratings.csv            # 評価データ
├── Thesis/                    # 論文・研究資料
│   ├── Resume/                # 論文要約
│   ├── Thesis/                # 論文本体
│   └── 2024-02-16.pptx        # 発表資料
├── recommender.ipynb          # メインプログラム
├── README.md                  # プロジェクト説明
└── LICENSE                    # ライセンス情報
```


⚠️ **注意**: `GetFeatures.ipynb`は外部APIを使用し、飲食店データを再度取得してしまうため、実行しないでください。`recommender.ipynb`のみを実行してください。

## 🚀 セットアップ
### 実行環境(参考)
- PC: Mac Book Air M1
- ソフトウェア: [Jupyter Notebook](https://jupyter.org)
- テキストエディタ: [Visual Studio Code](https://code.visualstudio.com)

### VScodeでJupyter Notebookを使う場合
以下を参照して環境構築を行なって下さい
- [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

### その他必要なインストール
#### Homebrewのインストール
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Pythonのインストール
```bash
brew install python
```

#### pipの確認
```bash
pip --version
```

#### NumPy, Scikit-Learn, matplotlib, japanize-matplotlib, scipyのインストール
```bash
pip install numpy scikit-learn matplotlib japanize-matplotlib scipy 
```

## 📄 利用について

### コード・データセット
[MIT License](LICENSE) の下で公開されています。

### 論文・研究資料
[CC BY 4.0](Thesis/LICENSE) の下で公開されています。
