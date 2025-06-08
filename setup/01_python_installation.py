#!/usr/bin/env python3
"""
=== Python インストール確認ツール ===

このプログラムは、お使いのコンピューターにPythonが正しく
インストールされているかを確認します。

実行方法:
  Windows: py setup/01_python_installation.py
  Mac/Linux: python3 setup/01_python_installation.py
"""

import sys
import platform
import os
from datetime import datetime


def print_banner():
    """プログラム開始時のバナーを表示"""
    print("=" * 50)
    print("🐍 Python インストール確認ツール")
    print("=" * 50)
    print()


def check_python_version():
    """Pythonのバージョンを確認"""
    print("📌 Pythonバージョン情報:")
    print(f"   バージョン: {sys.version.split()[0]}")
    print(f"   詳細: {sys.version}")
    print()
    
    # バージョン番号を分解
    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro
    
    # Python 3.8以上を推奨
    if major >= 3 and minor >= 8:
        print("✅ Pythonのバージョンは問題ありません！")
        return True
    elif major >= 3:
        print("⚠️  Python 3.8以上を推奨しています")
        print("   現在のバージョンでも学習は可能です")
        return True
    else:
        print("❌ Python 3が必要です")
        print("   Python 3をインストールしてください")
        return False


def check_system_info():
    """システム情報を表示"""
    print("\n📌 システム情報:")
    print(f"   OS: {platform.system()}")
    print(f"   OSバージョン: {platform.release()}")
    print(f"   マシンタイプ: {platform.machine()}")
    print(f"   プロセッサ: {platform.processor() or '情報なし'}")
    print(f"   現在時刻: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}")


def check_python_executable():
    """Python実行ファイルの場所を確認"""
    print("\n📌 Python実行ファイルの場所:")
    print(f"   {sys.executable}")
    
    # 仮想環境かどうかチェック
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("   ℹ️  仮想環境で実行されています")


def check_important_modules():
    """重要な標準モジュールの確認"""
    print("\n📌 標準モジュールの確認:")
    
    modules_to_check = [
        ('os', 'ファイル・ディレクトリ操作'),
        ('json', 'JSONデータの処理'),
        ('datetime', '日付・時刻の処理'),
        ('random', '乱数生成'),
        ('math', '数学関数'),
    ]
    
    all_ok = True
    for module_name, description in modules_to_check:
        try:
            __import__(module_name)
            print(f"   ✅ {module_name}: {description}")
        except ImportError:
            print(f"   ❌ {module_name}: インポートできません")
            all_ok = False
    
    return all_ok


def show_next_steps():
    """次のステップを表示"""
    print("\n" + "=" * 50)
    print("📚 次のステップ")
    print("=" * 50)
    
    print("\n環境の動作確認を行いましょう:")
    
    if platform.system() == "Windows":
        print("   py setup/02_environment_check.py")
    else:
        print("   python3 setup/02_environment_check.py")
    
    print("\nその後、基礎学習を開始できます:")
    
    if platform.system() == "Windows":
        print("   py basics/01_interpreter_basics.py")
    else:
        print("   python3 basics/01_interpreter_basics.py")


def main():
    """メイン処理"""
    print_banner()
    
    # 各種チェックを実行
    version_ok = check_python_version()
    check_system_info()
    check_python_executable()
    modules_ok = check_important_modules()
    
    # 総合判定
    print("\n" + "=" * 50)
    print("🎯 総合判定")
    print("=" * 50)
    
    if version_ok and modules_ok:
        print("\n✅ Pythonは正しくインストールされています！")
        print("   プログラミング学習を始める準備ができました。")
        show_next_steps()
    else:
        print("\n⚠️  いくつか問題があります。")
        print("   上記のメッセージを確認して対処してください。")
        
        if not version_ok:
            print("\n💡 ヒント:")
            print("   Python 3の最新版を公式サイトからダウンロード:")
            print("   https://www.python.org/downloads/")
    
    print("\n" + "=" * 50)
    print("頑張ってください！ 🚀")
    print("=" * 50)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ エラーが発生しました: {e}")
        print("   このエラーメッセージをメモして、ヘルプを求めてください。")