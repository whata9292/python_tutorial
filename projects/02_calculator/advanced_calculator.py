#!/usr/bin/env python3
"""
プロジェクト2: 高度な電卓アプリ

基本電卓の機能を拡張し、以下の機能を追加しています:
- 計算履歴の管理
- 高度な演算（平方根、べき乗、階乗など）
- 設定保存機能
- ユニットテスト

学習ポイント:
- クラスを使った設計
- ファイルI/O
- JSON形式でのデータ保存
- テストの重要性

対応章: basics/10_classes_and_objects.py完了後
"""

import math
import json
import os
from datetime import datetime

class AdvancedCalculator:
    """高度な電卓クラス"""
    
    def __init__(self):
        """電卓の初期化"""
        self.history = []
        self.settings = {
            "decimal_places": 6,
            "save_history": True,
            "show_steps": False
        }
        self.load_settings()
        self.load_history()
    
    def add(self, a, b):
        """足し算"""
        return a + b
    
    def subtract(self, a, b):
        """引き算"""
        return a - b
    
    def multiply(self, a, b):
        """掛け算"""
        return a * b
    
    def divide(self, a, b):
        """割り算"""
        if b == 0:
            raise ValueError("ゼロで割ることはできません")
        return a / b
    
    def power(self, base, exponent):
        """べき乗計算"""
        return base ** exponent
    
    def square_root(self, x):
        """平方根計算"""
        if x < 0:
            raise ValueError("負の数の平方根は計算できません")
        return math.sqrt(x)
    
    def factorial(self, n):
        """階乗計算"""
        if not isinstance(n, int) or n < 0:
            raise ValueError("階乗は非負の整数でのみ計算できます")
        if n > 170:  # オーバーフロー対策
            raise ValueError("数値が大きすぎます")
        return math.factorial(n)
    
    def logarithm(self, x, base=math.e):
        """対数計算"""
        if x <= 0:
            raise ValueError("正の数でのみ対数を計算できます")
        if base <= 0 or base == 1:
            raise ValueError("底は正の数で1以外である必要があります")
        return math.log(x, base)
    
    def sin(self, x):
        """正弦（度数）"""
        return math.sin(math.radians(x))
    
    def cos(self, x):
        """余弦（度数）"""
        return math.cos(math.radians(x))
    
    def tan(self, x):
        """正接（度数）"""
        return math.tan(math.radians(x))
    
    def format_result(self, result):
        """結果をフォーマットして表示"""
        if isinstance(result, float):
            if result.is_integer():
                return str(int(result))
            else:
                return f"{result:.{self.settings['decimal_places']}f}".rstrip('0').rstrip('.')
        return str(result)
    
    def add_to_history(self, expression, result):
        """計算履歴に追加"""
        if self.settings["save_history"]:
            entry = {
                "timestamp": datetime.now().isoformat(),
                "expression": expression,
                "result": result
            }
            self.history.append(entry)
            
            # 履歴が100件を超えたら古いものを削除
            if len(self.history) > 100:
                self.history = self.history[-100:]
    
    def show_history(self):
        """履歴を表示"""
        if not self.history:
            print("📝 計算履歴はありません")
            return
        
        print("\n📝 計算履歴（最新10件）:")
        print("-" * 50)
        
        recent_history = self.history[-10:]
        for i, entry in enumerate(recent_history, 1):
            timestamp = datetime.fromisoformat(entry["timestamp"])
            time_str = timestamp.strftime("%H:%M:%S")
            print(f"{i:2d}. [{time_str}] {entry['expression']} = {entry['result']}")
    
    def clear_history(self):
        """履歴をクリア"""
        self.history = []
        print("🗑️ 履歴をクリアしました")
    
    def save_settings(self):
        """設定をファイルに保存"""
        try:
            with open("calculator_settings.json", "w", encoding="utf-8") as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"❌ 設定の保存に失敗しました: {e}")
    
    def load_settings(self):
        """設定をファイルから読み込み"""
        try:
            if os.path.exists("calculator_settings.json"):
                with open("calculator_settings.json", "r", encoding="utf-8") as f:
                    self.settings.update(json.load(f))
        except Exception as e:
            print(f"⚠️ 設定の読み込みに失敗しました: {e}")
    
    def save_history(self):
        """履歴をファイルに保存"""
        if not self.settings["save_history"]:
            return
        
        try:
            with open("calculator_history.json", "w", encoding="utf-8") as f:
                json.dump(self.history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"❌ 履歴の保存に失敗しました: {e}")
    
    def load_history(self):
        """履歴をファイルから読み込み"""
        try:
            if os.path.exists("calculator_history.json"):
                with open("calculator_history.json", "r", encoding="utf-8") as f:
                    self.history = json.load(f)
        except Exception as e:
            print(f"⚠️ 履歴の読み込みに失敗しました: {e}")
    
    def show_settings(self):
        """現在の設定を表示"""
        print("\n⚙️ 現在の設定:")
        print(f"小数点以下桁数: {self.settings['decimal_places']}")
        print(f"履歴保存: {'有効' if self.settings['save_history'] else '無効'}")
        print(f"計算手順表示: {'有効' if self.settings['show_steps'] else '無効'}")
    
    def change_settings(self):
        """設定を変更"""
        print("\n⚙️ 設定変更")
        print("1. 小数点以下桁数")
        print("2. 履歴保存の切り替え")
        print("3. 計算手順表示の切り替え")
        print("0. 戻る")
        
        try:
            choice = input("選択: ").strip()
            
            if choice == "1":
                decimal_places = int(input("小数点以下桁数 (1-10): "))
                if 1 <= decimal_places <= 10:
                    self.settings["decimal_places"] = decimal_places
                    print(f"✅ 小数点以下桁数を {decimal_places} に設定しました")
                else:
                    print("❌ 1から10の範囲で入力してください")
            
            elif choice == "2":
                self.settings["save_history"] = not self.settings["save_history"]
                status = "有効" if self.settings["save_history"] else "無効"
                print(f"✅ 履歴保存を{status}にしました")
            
            elif choice == "3":
                self.settings["show_steps"] = not self.settings["show_steps"]
                status = "有効" if self.settings["show_steps"] else "無効"
                print(f"✅ 計算手順表示を{status}にしました")
            
            elif choice == "0":
                return
            
            else:
                print("❌ 無効な選択です")
            
            self.save_settings()
            
        except ValueError:
            print("❌ 無効な入力です")
    
    def get_number(self, prompt):
        """数値を安全に取得"""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("❌ 有効な数値を入力してください")
    
    def basic_operations_menu(self):
        """基本演算メニュー"""
        print("\n🔢 基本演算:")
        print("1. 足し算 (+)")
        print("2. 引き算 (-)")
        print("3. 掛け算 (×)")
        print("4. 割り算 (÷)")
        print("0. 戻る")
        
        choice = input("選択: ").strip()
        
        if choice in ['1', '2', '3', '4']:
            num1 = self.get_number("最初の数値: ")
            num2 = self.get_number("二番目の数値: ")
            
            try:
                if choice == '1':
                    result = self.add(num1, num2)
                    expression = f"{num1} + {num2}"
                elif choice == '2':
                    result = self.subtract(num1, num2)
                    expression = f"{num1} - {num2}"
                elif choice == '3':
                    result = self.multiply(num1, num2)
                    expression = f"{num1} × {num2}"
                elif choice == '4':
                    result = self.divide(num1, num2)
                    expression = f"{num1} ÷ {num2}"
                
                formatted_result = self.format_result(result)
                print(f"\n✅ 結果: {expression} = {formatted_result}")
                self.add_to_history(expression, formatted_result)
                
            except ValueError as e:
                print(f"❌ エラー: {e}")
        
        elif choice == '0':
            return
        else:
            print("❌ 無効な選択です")
    
    def advanced_operations_menu(self):
        """高度な演算メニュー"""
        print("\n🧮 高度な演算:")
        print("1. べき乗 (x^y)")
        print("2. 平方根 (√x)")
        print("3. 階乗 (x!)")
        print("4. 対数 (log)")
        print("5. 三角関数")
        print("0. 戻る")
        
        choice = input("選択: ").strip()
        
        try:
            if choice == '1':
                base = self.get_number("底: ")
                exponent = self.get_number("指数: ")
                result = self.power(base, exponent)
                expression = f"{base}^{exponent}"
                
            elif choice == '2':
                x = self.get_number("数値: ")
                result = self.square_root(x)
                expression = f"√{x}"
                
            elif choice == '3':
                n = int(self.get_number("数値 (整数): "))
                result = self.factorial(n)
                expression = f"{n}!"
                
            elif choice == '4':
                x = self.get_number("真数: ")
                base_input = input("底 (Enterで自然対数): ").strip()
                if base_input:
                    base = float(base_input)
                    result = self.logarithm(x, base)
                    expression = f"log_{base}({x})"
                else:
                    result = self.logarithm(x)
                    expression = f"ln({x})"
                
            elif choice == '5':
                self.trigonometry_menu()
                return
                
            elif choice == '0':
                return
            else:
                print("❌ 無効な選択です")
                return
            
            formatted_result = self.format_result(result)
            print(f"\n✅ 結果: {expression} = {formatted_result}")
            self.add_to_history(expression, formatted_result)
            
        except ValueError as e:
            print(f"❌ エラー: {e}")
    
    def trigonometry_menu(self):
        """三角関数メニュー"""
        print("\n📐 三角関数 (度数):")
        print("1. 正弦 (sin)")
        print("2. 余弦 (cos)")
        print("3. 正接 (tan)")
        print("0. 戻る")
        
        choice = input("選択: ").strip()
        
        try:
            if choice in ['1', '2', '3']:
                angle = self.get_number("角度 (度): ")
                
                if choice == '1':
                    result = self.sin(angle)
                    expression = f"sin({angle}°)"
                elif choice == '2':
                    result = self.cos(angle)
                    expression = f"cos({angle}°)"
                elif choice == '3':
                    result = self.tan(angle)
                    expression = f"tan({angle}°)"
                
                formatted_result = self.format_result(result)
                print(f"\n✅ 結果: {expression} = {formatted_result}")
                self.add_to_history(expression, formatted_result)
                
            elif choice == '0':
                return
            else:
                print("❌ 無効な選択です")
                
        except ValueError as e:
            print(f"❌ エラー: {e}")
    
    def show_main_menu(self):
        """メインメニューを表示"""
        print("\n" + "=" * 50)
        print("🧮 高度な電卓アプリ")
        print("=" * 50)
        print("1. 基本演算")
        print("2. 高度な演算")
        print("3. 履歴表示")
        print("4. 履歴クリア")
        print("5. 設定")
        print("6. 設定表示")
        print("0. 終了")
        print("=" * 50)
    
    def run(self):
        """電卓のメインループ"""
        print("🧮 高度な電卓アプリを開始します")
        
        while True:
            try:
                self.show_main_menu()
                choice = input("選択: ").strip()
                
                if choice == '1':
                    self.basic_operations_menu()
                elif choice == '2':
                    self.advanced_operations_menu()
                elif choice == '3':
                    self.show_history()
                elif choice == '4':
                    self.clear_history()
                elif choice == '5':
                    self.change_settings()
                elif choice == '6':
                    self.show_settings()
                elif choice == '0':
                    self.save_history()
                    print("\n👋 電卓を終了します")
                    break
                else:
                    print("❌ 無効な選択です")
                    
            except KeyboardInterrupt:
                print("\n\n👋 電卓を終了します")
                self.save_history()
                break
            except Exception as e:
                print(f"❌ 予期しないエラー: {e}")

def main():
    """メイン関数"""
    calculator = AdvancedCalculator()
    calculator.run()

if __name__ == "__main__":
    main()

"""
🎯 学習のポイント:

1. オブジェクト指向設計
   - クラスを使った機能のカプセル化
   - メソッドによる機能分割

2. ファイルI/O
   - JSON形式でのデータ保存・読み込み
   - 設定ファイルの管理

3. エラーハンドリング
   - 各演算に応じた適切なエラーチェック
   - ユーザーフレンドリーなエラーメッセージ

4. データ管理
   - 履歴の管理と表示
   - 設定の永続化

5. 数学関数の活用
   - mathモジュールの使用
   - 三角関数、対数、階乗等

🔧 改良案:
- 式パーサーの実装（"2+3*4"のような式を直接入力）
- グラフ機能の追加
- より多くの数学関数
- プラグインシステム

⚡ 実行方法:
python3 projects/02_calculator/advanced_calculator.py
"""