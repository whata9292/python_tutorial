#!/usr/bin/env python3
"""
===========================
第2章: 数値と文字列
===========================

Pythonで最も基本的なデータ型である数値と文字列について
詳しく学習します。

このファイルを実行すると、数値計算と文字列操作の
基本を習得できます。
"""

import platform
import math


def print_chapter_header():
    """章のヘッダーを表示"""
    print("=" * 50)
    print("第2章: 数値と文字列")
    print("=" * 50)
    print()


def lesson_1_number_types():
    """レッスン1: 数値の種類"""
    print("📚 レッスン1: 数値の種類")
    print("-" * 40)
    print()
    
    print("Pythonには主に3種類の数値型があります：")
    print()
    
    # 整数（int）
    print("1. 整数型（int）")
    print("   >>> age = 25")
    age = 25
    print(f"   >>> type(age)  # {type(age)}")
    print(f"   >>> age = {age}")
    print()
    
    # 浮動小数点数（float）
    print("2. 浮動小数点数型（float）")
    print("   >>> height = 170.5")
    height = 170.5
    print(f"   >>> type(height)  # {type(height)}")
    print(f"   >>> height = {height}")
    print()
    
    # 複素数（complex）
    print("3. 複素数型（complex）")
    print("   >>> z = 3 + 4j")
    z = 3 + 4j
    print(f"   >>> type(z)  # {type(z)}")
    print(f"   >>> z = {z}")
    print()
    
    print("💡 通常は int と float を使います")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_2_number_operations():
    """レッスン2: 数値の演算"""
    print("📚 レッスン2: 数値の演算")
    print("-" * 40)
    print()
    
    print("基本的な演算：")
    print()
    
    # 演算の例
    a, b = 17, 5
    print(f"a = {a}, b = {b} として：")
    print()
    
    operations = [
        ("a + b", a + b, "加算"),
        ("a - b", a - b, "減算"),
        ("a * b", a * b, "乗算"),
        ("a / b", a / b, "除算（結果は常にfloat）"),
        ("a // b", a // b, "整数除算（切り捨て）"),
        ("a % b", a % b, "剰余（余り）"),
        ("a ** b", a ** b, "べき乗"),
        ("-a", -a, "符号反転"),
        ("abs(-a)", abs(-a), "絶対値"),
    ]
    
    for expr, result, desc in operations:
        print(f"{expr:<10} = {result:<10} # {desc}")
    
    print()
    print("数学関数（mathモジュール）：")
    print()
    
    # math モジュールの例
    x = 16
    print(f"x = {x} として：")
    print(f"math.sqrt(x)  = {math.sqrt(x)}    # 平方根")
    print(f"math.ceil(3.2) = {math.ceil(3.2)}     # 切り上げ")
    print(f"math.floor(3.8) = {math.floor(3.8)}    # 切り捨て")
    print(f"math.pi       = {math.pi:.6f}  # 円周率")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_3_number_conversion():
    """レッスン3: 数値の型変換"""
    print("📚 レッスン3: 数値の型変換")
    print("-" * 40)
    print()
    
    print("異なる数値型への変換：")
    print()
    
    # 型変換の例
    print(">>> x = 3.14")
    x = 3.14
    print(f">>> int(x)    # {int(x)}  （小数部分を切り捨て）")
    print()
    
    print(">>> y = 42")
    y = 42
    print(f">>> float(y)  # {float(y)}  （整数を小数に）")
    print()
    
    print(">>> s = '123'")
    s = '123'
    print(f">>> int(s)    # {int(s)}  （文字列を整数に）")
    print()
    
    print(">>> s2 = '45.67'")
    s2 = '45.67'
    print(f">>> float(s2) # {float(s2)}  （文字列を小数に）")
    print()
    
    print("⚠️ 注意: 変換できない文字列はエラーになります")
    print("   例: int('abc') → ValueError")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_4_string_basics():
    """レッスン4: 文字列の基本"""
    print("📚 レッスン4: 文字列の基本")
    print("-" * 40)
    print()
    
    print("文字列の作成方法：")
    print()
    
    # 文字列の作成
    print("1. シングルクォート")
    print("   >>> name = 'Python'")
    name = 'Python'
    print(f"   >>> name = '{name}'")
    print()
    
    print("2. ダブルクォート")
    print("   >>> message = \"Hello, World!\"")
    message = "Hello, World!"
    print(f"   >>> message = \"{message}\"")
    print()
    
    print("3. トリプルクォート（複数行）")
    print("   >>> poem = '''")
    print("   Pythonは")
    print("   楽しい")
    print("   プログラミング言語'''")
    poem = '''Pythonは
楽しい
プログラミング言語'''
    print(f"   >>> print(poem)")
    print(poem)
    print()
    
    print("4. エスケープシーケンス")
    print(r"   >>> path = 'C:\\Users\\name'  # バックスラッシュ")
    path = 'C:\\Users\\name'
    print(f"   >>> path = '{path}'")
    print(r"   >>> quote = 'It\'s Python'   # シングルクォート内")
    quote = 'It\'s Python'
    print(f"   >>> quote = '{quote}'")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_5_string_operations():
    """レッスン5: 文字列の操作"""
    print("📚 レッスン5: 文字列の操作")
    print("-" * 40)
    print()
    
    print("文字列の結合と繰り返し：")
    print()
    
    # 結合
    first = "Python"
    last = "Programming"
    print(f">>> first = '{first}'")
    print(f">>> last = '{last}'")
    print(f">>> first + ' ' + last")
    print(f"'{first + ' ' + last}'")
    print()
    
    # 繰り返し
    star = "*"
    print(f">>> star = '{star}'")
    print(f">>> star * 10")
    print(f"'{star * 10}'")
    print()
    
    print("文字列の長さとインデックス：")
    print()
    
    text = "Python"
    print(f">>> text = '{text}'")
    print(f">>> len(text)  # {len(text)}")
    print(f">>> text[0]    # '{text[0]}'  （最初の文字）")
    print(f">>> text[-1]   # '{text[-1]}'  （最後の文字）")
    print(f">>> text[1:4]  # '{text[1:4]}'  （スライス）")
    print()
    
    print("大文字・小文字変換：")
    print()
    
    word = "Hello Python"
    print(f">>> word = '{word}'")
    print(f">>> word.upper()  # '{word.upper()}'")
    print(f">>> word.lower()  # '{word.lower()}'")
    print(f">>> word.title()  # '{word.title()}'")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_6_string_methods():
    """レッスン6: 便利な文字列メソッド"""
    print("📚 レッスン6: 便利な文字列メソッド")
    print("-" * 40)
    print()
    
    print("文字列の検索と置換：")
    print()
    
    sentence = "Python is fun. Python is powerful."
    print(f">>> sentence = '{sentence}'")
    print(f">>> sentence.count('Python')  # {sentence.count('Python')}")
    print(f">>> sentence.find('fun')      # {sentence.find('fun')}  （位置）")
    print(f">>> sentence.replace('Python', 'Programming')")
    print(f"    '{sentence.replace('Python', 'Programming')}'")
    print()
    
    print("文字列の分割と結合：")
    print()
    
    data = "apple,banana,orange"
    print(f">>> data = '{data}'")
    fruits = data.split(',')
    print(f">>> fruits = data.split(',')  # {fruits}")
    print(f">>> '-'.join(fruits)  # '{'-'.join(fruits)}'")
    print()
    
    print("前後の空白削除：")
    print()
    
    messy = "  Hello World  "
    print(f">>> messy = '{messy}'")
    print(f">>> messy.strip()   # '{messy.strip()}'")
    print(f">>> messy.lstrip()  # '{messy.lstrip()}'  （左のみ）")
    print(f">>> messy.rstrip()  # '{messy.rstrip()}'  （右のみ）")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_7_string_formatting():
    """レッスン7: 文字列のフォーマット"""
    print("📚 レッスン7: 文字列のフォーマット")
    print("-" * 40)
    print()
    
    print("f文字列（推奨）：")
    print()
    
    name = "太郎"
    age = 25
    height = 170.5
    
    print(f">>> name = '{name}'")
    print(f">>> age = {age}")
    print(f">>> height = {height}")
    print()
    
    # f文字列の例
    print(">>> message = f'私は{name}です。{age}歳です。'")
    message = f'私は{name}です。{age}歳です。'
    print(f">>> print(message)")
    print(message)
    print()
    
    # 式の埋め込み
    print(">>> calculation = f'10 + 20 = {10 + 20}'")
    calculation = f'10 + 20 = {10 + 20}'
    print(f">>> print(calculation)")
    print(calculation)
    print()
    
    # フォーマット指定
    print("数値のフォーマット：")
    pi = 3.14159
    print(f">>> pi = {pi}")
    print(f">>> f'円周率: {{pi:.2f}}'  # '{f'円周率: {pi:.2f}'}'  （小数点2桁）")
    print(f">>> f'{{1000000:,}}'      # '{1000000:,}'  （カンマ区切り）")
    print(f">>> f'{{0.75:.0%}}'       # '{0.75:.0%}'  （パーセント）")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def practice_exercises():
    """練習問題"""
    print("🏃 練習してみよう！")
    print("=" * 50)
    print()
    
    print("以下の練習問題を対話モードで試してください：")
    print()
    
    print("【練習1】 数値計算")
    print("1. 自分の年齢を変数 age に代入")
    print("2. 10年後の年齢を計算して表示")
    print("3. 生まれてから何日経ったか概算（age * 365）")
    print()
    
    print("【練習2】 文字列操作")
    print("1. 自分の名前を変数 name に代入")
    print("2. f'こんにちは、{name}さん！' を表示")
    print("3. name.upper() で大文字に変換")
    print("4. '*' * len(name) で名前の長さ分の星を表示")
    print()
    
    print("【練習3】 応用")
    print("1. 商品の価格 price = 1980")
    print("2. 消費税率 tax_rate = 0.1")
    print("3. 税込価格を計算: total = price * (1 + tax_rate)")
    print("4. f'税込 {total:.0f}円' で表示")
    print()
    
    input("練習が終わったらEnterキーを押してください...")
    print()


def show_summary():
    """まとめ"""
    print("📝 第2章のまとめ")
    print("=" * 50)
    print()
    
    print("数値について学んだこと：")
    print("✅ 整数(int)と浮動小数点数(float)の違い")
    print("✅ 基本的な算術演算")
    print("✅ 型変換（int(), float()）")
    print("✅ mathモジュールの数学関数")
    print()
    
    print("文字列について学んだこと：")
    print("✅ 文字列の作成方法（', \", '''）")
    print("✅ 文字列の結合(+)と繰り返し(*)") 
    print("✅ インデックスとスライス")
    print("✅ 便利な文字列メソッド")
    print("✅ f文字列によるフォーマット")
    print()
    
    print("次のステップ：")
    print("• リストやタプルなどのデータ構造")
    print("• より複雑なデータの扱い方")
    print()


def show_completion_message():
    """完了メッセージ"""
    print("\n" + "🎉" * 20)
    print("   ファイル 02 の学習完了！   ")
    print("🎉" * 20)
    
    print(f"\n📚 理解度テストを受けましょう")
    print("以下のコマンドをコピー&ペーストして実行してください:\n")
    
    # OS別コマンド表示
    python_cmd = "py" if platform.system() == "Windows" else "python3"
    print(f"   {python_cmd} quizzes/quiz_runner.py basics 02")
    
    print(f"\n✅ テスト合格後、次に進みましょう:")
    print(f"   {python_cmd} basics/03_lists_and_sequences.py")
    
    print("\n💡 困ったときは:")
    print(f"   {python_cmd} quizzes/quiz_runner.py help")
    print("=" * 50)


def main():
    """メイン処理"""
    print_chapter_header()
    
    # 各レッスンを順番に実行
    lesson_1_number_types()
    lesson_2_number_operations()
    lesson_3_number_conversion()
    lesson_4_string_basics()
    lesson_5_string_operations()
    lesson_6_string_methods()
    lesson_7_string_formatting()
    
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