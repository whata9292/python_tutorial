#!/usr/bin/env python3
"""
第2章「数値と文字列」理解度テスト

basics/02_numbers_and_strings.py の内容に基づく理解度確認テストです。
70%以上で合格となります。
"""

QUIZ_DATA = {
    "chapter": "02",
    "title": "数値と文字列",
    "description": "数値の基本操作、文字列の操作と書式設定について確認します",
    "passing_score": 70,
    "questions": [
        {
            "id": "q02_01",
            "type": "multiple_choice",
            "question": "Pythonで整数の割り算の結果を整数で取得したい場合、どの演算子を使いますか？",
            "code": None,
            "choices": [
                "/ （スラッシュ）",
                "// （ダブルスラッシュ）", 
                "% （パーセント）",
                "** （ダブルアスタリスク）"
            ],
            "correct": 1,
            "explanation": "// 演算子は整数除算（フロア除算）を行い、結果を整数で返します。/ は浮動小数点除算、% は余り、** は累乗です。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q02_02", 
            "type": "fill_blank",
            "question": "文字列の中で改行を表現する場合、どのエスケープシーケンスを使いますか？",
            "code_template": "message = 'こんにちは____世界'",
            "correct_answer": "\\n",
            "hints": [
                {
                    "level": 1,
                    "text": "エスケープシーケンスはバックスラッシュから始まります",
                    "penalty": 0
                },
                {
                    "level": 2, 
                    "text": "newline の n を使います",
                    "penalty": 10
                }
            ],
            "explanation": "\\n は改行文字を表すエスケープシーケンスです。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q02_03",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """x = 17
y = 5
print(x // y)
print(x % y)""",
            "choices": [
                "3\n2",
                "3.4\n2", 
                "3\n5",
                "4\n2"
            ],
            "correct": 0,
            "explanation": "17 // 5 = 3（整数除算）、17 % 5 = 2（余り）となります。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q02_04",
            "type": "multiple_choice",
            "question": "f-string（フォーマット済み文字列リテラル）の正しい書き方はどれですか？",
            "code": "name = 'Python'\nage = 30",
            "choices": [
                "print('私の名前は{name}、{age}歳です')",
                "print(f'私の名前は{name}、{age}歳です')", 
                "print('私の名前は%s、%d歳です' % name, age)",
                "print('私の名前は' + {name} + '、' + {age} + '歳です')"
            ],
            "correct": 1,
            "explanation": "f-string は文字列の前に f を付けて、{} 内に変数名を書きます。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q02_05",
            "type": "debug",
            "question": "以下のコードにはエラーがあります。修正してください",
            "buggy_code": '''name = "Alice"
age = 25
message = f"こんにちは、{name}さん。{age才です。"
print(message)''',
            "error_type": "TypeError",
            "correct_code": '''name = "Alice"
age = 25
message = f"こんにちは、{name}さん。{age}歳です。"
print(message)''',
            "explanation": "f-string内で{age才}となっていますが、「才」は文字なので{age}歳と書く必要があります。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q02_06",
            "type": "fill_blank",
            "question": "文字列のメソッドを使って、すべて大文字に変換するコードを完成させてください", 
            "code_template": "text = 'hello world'\nresult = text._____()\nprint(result)",
            "expected_output": "HELLO WORLD",
            "correct_answer": "upper",
            "hints": [
                {
                    "level": 1,
                    "text": "小文字を大文字に変換するメソッドです",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "「上」という意味の英単語です",
                    "penalty": 10
                }
            ],
            "explanation": "upper() メソッドは文字列をすべて大文字に変換します。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q02_07",
            "type": "predict_output", 
            "question": "以下のコードの実行結果を予測してください",
            "code": """text = "Python Programming"
print(len(text))
print(text[0])
print(text[-1])""",
            "choices": [
                "18\nP\ng",
                "17\nP\ng",
                "18\nP\nG", 
                "17\nP\nG"
            ],
            "correct": 0,
            "explanation": "文字列の長さは18、最初の文字はP、最後の文字（-1番目）はgです。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q02_08",
            "type": "implementation",
            "question": "ユーザーから名前と年齢を入力してもらい、「こんにちは、[名前]さん。[年齢]歳ですね。」と表示する関数を実装してください",
            "requirements": [
                "関数名: greet_user",
                "引数: name (文字列), age (整数)",
                "戻り値: フォーマットされた挨拶文字列"
            ],
            "test_cases": [
                {"input": ["太郎", 25], "expected": "こんにちは、太郎さん。25歳ですね。"},
                {"input": ["花子", 30], "expected": "こんにちは、花子さん。30歳ですね。"},
                {"input": ["次郎", 18], "expected": "こんにちは、次郎さん。18歳ですね。"}
            ],
            "template": """def greet_user(name, age):
    # ここに実装してください
    pass""",
            "hints": [
                {
                    "level": 1,
                    "text": "f-string を使って文字列をフォーマットします",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "f'こんにちは、{name}さん。{age}歳ですね。' のような形式です",
                    "penalty": 15
                }
            ],
            "explanation": "f-string を使って変数を文字列に埋め込みます。",
            "difficulty": 2,
            "category": "実装確認"
        }
    ]
}

def get_quiz_data():
    """クイズデータを返す"""
    return QUIZ_DATA

if __name__ == "__main__":
    print("第2章 数値と文字列 - 理解度テスト")
    print("=" * 40)
    print(f"問題数: {len(QUIZ_DATA['questions'])}")
    print(f"合格ライン: {QUIZ_DATA['passing_score']}%")
    print("\nこのファイルは quiz_runner.py から実行してください:")
    print("python3 quizzes/quiz_runner.py basics 02")