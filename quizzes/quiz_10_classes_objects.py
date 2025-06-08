#!/usr/bin/env python3
"""
第10章「クラスとオブジェクト」理解度テスト

basics/10_classes_and_objects.py の内容に基づく理解度確認テストです。
70%以上で合格となります。
"""

QUIZ_DATA = {
    "chapter": "10",
    "title": "クラスとオブジェクト",
    "description": "クラス定義、継承、特殊メソッド、ポリモーフィズム、プロパティについて確認します",
    "passing_score": 70,
    "questions": [
        {
            "id": "q10_01",
            "type": "multiple_choice",
            "question": "Pythonでクラスを定義するキーワードはどれですか？",
            "code": None,
            "choices": [
                "def",
                "class",
                "object",
                "type"
            ],
            "correct": 1,
            "explanation": "class キーワードを使ってクラスを定義します。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q10_02",
            "type": "multiple_choice",
            "question": "__init__ メソッドの役割は何ですか？",
            "code": None,
            "choices": [
                "クラスを削除する",
                "オブジェクトを初期化する",
                "メソッドを定義する",
                "継承関係を設定する"
            ],
            "correct": 1,
            "explanation": "__init__ はコンストラクタで、オブジェクトが作成される際に自動的に呼ばれ初期化を行います。",
            "difficulty": 1,
            "category": "理解確認"
        },
        {
            "id": "q10_03",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """class Car:
    wheels = 4  # クラス変数
    
    def __init__(self, brand):
        self.brand = brand  # インスタンス変数

car1 = Car("Toyota")
car2 = Car("Honda")
print(car1.wheels)
print(car2.brand)
print(Car.wheels)""",
            "choices": [
                "4\nHonda\n4",
                "Toyota\nHonda\n4",
                "4\nToyota\n4",
                "エラーが発生する"
            ],
            "correct": 0,
            "explanation": "クラス変数 wheels は全インスタンスで共有され、インスタンス変数 brand は各オブジェクト固有です。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q10_04",
            "type": "fill_blank",
            "question": "継承を使ってクラスを定義する正しい書き方を完成させてください",
            "code_template": "class Dog(____):\n    def bark(self):\n        return 'Woof!'",
            "correct_answer": "Animal",
            "hints": [
                {
                    "level": 1,
                    "text": "継承元となる親クラスの名前を書きます",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "一般的に動物クラスから犬クラスを継承します",
                    "penalty": 10
                }
            ],
            "explanation": "class 子クラス(親クラス): の形式で継承を定義します。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q10_05",
            "type": "predict_output",
            "question": "以下のコードの実行結果を予測してください",
            "code": """class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} ({self.pages}ページ)"
    
    def __len__(self):
        return self.pages

book = Book("Python入門", 300)
print(book)
print(len(book))""",
            "choices": [
                "Python入門 (300ページ)\n300",
                "Book object\n300",
                "Python入門\n300ページ",
                "エラーが発生する"
            ],
            "correct": 0,
            "explanation": "__str__ でprint()時の表示を、__len__ でlen()関数の動作をカスタマイズできます。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q10_06",
            "type": "debug",
            "question": "以下のコードにはエラーがあります。修正してください",
            "buggy_code": '''class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def speak(self):
        return f"{self.name} barks"

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())''',
            "error_type": "LogicalError",
            "correct_code": '''class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 親クラスの初期化を呼ぶ
        self.breed = breed
    
    def speak(self):
        return f"{self.name} barks"

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())''',
            "explanation": "継承したクラスでは super().__init__() を使って親クラスの初期化メソッドを呼ぶべきです。",
            "difficulty": 2,
            "category": "応用確認"
        },
        {
            "id": "q10_07",
            "type": "multiple_choice",
            "question": "@property デコレータの用途は何ですか？",
            "code": None,
            "choices": [
                "メソッドを高速化する",
                "属性のように使えるメソッドを作る",
                "クラス変数を定義する",
                "継承関係を設定する"
            ],
            "correct": 1,
            "explanation": "@property により、メソッドを属性のようにアクセスできるようになります。",
            "difficulty": 2,
            "category": "理解確認"
        },
        {
            "id": "q10_08",
            "type": "implementation",
            "question": "図形の面積計算クラス階層を実装してください",
            "requirements": [
                "抽象基底クラス: Shape (from abc import ABC, abstractmethod を使用)",
                "抽象メソッド: area() - 面積を返す",
                "具象クラス: Rectangle (矩形) - width, height 属性",
                "具象クラス: Circle (円) - radius 属性",
                "PI = 3.14159 を使用"
            ],
            "test_cases": [
                {"input": "Rectangle(4, 5).area()", "expected": 20},
                {"input": "Circle(3).area()", "expected": 28.27431},  # 3.14159 * 3 * 3
                {"input": "Rectangle(2, 3).area()", "expected": 6}
            ],
            "template": """from abc import ABC, abstractmethod

PI = 3.14159

class Shape(ABC):
    # ここに抽象基底クラスを実装してください
    pass

class Rectangle(Shape):
    # ここに矩形クラスを実装してください
    pass

class Circle(Shape):
    # ここに円クラスを実装してください
    pass""",
            "hints": [
                {
                    "level": 1,
                    "text": "@abstractmethod で抽象メソッドを定義し、各クラスで具体的な計算を実装",
                    "penalty": 0
                },
                {
                    "level": 2,
                    "text": "矩形の面積 = width * height、円の面積 = PI * radius * radius",
                    "penalty": 15
                },
                {
                    "level": 3,
                    "text": "class Shape(ABC):\n    @abstractmethod\n    def area(self):\n        pass\n\nclass Rectangle(Shape):\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n    \n    def area(self):\n        return self.width * self.height\n\nclass Circle(Shape):\n    def __init__(self, radius):\n        self.radius = radius\n    \n    def area(self):\n        return PI * self.radius * self.radius",
                    "penalty": 25
                }
            ],
            "explanation": "抽象基底クラスにより、共通のインターフェースを持つクラス階層を設計できます。",
            "difficulty": 3,
            "category": "実装確認"
        }
    ]
}

def get_quiz_data():
    """クイズデータを返す"""
    return QUIZ_DATA

if __name__ == "__main__":
    print("第10章 クラスとオブジェクト - 理解度テスト")
    print("=" * 40)
    print(f"問題数: {len(QUIZ_DATA['questions'])}")
    print(f"合格ライン: {QUIZ_DATA['passing_score']}%")
    print("\nこのファイルは quiz_runner.py から実行してください:")
    print("python3 quizzes/quiz_runner.py basics 10")