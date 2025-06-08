# 🧪 理解度テストシステム

学習内容の理解度を確認するためのテストシステムです。

## 📋 概要

各学習章の終了後に理解度テストを実施し、70%以上の正解で次の章へ進めます。

### テストの種類

1. **基礎テスト** - basics/01-12 各章のテスト
2. **プロジェクトテスト** - 各プロジェクト完了後のテスト

### 問題形式

- **選択肢問題** - 基礎知識の確認
- **穴埋め問題** - コードの理解確認
- **エラー修正問題** - デバッグスキルの確認
- **実行結果予測問題** - コードの動作理解
- **実装問題** - 実践的なコーディング力の確認

## 🚀 使い方

### テストの実行

```bash
# 基礎テスト
python3 quizzes/quiz_runner.py basics 01  # 第1章のテスト
python3 quizzes/quiz_runner.py basics 02  # 第2章のテスト

# プロジェクトテスト
python3 quizzes/quiz_runner.py project 01  # プロジェクト1のテスト

# その他のコマンド
python3 quizzes/quiz_runner.py progress   # 進捗確認
python3 quizzes/quiz_runner.py help       # ヘルプ表示
python3 quizzes/quiz_runner.py diagnose   # 環境診断
```

## 📊 合格基準

- **合格ライン**: 70%以上
- **再挑戦**: 3回まで可能
- **クーリング期間**: 1時間（同じテストの再受験まで）

## 💡 ヒント機能

- 各問題にはヒントが用意されています
- ヒントを使用すると若干の減点があります
- 段階的なヒントで理解を促進

## 📁 ディレクトリ構成

```
quizzes/
├── README.md              # このファイル
├── quiz_runner.py         # テスト実行エンジン
├── quiz_config.json       # 設定ファイル
├── error_handler.py       # エラーハンドリング
├── progress_tracker.py    # 進捗管理
├── basics/               # 基礎テスト問題
│   ├── quiz_01_interpreter.py
│   ├── quiz_02_numbers_strings.py
│   ├── quiz_03_lists.py
│   └── ...
├── projects/             # プロジェクトテスト
│   └── ...
└── results/             # テスト結果
    ├── progress.json    # 進捗データ
    └── scores/         # 個別成績
```

## 🎯 学習のコツ

1. **間違えを恐れない** - エラーから学ぶことが多い
2. **ヒントを活用** - 理解できない時は積極的に使う
3. **復習を大切に** - 間違えた問題は必ず見直す
4. **実践あるのみ** - コードを書いて試すことが重要

---

**頑張ってください！** 🚀