#!/usr/bin/env python3
"""
第6章「データ構造」理解度テスト

basics/06_data_structures.py の内容に基づく理解度確認テストです。
70%以上で合格となります。
"""

QUIZ_DATA = {
    "chapter": "06",
    "title": "データ構造",
    "description": "高度なデータ構造、セット、内包表記、ソート、zip関数、collectionsモジュールについて確認します",
    "passing_score": 70,
    "questions": [
        {
            "id": "q06_01",
            "type": "multiple_choice",
            "question": "セット（set）の特徴として正しいものはどれですか？",
            "code": None,
            "choices": [
                "要素の順序が保たれ、重複要素を持つことができる",
                "要素の順序は保たれないが、重複要素を持つことができる",
                "要素の順序が保たれ、重複要素を持つことができない",
                "要素の順序は保たれず、重複要素を持つことができない"
            ],
            "correct": 3,
            "explanation": "セットは順序を保たず（Python 3.7以降は挿入順序を保持）、重複要素を自動的に除去します。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q06_02",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = list(set(numbers))
print(sorted(unique_numbers))""",
            "choices": [
                "[1, 2, 3, 4]",
                "[1, 2, 2, 3, 3, 3, 4]",
                "[4, 3, 2, 1]",
                "順序は不定"
            ],
            "correct": 0,
            "explanation": "set() で重複が除去され、sorted() でソートされるため [1, 2, 3, 4] となります。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q06_03",
            "type": "fill_blank",
            "question": "リスト内包表記を使って、1から10までの数の平方を作成してください",
            "code_template": "squares = [____ for x in range(1, 11)]",
            "expected_output": "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]",
            "correct_answer": "x ** 2",
            "hints": [
                {
                    "level": 1,
                    "text": "平方は数値を2乗することです",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "** 演算子を使って累乗を計算します",
                    "penalty": 10
                }
            ],
            "explanation": "x ** 2 で x の2乗（平方）を計算します。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q06_04",
            "type": "multiple_choice",
            "question": "辞書内包表記の正しい書き方はどれですか？",
            "code": "words = ['apple', 'banana', 'cherry']",
            "choices": [
                "[word: len(word) for word in words]",
                "{word: len(word) for word in words}",
                "(word: len(word) for word in words)",
                "set(word: len(word) for word in words)"
            ],
            "correct": 1,
            "explanation": "辞書内包表記は {} を使い、key: value の形式で書きます。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q06_05",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
result = dict(zip(names, scores))
print(result['Bob'])""",
            "choices": [
                "85",
                "92",
                "78",
                "エラーが発生する"
            ],
            "correct": 1,
            "explanation": "zip() で names と scores をペアにし、dict() で辞書を作成。'Bob' のスコアは 92 です。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q06_06",
            "type": "debug",
            "question": "以下のコードにはエラーがあります。修正してください",
            "buggy_code": '''from collections import Counter
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(words)
print(counter.most_common(2))''',
            "error_type": "ImportError",
            "correct_code": '''from collections import Counter
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(words)
print(counter.most_common(2))''',
            "explanation": "このコードは実際には正しく動作します。Counter は collections モジュールからインポートでき、most_common(2) で最頻出の2つを取得できます。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q06_07",
            "type": "multiple_choice",
            "question": "lambda 関数について正しい説明はどれですか？",
            "code": "lambda x: x * 2",
            "choices": [
                "名前を持つ通常の関数で、複数行のコードを書ける",
                "無名関数で、単一の式のみを書ける",
                "クラスメソッドでのみ使用可能",
                "ループ内でのみ使用可能"
            ],
            "correct": 1,
            "explanation": "lambda は無名関数（匿名関数）で、単一の式のみを持つ簡潔な関数定義方法です。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q06_08",
            "type": "implementation",
            "question": "学生の成績データから、各科目の平均点を計算する関数を実装してください",
            "requirements": [
                "関数名: calculate_subject_averages",
                "引数: students (辞書のリスト。各辞書は {'name': '名前', 'math': 点数, 'english': 点数, 'science': 点数} の形式)",
                "戻り値: 各科目の平均点を含む辞書 {'math': 平均点, 'english': 平均点, 'science': 平均点}",
                "collectionsモジュールは使わずに実装"
            ],
            "test_cases": [
                {
                    "input": [[
                        {'name': '太郎', 'math': 80, 'english': 75, 'science': 85},
                        {'name': '花子', 'math': 90, 'english': 85, 'science': 80},
                        {'name': '次郎', 'math': 70, 'english': 80, 'science': 90}
                    ]],
                    "expected": {'math': 80.0, 'english': 80.0, 'science': 85.0}
                }
            ],
            "template": """def calculate_subject_averages(students):
    # ここに実装してください
    # 各科目の合計点と人数を計算し、平均を求める
    pass""",
            "hints": [
                {
                    "level": 1,
                    "text": "各科目ごとに合計点を計算し、学生数で割ります",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "辞書を使って各科目の合計を管理し、len(students) で人数を取得",
                    "penalty": 15
                },
                {
                    "level": 3,
                    "text": "subjects = ['math', 'english', 'science']\ntotals = {}\nfor subject in subjects:\n    total = sum(student[subject] for student in students)\n    totals[subject] = total / len(students)",
                    "penalty": 25
                }
            ],
            "explanation": "各科目について全学生の点数を合計し、学生数で割って平均を計算します。",
            "difficulty": 3,
            "category": "実装確認"
        }
    ]
}

def get_quiz_data():
    """クイズデータを返す"""
    return QUIZ_DATA

if __name__ == "__main__":
    print("第6章 データ構造 - 理解度テスト")
    print("=" * 40)
    print(f"問題数: {len(QUIZ_DATA['questions'])}")
    print(f"合格ライン: {QUIZ_DATA['passing_score']}%")
    print("\nこのファイルは quiz_runner.py から実行してください:")
    print("python3 quizzes/quiz_runner.py basics 06")