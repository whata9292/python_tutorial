#!/usr/bin/env python3
"""
=== 開発環境動作確認ツール ===

Pythonで実際にプログラムを作成・実行できる環境が
整っているかを確認します。

実行方法:
  Windows: py setup/02_environment_check.py
  Mac/Linux: python3 setup/02_environment_check.py
"""

import os
import sys
import platform
import subprocess
import tempfile
from pathlib import Path


def print_banner():
    """プログラム開始時のバナーを表示"""
    print("=" * 50)
    print("🔧 開発環境動作確認ツール")
    print("=" * 50)
    print()


def check_working_directory():
    """現在の作業ディレクトリを確認"""
    print("📌 作業ディレクトリの確認:")
    cwd = os.getcwd()
    print(f"   現在の場所: {cwd}")
    
    # python-tutorialディレクトリにいるか確認
    if "python-tutorial" in cwd or "python_tutorial" in cwd:
        print("   ✅ 正しいディレクトリにいます")
        return True
    else:
        print("   ⚠️  python-tutorialディレクトリにいない可能性があります")
        print("   💡 ヒント: 'cd python-tutorial' でディレクトリを移動してください")
        return True  # 警告のみ


def check_file_operations():
    """ファイル操作の確認"""
    print("\n📌 ファイル操作の確認:")
    
    # 一時ファイルを作成
    test_content = "Hello, Python World! 🐍"
    test_file = "test_file_temp.txt"
    
    try:
        # ファイル書き込み
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(test_content)
        print("   ✅ ファイル書き込み: OK")
        
        # ファイル読み込み
        with open(test_file, 'r', encoding='utf-8') as f:
            read_content = f.read()
        
        if read_content == test_content:
            print("   ✅ ファイル読み込み: OK")
        else:
            print("   ❌ ファイル読み込み: 内容が一致しません")
            return False
        
        # ファイル削除
        os.remove(test_file)
        print("   ✅ ファイル削除: OK")
        
        return True
        
    except Exception as e:
        print(f"   ❌ エラー: {e}")
        # クリーンアップ
        if os.path.exists(test_file):
            try:
                os.remove(test_file)
            except:
                pass
        return False


def check_encoding():
    """文字エンコーディングの確認"""
    print("\n📌 文字エンコーディングの確認:")
    
    test_strings = [
        ("英語", "Hello World"),
        ("日本語", "こんにちは、Python！"),
        ("絵文字", "🐍 🚀 ✨"),
        ("記号", "＃＄％＆＊"),
    ]
    
    all_ok = True
    for name, test_str in test_strings:
        try:
            # エンコード・デコードのテスト
            encoded = test_str.encode('utf-8')
            decoded = encoded.decode('utf-8')
            
            if decoded == test_str:
                print(f"   ✅ {name}: OK")
            else:
                print(f"   ❌ {name}: エンコード/デコードエラー")
                all_ok = False
        except Exception as e:
            print(f"   ❌ {name}: エラー - {e}")
            all_ok = False
    
    return all_ok


def check_basic_execution():
    """基本的なPythonコードの実行確認"""
    print("\n📌 Pythonコード実行の確認:")
    
    # 簡単な計算
    try:
        result = 2 + 2
        print(f"   ✅ 基本的な計算 (2 + 2 = {result}): OK")
    except:
        print("   ❌ 基本的な計算: エラー")
        return False
    
    # リスト操作
    try:
        fruits = ['apple', 'banana', 'orange']
        fruits.append('grape')
        print(f"   ✅ リスト操作 (要素数: {len(fruits)}): OK")
    except:
        print("   ❌ リスト操作: エラー")
        return False
    
    # 辞書操作
    try:
        person = {'name': 'Python太郎', 'age': 25}
        person['city'] = '東京'
        print(f"   ✅ 辞書操作 (キー数: {len(person)}): OK")
    except:
        print("   ❌ 辞書操作: エラー")
        return False
    
    # 関数定義
    try:
        def greet(name):
            return f"こんにちは、{name}さん！"
        
        message = greet("学習者")
        print(f"   ✅ 関数定義と実行: OK")
    except:
        print("   ❌ 関数定義と実行: エラー")
        return False
    
    return True


def check_pip_availability():
    """pipの利用可能性を確認（情報提供のみ）"""
    print("\n📌 パッケージ管理ツール (pip) の確認:")
    
    try:
        # pipのバージョンを確認
        result = subprocess.run(
            [sys.executable, '-m', 'pip', '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            print("   ✅ pip が利用可能です")
            pip_info = result.stdout.strip()
            if pip_info:
                print(f"   ℹ️  {pip_info.split('from')[0].strip()}")
        else:
            print("   ⚠️  pip が見つかりません")
            print("   💡 basics/12 で pip の使い方を学習します")
    except Exception as e:
        print("   ⚠️  pip の確認中にエラーが発生しました")
        print("   💡 basics/12 で詳しく学習します")


def create_practice_file():
    """練習用ファイルを作成"""
    print("\n📌 練習用ファイルの作成:")
    
    practice_file = "my_first_program.py"
    practice_content = '''#!/usr/bin/env python3
"""
初めてのPythonプログラム
作成日: 今日
"""

# あなたの名前を入力してください
name = "Python学習者"

# 挨拶メッセージを表示
print(f"こんにちは、{name}さん！")
print("Pythonプログラミングへようこそ！")
print()
print("このファイルを自由に編集して、")
print("Pythonの練習に使ってください。")

# 簡単な計算の例
print()
print("=== 計算の例 ===")
x = 10
y = 3
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y:.2f}")
'''
    
    try:
        with open(practice_file, 'w', encoding='utf-8') as f:
            f.write(practice_content)
        
        print(f"   ✅ '{practice_file}' を作成しました")
        print("\n   💡 このファイルを実行してみましょう:")
        
        if platform.system() == "Windows":
            print(f"      py {practice_file}")
        else:
            print(f"      python3 {practice_file}")
        
        return True
    except Exception as e:
        print(f"   ❌ ファイル作成エラー: {e}")
        return False


def show_summary():
    """確認結果のまとめを表示"""
    print("\n" + "=" * 50)
    print("🎯 環境確認完了！")
    print("=" * 50)
    
    print("\n✅ 開発環境は正常に動作しています！")
    print("   Pythonプログラミングを始める準備が整いました。")
    
    print("\n📚 次のステップ:")
    print("\n1. 作成された 'my_first_program.py' を実行してみる")
    print("2. 基礎学習を開始する:")
    
    if platform.system() == "Windows":
        print("   py basics/01_interpreter_basics.py")
    else:
        print("   python3 basics/01_interpreter_basics.py")
    
    print("\n💡 学習のヒント:")
    print("   • エラーを恐れずに、どんどん試してみましょう")
    print("   • わからないことがあったら、エラーメッセージをよく読みましょう")
    print("   • 各章の最後には理解度テストがあります")


def main():
    """メイン処理"""
    print_banner()
    
    # 各種チェックを実行
    all_ok = True
    
    all_ok &= check_working_directory()
    all_ok &= check_file_operations()
    all_ok &= check_encoding()
    all_ok &= check_basic_execution()
    
    # 追加情報
    check_pip_availability()
    
    # 練習用ファイルを作成
    create_practice_file()
    
    # まとめ
    if all_ok:
        show_summary()
    else:
        print("\n⚠️  いくつかの問題が見つかりました。")
        print("   上記のエラーメッセージを確認してください。")
    
    print("\n" + "=" * 50)
    print("頑張ってください！ 🚀")
    print("=" * 50)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  プログラムが中断されました。")
    except Exception as e:
        print(f"\n❌ 予期しないエラーが発生しました: {e}")
        print("   このエラーメッセージをメモして、ヘルプを求めてください。")