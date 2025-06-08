#!/usr/bin/env python3
"""
第12章「外部ライブラリ」理解度テスト

basics/12_external_libraries.py の内容に基づく理解度確認テストです。
70%以上で合格となります。
"""

QUIZ_DATA = {
    "chapter": "12",
    "title": "外部ライブラリ",
    "description": "pip、仮想環境、人気ライブラリ、ライブラリ選択、開発ワークフローについて確認します",
    "passing_score": 70,
    "questions": [
        {
            "id": "q12_01",
            "type": "multiple_choice",
            "question": "Pythonで外部パッケージをインストールするための標準ツールはどれですか？",
            "code": None,
            "choices": [
                "npm",
                "pip",
                "apt",
                "conda"
            ],
            "correct": 1,
            "explanation": "pip は Python の標準パッケージ管理ツールです。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q12_02",
            "type": "multiple_choice",
            "question": "仮想環境を作成する正しいコマンドはどれですか？",
            "code": None,
            "choices": [
                "python -m virtualenv myenv",
                "python -m venv myenv",
                "pip install venv myenv",
                "conda create myenv"
            ],
            "correct": 1,
            "explanation": "python -m venv で仮想環境を作成できます。venv は Python 3.3 以降に標準搭載されています。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q12_03",
            "type": "fill_blank",
            "question": "requirements.txt から依存関係を一括インストールするコマンドを完成させてください",
            "code_template": "pip install ____ requirements.txt",
            "correct_answer": "-r",
            "hints": [
                {
                    "level": 1,
                    "text": "requirements ファイルを指定するオプションです",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "requirement の頭文字です",
                    "penalty": 10
                }
            ],
            "explanation": "pip install -r requirements.txt で requirements ファイルから一括インストールできます。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q12_04",
            "type": "multiple_choice",
            "question": "現在インストールされているパッケージ一覧を確認するコマンドはどれですか？",
            "code": None,
            "choices": [
                "pip show",
                "pip list",
                "pip search",
                "pip info"
            ],
            "correct": 1,
            "explanation": "pip list でインストール済みパッケージの一覧を確認できます。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q12_05",
            "type": "predict_output",
            "question": "以下のrequirements.txtの内容について、正しい説明はどれですか？",
            "code": """requests==2.28.1
pandas>=1.4.0
numpy~=1.21.0
matplotlib""",
            "choices": [
                "すべて最新バージョンがインストールされる",
                "requests は 2.28.1、pandas は 1.4.0以上、numpy は 1.21.x、matplotlib は最新",
                "すべて固定バージョンがインストールされる",
                "エラーが発生する"
            ],
            "correct": 1,
            "explanation": "== は固定、>= は以上、~= は互換バージョン、バージョン指定なしは最新を意味します。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q12_06",
            "type": "debug",
            "question": "以下の仮想環境の使用手順にはエラーがあります。修正してください",
            "buggy_code": '''# 仮想環境の作成
python -m venv myproject_env

# 仮想環境の有効化（Mac/Linux）
source myproject_env/Scripts/activate  # 間違ったパス

# パッケージのインストール
pip install requests

# 仮想環境の無効化
deactivate''',
            "error_type": "PathError",
            "correct_code": '''# 仮想環境の作成
python -m venv myproject_env

# 仮想環境の有効化（Mac/Linux）
source myproject_env/bin/activate  # 正しいパス

# パッケージのインストール
pip install requests

# 仮想環境の無効化
deactivate''',
            "explanation": "Mac/Linux では bin/activate、Windows では Scripts/activate.bat を使用します。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q12_07",
            "type": "multiple_choice",
            "question": "ライブラリ選択時に考慮すべき要素として最も重要でないものはどれですか？",
            "code": None,
            "choices": [
                "アクティブな開発とメンテナンス",
                "ドキュメントの充実度",
                "開発者の国籍",
                "コミュニティサポート"
            ],
            "correct": 2,
            "explanation": "開発者の国籍は技術的品質とは関係ありません。重要なのは技術的な要素とサポート体制です。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q12_08",
            "type": "implementation",
            "question": "プロジェクトセットアップを自動化するスクリプトを実装してください",
            "requirements": [
                "関数名: setup_python_project",
                "引数: project_name (文字列), packages (パッケージのリスト)",
                "機能: プロジェクトディレクトリ作成、仮想環境作成、requirements.txt生成",
                "os, subprocess モジュールを使用",
                "戻り値: セットアップ成功時は True、失敗時は False"
            ],
            "test_cases": [
                {
                    "input": ["my_project", ["requests", "pandas"]],
                    "expected": True
                },
                {
                    "input": ["test_project", ["numpy"]],
                    "expected": True
                }
            ],
            "template": """import os
import subprocess

def setup_python_project(project_name, packages):
    # ここに実装してください
    # 1. プロジェクトディレクトリを作成
    # 2. 仮想環境を作成 (venv)
    # 3. requirements.txt ファイルを作成
    # 4. 各ステップでエラーハンドリングを行う
    # 5. 成功時は True、失敗時は False を返す
    pass""",
            "hints": [
                {
                    "level": 1,
                    "text": "os.makedirs() でディレクトリ作成、subprocess.run() でコマンド実行",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "try-except でエラーハンドリング、exist_ok=True でディレクトリ重複を許可",
                    "penalty": 15
                },
                {
                    "level": 3,
                    "text": "try:\n    os.makedirs(project_name, exist_ok=True)\n    venv_path = os.path.join(project_name, 'venv')\n    subprocess.run(['python', '-m', 'venv', venv_path], check=True)\n    req_path = os.path.join(project_name, 'requirements.txt')\n    with open(req_path, 'w') as f:\n        for pkg in packages:\n            f.write(f'{pkg}\\n')\n    return True\nexcept Exception:\n    return False",
                    "penalty": 25
                }
            ],
            "explanation": "プロジェクトセットアップの自動化により、開発環境の構築を効率化できます。",
            "difficulty": 3,
            "category": "実装確認"
        }
    ]
}

def get_quiz_data():
    """クイズデータを返す"""
    return QUIZ_DATA

if __name__ == "__main__":
    print("第12章 外部ライブラリ - 理解度テスト")
    print("=" * 40)
    print(f"問題数: {len(QUIZ_DATA['questions'])}")
    print(f"合格ライン: {QUIZ_DATA['passing_score']}%")
    print("\nこのファイルは quiz_runner.py から実行してください:")
    print("python3 quizzes/quiz_runner.py basics 12")