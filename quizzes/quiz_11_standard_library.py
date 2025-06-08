#!/usr/bin/env python3
"""
第11章「標準ライブラリ」理解度テスト

basics/11_standard_library.py の内容に基づく理解度確認テストです。
70%以上で合格となります。
"""

QUIZ_DATA = {
    "chapter": "11",
    "title": "標準ライブラリ",
    "description": "datetime、os、math、random、正規表現、collections、urllib、loggingモジュールについて確認します",
    "passing_score": 70,
    "questions": [
        {
            "id": "q11_01",
            "type": "multiple_choice",
            "question": "現在の日時を取得する正しい方法はどれですか？",
            "code": None,
            "choices": [
                "import time; time.now()",
                "import datetime; datetime.now()",
                "from datetime import datetime; datetime.now()",
                "import calendar; calendar.now()"
            ],
            "correct": 2,
            "explanation": "datetime モジュールから datetime クラスをインポートし、now() メソッドで現在時刻を取得します。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q11_02",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """import math

print(math.ceil(4.3))
print(math.floor(4.7))
print(math.sqrt(16))""",
            "choices": [
                "4\n4\n4",
                "5\n4\n4.0",
                "4\n5\n4",
                "5\n5\n4.0"
            ],
            "correct": 1,
            "explanation": "ceil() は切り上げで5、floor() は切り下げで4、sqrt() は平方根で4.0となります。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q11_03",
            "type": "fill_blank",
            "question": "正規表現で電話番号パターンを検索するコードを完成させてください",
            "code_template": """import re
text = "連絡先: 090-1234-5678"
pattern = r'\\d{3}-\\d{4}-\\d{4}'
match = re.______(pattern, text)""",
            "correct_answer": "search",
            "hints": [
                {
                    "level": 1,
                    "text": "文字列からパターンを検索するメソッドです",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "「探す」という意味の英単語です",
                    "penalty": 10
                }
            ],
            "explanation": "re.search() で文字列内のパターンを検索できます。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q11_04",
            "type": "multiple_choice",
            "question": "random モジュールで1から10までの整数をランダムに取得する方法はどれですか？",
            "code": None,
            "choices": [
                "random.random(1, 10)",
                "random.randint(1, 10)",
                "random.choice(1, 10)",
                "random.uniform(1, 10)"
            ],
            "correct": 1,
            "explanation": "randint(a, b) で a から b までの整数をランダムに取得できます。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q11_05",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """from collections import Counter

words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(words)
print(counter.most_common(2))""",
            "choices": [
                "[('apple', 3), ('banana', 2)]",
                "[('banana', 2), ('apple', 3)]",
                "{'apple': 3, 'banana': 2}",
                "['apple', 'banana']"
            ],
            "correct": 0,
            "explanation": "Counter.most_common(n) は出現回数の多い順にn個のタプルのリストを返します。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q11_06",
            "type": "debug",
            "question": "以下のコードにはエラーがあります。修正してください",
            "buggy_code": '''import os

# 現在のディレクトリのファイル一覧を取得
files = os.listdir()  # 引数が不足
for file in files:
    print(file)''',
            "error_type": "TypeError",
            "correct_code": '''import os

# 現在のディレクトリのファイル一覧を取得
files = os.listdir('.')  # 現在のディレクトリを指定
for file in files:
    print(file)''',
            "explanation": "os.listdir() にはディレクトリパスを引数として渡す必要があります。現在のディレクトリは '.' で指定します。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q11_07",
            "type": "multiple_choice",
            "question": "logging モジュールのログレベルを正しい順序（重要度が低い順）に並べたものはどれですか？",
            "code": None,
            "choices": [
                "DEBUG < INFO < WARNING < ERROR < CRITICAL",
                "INFO < DEBUG < WARNING < ERROR < CRITICAL", 
                "DEBUG < WARNING < INFO < ERROR < CRITICAL",
                "CRITICAL < ERROR < WARNING < INFO < DEBUG"
            ],
            "correct": 0,
            "explanation": "ログレベルは DEBUG（最低）→ INFO → WARNING → ERROR → CRITICAL（最高）の順序です。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q11_08",
            "type": "implementation",
            "question": "ファイルの情報を取得し、ログに記録する関数を実装してください",
            "requirements": [
                "関数名: analyze_file",
                "引数: filepath (文字列)",
                "機能: ファイルサイズ、更新日時を取得してログ出力",
                "os, datetime, logging モジュールを使用",
                "ファイルが存在しない場合はログエラーを出力",
                "戻り値: ファイル情報の辞書 (存在しない場合は None)"
            ],
            "test_cases": [
                {
                    "input": ["existing_file.txt"],
                    "expected": "{'size': 1234, 'modified': '2024-01-01 12:00:00'}"
                },
                {
                    "input": ["nonexistent.txt"],
                    "expected": None
                }
            ],
            "template": """import os
import datetime
import logging

def analyze_file(filepath):
    # ここに実装してください
    # 1. ファイルの存在確認
    # 2. 存在する場合: サイズと更新日時を取得してログ出力
    # 3. 存在しない場合: エラーログを出力してNoneを返す
    # 4. 情報を辞書形式で返す
    pass""",
            "hints": [
                {
                    "level": 1,
                    "text": "os.path.exists() でファイル存在確認、os.path.getsize() でサイズ取得",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "os.path.getmtime() で更新時刻取得、datetime.datetime.fromtimestamp() で変換",
                    "penalty": 15
                },
                {
                    "level": 3,
                    "text": "if not os.path.exists(filepath):\n    logging.error(f'ファイルが見つかりません: {filepath}')\n    return None\n\nsize = os.path.getsize(filepath)\nmtime = os.path.getmtime(filepath)\nmodified = datetime.datetime.fromtimestamp(mtime)\nlogging.info(f'ファイル分析: {filepath}, サイズ: {size}バイト')\nreturn {'size': size, 'modified': modified.strftime('%Y-%m-%d %H:%M:%S')}",
                    "penalty": 25
                }
            ],
            "explanation": "標準ライブラリを組み合わせてファイル情報の取得とログ出力を行います。",
            "difficulty": 3,
            "category": "実装確認"
        }
    ]
}

def get_quiz_data():
    """クイズデータを返す"""
    return QUIZ_DATA

if __name__ == "__main__":
    print("第11章 標準ライブラリ - 理解度テスト")
    print("=" * 40)
    print(f"問題数: {len(QUIZ_DATA['questions'])}")
    print(f"合格ライン: {QUIZ_DATA['passing_score']}%")
    print("\nこのファイルは quiz_runner.py から実行してください:")
    print("python3 quizzes/quiz_runner.py basics 11")