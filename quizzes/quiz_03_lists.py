#!/usr/bin/env python3
"""
第3章「リストとシーケンス」理解度テスト

basics/03_lists_and_sequences.py の内容に基づく理解度確認テストです。
70%以上で合格となります。
"""

QUIZ_DATA = {
    "chapter": "03",
    "title": "リストとシーケンス",
    "description": "リスト、タプル、辞書、セットの基本操作と活用方法について確認します",
    "passing_score": 70,
    "questions": [
        {
            "id": "q03_01",
            "type": "multiple_choice",
            "question": "リストの末尾に新しい要素を追加するメソッドはどれですか？",
            "code": "fruits = ['apple', 'banana']",
            "choices": [
                "fruits.add('orange')",
                "fruits.append('orange')",
                "fruits.insert('orange')",
                "fruits.push('orange')"
            ],
            "correct": 1,
            "explanation": "append() メソッドはリストの末尾に要素を追加します。add() はセット用、insert() は位置指定、push() はPythonにはありません。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q03_02",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])
print(numbers[-2:])""",
            "choices": [
                "[2, 3, 4]\n[4, 5]",
                "[1, 2, 3]\n[5]",
                "[2, 3]\n[4, 5]",
                "[2, 3, 4]\n[5]"
            ],
            "correct": 0,
            "explanation": "numbers[1:4] は インデックス1から3まで[2, 3, 4]、numbers[-2:] は後ろから2番目以降[4, 5]です。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q03_03",
            "type": "multiple_choice",
            "question": "辞書で存在しないキーにアクセスした場合にエラーを避ける方法はどれですか？",
            "code": "person = {'name': '太郎', 'age': 25}",
            "choices": [
                "person['height']",
                "person.get('height')",
                "person.find('height')",
                "person.search('height')"
            ],
            "correct": 1,
            "explanation": "get() メソッドは存在しないキーの場合 None を返すためエラーになりません。直接アクセスするとKeyErrorが発生します。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q03_04",
            "type": "fill_blank",
            "question": "リスト内包表記を使って、1から10までの数の中で偶数のみのリストを作成してください",
            "code_template": "even_numbers = [x for x in range(1, 11) if ____]",
            "expected_output": "[2, 4, 6, 8, 10]",
            "correct_answer": "x % 2 == 0",
            "hints": [
                {
                    "level": 1,
                    "text": "偶数は2で割った余りが0になります",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "% 演算子を使って余りを計算します",
                    "penalty": 10
                }
            ],
            "explanation": "x % 2 == 0 は偶数を判定する条件式です。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q03_05",
            "type": "debug",
            "question": "以下のコードにはエラーがあります。修正してください",
            "buggy_code": '''fruits = ['apple', 'banana', 'orange']
fruits[3] = 'grape'
print(fruits)''',
            "error_type": "IndexError",
            "correct_code": '''fruits = ['apple', 'banana', 'orange']
fruits.append('grape')
print(fruits)''',
            "explanation": "リストのインデックスは0から始まるため、3要素のリストでインデックス3は存在しません。末尾に追加するにはappend()を使います。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q03_06",
            "type": "multiple_choice",
            "question": "タプルとリストの主な違いは何ですか？",
            "code": None,
            "choices": [
                "タプルは数値のみ、リストは文字列のみ格納できる",
                "タプルは変更不可能、リストは変更可能",
                "タプルは順序なし、リストは順序あり",
                "タプルは1つの型のみ、リストは複数の型を格納できる"
            ],
            "correct": 1,
            "explanation": "タプルは immutable（変更不可能）、リストは mutable（変更可能）です。両方とも複数の型を格納でき、順序があります。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q03_07",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 & set2)
print(set1 | set2)""",
            "choices": [
                "{3, 4}\n{1, 2, 3, 4, 5, 6}",
                "{1, 2}\n{5, 6}",
                "{3, 4}\n{1, 2, 5, 6}",
                "{1, 2, 3, 4}\n{3, 4, 5, 6}"
            ],
            "correct": 0,
            "explanation": "& は積集合（共通要素）{3, 4}、| は和集合（全要素）{1, 2, 3, 4, 5, 6}を返します。",
            "difficulty": 3,
            "category": "応用確認"
        },
        {
            "id": "q03_08",
            "type": "implementation",
            "question": "辞書のリストから特定のキーの値をすべて抽出する関数を実装してください",
            "requirements": [
                "関数名: extract_values",
                "引数: data_list (辞書のリスト), key (文字列)",
                "戻り値: 指定されたキーの値のリスト（存在しない場合は除外）"
            ],
            "test_cases": [
                {
                    "input": [
                        [{"name": "太郎", "age": 25}, {"name": "花子", "age": 30}, {"name": "次郎"}],
                        "age"
                    ],
                    "expected": [25, 30]
                },
                {
                    "input": [
                        [{"price": 100}, {"price": 200}, {"discount": 50}],
                        "price"
                    ],
                    "expected": [100, 200]
                }
            ],
            "template": """def extract_values(data_list, key):
    # ここに実装してください
    pass""",
            "hints": [
                {
                    "level": 1,
                    "text": "forループで各辞書を処理し、キーが存在するかチェックします",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "in演算子でキーの存在確認、または get() メソッドを使用します",
                    "penalty": 15
                },
                {
                    "level": 3,
                    "text": "result = []\nfor item in data_list:\n    if key in item:\n        result.append(item[key])",
                    "penalty": 25
                }
            ],
            "explanation": "辞書のリストを反復処理し、各辞書でキーが存在する場合のみ値を抽出します。",
            "difficulty": 3,
            "category": "実装確認"
        }
    ]
}

def get_quiz_data():
    """クイズデータを返す"""
    return QUIZ_DATA

if __name__ == "__main__":
    print("第3章 リストとシーケンス - 理解度テスト")
    print("=" * 40)
    print(f"問題数: {len(QUIZ_DATA['questions'])}")
    print(f"合格ライン: {QUIZ_DATA['passing_score']}%")
    print("\nこのファイルは quiz_runner.py から実行してください:")
    print("python3 quizzes/quiz_runner.py basics 03")