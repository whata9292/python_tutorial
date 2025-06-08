#!/usr/bin/env python3
"""
プロジェクト2: 基本電卓アプリ

このプログラムは基本的な四則演算ができる電卓アプリです。
関数を使って機能を分割し、エラーハンドリングも含まれています。

学習ポイント:
- 関数の定義と使用
- 基本的なエラーハンドリング
- ユーザーインターフェースの設計
- 繰り返し処理とメニュー

対応章: basics/05_functions.py完了後
"""

def add(a, b):
    """二つの数を足し算する関数"""
    return a + b

def subtract(a, b):
    """二つの数を引き算する関数"""
    return a - b

def multiply(a, b):
    """二つの数を掛け算する関数"""
    return a * b

def divide(a, b):
    """二つの数を割り算する関数"""
    if b == 0:
        raise ValueError("ゼロで割ることはできません")
    return a / b

def get_number(prompt):
    """
    ユーザーから数値を安全に取得する関数
    
    Args:
        prompt (str): ユーザーに表示するメッセージ
        
    Returns:
        float: 入力された数値
    """
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("❌ エラー: 有効な数値を入力してください")

def get_operation():
    """
    ユーザーから演算子を取得する関数
    
    Returns:
        str: 選択された演算子
    """
    print("\n🔢 演算を選択してください:")
    print("1. 足し算 (+)")
    print("2. 引き算 (-)")
    print("3. 掛け算 (×)")
    print("4. 割り算 (÷)")
    
    while True:
        try:
            choice = input("選択 (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                return choice
            else:
                print("❌ エラー: 1から4の数字を入力してください")
        except KeyboardInterrupt:
            print("\n\n👋 電卓を終了します")
            return None

def calculate(num1, num2, operation):
    """
    計算を実行する関数
    
    Args:
        num1 (float): 最初の数値
        num2 (float): 二番目の数値
        operation (str): 演算子 ('1', '2', '3', '4')
        
    Returns:
        float: 計算結果
    """
    try:
        if operation == '1':
            return add(num1, num2)
        elif operation == '2':
            return subtract(num1, num2)
        elif operation == '3':
            return multiply(num1, num2)
        elif operation == '4':
            return divide(num1, num2)
    except ValueError as e:
        print(f"❌ 計算エラー: {e}")
        return None

def display_result(num1, num2, operation, result):
    """
    計算結果を分かりやすく表示する関数
    
    Args:
        num1 (float): 最初の数値
        num2 (float): 二番目の数値
        operation (str): 演算子
        result (float): 計算結果
    """
    if result is None:
        return
    
    # 演算記号の変換
    symbols = {'1': '+', '2': '-', '3': '×', '4': '÷'}
    symbol = symbols[operation]
    
    # 整数の場合は小数点を表示しない
    if num1.is_integer():
        num1 = int(num1)
    if num2.is_integer():
        num2 = int(num2)
    if result.is_integer():
        result = int(result)
    
    print(f"\n✅ 計算結果:")
    print(f"   {num1} {symbol} {num2} = {result}")

def show_welcome():
    """ウェルカムメッセージを表示する関数"""
    print("=" * 50)
    print("🧮 基本電卓アプリ")
    print("=" * 50)
    print("四則演算ができるシンプルな電卓です")
    print("終了するには Ctrl+C を押してください")
    print("=" * 50)

def main():
    """メイン関数 - 電卓のメインループ"""
    show_welcome()
    
    while True:
        try:
            print("\n" + "-" * 30)
            
            # 演算子の選択
            operation = get_operation()
            if operation is None:  # Ctrl+C で終了
                break
            
            # 数値の入力
            num1 = get_number("最初の数値を入力: ")
            num2 = get_number("二番目の数値を入力: ")
            
            # 計算実行
            result = calculate(num1, num2, operation)
            
            # 結果表示
            display_result(num1, num2, operation, result)
            
            # 継続確認
            print("\n🔄 もう一度計算しますか？")
            continue_calc = input("続ける場合は Enter、終了する場合は 'q' を入力: ").strip().lower()
            if continue_calc == 'q':
                break
                
        except KeyboardInterrupt:
            print("\n\n👋 電卓を終了します")
            break
        except Exception as e:
            print(f"❌ 予期しないエラーが発生しました: {e}")
            print("もう一度お試しください")

if __name__ == "__main__":
    main()

"""
🎯 学習のポイント:

1. 関数の分割
   - 各機能を独立した関数として実装
   - 再利用可能で理解しやすいコード

2. エラーハンドリング
   - try-except文を使った安全な入力処理
   - ゼロ除算のエラーチェック

3. ユーザーインターフェース
   - 分かりやすいメニュー表示
   - エラーメッセージとフィードバック

4. プログラムの構造
   - main関数によるメインループ
   - 各機能の責任分離

🔧 改良案:
- 履歴機能の追加
- より高度な演算（平方根、べき乗など）
- 計算結果の保存機能
- より美しいUI

⚡ 実行方法:
python3 projects/02_calculator/basic_calculator.py
"""