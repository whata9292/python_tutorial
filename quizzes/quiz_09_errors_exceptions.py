#!/usr/bin/env python3
"""
第9章「エラーと例外処理」理解度テスト

basics/09_errors_and_exceptions.py の内容に基づく理解度確認テストです。
70%以上で合格となります。
"""

QUIZ_DATA = {
    "chapter": "09",
    "title": "エラーと例外処理",
    "description": "try-except文、例外の種類、カスタム例外、デバッグ技法について確認します",
    "passing_score": 70,
    "questions": [
        {
            "id": "q09_01",
            "type": "multiple_choice",
            "question": "Pythonで例外を捕捉するために使用するキーワードの組み合わせはどれですか？",
            "code": None,
            "choices": [
                "try - catch",
                "try - except",
                "catch - except",
                "handle - error"
            ],
            "correct": 1,
            "explanation": "Python では try-except 文を使って例外を捕捉します。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q09_02",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """try:
    result = 10 / 0
    print("計算成功")
except ZeroDivisionError:
    print("ゼロ除算エラー")
except Exception:
    print("その他のエラー")
else:
    print("例外なし")
finally:
    print("必ず実行")""",
            "choices": [
                "計算成功\n例外なし\n必ず実行",
                "ゼロ除算エラー\n必ず実行",
                "その他のエラー\n必ず実行",
                "ゼロ除算エラー\n例外なし\n必ず実行"
            ],
            "correct": 1,
            "explanation": "ゼロ除算でZeroDivisionErrorが発生し、finally節は必ず実行されます。else節は例外がない場合のみ実行されます。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q09_03",
            "type": "fill_blank",
            "question": "意図的に例外を発生させるために使用するキーワードを入力してください",
            "code_template": """def validate_age(age):
    if age < 0:
        ____ ValueError("年齢は0以上である必要があります")
    return True""",
            "correct_answer": "raise",
            "hints": [
                {
                    "level": 1,
                    "text": "例外を「発生させる」「投げる」ためのキーワードです",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "英語で「上げる」という意味の単語です",
                    "penalty": 10
                }
            ],
            "explanation": "raise キーワードで意図的に例外を発生させることができます。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q09_04",
            "type": "multiple_choice",
            "question": "存在しないリストのインデックスにアクセスした場合に発生する例外はどれですか？",
            "code": "my_list = [1, 2, 3]\nprint(my_list[5])",
            "choices": [
                "NameError",
                "IndexError",
                "KeyError",
                "ValueError"
            ],
            "correct": 1,
            "explanation": "リストの範囲外インデックスにアクセスすると IndexError が発生します。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q09_05",
            "type": "debug",
            "question": "以下のコードにはエラーがあります。修正してください",
            "buggy_code": '''def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("ゼロで割ることはできません")
        # return文が抜けている

answer = safe_divide(10, 0)
print(f"結果: {answer}")''',
            "error_type": "NoneType",
            "correct_code": '''def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("ゼロで割ることはできません")
        return None  # または適切なデフォルト値

answer = safe_divide(10, 0)
print(f"結果: {answer}")''',
            "explanation": "例外処理ブロックでも適切な戻り値を返す必要があります。return文がないとNoneが返されます。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q09_06",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """try:
    data = {'name': '太郎', 'age': 25}
    print(data['height'])
except KeyError as e:
    print(f"キーエラー: {e}")
except Exception as e:
    print(f"その他のエラー: {e}")""",
            "choices": [
                "キーエラー: 'height'",
                "その他のエラー: 'height'",
                "KeyError: 'height'",
                "エラーは発生しない"
            ],
            "correct": 0,
            "explanation": "存在しないキー 'height' にアクセスするとKeyErrorが発生し、except KeyError で捕捉されます。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q09_07",
            "type": "multiple_choice",
            "question": "カスタム例外クラスを作成する際の正しい書き方はどれですか？",
            "code": None,
            "choices": [
                "class MyError:",
                "class MyError(Error):",
                "class MyError(Exception):",
                "class MyError(BaseException):"
            ],
            "correct": 2,
            "explanation": "カスタム例外は Exception クラスを継承して作成するのが一般的です。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q09_08",
            "type": "implementation",
            "question": "銀行口座の入出金を安全に処理するクラスを実装してください",
            "requirements": [
                "クラス名: SafeBankAccount",
                "初期化: __init__(self, initial_balance=0)",
                "メソッド: withdraw(self, amount) - 出金処理",
                "残高不足の場合はカスタム例外 InsufficientFundsError を発生",
                "負の金額の場合は ValueError を発生",
                "成功時は新しい残高を返す"
            ],
            "test_cases": [
                {"input": "account = SafeBankAccount(1000); account.withdraw(300)", "expected": 700},
                {"input": "account = SafeBankAccount(100); account.withdraw(200)", "expected": "InsufficientFundsError"},
                {"input": "account = SafeBankAccount(100); account.withdraw(-50)", "expected": "ValueError"}
            ],
            "template": """# カスタム例外の定義
class InsufficientFundsError(Exception):
    pass

class SafeBankAccount:
    def __init__(self, initial_balance=0):
        # ここに実装してください
        pass
    
    def withdraw(self, amount):
        # ここに実装してください
        # 1. 負の金額チェック -> ValueError
        # 2. 残高不足チェック -> InsufficientFundsError  
        # 3. 正常処理: 残高から減算して新残高を返す
        pass""",
            "hints": [
                {
                    "level": 1,
                    "text": "if文で条件をチェックし、raise で例外を発生させます",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "amount < 0 で負数チェック、amount > self.balance で残高チェック",
                    "penalty": 15
                },
                {
                    "level": 3,
                    "text": "def __init__(self, initial_balance=0):\n    self.balance = initial_balance\n\ndef withdraw(self, amount):\n    if amount < 0:\n        raise ValueError('金額は0以上である必要があります')\n    if amount > self.balance:\n        raise InsufficientFundsError('残高不足です')\n    self.balance -= amount\n    return self.balance",
                    "penalty": 25
                }
            ],
            "explanation": "適切な例外処理により、不正な操作を防ぎ、エラーの原因を明確にできます。",
            "difficulty": 3,
            "category": "実装確認"
        }
    ]
}

def get_quiz_data():
    """クイズデータを返す"""
    return QUIZ_DATA

if __name__ == "__main__":
    print("第9章 エラーと例外処理 - 理解度テスト")
    print("=" * 40)
    print(f"問題数: {len(QUIZ_DATA['questions'])}")
    print(f"合格ライン: {QUIZ_DATA['passing_score']}%")
    print("\nこのファイルは quiz_runner.py から実行してください:")
    print("python3 quizzes/quiz_runner.py basics 09")