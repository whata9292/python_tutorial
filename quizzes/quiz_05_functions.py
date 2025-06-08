#!/usr/bin/env python3
"""
第5章「関数」理解度テスト

basics/05_functions.py の内容に基づく理解度確認テストです。
70%以上で合格となります。
"""

QUIZ_DATA = {
    "chapter": "05",
    "title": "関数",
    "description": "関数の定義、引数、戻り値、スコープ、高度な機能について確認します",
    "passing_score": 70,
    "questions": [
        {
            "id": "q05_01",
            "type": "multiple_choice",
            "question": "Pythonで関数を定義するキーワードはどれですか？",
            "code": None,
            "choices": [
                "function",
                "def",
                "func",
                "define"
            ],
            "correct": 1,
            "explanation": "Python では def キーワードを使って関数を定義します。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q05_02",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """def greet(name, greeting="こんにちは"):
    return f"{greeting}、{name}さん"

print(greet("太郎"))
print(greet("花子", "おはよう"))""",
            "choices": [
                "こんにちは、太郎さん\nおはよう、花子さん",
                "太郎さん、こんにちは\n花子さん、おはよう",
                "こんにちは太郎\nおはよう花子",
                "エラーが発生する"
            ],
            "correct": 0,
            "explanation": "デフォルト引数により、第2引数が省略された場合は「こんにちは」が使用されます。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q05_03",
            "type": "fill_blank",
            "question": "関数から値を返すために使用するキーワードを入力してください",
            "code_template": """def add_numbers(a, b):
    result = a + b
    ____ result""",
            "correct_answer": "return",
            "hints": [
                {
                    "level": 1,
                    "text": "関数の結果を呼び出し元に渡すキーワードです",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "英語で「返す」という意味の単語です",
                    "penalty": 10
                }
            ],
            "explanation": "return キーワードで関数の戻り値を指定します。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q05_04",
            "type": "multiple_choice",
            "question": "関数内で定義された変数のスコープについて正しい説明はどれですか？",
            "code": """def my_function():
    local_var = 10
    print(local_var)

my_function()
print(local_var)  # この行について""",
            "choices": [
                "local_var は関数外でも使用できる",
                "local_var は関数内でのみ使用でき、関数外ではエラーになる",
                "local_var は自動的にグローバル変数になる",
                "local_var は他の関数でも使用できる"
            ],
            "correct": 1,
            "explanation": "関数内で定義された変数はローカルスコープを持ち、関数外からはアクセスできません。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q05_05",
            "type": "debug",
            "question": "以下のコードにはエラーがあります。修正してください",
            "buggy_code": '''def calculate_area(radius):
    pi = 3.14159
    area = pi * radius * radius
    # return 文が抜けている

result = calculate_area(5)
print(result)''',
            "error_type": "NoneType",
            "correct_code": '''def calculate_area(radius):
    pi = 3.14159
    area = pi * radius * radius
    return area

result = calculate_area(5)
print(result)''',
            "explanation": "関数で計算結果を返すには return 文が必要です。return がないと None が返されます。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q05_06",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """def modify_list(lst):
    lst.append(4)
    return lst

numbers = [1, 2, 3]
result = modify_list(numbers)
print(numbers)
print(result)""",
            "choices": [
                "[1, 2, 3]\n[1, 2, 3, 4]",
                "[1, 2, 3, 4]\n[1, 2, 3, 4]",
                "[1, 2, 3]\n[1, 2, 3]",
                "エラーが発生する"
            ],
            "correct": 1,
            "explanation": "リストは可変オブジェクトなので、関数内での変更が元のオブジェクトに反映されます。",
            "difficulty": 3,
            "category": "応用確認"
        },
        {
            "id": "q05_07",
            "type": "multiple_choice",
            "question": "*args と **kwargs について正しい説明はどれですか？",
            "code": "def my_function(*args, **kwargs):",
            "choices": [
                "*args は辞書、**kwargs はリストを受け取る",
                "*args は可変長位置引数、**kwargs は可変長キーワード引数を受け取る",
                "*args と **kwargs は固定の変数名で変更できない",
                "*args は文字列、**kwargs は数値のみ受け取る"
            ],
            "correct": 1,
            "explanation": "*args は可変長の位置引数をタプルで、**kwargs は可変長のキーワード引数を辞書で受け取ります。",
            "difficulty": 3,
            "category": "理解確認"
        },
        {
            "id": "q05_08",
            "type": "implementation",
            "question": "数値のリストを受け取り、その平均値を計算する関数を実装してください",
            "requirements": [
                "関数名: calculate_average",
                "引数: numbers (数値のリスト)",
                "戻り値: 平均値（浮動小数点数）",
                "空のリストの場合は 0 を返す"
            ],
            "test_cases": [
                {"input": [[1, 2, 3, 4, 5]], "expected": 3.0},
                {"input": [[10, 20, 30]], "expected": 20.0},
                {"input": [[100]], "expected": 100.0},
                {"input": [[]], "expected": 0}
            ],
            "template": """def calculate_average(numbers):
    # ここに実装してください
    pass""",
            "hints": [
                {
                    "level": 1,
                    "text": "平均 = 合計 ÷ 個数 で計算します",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "sum() 関数と len() 関数を使用します",
                    "penalty": 10
                },
                {
                    "level": 3,
                    "text": "if len(numbers) == 0:\n    return 0\nreturn sum(numbers) / len(numbers)",
                    "penalty": 20
                }
            ],
            "explanation": "リストの合計を個数で割って平均を計算します。空のリストの場合はゼロ除算を避けるため0を返します。",
            "difficulty": 2,
            "category": "実装確認"
        }
    ]
}

def get_quiz_data():
    """クイズデータを返す"""
    return QUIZ_DATA

if __name__ == "__main__":
    print("第5章 関数 - 理解度テスト")
    print("=" * 40)
    print(f"問題数: {len(QUIZ_DATA['questions'])}")
    print(f"合格ライン: {QUIZ_DATA['passing_score']}%")
    print("\nこのファイルは quiz_runner.py から実行してください:")
    print("python3 quizzes/quiz_runner.py basics 05")