# 🧪 理解度テストシステム

学習内容の理解度を確認するためのテストシステムです。

## 📋 概要

各学習章の終了後に理解度テストを実施し、70%以上の正解で次の章へ進めます。

### テストの種類

1. **基礎テスト** - basics/01-12 各章のテスト（全12章分完備）
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
# 基礎テスト実行例
python3 quizzes/quiz_runner.py basics 01  # 第1章: インタープリター基礎
python3 quizzes/quiz_runner.py basics 02  # 第2章: 数値と文字列
python3 quizzes/quiz_runner.py basics 03  # 第3章: リストとシーケンス
...
python3 quizzes/quiz_runner.py basics 12  # 第12章: 外部ライブラリ

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
├── quiz_01_interpreter.py         # 第1章: インタープリター基礎
├── quiz_02_numbers_strings.py     # 第2章: 数値と文字列
├── quiz_03_lists.py               # 第3章: リストとシーケンス
├── quiz_04_control_flow.py        # 第4章: 制御フロー
├── quiz_05_functions.py           # 第5章: 関数
├── quiz_06_data_structures.py     # 第6章: データ構造
├── quiz_07_modules_packages.py    # 第7章: モジュールとパッケージ
├── quiz_08_input_output.py        # 第8章: 入出力処理
├── quiz_09_errors_exceptions.py   # 第9章: エラーと例外処理
├── quiz_10_classes_objects.py     # 第10章: クラスとオブジェクト
├── quiz_11_standard_library.py    # 第11章: 標準ライブラリ
├── quiz_12_external_libraries.py  # 第12章: 外部ライブラリ
├── projects/             # プロジェクトテスト
│   └── ...
└── results/             # テスト結果
    ├── progress.json    # 進捗データ
    └── scores/         # 個別成績
```

## 📖 各章クイズの内容

| 章 | ファイル名 | 主な内容 |
|:--:|:-----------|:---------|
| 01 | quiz_01_interpreter.py | Python実行、基本操作、変数 |
| 02 | quiz_02_numbers_strings.py | 数値計算、文字列操作、フォーマット |
| 03 | quiz_03_lists.py | リスト操作、インデックス、スライス |
| 04 | quiz_04_control_flow.py | if文、ループ、制御構文 |
| 05 | quiz_05_functions.py | 関数定義、引数、スコープ |
| 06 | quiz_06_data_structures.py | 辞書、セット、タプル |
| 07 | quiz_07_modules_packages.py | import、モジュール作成 |
| 08 | quiz_08_input_output.py | ファイル操作、JSON、CSV |
| 09 | quiz_09_errors_exceptions.py | try-except、カスタム例外 |
| 10 | quiz_10_classes_objects.py | クラス定義、継承、特殊メソッド |
| 11 | quiz_11_standard_library.py | datetime、os、正規表現等 |
| 12 | quiz_12_external_libraries.py | pip、仮想環境、ライブラリ選択 |

## 🎯 学習のコツ

1. **間違えを恐れない** - エラーから学ぶことが多い
2. **ヒントを活用** - 理解できない時は積極的に使う
3. **復習を大切に** - 間違えた問題は必ず見直す
4. **実践あるのみ** - コードを書いて試すことが重要
5. **段階的学習** - 前の章を理解してから次へ進む

---

**頑張ってください！** 🚀