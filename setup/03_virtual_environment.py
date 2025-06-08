#!/usr/bin/env python3
"""
=== 仮想環境入門 ===

このファイルは basics/12_external_libraries.py を完了してから
学習してください。

仮想環境は、プロジェクトごとに独立したPython環境を作成する
仕組みです。異なるプロジェクトで異なるバージョンのライブラリを
使い分けることができます。

実行方法:
  Windows: py setup/03_virtual_environment.py
  Mac/Linux: python3 setup/03_virtual_environment.py
"""

import os
import sys
import platform
import subprocess
from pathlib import Path


def print_banner():
    """プログラム開始時のバナーを表示"""
    print("=" * 50)
    print("🌐 Python仮想環境入門")
    print("=" * 50)
    print()


def check_prerequisites():
    """前提条件の確認"""
    print("📌 前提条件の確認:")
    
    # basics/12の完了確認（簡易的）
    print("\n⚠️  このレッスンを始める前に:")
    print("   1. basics/01-11 を完了していること")
    print("   2. basics/12_external_libraries.py を完了していること")
    print("   3. pip の基本的な使い方を理解していること")
    
    response = input("\n上記を完了していますか？ (yes/no): ").lower()
    
    if response != 'yes':
        print("\n💡 まずは basics/12_external_libraries.py を完了してください！")
        return False
    
    print("\n✅ 素晴らしい！仮想環境について学びましょう。")
    return True


def explain_virtual_environment():
    """仮想環境の概念を説明"""
    print("\n" + "=" * 50)
    print("📚 仮想環境とは？")
    print("=" * 50)
    
    print("""
仮想環境は「プロジェクト専用の部屋」のようなものです。

🏠 例えで説明すると:
   • あなたの家（コンピューター）に複数の部屋（仮想環境）がある
   • 各部屋には異なる家具（ライブラリ）を置ける
   • 部屋Aには本棚v1.0、部屋Bには本棚v2.0を置ける
   • 部屋ごとに独立しているので、干渉しない

💡 なぜ必要？
   1. プロジェクトAは requests 2.25.0 が必要
   2. プロジェクトBは requests 2.31.0 が必要
   3. 仮想環境なしでは、同時に両方を満たせない
   4. 仮想環境があれば、各プロジェクトで異なるバージョンを使える
""")
    
    input("\nEnterキーを押して続ける...")


def demonstrate_venv_creation():
    """仮想環境の作成方法を実演"""
    print("\n" + "=" * 50)
    print("🛠️ 仮想環境の作成")
    print("=" * 50)
    
    venv_name = "tutorial-env"
    
    print(f"\n仮想環境 '{venv_name}' を作成するコマンド:")
    print(f"   {sys.executable} -m venv {venv_name}")
    
    print("\n実行してみましょうか？")
    print("（デモ用の仮想環境を作成します）")
    
    response = input("\n作成しますか？ (yes/no): ").lower()
    
    if response == 'yes':
        try:
            print(f"\n仮想環境を作成中...")
            subprocess.run([sys.executable, '-m', 'venv', venv_name], check=True)
            print(f"✅ 仮想環境 '{venv_name}' を作成しました！")
            
            # ディレクトリ構造を表示
            print(f"\n📁 作成されたディレクトリ:")
            venv_path = Path(venv_name)
            if venv_path.exists():
                for item in sorted(venv_path.iterdir())[:5]:  # 最初の5個だけ表示
                    print(f"   - {item.name}/")
                print("   ...")
            
            return venv_name
        except Exception as e:
            print(f"❌ エラー: {e}")
            return None
    else:
        print("\n💡 後で自分で作成してみてください！")
        return None


def show_activation_commands(venv_name):
    """仮想環境の有効化コマンドを表示"""
    print("\n" + "=" * 50)
    print("🚀 仮想環境の有効化")
    print("=" * 50)
    
    print("\n仮想環境を有効化するコマンド:")
    
    if platform.system() == "Windows":
        print(f"\n   # Windows (コマンドプロンプト)")
        print(f"   {venv_name}\\Scripts\\activate.bat")
        print(f"\n   # Windows (PowerShell)")
        print(f"   {venv_name}\\Scripts\\Activate.ps1")
    else:
        print(f"\n   # Mac/Linux")
        print(f"   source {venv_name}/bin/activate")
    
    print("\n📌 有効化すると:")
    print(f"   • プロンプトに ({venv_name}) が表示される")
    print("   • pip install したパッケージは仮想環境内にインストールされる")
    print("   • 他のプロジェクトに影響を与えない")
    
    print("\n無効化するコマンド:")
    print("   deactivate")


def show_practical_workflow():
    """実践的なワークフローを表示"""
    print("\n" + "=" * 50)
    print("📋 実践的なワークフロー")
    print("=" * 50)
    
    print("""
プロジェクトでの仮想環境の使い方:

1️⃣ プロジェクトディレクトリを作成
   mkdir my-weather-app
   cd my-weather-app

2️⃣ 仮想環境を作成
   python3 -m venv venv

3️⃣ 仮想環境を有効化
   # Mac/Linux
   source venv/bin/activate
   
   # Windows
   venv\\Scripts\\activate

4️⃣ 必要なパッケージをインストール
   pip install requests
   pip install beautifulsoup4

5️⃣ requirements.txt に記録
   pip freeze > requirements.txt

6️⃣ 開発作業
   # コードを書く、実行する

7️⃣ 作業終了時は無効化
   deactivate
""")


def show_best_practices():
    """ベストプラクティスを表示"""
    print("\n" + "=" * 50)
    print("✨ ベストプラクティス")
    print("=" * 50)
    
    print("""
仮想環境を使う際の推奨事項:

✅ DO（やるべきこと）:
   • プロジェクトごとに仮想環境を作成
   • requirements.txt でパッケージを管理
   • .gitignore に仮想環境フォルダを追加
   • README.md に環境構築手順を記載

❌ DON'T（やってはいけないこと）:
   • 仮想環境をGitにコミットしない
   • グローバル環境に直接パッケージをインストールしない
   • 仮想環境の中身を直接編集しない

💡 名前の慣例:
   • venv: 最も一般的
   • .venv: 隠しフォルダにしたい場合
   • env: シンプルな名前
   • プロジェクト名-env: 明示的な名前
""")


def cleanup_demo(venv_name):
    """デモ用仮想環境のクリーンアップ"""
    if venv_name and Path(venv_name).exists():
        print(f"\n🧹 デモ用仮想環境 '{venv_name}' を削除しますか？")
        response = input("削除する？ (yes/no): ").lower()
        
        if response == 'yes':
            try:
                import shutil
                shutil.rmtree(venv_name)
                print("✅ 削除しました")
            except Exception as e:
                print(f"❌ 削除エラー: {e}")
                print("   手動で削除してください")


def show_next_steps():
    """次のステップを表示"""
    print("\n" + "=" * 50)
    print("🎯 次のステップ")
    print("=" * 50)
    
    print("""
仮想環境の基本を学びました！

次は実際のプロジェクトで使ってみましょう:
   1. projects/04_weather_app/ で仮想環境を作成
   2. 必要なパッケージをインストール
   3. アプリケーションを開発

プロジェクト開始コマンド:""")
    
    if platform.system() == "Windows":
        print("   py projects/04_weather_app/README.md")
    else:
        print("   python3 projects/04_weather_app/README.md")
    
    print("\n💪 仮想環境をマスターして、")
    print("   プロフェッショナルな開発環境を構築しましょう！")


def main():
    """メイン処理"""
    print_banner()
    
    # 前提条件の確認
    if not check_prerequisites():
        return
    
    # 仮想環境の説明
    explain_virtual_environment()
    
    # 仮想環境の作成デモ
    venv_name = demonstrate_venv_creation()
    
    # 有効化方法の説明
    if venv_name:
        show_activation_commands(venv_name)
    else:
        show_activation_commands("venv")  # 例として表示
    
    # 実践的なワークフロー
    show_practical_workflow()
    
    # ベストプラクティス
    show_best_practices()
    
    # クリーンアップ
    if venv_name:
        cleanup_demo(venv_name)
    
    # 次のステップ
    show_next_steps()
    
    print("\n" + "=" * 50)
    print("お疲れ様でした！ 🎉")
    print("=" * 50)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  プログラムが中断されました。")
    except Exception as e:
        print(f"\n❌ エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()