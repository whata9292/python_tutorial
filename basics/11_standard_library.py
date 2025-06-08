#!/usr/bin/env python3
"""
===========================
第11章: 標準ライブラリ
===========================

Pythonに付属する豊富な標準ライブラリを活用する方法を学習します。
ファイル操作、日時処理、数学計算、ネットワーク通信など
実用的なプログラムに必要な機能を習得しましょう。

このファイルを実行すると、標準ライブラリの威力を
実感できます。
"""

import platform
import os
import sys
import datetime
import time
import random
import math
import re
import urllib.request
import json
import csv
import logging
from pathlib import Path
from collections import defaultdict, Counter
from itertools import combinations, permutations


def print_chapter_header():
    """章のヘッダーを表示"""
    print("=" * 50)
    print("第11章: 標準ライブラリ")
    print("=" * 50)
    print()


def lesson_1_datetime_time():
    """レッスン1: 日時処理（datetime、time）"""
    print("📚 レッスン1: 日時処理（datetime、time）")
    print("-" * 40)
    print()
    
    print("日付と時刻の処理は多くのプログラムで必要です。")
    print()
    
    # datetime の基本
    print("datetime モジュール:")
    print(">>> from datetime import datetime, date, time, timedelta")
    print(">>> ")
    now = datetime.now()
    print(f">>> now = datetime.now()  # {now}")
    print()
    
    # 日付の作成
    print("特定の日付の作成:")
    birthday = datetime(1990, 5, 15, 14, 30)
    print(f">>> birthday = datetime(1990, 5, 15, 14, 30)")
    print(f">>> birthday  # {birthday}")
    print()
    
    # 日付の操作
    print("日付の計算:")
    print(">>> from datetime import timedelta")
    tomorrow = now + timedelta(days=1)
    print(f">>> tomorrow = now + timedelta(days=1)")
    print(f">>> tomorrow  # {tomorrow.strftime('%Y年%m月%d日')}")
    
    next_week = now + timedelta(weeks=1)
    print(f">>> next_week = now + timedelta(weeks=1)")
    print(f">>> next_week  # {next_week.strftime('%Y年%m月%d日')}")
    print()
    
    # フォーマット
    print("日付のフォーマット:")
    formats = [
        ('%Y-%m-%d', '年-月-日'),
        ('%Y年%m月%d日', '日本語形式'),
        ('%A, %B %d, %Y', '英語長形式'),
        ('%H:%M:%S', '時:分:秒'),
    ]
    
    for fmt, desc in formats:
        print(f">>> now.strftime('{fmt}')  # '{now.strftime(fmt)}'  ({desc})")
    print()
    
    # 文字列から日付へ
    print("文字列から日付オブジェクトへ:")
    date_str = "2024-12-25"
    print(f">>> date_str = '{date_str}'")
    print(">>> parsed = datetime.strptime(date_str, '%Y-%m-%d')")
    parsed = datetime.strptime(date_str, '%Y-%m-%d')
    print(f">>> parsed  # {parsed}")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_2_os_sys():
    """レッスン2: システム操作（os、sys）"""
    print("📚 レッスン2: システム操作（os、sys）")
    print("-" * 40)
    print()
    
    print("システム情報の取得とファイルシステムの操作を学びます。")
    print()
    
    # os モジュール
    print("os モジュール（ファイルシステム）:")
    print(f">>> os.getcwd()  # '{os.getcwd()}'  （現在ディレクトリ）")
    print(f">>> os.name      # '{os.name}'  （OS名）")
    print()
    
    # 環境変数
    print("環境変数の取得:")
    path_var = os.environ.get('PATH', '未設定')
    print(f">>> os.environ.get('PATH')[:50] + '...'")
    print(f"    '{path_var[:50]}...'")
    
    # ユーザーディレクトリ
    home = os.path.expanduser('~')
    print(f">>> os.path.expanduser('~')  # '{home}'  （ホームディレクトリ）")
    print()
    
    # sys モジュール
    print("sys モジュール（Python実行環境）:")
    print(f">>> sys.version[:20] + '...'  # '{sys.version[:20]}...'  （Pythonバージョン）")
    print(f">>> sys.platform  # '{sys.platform}'  （プラットフォーム）")
    print(f">>> len(sys.path)  # {len(sys.path)}  （モジュール検索パス数）")
    print()
    
    # コマンドライン引数（シミュレート）
    print("コマンドライン引数:")
    print(">>> import sys")
    print(">>> # sys.argv  # ['script.py', 'arg1', 'arg2', ...]")
    print(f">>> sys.argv[0]  # '{sys.argv[0]}'  （スクリプト名）")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_3_math_random():
    """レッスン3: 数学とランダム（math、random）"""
    print("📚 レッスン3: 数学とランダム（math、random）")
    print("-" * 40)
    print()
    
    print("数学計算とランダム処理の機能を学びます。")
    print()
    
    # math モジュール
    print("math モジュール:")
    print(f">>> math.pi      # {math.pi}")
    print(f">>> math.e       # {math.e}")
    print(f">>> math.sqrt(16)  # {math.sqrt(16)}")
    print(f">>> math.ceil(3.2)  # {math.ceil(3.2)}")
    print(f">>> math.floor(3.8)  # {math.floor(3.8)}")
    print(f">>> math.sin(math.pi/2)  # {math.sin(math.pi/2):.1f}")
    print(f">>> math.log(math.e)  # {math.log(math.e):.1f}")
    print()
    
    # random モジュール
    print("random モジュール:")
    random.seed(42)  # 再現性のため
    print(">>> import random")
    print(">>> random.seed(42)  # シードを設定（再現性のため）")
    print()
    
    print(f">>> random.random()  # {random.random():.3f}  （0.0-1.0の小数）")
    print(f">>> random.randint(1, 10)  # {random.randint(1, 10)}  （1-10の整数）")
    print(f">>> random.uniform(1.0, 10.0)  # {random.uniform(1.0, 10.0):.2f}  （1.0-10.0の小数）")
    print()
    
    choices = ['apple', 'banana', 'orange', 'grape']
    print(f">>> choices = {choices}")
    print(f">>> random.choice(choices)  # '{random.choice(choices)}'  （1つ選択）")
    sample = random.sample(choices, 2)
    print(f">>> random.sample(choices, 2)  # {sample}  （重複なし2つ選択）")
    print()
    
    # リストのシャッフル
    numbers = [1, 2, 3, 4, 5]
    print(f">>> numbers = {numbers}")
    shuffled = numbers.copy()
    random.shuffle(shuffled)
    print(f">>> random.shuffle(numbers)  # {shuffled}  （元のリストを変更）")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_4_regex():
    """レッスン4: 正規表現（re）"""
    print("📚 レッスン4: 正規表現（re）")
    print("-" * 40)
    print()
    
    print("文字列のパターンマッチングに便利な正規表現を学びます。")
    print()
    
    # 基本的なマッチング
    print("基本的なマッチング:")
    text = "私の電話番号は090-1234-5678です。"
    phone_pattern = r'\d{3}-\d{4}-\d{4}'
    
    print(f">>> text = '{text}'")
    print(f">>> phone_pattern = r'{phone_pattern}'")
    print(">>> match = re.search(phone_pattern, text)")
    match = re.search(phone_pattern, text)
    if match:
        print(f">>> match.group()  # '{match.group()}'")
    print()
    
    # メールアドレスの検索
    print("メールアドレスの抽出:")
    email_text = "連絡先: john@example.com, alice@test.org"
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    print(f">>> email_text = '{email_text}'")
    print(">>> email_pattern = r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'")
    emails = re.findall(email_pattern, email_text)
    print(f">>> re.findall(email_pattern, email_text)")
    print(f"    {emails}")
    print()
    
    # 文字列の置換
    print("文字列の置換:")
    masked_text = re.sub(r'\d{3}-\d{4}-\d{4}', 'XXX-XXXX-XXXX', text)
    print(">>> masked = re.sub(r'\\d{3}-\\d{4}-\\d{4}', 'XXX-XXXX-XXXX', text)")
    print(f">>> masked  # '{masked_text}'")
    print()
    
    # 分割
    print("文字列の分割:")
    data = "apple,banana;orange:grape"
    print(f">>> data = '{data}'")
    parts = re.split(r'[,;:]', data)
    print(">>> re.split(r'[,;:]', data)")
    print(f"    {parts}")
    print()
    
    print("💡 正規表現は強力ですが、複雑になりすぎないよう注意")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_5_collections_itertools():
    """レッスン5: コレクションとイテレータ（collections、itertools）"""
    print("📚 レッスン5: コレクションとイテレータ（collections、itertools）")
    print("-" * 40)
    print()
    
    print("高度なデータ構造と効率的なループ処理を学びます。")
    print()
    
    # collections.Counter
    print("collections.Counter（要素の計数）:")
    text = "hello world"
    print(f">>> text = '{text}'")
    counter = Counter(text)
    print(f">>> counter = Counter(text)")
    print(f">>> counter  # {dict(counter)}")
    print(f">>> counter.most_common(3)  # {counter.most_common(3)}")
    print()
    
    # collections.defaultdict
    print("collections.defaultdict（デフォルト値付き辞書）:")
    print(">>> from collections import defaultdict")
    groups = defaultdict(list)
    students = [('A組', '太郎'), ('B組', '花子'), ('A組', '次郎')]
    
    print(f">>> students = {students}")
    print(">>> groups = defaultdict(list)")
    print(">>> for group, name in students:")
    print("...     groups[group].append(name)")
    
    for group, name in students:
        groups[group].append(name)
    
    print(f">>> dict(groups)  # {dict(groups)}")
    print()
    
    # itertools.combinations
    print("itertools.combinations（組み合わせ）:")
    items = ['A', 'B', 'C', 'D']
    print(f">>> items = {items}")
    print(">>> list(combinations(items, 2))")
    combos = list(combinations(items, 2))
    print(f"    {combos}")
    print()
    
    # itertools.permutations
    print("itertools.permutations（順列）:")
    print(">>> list(permutations(['X', 'Y'], 2))")
    perms = list(permutations(['X', 'Y'], 2))
    print(f"    {perms}")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_6_networking():
    """レッスン6: ネットワーク（urllib）"""
    print("📚 レッスン6: ネットワーク（urllib）")
    print("-" * 40)
    print()
    
    print("インターネットからデータを取得する基本的な方法を学びます。")
    print()
    
    # HTTP リクエスト（シミュレーション）
    print("HTTP リクエストの基本:")
    print(">>> import urllib.request")
    print(">>> import json")
    print(">>> ")
    print(">>> # 実際のリクエスト例（実行はしません）")
    print(">>> # url = 'https://api.example.com/data'")
    print(">>> # response = urllib.request.urlopen(url)")
    print(">>> # data = response.read().decode('utf-8')")
    print(">>> # json_data = json.loads(data)")
    print()
    
    # JSONデータの処理例
    print("JSONデータの処理例:")
    sample_json = '''
    {
        "users": [
            {"name": "Alice", "age": 25, "city": "Tokyo"},
            {"name": "Bob", "age": 30, "city": "Osaka"}
        ],
        "total": 2
    }
    '''
    
    print(">>> sample_json = '''")
    print(sample_json.strip())
    print("... '''")
    print(">>> data = json.loads(sample_json)")
    data = json.loads(sample_json)
    print(">>> for user in data['users']:")
    print("...     print(f\"{user['name']} ({user['age']}) - {user['city']}\")")
    
    for user in data['users']:
        print(f"    {user['name']} ({user['age']}) - {user['city']}")
    print()
    
    # URLの解析
    print("URLの解析:")
    print(">>> from urllib.parse import urlparse, parse_qs")
    url = "https://example.com/search?q=python&category=programming"
    print(f">>> url = '{url}'")
    print(">>> parsed = urlparse(url)")
    
    from urllib.parse import urlparse, parse_qs
    parsed = urlparse(url)
    print(f">>> parsed.netloc  # '{parsed.netloc}'  （ドメイン）")
    print(f">>> parsed.path    # '{parsed.path}'  （パス）")
    print(f">>> parsed.query   # '{parsed.query}'  （クエリ文字列）")
    
    query_params = parse_qs(parsed.query)
    print(f">>> parse_qs(parsed.query)  # {query_params}")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_7_logging():
    """レッスン7: ログ出力（logging）"""
    print("📚 レッスン7: ログ出力（logging）")
    print("-" * 40)
    print()
    
    print("プログラムの実行状況を記録するロギングを学びます。")
    print()
    
    # ログレベル
    print("ログレベル:")
    print("DEBUG < INFO < WARNING < ERROR < CRITICAL")
    print()
    
    # 基本的なログ設定
    print("基本的なログ出力:")
    print(">>> import logging")
    print(">>> logging.basicConfig(")
    print("...     level=logging.INFO,")
    print("...     format='%(asctime)s - %(levelname)s - %(message)s'")
    print("... )")
    
    # ログ出力のシミュレーション（実際には設定しない）
    print(">>> logging.info('プログラム開始')")
    print("    2024-01-01 12:00:00,000 - INFO - プログラム開始")
    
    print(">>> logging.warning('注意が必要です')")
    print("    2024-01-01 12:00:01,000 - WARNING - 注意が必要です")
    
    print(">>> logging.error('エラーが発生しました')")
    print("    2024-01-01 12:00:02,000 - ERROR - エラーが発生しました")
    print()
    
    # ファイルへのログ出力
    print("ファイルへのログ出力:")
    print(">>> logging.basicConfig(")
    print("...     filename='app.log',")
    print("...     level=logging.DEBUG,")
    print("...     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'")
    print("... )")
    print()
    
    # ロガーの作成
    print("カスタムロガーの作成:")
    print(">>> logger = logging.getLogger('my_app')")
    print(">>> logger.info('アプリケーション固有のログ')")
    print()
    
    print("💡 本格的なアプリケーションではログは必須です")
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
    
    print("【練習1】日付計算ツール")
    print("2つの日付の差を計算するプログラム")
    print("営業日（土日を除く）の計算も実装")
    print()
    
    print("【練習2】ファイル整理スクリプト")
    print("指定フォルダ内のファイルを拡張子別に分類")
    print("ログ出力でどのファイルを移動したか記録")
    print()
    
    print("【練習3】テキスト解析ツール")
    print("テキストファイルから単語の出現頻度を分析")
    print("正規表現で特定パターンを抽出")
    print()
    
    print("【練習4】簡易Webスクレイパー")
    print("URLからデータを取得してJSONで保存")
    print("エラーハンドリングとログ出力を含める")
    print()
    
    input("練習が終わったらEnterキーを押してください...")
    print()


def show_useful_modules():
    """便利なモジュール一覧"""
    print("🔧 その他の便利な標準モジュール")
    print("=" * 50)
    print()
    
    modules = [
        ("argparse", "コマンドライン引数の解析"),
        ("configparser", "設定ファイルの読み書き"),
        ("sqlite3", "SQLiteデータベース操作"),
        ("hashlib", "ハッシュ値の計算"),
        ("base64", "Base64エンコード/デコード"),
        ("gzip", "Gzip圧縮/展開"),
        ("pickle", "Pythonオブジェクトのシリアライズ"),
        ("threading", "マルチスレッド処理"),
        ("multiprocessing", "マルチプロセス処理"),
        ("subprocess", "外部プロセスの実行"),
        ("unittest", "ユニットテスト"),
        ("doctest", "ドキュメント内テスト"),
        ("tempfile", "一時ファイル作成"),
        ("shutil", "高レベルファイル操作"),
        ("glob", "ファイル名パターンマッチング"),
    ]
    
    print("モジュール名".ljust(20) + "説明")
    print("-" * 50)
    for module, description in modules:
        print(f"{module:<20} {description}")
    print()
    
    print("💡 Python標準ライブラリのドキュメント:")
    print("   https://docs.python.org/ja/3/library/")
    print()


def show_summary():
    """まとめ"""
    print("📝 第11章のまとめ")
    print("=" * 50)
    print()
    
    print("標準ライブラリについて学んだこと：")
    print("✅ datetime/time - 日時処理")
    print("✅ os/sys - システム操作とファイルシステム")
    print("✅ math/random - 数学計算とランダム処理")
    print("✅ re - 正規表現によるパターンマッチング")
    print("✅ collections/itertools - 高度なデータ構造")
    print("✅ urllib - ネットワーク通信")
    print("✅ logging - ログ出力")
    print()
    
    print("標準ライブラリの活用メリット：")
    print("• 追加インストール不要")
    print("• 高品質で安定している")
    print("• 豊富な機能をカバー")
    print("• 効率的な実装")
    print()
    
    print("次のステップ：")
    print("• 外部ライブラリの活用")
    print("• より大規模なプロジェクト開発")
    print()


def show_completion_message():
    """完了メッセージ"""
    print("\n" + "🎉" * 20)
    print("   ファイル 11 の学習完了！   ")
    print("🎉" * 20)
    
    print(f"\n📚 理解度テストを受けましょう")
    print("以下のコマンドをコピー&ペーストして実行してください:\n")
    
    # OS別コマンド表示
    python_cmd = "py" if platform.system() == "Windows" else "python3"
    print(f"   {python_cmd} quizzes/quiz_runner.py basics 11")
    
    print(f"\n✅ テスト合格後、次に進みましょう:")
    print(f"   {python_cmd} basics/12_external_libraries.py")
    
    print("\n💡 困ったときは:")
    print(f"   {python_cmd} quizzes/quiz_runner.py help")
    print("=" * 50)


def main():
    """メイン処理"""
    print_chapter_header()
    
    # 各レッスンを順番に実行
    lesson_1_datetime_time()
    lesson_2_os_sys()
    lesson_3_math_random()
    lesson_4_regex()
    lesson_5_collections_itertools()
    lesson_6_networking()
    lesson_7_logging()
    
    # 練習問題
    practice_exercises()
    
    # 便利なモジュール一覧
    show_useful_modules()
    
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