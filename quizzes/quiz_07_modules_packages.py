#!/usr/bin/env python3
"""
第7章「モジュールとパッケージ」理解度テスト

basics/07_modules_and_packages.py の内容に基づく理解度確認テストです。
70%以上で合格となります。
"""

QUIZ_DATA = {
    "chapter": "07",
    "title": "モジュールとパッケージ",
    "description": "モジュールのインポート、作成、パッケージ構造、検索パス、ベストプラクティスについて確認します",
    "passing_score": 70,
    "questions": [
        {
            "id": "q07_01",
            "type": "multiple_choice",
            "question": "Pythonで特定の関数のみをモジュールからインポートする正しい方法はどれですか？",
            "code": None,
            "choices": [
                "import math.sqrt",
                "from math import sqrt",
                "import sqrt from math",
                "use math.sqrt"
            ],
            "correct": 1,
            "explanation": "from モジュール名 import 関数名 の形式で特定の関数のみをインポートできます。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q07_02",
            "type": "multiple_choice",
            "question": "__name__ == '__main__' の条件文の目的は何ですか？",
            "code": None,
            "choices": [
                "モジュールがインポートされた時のみ実行する",
                "モジュールが直接実行された時のみ実行する",
                "関数が定義された時のみ実行する",
                "クラスが作成された時のみ実行する"
            ],
            "correct": 1,
            "explanation": "__name__ == '__main__' は、そのファイルが直接実行された場合のみ True になります。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q07_03",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """import math as m
from datetime import datetime as dt

print(type(m.pi))
print(type(dt.now()))""",
            "choices": [
                "<class 'float'>\n<class 'datetime.datetime'>",
                "<class 'int'>\n<class 'time'>",
                "<class 'math'>\n<class 'datetime'>",
                "エラーが発生する"
            ],
            "correct": 0,
            "explanation": "math.pi は float 型、datetime.now() は datetime オブジェクトを返します。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q07_04",
            "type": "fill_blank",
            "question": "モジュールの検索パスを確認するために使用するリストを完成させてください",
            "code_template": """import sys
print(____)""",
            "correct_answer": "sys.path",
            "hints": [
                {
                    "level": 1,
                    "text": "sys モジュールにあるモジュール検索パスのリストです",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "path という名前のリストです",
                    "penalty": 10
                }
            ],
            "explanation": "sys.path にはPythonがモジュールを検索するディレクトリのリストが含まれています。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q07_05",
            "type": "debug",
            "question": "以下のコードにはエラーがあります。修正してください",
            "buggy_code": '''# my_module.py の内容
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

# main.py の内容
import my_module

print(greet("Alice"))  # エラー: name 'greet' is not defined
print(PI)  # エラー: name 'PI' is not defined''',
            "error_type": "NameError",
            "correct_code": '''# my_module.py の内容
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

# main.py の内容
import my_module

print(my_module.greet("Alice"))  # 修正: モジュール名を付ける
print(my_module.PI)  # 修正: モジュール名を付ける''',
            "explanation": "import でモジュール全体をインポートした場合、関数や変数にはモジュール名.名前 でアクセスする必要があります。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q07_06",
            "type": "multiple_choice",
            "question": "パッケージであることを示すために必要なファイルはどれですか？",
            "code": None,
            "choices": [
                "package.py",
                "__init__.py",
                "main.py",
                "setup.py"
            ],
            "correct": 1,
            "explanation": "__init__.py ファイルがあることで、そのディレクトリがPythonパッケージとして認識されます。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q07_07",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """# sample_module.py の内容
def public_function():
    return "公開関数"

def _private_function():
    return "プライベート関数"

# main.py の内容
from sample_module import *
print(dir())  # 現在の名前空間の確認（簡略化）""",
            "choices": [
                "public_function のみインポートされる",
                "_private_function のみインポートされる", 
                "両方の関数がインポートされる",
                "どちらの関数もインポートされない"
            ],
            "correct": 0,
            "explanation": "from module import * では、アンダースコアで始まる名前（プライベート）は通常インポートされません。",
            "difficulty": 3,
            "category": "応用確認"
        },
        {
            "id": "q07_08",
            "type": "implementation",
            "question": "計算機能を提供するモジュールを作成してください",
            "requirements": [
                "ファイル名の想定: calculator.py",
                "以下の関数を含むモジュールの内容を実装:",
                "  - add(a, b): 加算",
                "  - multiply(a, b): 乗算", 
                "  - calculate_circle_area(radius): 円の面積計算",
                "  - PI定数: 3.14159",
                "直接実行時は簡単なテストを実行"
            ],
            "test_cases": [
                {"input": "add(2, 3)", "expected": 5},
                {"input": "multiply(4, 5)", "expected": 20},
                {"input": "calculate_circle_area(2)", "expected": 12.56636}
            ],
            "template": """# calculator.py の内容

# ここに実装してください
# PI定数の定義
# add関数の定義
# multiply関数の定義  
# calculate_circle_area関数の定義
# __name__ == '__main__' でのテスト実行

pass""",
            "hints": [
                {
                    "level": 1,
                    "text": "PI = 3.14159 で定数を定義し、各関数は基本的な演算を行います",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "円の面積 = PI * radius * radius で計算します",
                    "penalty": 15
                },
                {
                    "level": 3,
                    "text": "PI = 3.14159\n\ndef add(a, b):\n    return a + b\n\ndef multiply(a, b):\n    return a * b\n\ndef calculate_circle_area(radius):\n    return PI * radius * radius\n\nif __name__ == '__main__':\n    print(f'2 + 3 = {add(2, 3)}')",
                    "penalty": 25
                }
            ],
            "explanation": "モジュールは関数と定数を定義し、__name__ == '__main__' で直接実行時の動作を指定します。",
            "difficulty": 3,
            "category": "実装確認"
        }
    ]
}

def get_quiz_data():
    """クイズデータを返す"""
    return QUIZ_DATA

if __name__ == "__main__":
    print("第7章 モジュールとパッケージ - 理解度テスト")
    print("=" * 40)
    print(f"問題数: {len(QUIZ_DATA['questions'])}")
    print(f"合格ライン: {QUIZ_DATA['passing_score']}%")
    print("\nこのファイルは quiz_runner.py から実行してください:")
    print("python3 quizzes/quiz_runner.py basics 07")