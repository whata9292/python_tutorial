#!/usr/bin/env python3
"""
第8章「入出力処理」理解度テスト

basics/08_input_output.py の内容に基づく理解度確認テストです。
70%以上で合格となります。
"""

QUIZ_DATA = {
    "chapter": "08",
    "title": "入出力処理",
    "description": "ファイル操作、ファイルモード、pathlib、JSON、CSV、エラーハンドリングについて確認します",
    "passing_score": 70,
    "questions": [
        {
            "id": "q08_01",
            "type": "multiple_choice",
            "question": "ファイルを安全に開いて自動的に閉じるために推奨される方法はどれですか？",
            "code": None,
            "choices": [
                "file = open('test.txt'); file.close()",
                "with open('test.txt') as file:",
                "file = open('test.txt')",
                "open('test.txt').read()"
            ],
            "correct": 1,
            "explanation": "with文を使うことで、ブロックを抜ける際に自動的にファイルが閉じられます。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q08_02",
            "type": "multiple_choice",
            "question": "ファイルを追記モードで開く正しいモードはどれですか？",
            "code": None,
            "choices": [
                "'r'",
                "'w'",
                "'a'",
                "'x'"
            ],
            "correct": 2,
            "explanation": "'a' モードはファイルの末尾に内容を追加します。'w' は上書き、'r' は読み込み専用、'x' は新規作成専用です。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q08_03",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """from pathlib import Path

p = Path('example.txt')
print(p.name)
print(p.suffix)
print(p.stem)""",
            "choices": [
                "example.txt\n.txt\nexample",
                "example\ntxt\nexample.txt",
                "example.txt\ntxt\nexample",
                "Path('example.txt')\n.txt\nexample"
            ],
            "correct": 0,
            "explanation": "name はファイル名全体、suffix は拡張子、stem は拡張子を除いたファイル名を返します。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q08_04",
            "type": "fill_blank",
            "question": "JSON文字列をPythonの辞書に変換するメソッドを完成させてください",
            "code_template": """import json
json_string = '{"name": "太郎", "age": 25}'
data = json.______(json_string)""",
            "correct_answer": "loads",
            "hints": [
                {
                    "level": 1,
                    "text": "JSON文字列を読み込んでPythonオブジェクトに変換します",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "load + s の形で、s は string を意味します",
                    "penalty": 10
                }
            ],
            "explanation": "json.loads() は JSON文字列をPythonオブジェクトに変換します。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q08_05",
            "type": "debug",
            "question": "以下のコードにはエラーがあります。修正してください",
            "buggy_code": '''import csv

# CSVファイルの書き込み
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['名前', '年齢'])
    writer.writerow(['太郎', 25])
    
# CSVファイルの読み込み
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)''',
            "error_type": "EncodingError",
            "correct_code": '''import csv

# CSVファイルの書き込み
with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['名前', '年齢'])
    writer.writerow(['太郎', 25])
    
# CSVファイルの読み込み
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)''',
            "explanation": "CSV操作では newline='' と encoding='utf-8' を指定して文字化けを防ぎます。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q08_06",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
        print("ファイル読み込み成功")
except FileNotFoundError:
    print("ファイルが見つかりません")
except Exception as e:
    print(f"その他のエラー: {e}")
finally:
    print("処理完了")""",
            "choices": [
                "ファイル読み込み成功\n処理完了",
                "ファイルが見つかりません\n処理完了",
                "その他のエラー: ...\n処理完了",
                "エラーが発生してプログラム終了"
            ],
            "correct": 1,
            "explanation": "存在しないファイルを開こうとすると FileNotFoundError が発生し、finally ブロックは必ず実行されます。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q08_07",
            "type": "multiple_choice",
            "question": "DictReader を使ってCSVファイルを読み込む利点は何ですか？",
            "code": None,
            "choices": [
                "ファイルサイズが小さくなる",
                "読み込み速度が向上する",
                "ヘッダー行をキーとして辞書形式でアクセスできる",
                "メモリ使用量が削減される"
            ],
            "correct": 2,
            "explanation": "DictReader は最初の行をヘッダーとして扱い、各行を辞書として読み込むため、列名でアクセスできます。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q08_08",
            "type": "implementation",
            "question": "設定ファイルを管理する関数を実装してください",
            "requirements": [
                "関数名: manage_config",
                "引数: action ('load' または 'save'), filename (文字列), data=None (辞書、saveの時のみ)",
                "戻り値: loadの場合は設定辞書、saveの場合はTrue/False（成功/失敗）",
                "JSON形式でファイルに保存・読み込み",
                "ファイルが存在しない場合は空の辞書を返す"
            ],
            "test_cases": [
                {
                    "input": ["save", "config.json", {"theme": "dark", "lang": "ja"}],
                    "expected": True
                },
                {
                    "input": ["load", "config.json"],
                    "expected": {"theme": "dark", "lang": "ja"}
                },
                {
                    "input": ["load", "nonexistent.json"],
                    "expected": {}
                }
            ],
            "template": """def manage_config(action, filename, data=None):
    # ここに実装してください
    # action が 'save' の場合: data を JSON形式で filename に保存
    # action が 'load' の場合: filename から JSON を読み込んで辞書として返す
    # ファイルが存在しない場合は空の辞書 {} を返す
    pass""",
            "hints": [
                {
                    "level": 1,
                    "text": "json.dump() で保存、json.load() で読み込み、try-except で FileNotFoundError を処理",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "if action == 'save': で分岐し、with open() を使って安全にファイル操作",
                    "penalty": 15
                },
                {
                    "level": 3,
                    "text": "import json\n\nif action == 'save':\n    try:\n        with open(filename, 'w') as f:\n            json.dump(data, f)\n        return True\n    except:\n        return False\nelif action == 'load':\n    try:\n        with open(filename, 'r') as f:\n            return json.load(f)\n    except FileNotFoundError:\n        return {}",
                    "penalty": 25
                }
            ],
            "explanation": "JSON形式での設定ファイル管理は、辞書データの永続化によく使われる手法です。",
            "difficulty": 3,
            "category": "実装確認"
        }
    ]
}

def get_quiz_data():
    """クイズデータを返す"""
    return QUIZ_DATA

if __name__ == "__main__":
    print("第8章 入出力処理 - 理解度テスト")
    print("=" * 40)
    print(f"問題数: {len(QUIZ_DATA['questions'])}")
    print(f"合格ライン: {QUIZ_DATA['passing_score']}%")
    print("\nこのファイルは quiz_runner.py から実行してください:")
    print("python3 quizzes/quiz_runner.py basics 08")