# 決定木を用いた飲食店推薦アルゴリズムの提案

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

## フォルダ説明
*Restaurants*: 飲食店情報及び取得, [GetFeatures.ipynb](https://github.com/Ryosuke1025/RecommenderAlgorithm/blob/main/Restaurants/GetFeatures.ipynb)はAPIから情報を取得するコードを含んでいるため, 実行しないようにして下さい.<br>
*Users*: ユーザーの評価情報及び取得
