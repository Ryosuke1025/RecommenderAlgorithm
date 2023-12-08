# 決定木を用いた飲食店推薦アルゴリズムの提案

<img src="https://img.shields.io/badge/-Visual%20Studio%20Code-007ACC.svg?logo=visual-studio-code&style=flat"> <img src="https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat"> <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=flat&logo=jupyter&logoColor=white">

## 概要
本研究では, 決定木を用いた飲食店推薦アルゴリズムを評価しました.

## 実行環境(参考)
- PC: Mac Book Air M1
- ソフトウェア: [Jupyter Notebook](https://jupyter.org)
- テキストエディタ: [Visual Studio Code](https://code.visualstudio.com)

## VScodeでJupyter Notebookを使う場合
以下を参照して環境構築を行なって下さい
- [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

## その他必要なインストール
### Homebrewのインストール
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Pythonのインストール
```bash
brew install python
```

### pipの確認
```bash
pip --version
```

### NumPy, Scikit-Learn, matplotlib, japanize-matplotlib, scipyのインストール
```bash
pip install numpy scikit-learn matplotlib japanize-matplotlib scipy 
```

## フォルダ及びファイル説明
- [Restaurants](https://github.com/Ryosuke1025/RecommenderAlgorithm/tree/main/Restaurants)<br>
飲食店情報及び取得, [GetFeatures.ipynb](https://github.com/Ryosuke1025/RecommenderAlgorithm/blob/main/Restaurants/GetFeatures.ipynb)はAPIから情報を取得するコードを含んでいるため, 必ず実行しないようにして下さい.<br>
- [Users](https://github.com/Ryosuke1025/RecommenderAlgorithm/tree/main/Users)<br>
ユーザーの評価情報及び取得<br>
- [Recommender.ipynb](https://github.com/Ryosuke1025/RecommenderAlgorithm/tree/main/recommender.ipynb)<br>
メインプログラムで, こちらのファイルのみを実行するようにして下さい
