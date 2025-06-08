#!/usr/bin/env python3
"""
===========================
第12章: 外部ライブラリ
===========================

Pythonの力を最大限に活用するための外部ライブラリの
使い方を学習します。pip を使ったパッケージ管理、
人気のライブラリの紹介、仮想環境の活用など
実践的なPython開発に欠かせない知識を習得しましょう。

このファイルを実行すると、Python生態系の豊富さを
実感できます。
"""

import platform
import subprocess
import sys
from pathlib import Path


def print_chapter_header():
    """章のヘッダーを表示"""
    print("=" * 50)
    print("第12章: 外部ライブラリ")
    print("=" * 50)
    print()


def lesson_1_package_management():
    """レッスン1: パッケージ管理（pip）"""
    print("📚 レッスン1: パッケージ管理（pip）")
    print("-" * 40)
    print()
    
    print("pip は Python のパッケージ管理ツールです。")
    print("PyPI（Python Package Index）から簡単にインストールできます。")
    print()
    
    # pipの基本コマンド
    print("pip の基本コマンド:")
    print()
    print("パッケージのインストール:")
    print(">>> pip install requests")
    print(">>> pip install pandas numpy matplotlib")
    print()
    
    print("特定バージョンのインストール:")
    print(">>> pip install django==3.2.0")
    print(">>> pip install 'numpy>=1.20,<2.0'")
    print()
    
    print("インストール済みパッケージの確認:")
    print(">>> pip list")
    print()
    
    print("パッケージ情報の表示:")
    print(">>> pip show requests")
    print()
    
    print("パッケージのアップグレード:")
    print(">>> pip install --upgrade requests")
    print()
    
    print("パッケージのアンインストール:")
    print(">>> pip uninstall requests")
    print()
    
    # requirements.txt
    print("requirements.txt で依存関係を管理:")
    print()
    print("# requirements.txt の例")
    print("-" * 30)
    print("requests==2.28.1")
    print("pandas>=1.4.0")
    print("matplotlib")
    print("numpy~=1.21.0")
    print("-" * 30)
    print()
    
    print(">>> pip install -r requirements.txt  # 一括インストール")
    print(">>> pip freeze > requirements.txt    # 現在の環境を保存")
    print()
    
    # 現在インストールされているパッケージの確認
    print("現在の環境にインストールされているパッケージ（一部）:")
    try:
        import pkg_resources
        installed = [pkg.project_name for pkg in pkg_resources.working_set]
        # 標準的でないパッケージのみ表示（簡易版）
        common_external = [pkg for pkg in installed if pkg.lower() in 
                          ['requests', 'numpy', 'pandas', 'matplotlib', 'django', 
                           'flask', 'pillow', 'beautifulsoup4', 'selenium']]
        if common_external:
            for pkg in common_external[:5]:
                print(f"  ✅ {pkg}")
        else:
            print("  （外部ライブラリは検出されませんでした）")
    except ImportError:
        print("  （パッケージ情報を取得できませんでした）")
    print()
    
    print("💡 PyPI (https://pypi.org) で利用可能なパッケージを")
    print("   検索してみましょう")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_2_virtual_environments():
    """レッスン2: 仮想環境"""
    print("📚 レッスン2: 仮想環境")
    print("-" * 40)
    print()
    
    print("仮想環境で、プロジェクトごとに独立した")
    print("Python環境を作成できます。")
    print()
    
    # venv の使い方
    print("venv モジュールを使った仮想環境:")
    print()
    print("仮想環境の作成:")
    print(">>> python -m venv myproject_env")
    print(">>> # myproject_env/ ディレクトリが作成される")
    print()
    
    print("仮想環境の有効化:")
    if platform.system() == "Windows":
        print(">>> myproject_env\\Scripts\\activate      # Windows")
    else:
        print(">>> source myproject_env/bin/activate    # Mac/Linux")
    print(">>> # プロンプトが (myproject_env) で始まる")
    print()
    
    print("パッケージのインストール（仮想環境内）:")
    print(">>> pip install requests pandas")
    print(">>> # この環境でのみ利用可能")
    print()
    
    print("仮想環境の無効化:")
    print(">>> deactivate")
    print()
    
    # 仮想環境の利点
    print("仮想環境のメリット:")
    print("• プロジェクト間でのライブラリの競合を回避")
    print("• 異なるバージョンのライブラリを使い分け")
    print("• クリーンな環境でのテスト")
    print("• 本番環境の再現")
    print()
    
    # その他の仮想環境ツール
    print("その他の仮想環境ツール:")
    print("• virtualenv - より高機能な仮想環境")
    print("• conda - 科学計算に特化したパッケージ管理")
    print("• poetry - 依存関係管理とビルドツール")
    print("• pipenv - pip と virtualenv の統合")
    print()
    
    print("💡 新しいプロジェクトを始める時は")
    print("   必ず仮想環境を作成しましょう")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_3_popular_libraries():
    """レッスン3: 人気のライブラリ紹介"""
    print("📚 レッスン3: 人気のライブラリ紹介")
    print("-" * 40)
    print()
    
    print("Pythonで広く使われている外部ライブラリを紹介します。")
    print()
    
    # Webフレームワーク
    print("🌐 Webフレームワーク:")
    print()
    print("Django:")
    print("• フルスタックWebフレームワーク")
    print("• 管理画面、ORM、認証機能が標準装備")
    print(">>> pip install django")
    print()
    
    print("Flask:")
    print("• 軽量でシンプルなWebフレームワーク")
    print("• 小さなアプリやAPIに最適")
    print(">>> pip install flask")
    print()
    
    print("FastAPI:")
    print("• 高速なAPI開発フレームワーク")
    print("• 自動的なAPI ドキュメント生成")
    print(">>> pip install fastapi")
    print()
    
    # データ分析・科学計算
    print("📊 データ分析・科学計算:")
    print()
    print("NumPy:")
    print("• 数値計算の基盤ライブラリ")
    print("• 多次元配列と数学関数")
    print(">>> pip install numpy")
    print()
    
    print("pandas:")
    print("• データ分析・操作のためのライブラリ")
    print("• CSV、Excel、データベースとの連携")
    print(">>> pip install pandas")
    print()
    
    print("matplotlib:")
    print("• グラフ・可視化ライブラリ")
    print("• 様々な種類のグラフを作成")
    print(">>> pip install matplotlib")
    print()
    
    print("scikit-learn:")
    print("• 機械学習ライブラリ")
    print("• 分類、回帰、クラスタリングなど")
    print(">>> pip install scikit-learn")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()
    
    # その他の便利なライブラリ
    print("🔧 その他の便利なライブラリ:")
    print()
    print("requests:")
    print("• HTTP リクエストライブラリ")
    print("• Web API の利用に必須")
    print(">>> pip install requests")
    print()
    
    print("Beautiful Soup:")
    print("• HTML/XML パーサー")
    print("• Webスクレイピングに便利")
    print(">>> pip install beautifulsoup4")
    print()
    
    print("Pillow (PIL):")
    print("• 画像処理ライブラリ")
    print("• 画像の読み込み、編集、保存")
    print(">>> pip install Pillow")
    print()
    
    print("python-dotenv:")
    print("• 環境変数を .env ファイルから読み込み")
    print("• 設定の管理に便利")
    print(">>> pip install python-dotenv")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_4_library_examples():
    """レッスン4: ライブラリの使用例"""
    print("📚 レッスン4: ライブラリの使用例")
    print("-" * 40)
    print()
    
    print("実際にライブラリを使った簡単な例を見てみましょう。")
    print("（ライブラリがインストールされていない場合は概要のみ）")
    print()
    
    # requests の例
    print("requests ライブラリの例:")
    print(">>> import requests")
    print(">>> ")
    print(">>> # Web API からデータを取得")
    print(">>> response = requests.get('https://api.github.com/user', ")
    print("...                         headers={'User-Agent': 'Python-Tutorial'})")
    print(">>> if response.status_code == 200:")
    print("...     data = response.json()")
    print("...     print(f'取得成功: {len(data)} 件のデータ')")
    print()
    
    # pandas の例（概要）
    print("pandas ライブラリの例:")
    print(">>> import pandas as pd")
    print(">>> ")
    print(">>> # CSV ファイルの読み込み")
    print(">>> df = pd.read_csv('data.csv')")
    print(">>> print(df.head())  # 最初の5行を表示")
    print(">>> ")
    print(">>> # データの集計")
    print(">>> summary = df.groupby('category').sum()")
    print(">>> print(summary)")
    print()
    
    # matplotlib の例（概要）
    print("matplotlib ライブラリの例:")
    print(">>> import matplotlib.pyplot as plt")
    print(">>> ")
    print(">>> # 簡単なグラフの作成")
    print(">>> x = [1, 2, 3, 4, 5]")
    print(">>> y = [2, 4, 6, 8, 10]")
    print(">>> plt.plot(x, y)")
    print(">>> plt.title('簡単な線グラフ')")
    print(">>> plt.xlabel('X軸')")
    print(">>> plt.ylabel('Y軸')")
    print(">>> plt.show()  # グラフを表示")
    print()
    
    # 実際に requests を試してみる（あれば）
    print("実際の例（使用可能な場合）:")
    try:
        import requests
        print("✅ requests が利用可能です")
        print(">>> # JSONPlaceholder API を使った例")
        print(">>> response = requests.get('https://jsonplaceholder.typicode.com/posts/1')")
        
        try:
            response = requests.get('https://jsonplaceholder.typicode.com/posts/1', timeout=3)
            if response.status_code == 200:
                data = response.json()
                print(f">>> response.status_code  # {response.status_code}")
                print(f">>> data['title'][:30] + '...'  # '{data['title'][:30]}...'")
            else:
                print(f">>> response.status_code  # {response.status_code}")
        except Exception as e:
            print(f">>> # ネットワークエラー: {type(e).__name__}")
    except ImportError:
        print("ℹ️  requests がインストールされていません")
        print("   インストール方法: pip install requests")
    
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_5_library_selection():
    """レッスン5: ライブラリの選び方"""
    print("📚 レッスン5: ライブラリの選び方")
    print("-" * 40)
    print()
    
    print("適切なライブラリを選ぶための基準を学びます。")
    print()
    
    # 選択基準
    print("ライブラリ選択の基準:")
    print()
    print("1. アクティブな開発:")
    print("   • 最近のコミット履歴")
    print("   • 継続的なリリース")
    print("   • GitHub のスター数、フォーク数")
    print()
    
    print("2. ドキュメントの品質:")
    print("   • 分かりやすい説明")
    print("   • 豊富な使用例")
    print("   • API リファレンス")
    print()
    
    print("3. コミュニティサポート:")
    print("   • Stack Overflow での質問・回答")
    print("   • GitHub Issues の対応状況")
    print("   • チュートリアルやブログ記事")
    print()
    
    print("4. 依存関係:")
    print("   • 必要な他ライブラリの数")
    print("   • ライセンスの互換性")
    print("   • セキュリティアップデートの頻度")
    print()
    
    # 信頼できるソース
    print("信頼できる情報源:")
    print("• PyPI (https://pypi.org) - 公式パッケージリポジトリ")
    print("• GitHub - ソースコードとIssues")
    print("• Read the Docs - ドキュメント")
    print("• Stack Overflow - 質問と回答")
    print("• Python.org - 公式推奨")
    print()
    
    # 目的別推奨ライブラリ
    print("目的別推奨ライブラリ:")
    print()
    print("Web開発: Django, Flask, FastAPI")
    print("データ分析: pandas, NumPy, matplotlib")
    print("機械学習: scikit-learn, TensorFlow, PyTorch")
    print("HTTP通信: requests, httpx")
    print("スクレイピング: Beautiful Soup, Scrapy")
    print("GUI: tkinter（標準）, PyQt, Kivy")
    print("テスト: pytest, unittest（標準）")
    print("型チェック: mypy, pydantic")
    print()
    
    print("💡 まずは公式ドキュメントとサンプルコードを")
    print("   確認してから導入を検討しましょう")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_6_development_workflow():
    """レッスン6: 開発ワークフロー"""
    print("📚 レッスン6: 外部ライブラリを使った開発ワークフロー")
    print("-" * 40)
    print()
    
    print("外部ライブラリを活用した実践的な開発手順を学びます。")
    print()
    
    # プロジェクト開始手順
    print("新規プロジェクトの開始手順:")
    print()
    print("1. プロジェクトディレクトリの作成:")
    print(">>> mkdir my_awesome_project")
    print(">>> cd my_awesome_project")
    print()
    
    print("2. 仮想環境の作成・有効化:")
    print(">>> python -m venv venv")
    if platform.system() == "Windows":
        print(">>> venv\\Scripts\\activate")
    else:
        print(">>> source venv/bin/activate")
    print()
    
    print("3. 必要なライブラリのインストール:")
    print(">>> pip install requests pandas matplotlib")
    print(">>> pip freeze > requirements.txt")
    print()
    
    print("4. プロジェクト構造の作成:")
    print("my_awesome_project/")
    print("├── venv/                 # 仮想環境")
    print("├── src/                  # ソースコード")
    print("│   ├── __init__.py")
    print("│   └── main.py")
    print("├── tests/                # テストコード")
    print("│   └── test_main.py")
    print("├── docs/                 # ドキュメント")
    print("├── requirements.txt      # 依存関係")
    print("├── README.md            # プロジェクト説明")
    print("└── .gitignore           # Git除外設定")
    print()
    
    # .gitignore の例
    print("5. .gitignore の設定:")
    print("# .gitignore の例")
    print("-" * 30)
    print("venv/")
    print("__pycache__/")
    print("*.pyc")
    print(".env")
    print("*.log")
    print(".DS_Store")
    print("-" * 30)
    print()
    
    # 開発サイクル
    print("開発サイクル:")
    print("1. 機能の実装")
    print("2. テストの作成・実行")
    print("3. ドキュメントの更新")
    print("4. コードレビュー")
    print("5. バージョン管理（Git）")
    print("6. デプロイ")
    print()
    
    # バージョン管理
    print("ライブラリのバージョン管理:")
    print("• requirements.txt で明確にバージョンを指定")
    print("• 定期的なアップデート計画")
    print("• 破壊的変更への対応準備")
    print("• セキュリティアップデートの迅速な適用")
    print()
    
    print("💡 チーム開発では、全員が同じ環境で")
    print("   作業できるよう環境構築を自動化しましょう")
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
    
    print("【練習1】仮想環境の作成")
    print("新しい仮想環境を作成し、requests をインストール")
    print("簡単なAPIリクエストを実行")
    print()
    
    print("【練習2】requirements.txt の管理")
    print("現在の環境の requirements.txt を作成")
    print("新しい環境で requirements.txt からインストール")
    print()
    
    print("【練習3】ライブラリの調査")
    print("興味のある分野のライブラリを PyPI で検索")
    print("ドキュメントを読んで使用例を理解")
    print()
    
    print("【練習4】小さなプロジェクト")
    print("requests と json を使って天気情報を取得")
    print("結果をファイルに保存するプログラムを作成")
    print()
    
    print("【練習5】プロジェクト構造の作成")
    print("適切なディレクトリ構造を持つプロジェクトを作成")
    print("仮想環境、.gitignore、README.md を含める")
    print()
    
    input("練習が終わったらEnterキーを押してください...")
    print()


def show_next_steps():
    """次のステップ"""
    print("🚀 次のステップ")
    print("=" * 50)
    print()
    
    print("基礎学習完了後の学習パス:")
    print()
    
    print("1. 専門分野への深堀り:")
    print("   • Web開発: Django/Flask チュートリアル")
    print("   • データ分析: pandas/NumPy の詳細学習")
    print("   • 機械学習: scikit-learn や TensorFlow")
    print("   • 自動化: Selenium や automation スクリプト")
    print()
    
    print("2. 開発スキルの向上:")
    print("   • テスト駆動開発 (pytest)")
    print("   • コード品質管理 (black, flake8, mypy)")
    print("   • Git/GitHub の活用")
    print("   • CI/CD パイプライン")
    print()
    
    print("3. アーキテクチャとデザインパターン:")
    print("   • オブジェクト指向設計の深化")
    print("   • デザインパターンの学習")
    print("   • アーキテクチャパターン")
    print("   • パフォーマンス最適化")
    print()
    
    print("4. 実践プロジェクト:")
    print("   • 個人プロジェクトの開発")
    print("   • オープンソースへの貢献")
    print("   • ポートフォリオの構築")
    print("   • 技術ブログの執筆")
    print()
    
    print("5. コミュニティ参加:")
    print("   • Python勉強会への参加")
    print("   • PyCon などの技術カンファレンス")
    print("   • オンラインコミュニティ")
    print("   • メンターやメンティー関係")
    print()
    
    print("推奨リソース:")
    print("• 公式ドキュメント: https://docs.python.org/ja/")
    print("• PyPI: https://pypi.org/")
    print("• Real Python: https://realpython.com/")
    print("• Python.org: https://www.python.org/")
    print()


def show_summary():
    """まとめ"""
    print("📝 第12章のまとめ")
    print("=" * 50)
    print()
    
    print("外部ライブラリについて学んだこと：")
    print("✅ pip による パッケージ管理")
    print("✅ 仮想環境の作成と活用")
    print("✅ requirements.txt による依存関係管理")
    print("✅ 人気ライブラリの紹介と特徴")
    print("✅ ライブラリ選択の基準")
    print("✅ 実践的な開発ワークフロー")
    print()
    
    print("外部ライブラリ活用のメリット：")
    print("• 開発効率の大幅な向上")
    print("• 高品質なコードの再利用")
    print("• 専門分野への素早いアクセス")
    print("• コミュニティのベストプラクティス活用")
    print()
    
    print("重要なポイント：")
    print("• 仮想環境で依存関係を管理")
    print("• ライブラリ選択は慎重に")
    print("• ドキュメントを必ず確認")
    print("• セキュリティアップデートに注意")
    print()
    
    print("次のステップ：")
    print("• 興味のある分野の深堀り学習")
    print("• 実際のプロジェクトでの実践")
    print("• コミュニティへの参加")
    print()


def show_completion_message():
    """完了メッセージ"""
    print("\n" + "🎉" * 50)
    print("        🎓 Python基礎学習 完全制覇！ 🎓        ")
    print("🎉" * 50)
    
    print(f"\n🏆 おめでとうございます！")
    print("全12章のPython基礎学習が完了しました！")
    print()
    
    print("📚 学習した内容:")
    print("01. インタープリター基礎   02. 数値と文字列")
    print("03. リストとシーケンス     04. 制御フロー")
    print("05. 関数                   06. データ構造")
    print("07. モジュールとパッケージ 08. 入出力処理")
    print("09. エラーと例外処理       10. クラスとオブジェクト")
    print("11. 標準ライブラリ         12. 外部ライブラリ")
    print()
    
    print(f"📚 最後の理解度テストを受けましょう")
    print("以下のコマンドをコピー&ペーストして実行してください:\n")
    
    # OS別コマンド表示
    python_cmd = "py" if platform.system() == "Windows" else "python3"
    print(f"   {python_cmd} quizzes/quiz_runner.py basics 12")
    
    print(f"\n🚀 次のステップに進みましょう:")
    print(f"   {python_cmd} exercises/")
    print(f"   {python_cmd} projects/")
    
    print("\n💡 困ったときは:")
    print(f"   {python_cmd} quizzes/quiz_runner.py help")
    
    print("\n" + "=" * 50)
    print("        Python の旅はここから始まります！        ")
    print("        Keep coding and have fun! 🐍✨        ")
    print("=" * 50)


def main():
    """メイン処理"""
    print_chapter_header()
    
    # 各レッスンを順番に実行
    lesson_1_package_management()
    lesson_2_virtual_environments()
    lesson_3_popular_libraries()
    lesson_4_library_examples()
    lesson_5_library_selection()
    lesson_6_development_workflow()
    
    # 練習問題
    practice_exercises()
    
    # 次のステップ
    show_next_steps()
    
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