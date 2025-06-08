#!/usr/bin/env python3
"""
===========================
第7章: モジュールとパッケージ
===========================

コードを複数のファイルに分割して整理する方法を学びます。
モジュールの作成、インポート、パッケージ構造について
理解しましょう。

このファイルを実行すると、より大規模なプログラムを
構築する基礎が身につきます。
"""

import platform
import sys
import os
import math
import random
from datetime import datetime


def print_chapter_header():
    """章のヘッダーを表示"""
    print("=" * 50)
    print("第7章: モジュールとパッケージ")
    print("=" * 50)
    print()


def lesson_1_import_basics():
    """レッスン1: import の基本"""
    print("📚 レッスン1: import の基本")
    print("-" * 40)
    print()
    
    print("モジュールは Python ファイル（.py）です。")
    print("import で他のモジュールの機能を使えます。")
    print()
    
    # import の基本形
    print("import の基本形:")
    print(">>> import math")
    print(">>> math.pi")
    print(f"    {math.pi}")
    print(">>> math.sqrt(16)")
    print(f"    {math.sqrt(16)}")
    print()
    
    # from import
    print("from import で特定の関数だけインポート:")
    print(">>> from math import sqrt, pi")
    print(">>> sqrt(25)  # mathを付けずに使える")
    from math import sqrt, pi
    print(f"    {sqrt(25)}")
    print()
    
    # import as
    print("import as で別名を付ける:")
    print(">>> import datetime as dt")
    print(">>> dt.datetime.now()")
    import datetime as dt
    print(f"    {dt.datetime.now()}")
    print()
    
    # ワイルドカードインポート（非推奨）
    print("ワイルドカードインポート（非推奨）:")
    print(">>> from math import *  # すべてをインポート")
    print(">>> # 名前空間が汚染されるので避けましょう")
    print()
    
    print("💡 明示的なインポートで、")
    print("   どこから何を使っているか分かりやすくしましょう")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_2_creating_modules():
    """レッスン2: モジュールの作成"""
    print("📚 レッスン2: モジュールの作成")
    print("-" * 40)
    print()
    
    print("自分でモジュールを作ってみましょう。")
    print()
    
    # モジュールの例
    print("例: my_math.py というファイルを作成")
    print()
    print("# my_math.py の内容")
    print("-" * 30)
    print('"""')
    print('数学関連のユーティリティ関数')
    print('"""')
    print()
    print("def add(a, b):")
    print('    """2つの数を足す"""')
    print("    return a + b")
    print()
    print("def multiply(a, b):")
    print('    """2つの数を掛ける"""')
    print("    return a * b")
    print()
    print("PI = 3.14159")
    print("-" * 30)
    print()
    
    print("使い方:")
    print(">>> import my_math")
    print(">>> my_math.add(5, 3)")
    print("    8")
    print(">>> my_math.PI")
    print("    3.14159")
    print()
    
    # __name__ の説明
    print("__name__ 変数について:")
    print(">>> # モジュールが直接実行された場合")
    print(">>> if __name__ == '__main__':")
    print("...     print('このモジュールが直接実行されました')")
    print(">>> # importされた場合は実行されない")
    print()
    
    print("💡 モジュールにはテストコードを")
    print("   if __name__ == '__main__': の中に書きましょう")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_3_module_search_path():
    """レッスン3: モジュールの検索パス"""
    print("📚 レッスン3: モジュールの検索パス")
    print("-" * 40)
    print()
    
    print("Python がモジュールを探す場所を理解しましょう。")
    print()
    
    # sys.path の表示
    print("モジュール検索パス (sys.path):")
    print(">>> import sys")
    print(">>> for path in sys.path[:5]:  # 最初の5個")
    print("...     print(path)")
    print()
    
    for path in sys.path[:5]:
        print(f"    {path}")
    print("    ...")
    print()
    
    print("検索順序:")
    print("1. 現在のディレクトリ")
    print("2. PYTHONPATH 環境変数のディレクトリ")
    print("3. 標準ライブラリのディレクトリ")
    print("4. site-packages（インストールしたパッケージ）")
    print()
    
    # カレントディレクトリ
    print("現在の作業ディレクトリ:")
    print(">>> import os")
    print(">>> os.getcwd()")
    print(f"    {os.getcwd()}")
    print()
    
    # モジュールの場所を調べる
    print("モジュールの場所を調べる:")
    print(">>> import math")
    print(">>> math.__file__")
    if hasattr(math, '__file__'):
        print(f"    {math.__file__}")
    else:
        print("    （組み込みモジュール）")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_4_packages():
    """レッスン4: パッケージ"""
    print("📚 レッスン4: パッケージ")
    print("-" * 40)
    print()
    
    print("パッケージは複数のモジュールをまとめたものです。")
    print("ディレクトリで階層構造を作ります。")
    print()
    
    # パッケージ構造の例
    print("パッケージ構造の例:")
    print()
    print("myproject/")
    print("├── __init__.py        # パッケージであることを示す")
    print("├── utils/")
    print("│   ├── __init__.py")
    print("│   ├── math_tools.py")
    print("│   └── string_tools.py")
    print("└── main.py")
    print()
    
    print("インポート方法:")
    print(">>> # main.py から")
    print(">>> from utils import math_tools")
    print(">>> from utils.string_tools import capitalize_words")
    print(">>> ")
    print(">>> # または")
    print(">>> import utils.math_tools")
    print(">>> utils.math_tools.add(1, 2)")
    print()
    
    # __init__.py の役割
    print("__init__.py の役割:")
    print("1. そのディレクトリがパッケージであることを示す")
    print("2. パッケージの初期化コードを書ける")
    print("3. __all__ で公開するモジュールを指定できる")
    print()
    
    print("# utils/__init__.py の例")
    print("-" * 30)
    print("from .math_tools import add, multiply")
    print("from .string_tools import capitalize_words")
    print()
    print("__all__ = ['add', 'multiply', 'capitalize_words']")
    print("-" * 30)
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_5_standard_modules():
    """レッスン5: よく使う標準モジュール"""
    print("📚 レッスン5: よく使う標準モジュール")
    print("-" * 40)
    print()
    
    print("Python には便利な標準モジュールがたくさんあります。")
    print()
    
    # os モジュール
    print("os - OS関連の機能:")
    print(">>> import os")
    print(">>> os.getcwd()  # 現在のディレクトリ")
    print(f"    '{os.getcwd()}'")
    print(">>> os.listdir('.')[:3]  # ファイル一覧（最初の3個）")
    print(f"    {os.listdir('.')[:3]}")
    print()
    
    # random モジュール
    print("random - 乱数生成:")
    print(">>> import random")
    print(">>> random.randint(1, 10)  # 1〜10の整数")
    print(f"    {random.randint(1, 10)}")
    print(">>> random.choice(['apple', 'banana', 'orange'])")
    print(f"    '{random.choice(['apple', 'banana', 'orange'])}'")
    print()
    
    # datetime モジュール
    print("datetime - 日付と時刻:")
    print(">>> from datetime import datetime, timedelta")
    print(">>> now = datetime.now()")
    now = datetime.now()
    print(f">>> now  # {now}")
    print(">>> tomorrow = now + timedelta(days=1)")
    tomorrow = now + timedelta(days=1)
    print(f">>> tomorrow.strftime('%Y年%m月%d日')")
    print(f"    '{tomorrow.strftime('%Y年%m月%d日')}'")
    print()
    
    # json モジュール
    print("json - JSONデータの処理:")
    print(">>> import json")
    print(">>> data = {'name': '太郎', 'age': 25}")
    print(">>> json_str = json.dumps(data, ensure_ascii=False)")
    import json
    data = {'name': '太郎', 'age': 25}
    json_str = json.dumps(data, ensure_ascii=False)
    print(f'>>> json_str  # {json_str}')
    print()
    
    print("💡 標準ライブラリのドキュメントを読んで")
    print("   さまざまなモジュールを活用しましょう")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_6_best_practices():
    """レッスン6: ベストプラクティス"""
    print("📚 レッスン6: モジュール設計のベストプラクティス")
    print("-" * 40)
    print()
    
    print("良いモジュール設計のための指針を学びます。")
    print()
    
    # 命名規則
    print("1. 命名規則:")
    print("   • モジュール名: 小文字とアンダースコア")
    print("     例: my_module.py, data_processor.py")
    print("   • パッケージ名: 小文字（アンダースコアなし推奨）")
    print("     例: mypackage, utilities")
    print()
    
    # インポートの順序
    print("2. インポートの順序:")
    print("   1) 標準ライブラリ")
    print("   2) サードパーティライブラリ")
    print("   3) ローカルモジュール")
    print()
    print("# 良い例")
    print("-" * 30)
    print("import os")
    print("import sys")
    print("from datetime import datetime")
    print()
    print("import requests  # サードパーティ")
    print("import pandas as pd")
    print()
    print("from myproject import utils")
    print("from .helpers import calculate")
    print("-" * 30)
    print()
    
    # 循環インポートの回避
    print("3. 循環インポートの回避:")
    print("   • モジュールAがBをインポートし、")
    print("     BがAをインポートすると問題発生")
    print("   • 解決策: 共通部分を別モジュールに分離")
    print()
    
    # 相対インポート vs 絶対インポート
    print("4. 相対 vs 絶対インポート:")
    print("   • パッケージ内: 相対インポート")
    print("     from .utils import helper")
    print("   • パッケージ外: 絶対インポート")
    print("     from myproject.utils import helper")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def practice_exercises():
    """練習問題"""
    print("🏃 練習してみよう！")
    print("=" * 50)
    print()
    
    print("以下の練習問題を試してください：")
    print()
    
    print("【練習1】簡単なモジュール作成")
    print("calculator.py を作成して、四則演算の関数を定義")
    print("別ファイルからインポートして使用")
    print()
    
    print("【練習2】パッケージ構造の作成")
    print("game/ パッケージを作成")
    print("├── __init__.py")
    print("├── player.py  # Player クラス")
    print("└── utils.py   # ユーティリティ関数")
    print()
    
    print("【練習3】標準モジュールの活用")
    print("random と datetime を使って")
    print("ランダムな日付を生成する関数を作成")
    print()
    
    print("【練習4】モジュール検索")
    print("インストール済みモジュールの場所を調べる")
    print("sys.path にパスを追加してみる")
    print()
    
    input("練習が終わったらEnterキーを押してください...")
    print()


def show_summary():
    """まとめ"""
    print("📝 第7章のまとめ")
    print("=" * 50)
    print()
    
    print("モジュールとパッケージについて学んだこと：")
    print("✅ import 文の各種形式")
    print("✅ モジュールの作成方法")
    print("✅ __name__ == '__main__' の使い方")
    print("✅ モジュール検索パス（sys.path）")
    print("✅ パッケージ構造と __init__.py")
    print("✅ 標準モジュールの活用")
    print("✅ インポートのベストプラクティス")
    print()
    
    print("モジュール化のメリット：")
    print("• コードの再利用性向上")
    print("• 保守性の向上")
    print("• 名前空間の分離")
    print("• チーム開発の効率化")
    print()
    
    print("次のステップ：")
    print("• ファイル入出力の詳細")
    print("• エラー処理と例外")
    print()


def show_completion_message():
    """完了メッセージ"""
    print("\n" + "🎉" * 20)
    print("   ファイル 07 の学習完了！   ")
    print("🎉" * 20)
    
    print(f"\n📚 理解度テストを受けましょう")
    print("以下のコマンドをコピー&ペーストして実行してください:\n")
    
    # OS別コマンド表示
    python_cmd = "py" if platform.system() == "Windows" else "python3"
    print(f"   {python_cmd} quizzes/quiz_runner.py basics 07")
    
    print(f"\n✅ テスト合格後、次に進みましょう:")
    print(f"   {python_cmd} basics/08_input_output.py")
    
    print("\n💡 困ったときは:")
    print(f"   {python_cmd} quizzes/quiz_runner.py help")
    print("=" * 50)


def main():
    """メイン処理"""
    print_chapter_header()
    
    # 各レッスンを順番に実行
    lesson_1_import_basics()
    lesson_2_creating_modules()
    lesson_3_module_search_path()
    lesson_4_packages()
    lesson_5_standard_modules()
    lesson_6_best_practices()
    
    # 練習問題
    practice_exercises()
    
    # まとめ
    show_summary()
    
    # 完了メッセージ
    show_completion_message()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nプログラムを中断しました。")
        print("続きはまた後で！")
    except Exception as e:
        print(f"\nエラーが発生しました: {e}")
        print("エラーの内容を確認して、もう一度試してください。")