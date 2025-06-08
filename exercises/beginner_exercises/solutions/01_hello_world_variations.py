#!/usr/bin/env python3
"""
===========================================
解答例1: Hello World のバリエーション
===========================================

基礎的な出力とコメントの解答例です。
これは一例なので、他の書き方でも正解です！
"""

print("=" * 50)
print("解答例1: Hello World のバリエーション")
print("=" * 50)
print()

# 【問題1の解答】基本的なHello World
print("問題1の解答:")
print("-----------------------------------------------")
print("Hello, World!")
print()

# 【問題2の解答】変数を使ったHello World
print("問題2の解答:")
print("-----------------------------------------------")
message = "Hello, Python!"
print(message)
print()

# 【問題3の解答】フォーマット文字列を使った挨拶
print("問題3の解答:")
print("-----------------------------------------------")
name = "Python学習者"  # ここは自分の名前に変更
print(f"こんにちは、{name}さん！")
print()

# 【問題4の解答】複数行のメッセージ
print("問題4の解答:")
print("-----------------------------------------------")
print("===== Pythonへようこそ！ =====")
print("プログラミングは楽しいです")
print("一緒に頑張りましょう！")
print("==============================")
print()

# 別解1: トリプルクォートを使用
print("問題4の別解（トリプルクォート）:")
message = """===== Pythonへようこそ！ =====
プログラミングは楽しいです
一緒に頑張りましょう！
=============================="""
print(message)
print()

# 【問題5の解答】計算結果を含むメッセージ
print("問題5の解答:")
print("-----------------------------------------------")
a = 10
b = 20
result = a + b
print(f"{a} + {b} = {result}")
print()

# 別解: 直接計算
print("問題5の別解:")
print(f"15 + 25 = {15 + 25}")
print()

# 【問題6の解答】装飾的な表示
print("問題6の解答:")
print("-----------------------------------------------")
print("********************")
print("*   Hello Python   *")
print("********************")
print()

# 別解1: 変数を使用
print("問題6の別解1:")
border = "*" * 20
print(border)
print("*   Hello Python   *")
print(border)
print()

# 別解2: より動的に
print("問題6の別解2:")
message = "Hello Python"
width = len(message) + 6
border = "*" * width
spaces = " " * 2
print(border)
print(f"*{spaces}{message}{spaces}*")
print(border)
print()

# 【ボーナス問題の解答】現在時刻を含む挨拶
print("ボーナス問題の解答:")
print("-----------------------------------------------")
from datetime import datetime

now = datetime.now()
print(f"現在時刻: {now.strftime('%Y年%m月%d日 %H:%M:%S')}")
print(f"こんにちは！今は{now.hour}時です。")
print()

# より高度な例
print("ボーナス問題の発展例:")
hour = now.hour
if hour < 12:
    greeting = "おはようございます"
elif hour < 18:
    greeting = "こんにちは"
else:
    greeting = "こんばんは"

print(f"{greeting}！現在は{now.strftime('%H:%M')}です。")
print()

print("=" * 50)
print("💡 学習ポイント")
print("=" * 50)
print("✅ print() 関数の基本的な使い方")
print("✅ 変数への代入と使用")
print("✅ f文字列（f-string）によるフォーマット")
print("✅ 文字列の繰り返し（* 演算子）")
print("✅ トリプルクォートによる複数行文字列")
print("✅ datetime モジュールの基本的な使用")
print("✅ 条件分岐の応用（ボーナス問題）")
print()
print("🚀 次のステップ:")
print("- より複雑な文字列操作")
print("- ユーザー入力の処理")
print("- 数値計算の実践")
print("=" * 50)