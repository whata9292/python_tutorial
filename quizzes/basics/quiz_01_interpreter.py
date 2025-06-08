#!/usr/bin/env python3
"""
第1章「インタープリター基礎」理解度テスト問題集

このファイルには第1章の理解度を確認するための
問題が含まれています。
"""

quiz_data = {
    "title": "第1章: Pythonインタープリター基礎",
    "description": "Pythonインタープリターの基本的な使い方",
    "total_questions": 6,
    "time_limit": None,  # 時間制限なし
    "questions": [
        {
            "id": 1,
            "type": "multiple_choice",
            "question": "Pythonの対話モード（インタラクティブモード）を起動するコマンドはどれですか？",
            "code": None,
            "choices": [
                "python3（Mac/Linux）または py（Windows）",
                "python-shell",
                "interactive",
                "python-console"
            ],
            "correct": 0,
            "explanation": "システムによって異なりますが、python3やpyコマンドで対話モードを起動できます。",
            "difficulty": 1,
            "hints": [
                {
                    "level": 1,
                    "text": "Pythonのバージョンに関連するコマンドです",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "Windows では 'py'、Mac/Linux では 'python3' が一般的",
                    "penalty": 5
                }
            ]
        },
        {
            "id": 2,
            "type": "fill_blank",
            "question": "Pythonで変数xに値10を代入するコードを完成させてください",
            "code_template": "x ____ 10",
            "expected_output": None,
            "correct_answer": "=",
            "explanation": "= は代入演算子で、右辺の値を左辺の変数に代入します。",
            "hints": [
                {
                    "level": 1,
                    "text": "数学の等号に似た記号を使います",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "代入には '=' を使用します",
                    "penalty": 10
                }
            ],
            "difficulty": 1
        },
        {
            "id": 3,
            "type": "multiple_choice",
            "question": "2の3乗を計算するPythonの演算子はどれですか？",
            "code": None,
            "choices": [
                "2 ^ 3",
                "2 ** 3",
                "2 pow 3",
                "power(2, 3)"
            ],
            "correct": 1,
            "explanation": "**がべき乗演算子です。^は排他的論理和（XOR）で、べき乗ではありません。",
            "difficulty": 2,
            "hints": [
                {
                    "level": 1,
                    "text": "アスタリスク（*）を使った演算子です",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "アスタリスクを2つ続けて書きます",
                    "penalty": 10
                }
            ]
        },
        {
            "id": 4,
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": '''
x = 5
y = 3
result = x + y * 2
print(result)
''',
            "choices": [
                "16",
                "11",
                "13",
                "10"
            ],
            "correct": 1,
            "explanation": "演算の優先順位により、y * 2 が先に計算され(3 * 2 = 6)、その後 x + 6 = 5 + 6 = 11となります。",
            "difficulty": 2,
            "hints": [
                {
                    "level": 1,
                    "text": "数学と同じように、掛け算が足し算より先に実行されます",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "y * 2 = 3 * 2 = 6、そして x + 6 = 5 + 6",
                    "penalty": 15
                }
            ]
        },
        {
            "id": 5,
            "type": "fill_blank",
            "question": "Pythonでヘルプ機能を使って print 関数の説明を見るコードを完成させてください",
            "code_template": "______(print)",
            "expected_output": None,
            "correct_answer": "help",
            "explanation": "help()関数を使うと、指定した関数やオブジェクトの詳細な説明を見ることができます。",
            "hints": [
                {
                    "level": 1,
                    "text": "困ったときに使う、「助け」を意味する英単語です",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "'help' という関数名です",
                    "penalty": 10
                }
            ],
            "difficulty": 1
        },
        {
            "id": 6,
            "type": "multiple_choice",
            "question": "Pythonの対話モードで「>>>」が表示される意味は何ですか？",
            "code": None,
            "choices": [
                "エラーが発生している",
                "プログラムが実行中",
                "入力を待っている",
                "プログラムが終了した"
            ],
            "correct": 2,
            "explanation": "「>>>」はプロンプトと呼ばれ、Pythonインタープリターがユーザーからの入力を待っていることを示します。",
            "difficulty": 1,
            "hints": [
                {
                    "level": 1,
                    "text": "ユーザーが何かをするのを待っている状態です",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "コマンドやコードの入力を待っています",
                    "penalty": 5
                }
            ]
        }
    ],
    "review_topics": [
        "Pythonインタープリターの起動方法",
        "変数への代入（=演算子）",
        "算術演算子（特にべき乗**）",
        "演算の優先順位",
        "help()関数の使い方",
        "対話モードのプロンプト（>>>）の意味"
    ]
}

# テスト実行用の関数
def get_quiz_data():
    """問題データを返す"""
    return quiz_data

if __name__ == "__main__":
    print("第1章の理解度テスト問題データ")
    print(f"問題数: {quiz_data['total_questions']}")
    print(f"タイトル: {quiz_data['title']}")
    for i, question in enumerate(quiz_data['questions'], 1):
        print(f"{i}. {question['question'][:50]}...")