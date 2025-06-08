# 🔧 環境構築ガイド

Pythonプログラミングを始めるための環境を整えましょう！

## 📋 このセクションの内容

1. **01_python_installation.py** - Pythonが正しくインストールされているか確認
2. **02_environment_check.py** - 開発環境の動作確認
3. **03_virtual_environment.py** - 仮想環境の作成と使い方（basics/12の後に学習）

## 🚀 始め方

### ステップ1: Pythonのインストール確認

まず、Pythonがインストールされているか確認しましょう：

```bash
# Windowsの場合
py setup/01_python_installation.py

# Macの場合
python3 setup/01_python_installation.py
```

### ステップ2: 環境の動作確認

次に、開発環境が正しく動作するか確認します：

```bash
# Windowsの場合
py setup/02_environment_check.py

# Macの場合
python3 setup/02_environment_check.py
```

## 💡 Pythonがインストールされていない場合

### Windows
1. [Python公式サイト](https://www.python.org/downloads/)から最新版をダウンロード
2. インストーラーを実行
3. **重要**: 「Add Python to PATH」にチェックを入れる
4. インストール完了後、コマンドプロンプトを再起動

### Mac
1. Homebrewがインストールされている場合：
   ```bash
   brew install python3
   ```
2. または[Python公式サイト](https://www.python.org/downloads/)からダウンロード

### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

## 🎯 学習の流れ

1. **01と02を完了** → basics/セクションへ進む
2. **basics/12まで完了** → 03_virtual_environment.pyを学習
3. 仮想環境を使ってプロジェクト開発へ

## ❓ よくある質問

**Q: 「py」と「python3」の違いは？**  
A: Windowsでは「py」、Mac/Linuxでは「python3」を使います。

**Q: エラーが出て実行できません**  
A: 以下を確認してください：
- 正しいフォルダにいるか（`ls`または`dir`で確認）
- Pythonがインストールされているか
- コマンドのスペルが正しいか

**Q: 仮想環境って何？**  
A: プロジェクトごとに独立したPython環境を作る仕組みです。basics/12で外部ライブラリを学んだ後に詳しく説明します。

---

準備ができたら、さっそく始めましょう！ 🚀