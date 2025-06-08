#!/usr/bin/env python3
"""
第4章「制御フロー」理解度テスト

basics/04_control_flow.py の内容に基づく理解度確認テストです。
70%以上で合格となります。
"""

QUIZ_DATA = {
    "chapter": "04",
    "title": "制御フロー",
    "description": "if文、for文、while文、条件分岐とループ処理について確認します",
    "passing_score": 70,
    "questions": [
        {
            "id": "q04_01",
            "type": "multiple_choice",
            "question": "Pythonの if 文で正しい書き方はどれですか？",
            "code": None,
            "choices": [
                "if (x == 5) { print('5です') }",
                "if x == 5: print('5です')",
                "if x == 5 then print('5です')",
                "if x == 5 do print('5です')"
            ],
            "correct": 1,
            "explanation": "Python の if 文は条件の後にコロン(:)を付け、波括弧は使いません。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q04_02",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """for i in range(3):
    for j in range(2):
        print(f"{i}-{j}")""",
            "choices": [
                "0-0\n0-1\n1-0\n1-1\n2-0\n2-1",
                "0-0\n1-1\n2-2",
                "0-0\n1-0\n2-0\n0-1\n1-1\n2-1",
                "1-1\n1-2\n2-1\n2-2\n3-1\n3-2"
            ],
            "correct": 0,
            "explanation": "ネストしたループでは、外側のループの各回に対して内側のループが完全に実行されます。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q04_03",
            "type": "fill_blank",
            "question": "リスト内の偶数のみを表示するコードを完成させてください",
            "code_template": """numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num ____ == 0:
        print(num)""",
            "correct_answer": "% 2",
            "hints": [
                {
                    "level": 1,
                    "text": "偶数は2で割った余りが0になります",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "余りを求める演算子を使います",
                    "penalty": 10
                }
            ],
            "explanation": "% 2 で2で割った余りを求め、0と比較して偶数判定します。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q04_04",
            "type": "multiple_choice",
            "question": "while ループを終了させるために使うキーワードはどれですか？",
            "code": None,
            "choices": [
                "stop",
                "break",
                "exit",
                "end"
            ],
            "correct": 1,
            "explanation": "break キーワードはループを強制終了させます。continue は次の反復にスキップ、exit は プログラム全体を終了します。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q04_05",
            "type": "debug",
            "question": "以下の無限ループになるコードを修正してください",
            "buggy_code": '''count = 0
while count < 5:
    print(count)
    # count += 1 が抜けている''',
            "error_type": "InfiniteLoop",
            "correct_code": '''count = 0
while count < 5:
    print(count)
    count += 1''',
            "explanation": "while ループでは条件変数を更新しないと無限ループになります。count += 1 で変数を増加させる必要があります。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q04_06",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        continue
    if num == 5:
        break
    print(num)""",
            "choices": [
                "1\n2",
                "1\n2\n4",
                "1\n2\n3\n4",
                "1\n2\n4\n5"
            ],
            "correct": 0,
            "explanation": "3のときはcontinueでスキップ、5のときはbreakでループ終了するため、1と2のみ表示されます。",
            "difficulty": 3,
            "category": "応用確認"
        },
        {
            "id": "q04_07",
            "type": "multiple_choice",
            "question": "elif 文について正しい説明はどれですか？",
            "code": None,
            "choices": [
                "else if の略で、複数の条件を順番にチェックできる",
                "else と同じで、すべての条件が False の時に実行される",
                "if と同じで、条件が True の時に実行される",
                "for ループの中でのみ使用できる"
            ],
            "correct": 0,
            "explanation": "elif は else if の略で、最初の if が False の場合に次の条件をチェックします。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q04_08",
            "type": "implementation",
            "question": "1から指定された数までの合計を計算する関数を実装してください",
            "requirements": [
                "関数名: calculate_sum",
                "引数: n (正の整数)",
                "戻り値: 1からnまでの数の合計",
                "ループを使用して計算すること"
            ],
            "test_cases": [
                {"input": [5], "expected": 15},  # 1+2+3+4+5
                {"input": [10], "expected": 55}, # 1+2+...+10
                {"input": [1], "expected": 1},   # 1
                {"input": [3], "expected": 6}    # 1+2+3
            ],
            "template": """def calculate_sum(n):
    # ここに実装してください
    # for ループまたは while ループを使用
    pass""",
            "hints": [
                {
                    "level": 1,
                    "text": "合計を保存する変数を初期化し、ループで足していきます",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "for i in range(1, n+1): を使って1からnまでループします",
                    "penalty": 15
                },
                {
                    "level": 3,
                    "text": "total = 0\nfor i in range(1, n+1):\n    total += i\nreturn total",
                    "penalty": 25
                }
            ],
            "explanation": "ループを使って1からnまでの数を順番に合計に加算していきます。",
            "difficulty": 2,
            "category": "実装確認"
        }
    ]
}

def get_quiz_data():
    """クイズデータを返す"""
    return QUIZ_DATA

if __name__ == "__main__":
    print("第4章 制御フロー - 理解度テスト")
    print("=" * 40)
    print(f"問題数: {len(QUIZ_DATA['questions'])}")
    print(f"合格ライン: {QUIZ_DATA['passing_score']}%")
    print("\nこのファイルは quiz_runner.py から実行してください:")
    print("python3 quizzes/quiz_runner.py basics 04")