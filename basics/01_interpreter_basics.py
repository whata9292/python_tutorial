#!/usr/bin/env python3
"""
=================================
第1章: Pythonインタープリター基礎
=================================

Pythonプログラミングの第一歩として、
Pythonインタープリター（対話モード）の使い方を学びます。

このファイルを実行すると、インタープリターの基本的な
使い方を体験できます。
"""

import sys
import platform


def print_chapter_header():
    """章のヘッダーを表示"""
    print("=" * 50)
    print("第1章: Pythonインタープリター基礎")
    print("=" * 50)
    print()


def lesson_1_what_is_interpreter():
    """レッスン1: インタープリターとは？"""
    print("📚 レッスン1: インタープリターとは？")
    print("-" * 40)
    print()
    
    print("Pythonインタープリターは、Pythonコードを")
    print("1行ずつ実行してくれるプログラムです。")
    print()
    print("2つの使い方があります：")
    print("1. 対話モード（インタラクティブモード）")
    print("   → コマンドを1行ずつ入力して実行")
    print("2. スクリプトモード")
    print("   → ファイルに書いたコードをまとめて実行")
    print()
    print("今あなたが実行しているのはスクリプトモードです！")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_2_starting_interpreter():
    """レッスン2: インタープリターの起動"""
    print("📚 レッスン2: インタープリターの起動")
    print("-" * 40)
    print()
    
    print("対話モードを起動する方法：")
    print()
    
    if platform.system() == "Windows":
        print("Windows:")
        print("  コマンドプロンプトで「py」と入力してEnter")
        print("  または「python」と入力してEnter")
    else:
        print("Mac/Linux:")
        print("  ターミナルで「python3」と入力してEnter")
        print("  または「python」と入力してEnter")
    
    print()
    print("すると、このような表示が出ます：")
    print()
    print("Python 3.x.x (main, ...)")
    print("Type \"help\", \"copyright\", \"credits\" or \"license\"...")
    print(">>>")
    print()
    print("「>>>」は入力を待っているという意味です。")
    print("ここにPythonコードを入力できます！")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_3_basic_calculations():
    """レッスン3: 基本的な計算"""
    print("📚 レッスン3: 基本的な計算")
    print("-" * 40)
    print()
    
    print("インタープリターは電卓として使えます。")
    print("実際に計算してみましょう：")
    print()
    
    calculations = [
        ("2 + 3", 2 + 3, "足し算"),
        ("10 - 4", 10 - 4, "引き算"),
        ("5 * 6", 5 * 6, "掛け算"),
        ("15 / 3", 15 / 3, "割り算"),
        ("16 // 5", 16 // 5, "整数除算（商）"),
        ("16 % 5", 16 % 5, "剰余（余り）"),
        ("2 ** 8", 2 ** 8, "べき乗（2の8乗）"),
    ]
    
    for expression, result, description in calculations:
        print(f">>> {expression}")
        print(f"{result}    # {description}")
        print()
    
    print("💡 ヒント: 対話モードでは、計算結果がすぐに表示されます")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_4_variables():
    """レッスン4: 変数の使い方"""
    print("📚 レッスン4: 変数の使い方")
    print("-" * 40)
    print()
    
    print("変数は値を保存する「箱」のようなものです。")
    print()
    
    # 変数の例を実行
    print(">>> x = 10")
    x = 10
    print(">>> y = 3")
    y = 3
    print(">>> x + y")
    print(x + y)
    print()
    
    print(">>> name = 'Python'")
    name = 'Python'
    print(">>> print('Hello, ' + name + '!')")
    print('Hello, ' + name + '!')
    print()
    
    print(">>> price = 100")
    price = 100
    print(">>> quantity = 5")
    quantity = 5
    print(">>> total = price * quantity")
    total = price * quantity
    print(">>> print(f'合計金額: {total}円')")
    print(f'合計金額: {total}円')
    print()
    
    print("💡 ヒント: 変数名は分かりやすい名前を付けましょう")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_5_help_function():
    """レッスン5: ヘルプ機能"""
    print("📚 レッスン5: ヘルプ機能")
    print("-" * 40)
    print()
    
    print("Pythonには便利なヘルプ機能があります。")
    print()
    
    print("1. help() - ヘルプシステムを起動")
    print("   >>> help()")
    print("   help> と表示されたら、調べたいものを入力")
    print("   終了は quit または Ctrl+D")
    print()
    
    print("2. help(関数名) - 特定の関数のヘルプを表示")
    print("   >>> help(print)")
    print("   print関数の詳しい説明が表示されます")
    print()
    
    print("3. dir() - 使える機能の一覧")
    print("   >>> dir()")
    print("   現在使える変数や関数の一覧")
    print()
    
    print("4. type() - オブジェクトの型を調べる")
    print("   >>> type(42)")
    print("   <class 'int'>  # 整数型")
    print("   >>> type('Hello')")
    print("   <class 'str'>  # 文字列型")
    print()
    
    print("💡 ヒント: 分からないことがあったら help() を活用！")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_6_exiting_interpreter():
    """レッスン6: インタープリターの終了"""
    print("📚 レッスン6: インタープリターの終了")
    print("-" * 40)
    print()
    
    print("対話モードを終了する方法：")
    print()
    
    print("1. exit() または quit() と入力")
    print("   >>> exit()")
    print()
    
    print("2. キーボードショートカット")
    if platform.system() == "Windows":
        print("   Ctrl + Z を押してからEnter")
    else:
        print("   Ctrl + D")
    print()
    
    print("終了すると、通常のコマンドラインに戻ります。")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def practice_session():
    """練習セッション"""
    print("🏃 練習セッション")
    print("=" * 50)
    print()
    
    print("それでは、実際に対話モードを試してみましょう！")
    print()
    print("以下の手順で練習してください：")
    print()
    print("1. 新しいターミナル/コマンドプロンプトを開く")
    print()
    
    if platform.system() == "Windows":
        print("2. 「py」と入力してEnter")
    else:
        print("2. 「python3」と入力してEnter")
    
    print()
    print("3. 以下を順番に試してみる：")
    print("   a) 100 + 200")
    print("   b) 'Hello' + ' World'")
    print("   c) age = 25")
    print("   d) print(f'私は{age}歳です')")
    print("   e) help(len)")
    print("   f) exit()")
    print()
    print("4. このプログラムに戻ってくる")
    print()
    
    input("練習が終わったらEnterキーを押してください...")
    print()


def show_summary():
    """まとめ"""
    print("📝 第1章のまとめ")
    print("=" * 50)
    print()
    
    print("今回学んだこと：")
    print("✅ Pythonインタープリターの2つのモード")
    print("✅ 対話モードの起動と終了")
    print("✅ 基本的な計算")
    print("✅ 変数の使い方")
    print("✅ ヘルプ機能の活用")
    print()
    
    print("次のステップ：")
    print("• より複雑な計算や文字列操作")
    print("• データ型の詳細")
    print("• プログラムの制御構造")
    print()


def show_completion_message():
    """完了メッセージ"""
    print("\n" + "🎉" * 20)
    print("   ファイル 01 の学習完了！   ")
    print("🎉" * 20)
    
    print(f"\n📚 理解度テストを受けましょう")
    print("以下のコマンドをコピー&ペーストして実行してください:\n")
    
    # OS別コマンド表示
    python_cmd = "py" if platform.system() == "Windows" else "python3"
    print(f"   {python_cmd} quizzes/quiz_runner.py basics 01")
    
    print(f"\n✅ テスト合格後、次に進みましょう:")
    print(f"   {python_cmd} basics/02_numbers_and_strings.py")
    
    print("\n💡 困ったときは:")
    print(f"   {python_cmd} quizzes/quiz_runner.py help")
    print("=" * 50)


def main():
    """メイン処理"""
    print_chapter_header()
    
    # 各レッスンを順番に実行
    lesson_1_what_is_interpreter()
    lesson_2_starting_interpreter()
    lesson_3_basic_calculations()
    lesson_4_variables()
    lesson_5_help_function()
    lesson_6_exiting_interpreter()
    
    # 練習セッション
    practice_session()
    
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