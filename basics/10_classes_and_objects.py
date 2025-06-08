#!/usr/bin/env python3
"""
===========================
第10章: クラスとオブジェクト
===========================

オブジェクト指向プログラミングの基本概念を学習します。
クラス、オブジェクト、継承、ポリモーフィズムなど
現代的なプログラミングの重要な概念を習得しましょう。

このファイルを実行すると、オブジェクト指向プログラミングの
基礎から応用まで理解できます。
"""

import platform
from datetime import datetime


def print_chapter_header():
    """章のヘッダーを表示"""
    print("=" * 50)
    print("第10章: クラスとオブジェクト")
    print("=" * 50)
    print()


def lesson_1_class_basics():
    """レッスン1: クラスの基本"""
    print("📚 レッスン1: クラスの基本")
    print("-" * 40)
    print()
    
    print("クラスはオブジェクトの設計図です。")
    print("データ（属性）と処理（メソッド）をまとめて管理できます。")
    print()
    
    # 最初のクラス
    print("最初のクラス:")
    print(">>> class Person:")
    print("...     def __init__(self, name, age):")
    print("...         self.name = name")
    print("...         self.age = age")
    print("...     ")
    print("...     def greet(self):")
    print("...         return f'こんにちは、{self.name}です。{self.age}歳です。'")
    
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def greet(self):
            return f'こんにちは、{self.name}です。{self.age}歳です。'
    
    print(">>> # オブジェクトの作成")
    print(">>> person1 = Person('太郎', 25)")
    person1 = Person('太郎', 25)
    print(">>> person2 = Person('花子', 30)")
    person2 = Person('花子', 30)
    print()
    
    print(">>> print(person1.greet())")
    print(f"    {person1.greet()}")
    print(">>> print(person2.greet())")
    print(f"    {person2.greet()}")
    print()
    
    print(">>> # 属性へのアクセス")
    print(f">>> person1.name  # '{person1.name}'")
    print(f">>> person1.age   # {person1.age}")
    print()
    
    print("💡 __init__ はコンストラクタ（初期化メソッド）")
    print("   self は自分自身のオブジェクトを表す")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_2_attributes_methods():
    """レッスン2: 属性とメソッド"""
    print("📚 レッスン2: 属性とメソッド")
    print("-" * 40)
    print()
    
    print("クラスには様々な種類の属性とメソッドがあります。")
    print()
    
    # より詳細なクラス
    print("詳細なクラスの例:")
    print(">>> class BankAccount:")
    print("...     # クラス変数（全インスタンスで共有）")
    print("...     bank_name = 'Python銀行'")
    print("...     ")
    print("...     def __init__(self, owner, initial_balance=0):")
    print("...         # インスタンス変数（各オブジェクト固有）")
    print("...         self.owner = owner")
    print("...         self.balance = initial_balance")
    print("...         self.transaction_history = []")
    print("...     ")
    print("...     def deposit(self, amount):")
    print("...         '''入金'''")
    print("...         if amount > 0:")
    print("...             self.balance += amount")
    print("...             self._add_transaction(f'入金: {amount}円')")
    print("...             return True")
    print("...         return False")
    print("...     ")
    print("...     def withdraw(self, amount):")
    print("...         '''出金'''")
    print("...         if 0 < amount <= self.balance:")
    print("...             self.balance -= amount")
    print("...             self._add_transaction(f'出金: {amount}円')")
    print("...             return True")
    print("...         return False")
    print("...     ")
    print("...     def _add_transaction(self, description):")
    print("...         '''プライベートメソッド（内部使用）'''")
    print("...         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')")
    print("...         self.transaction_history.append(f'{timestamp}: {description}')")
    print("...     ")
    print("...     def get_statement(self):")
    print("...         '''明細書を取得'''")
    print("...         statement = f'=== {self.bank_name} 通帳 ===\\n'")
    print("...         statement += f'口座名義: {self.owner}\\n'")
    print("...         statement += f'残高: {self.balance}円\\n\\n'")
    print("...         statement += '取引履歴:\\n'")
    print("...         for transaction in self.transaction_history[-5:]:")
    print("...             statement += f'  {transaction}\\n'")
    print("...         return statement")
    
    class BankAccount:
        # クラス変数（全インスタンスで共有）
        bank_name = 'Python銀行'
        
        def __init__(self, owner, initial_balance=0):
            # インスタンス変数（各オブジェクト固有）
            self.owner = owner
            self.balance = initial_balance
            self.transaction_history = []
        
        def deposit(self, amount):
            """入金"""
            if amount > 0:
                self.balance += amount
                self._add_transaction(f'入金: {amount}円')
                return True
            return False
        
        def withdraw(self, amount):
            """出金"""
            if 0 < amount <= self.balance:
                self.balance -= amount
                self._add_transaction(f'出金: {amount}円')
                return True
            return False
        
        def _add_transaction(self, description):
            """プライベートメソッド（内部使用）"""
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
            self.transaction_history.append(f'{timestamp}: {description}')
        
        def get_statement(self):
            """明細書を取得"""
            statement = f'=== {self.bank_name} 通帳 ===\n'
            statement += f'口座名義: {self.owner}\n'
            statement += f'残高: {self.balance}円\n\n'
            statement += '取引履歴:\n'
            for transaction in self.transaction_history[-5:]:
                statement += f'  {transaction}\n'
            return statement
    
    print(">>> # 口座を作成")
    print(">>> account = BankAccount('山田太郎', 10000)")
    account = BankAccount('山田太郎', 10000)
    print(">>> account.deposit(5000)")
    account.deposit(5000)
    print(">>> account.withdraw(3000)")
    account.withdraw(3000)
    print()
    
    print(">>> print(account.get_statement())")
    print(account.get_statement())
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_3_special_methods():
    """レッスン3: 特殊メソッド（マジックメソッド）"""
    print("📚 レッスン3: 特殊メソッド（マジックメソッド）")
    print("-" * 40)
    print()
    
    print("__で囲まれた特殊メソッドで、オブジェクトの振る舞いを定義できます。")
    print()
    
    # 特殊メソッドを持つクラス
    print("特殊メソッドの例:")
    print(">>> class Book:")
    print("...     def __init__(self, title, author, pages):")
    print("...         self.title = title")
    print("...         self.author = author")
    print("...         self.pages = pages")
    print("...     ")
    print("...     def __str__(self):")
    print("...         '''print()で表示される文字列'''")
    print("...         return f'{self.title} by {self.author}'")
    print("...     ")
    print("...     def __repr__(self):")
    print("...         '''開発者向けの表現'''")
    print("...         return f'Book(\"{self.title}\", \"{self.author}\", {self.pages})'")
    print("...     ")
    print("...     def __len__(self):")
    print("...         '''len()で呼ばれる'''")
    print("...         return self.pages")
    print("...     ")
    print("...     def __lt__(self, other):")
    print("...         '''< 演算子での比較'''")
    print("...         return self.pages < other.pages")
    print("...     ")
    print("...     def __add__(self, other):")
    print("...         '''+ 演算子での加算'''")
    print("...         return self.pages + other.pages")
    
    class Book:
        def __init__(self, title, author, pages):
            self.title = title
            self.author = author
            self.pages = pages
        
        def __str__(self):
            """print()で表示される文字列"""
            return f'{self.title} by {self.author}'
        
        def __repr__(self):
            """開発者向けの表現"""
            return f'Book("{self.title}", "{self.author}", {self.pages})'
        
        def __len__(self):
            """len()で呼ばれる"""
            return self.pages
        
        def __lt__(self, other):
            """< 演算子での比較"""
            return self.pages < other.pages
        
        def __add__(self, other):
            """+ 演算子での加算"""
            return self.pages + other.pages
    
    print(">>> book1 = Book('Python入門', '山田', 300)")
    book1 = Book('Python入門', '山田', 300)
    print(">>> book2 = Book('Web開発', '田中', 250)")
    book2 = Book('Web開発', '田中', 250)
    print()
    
    print(f">>> print(book1)      # {book1}")
    print(f">>> len(book1)        # {len(book1)}")
    print(f">>> book1 < book2     # {book1 < book2}")
    print(f">>> book1 + book2     # {book1 + book2}")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_4_inheritance():
    """レッスン4: 継承"""
    print("📚 レッスン4: 継承")
    print("-" * 40)
    print()
    
    print("継承により、既存のクラスを基に新しいクラスを作成できます。")
    print()
    
    # 基底クラス
    print("基底クラス（親クラス）:")
    print(">>> class Animal:")
    print("...     def __init__(self, name, species):")
    print("...         self.name = name")
    print("...         self.species = species")
    print("...     ")
    print("...     def make_sound(self):")
    print("...         return f'{self.name}が鳴いています'")
    print("...     ")
    print("...     def info(self):")
    print("...         return f'{self.name}は{self.species}です'")
    
    class Animal:
        def __init__(self, name, species):
            self.name = name
            self.species = species
        
        def make_sound(self):
            return f'{self.name}が鳴いています'
        
        def info(self):
            return f'{self.name}は{self.species}です'
    
    # 派生クラス
    print(">>> # 派生クラス（子クラス）")
    print(">>> class Dog(Animal):")
    print("...     def __init__(self, name, breed):")
    print("...         super().__init__(name, '犬')  # 親クラスの初期化")
    print("...         self.breed = breed")
    print("...     ")
    print("...     def make_sound(self):  # メソッドのオーバーライド")
    print("...         return f'{self.name}がワンワン鳴いています'")
    print("...     ")
    print("...     def fetch(self):  # 新しいメソッド")
    print("...         return f'{self.name}がボールを取ってきました'")
    
    class Dog(Animal):
        def __init__(self, name, breed):
            super().__init__(name, '犬')  # 親クラスの初期化
            self.breed = breed
        
        def make_sound(self):  # メソッドのオーバーライド
            return f'{self.name}がワンワン鳴いています'
        
        def fetch(self):  # 新しいメソッド
            return f'{self.name}がボールを取ってきました'
    
    print(">>> class Cat(Animal):")
    print("...     def __init__(self, name, color):")
    print("...         super().__init__(name, '猫')")
    print("...         self.color = color")
    print("...     ")
    print("...     def make_sound(self):")
    print("...         return f'{self.name}がニャーニャー鳴いています'")
    print("...     ")
    print("...     def climb(self):")
    print("...         return f'{self.name}が木に登りました'")
    
    class Cat(Animal):
        def __init__(self, name, color):
            super().__init__(name, '猫')
            self.color = color
        
        def make_sound(self):
            return f'{self.name}がニャーニャー鳴いています'
        
        def climb(self):
            return f'{self.name}が木に登りました'
    
    print(">>> # 使用例")
    print(">>> dog = Dog('ポチ', '柴犬')")
    dog = Dog('ポチ', '柴犬')
    print(">>> cat = Cat('タマ', '白')")
    cat = Cat('タマ', '白')
    print()
    
    print(f">>> dog.info()        # {dog.info()}")
    print(f">>> dog.make_sound()  # {dog.make_sound()}")
    print(f">>> dog.fetch()       # {dog.fetch()}")
    print()
    print(f">>> cat.info()        # {cat.info()}")
    print(f">>> cat.make_sound()  # {cat.make_sound()}")
    print(f">>> cat.climb()       # {cat.climb()}")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_5_polymorphism():
    """レッスン5: ポリモーフィズム"""
    print("📚 レッスン5: ポリモーフィズム")
    print("-" * 40)
    print()
    
    print("ポリモーフィズムにより、同じインターフェースで")
    print("異なるオブジェクトを扱えます。")
    print()
    
    # 前のレッスンのクラスを使用
    print("ポリモーフィズムの例:")
    print(">>> def animal_concert(animals):")
    print("...     '''動物たちのコンサート'''")
    print("...     print('🎵 動物コンサート開始！ 🎵')")
    print("...     for animal in animals:")
    print("...         print(f'  {animal.make_sound()}')")
    print("...     print('🎵 コンサート終了！ 🎵')")
    
    def animal_concert(animals):
        """動物たちのコンサート"""
        print('🎵 動物コンサート開始！ 🎵')
        for animal in animals:
            print(f'  {animal.make_sound()}')
        print('🎵 コンサート終了！ 🎵')
    
    # 異なるクラスのオブジェクトを同じように扱う
    class Dog:
        def __init__(self, name):
            self.name = name
        def make_sound(self):
            return f'{self.name}がワンワン鳴いています'
    
    class Cat:
        def __init__(self, name):
            self.name = name
        def make_sound(self):
            return f'{self.name}がニャーニャー鳴いています'
    
    class Bird:
        def __init__(self, name):
            self.name = name
        def make_sound(self):
            return f'{self.name}がチュンチュン鳴いています'
    
    print(">>> animals = [")
    print("...     Dog('ポチ'),")
    print("...     Cat('タマ'),")
    print("...     Bird('ピーチャン')")
    print("... ]")
    animals = [
        Dog('ポチ'),
        Cat('タマ'),
        Bird('ピーチャン')
    ]
    
    print(">>> animal_concert(animals)")
    animal_concert(animals)
    print()
    
    # 抽象基底クラスの概念
    print("抽象基底クラス（ABCモジュール）の活用:")
    print(">>> from abc import ABC, abstractmethod")
    print(">>> ")
    print(">>> class Shape(ABC):")
    print("...     @abstractmethod")
    print("...     def area(self):")
    print("...         pass")
    print("...     ")
    print("...     @abstractmethod")
    print("...     def perimeter(self):")
    print("...         pass")
    
    from abc import ABC, abstractmethod
    
    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass
        
        @abstractmethod
        def perimeter(self):
            pass
    
    print(">>> class Rectangle(Shape):")
    print("...     def __init__(self, width, height):")
    print("...         self.width = width")
    print("...         self.height = height")
    print("...     ")
    print("...     def area(self):")
    print("...         return self.width * self.height")
    print("...     ")
    print("...     def perimeter(self):")
    print("...         return 2 * (self.width + self.height)")
    
    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
        
        def area(self):
            return self.width * self.height
        
        def perimeter(self):
            return 2 * (self.width + self.height)
    
    print(">>> rect = Rectangle(5, 3)")
    rect = Rectangle(5, 3)
    print(f">>> rect.area()       # {rect.area()}")
    print(f">>> rect.perimeter()  # {rect.perimeter()}")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_6_class_design():
    """レッスン6: クラス設計のベストプラクティス"""
    print("📚 レッスン6: クラス設計のベストプラクティス")
    print("-" * 40)
    print()
    
    print("良いクラス設計のための指針を学びます。")
    print()
    
    # プロパティ（getter/setter）
    print("プロパティ（@property）の活用:")
    print(">>> class Temperature:")
    print("...     def __init__(self, celsius=0):")
    print("...         self._celsius = celsius")
    print("...     ")
    print("...     @property")
    print("...     def celsius(self):")
    print("...         return self._celsius")
    print("...     ")
    print("...     @celsius.setter")
    print("...     def celsius(self, value):")
    print("...         if value < -273.15:")
    print("...             raise ValueError('絶対零度未満は設定できません')")
    print("...         self._celsius = value")
    print("...     ")
    print("...     @property")
    print("...     def fahrenheit(self):")
    print("...         return self._celsius * 9/5 + 32")
    print("...     ")
    print("...     @fahrenheit.setter")
    print("...     def fahrenheit(self, value):")
    print("...         self.celsius = (value - 32) * 5/9")
    
    class Temperature:
        def __init__(self, celsius=0):
            self._celsius = celsius
        
        @property
        def celsius(self):
            return self._celsius
        
        @celsius.setter
        def celsius(self, value):
            if value < -273.15:
                raise ValueError('絶対零度未満は設定できません')
            self._celsius = value
        
        @property
        def fahrenheit(self):
            return self._celsius * 9/5 + 32
        
        @fahrenheit.setter
        def fahrenheit(self, value):
            self.celsius = (value - 32) * 5/9
    
    print(">>> temp = Temperature(25)")
    temp = Temperature(25)
    print(f">>> temp.celsius      # {temp.celsius}")
    print(f">>> temp.fahrenheit   # {temp.fahrenheit}")
    print(">>> temp.celsius = 30")
    temp.celsius = 30
    print(f">>> temp.fahrenheit   # {temp.fahrenheit}")
    print()
    
    # 設計の原則
    print("設計の原則:")
    print("1. 単一責任の原則")
    print("   → 1つのクラスは1つの責任を持つ")
    print()
    print("2. カプセル化")
    print("   → 内部実装を隠し、公開インターフェースを提供")
    print()
    print("3. 継承よりコンポジション")
    print("   → 「is-a」より「has-a」を優先検討")
    print()
    print("4. 明確な命名")
    print("   → クラス名、メソッド名は目的を明確に表現")
    print()
    
    # 実践例
    print("実践例（学生管理システム）:")
    print(">>> class Student:")
    print("...     def __init__(self, student_id, name):")
    print("...         self.student_id = student_id")
    print("...         self.name = name")
    print("...         self._grades = []")
    print("...     ")
    print("...     def add_grade(self, subject, score):")
    print("...         if 0 <= score <= 100:")
    print("...             self._grades.append({'subject': subject, 'score': score})")
    print("...         else:")
    print("...             raise ValueError('成績は0-100の範囲で入力してください')")
    print("...     ")
    print("...     @property")
    print("...     def average_grade(self):")
    print("...         if not self._grades:")
    print("...             return 0")
    print("...         return sum(g['score'] for g in self._grades) / len(self._grades)")
    print("...     ")
    print("...     def __str__(self):")
    print("...         return f'学生ID: {self.student_id}, 名前: {self.name}, 平均点: {self.average_grade:.1f}'")
    
    class Student:
        def __init__(self, student_id, name):
            self.student_id = student_id
            self.name = name
            self._grades = []
        
        def add_grade(self, subject, score):
            if 0 <= score <= 100:
                self._grades.append({'subject': subject, 'score': score})
            else:
                raise ValueError('成績は0-100の範囲で入力してください')
        
        @property
        def average_grade(self):
            if not self._grades:
                return 0
            return sum(g['score'] for g in self._grades) / len(self._grades)
        
        def __str__(self):
            return f'学生ID: {self.student_id}, 名前: {self.name}, 平均点: {self.average_grade:.1f}'
    
    print(">>> student = Student('S001', '山田太郎')")
    student = Student('S001', '山田太郎')
    print(">>> student.add_grade('数学', 85)")
    student.add_grade('数学', 85)
    print(">>> student.add_grade('英語', 92)")
    student.add_grade('英語', 92)
    print(f">>> print(student)")
    print(f"    {student}")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def practice_exercises():
    """練習問題"""
    print("🏃 練習してみよう！")
    print("=" * 50)
    print()
    
    print("以下の練習問題を試してください：")
    print()
    
    print("【練習1】車クラスの設計")
    print("Vehicle基底クラスを作成し、Car、Bicycleを継承")
    print("start_engine()、stop_engine()メソッドを実装")
    print()
    
    print("【練習2】図書館管理システム")
    print("Book、Library、Memberクラスを設計")
    print("貸出、返却、検索機能を実装")
    print()
    
    print("【練習3】ゲームキャラクター")
    print("Character基底クラスから、Warrior、Mageを継承")
    print("attack()、defend()、use_skill()メソッドを実装")
    print()
    
    print("【練習4】データコンテナ")
    print("Stack、Queueクラスを作成")
    print("push/pop、enqueue/dequeue操作を実装")
    print()
    
    input("練習が終わったらEnterキーを押してください...")
    print()


def show_summary():
    """まとめ"""
    print("📝 第10章のまとめ")
    print("=" * 50)
    print()
    
    print("クラスとオブジェクトについて学んだこと：")
    print("✅ クラスの定義と__init__メソッド")
    print("✅ インスタンス変数とクラス変数")
    print("✅ メソッドの定義と呼び出し")
    print("✅ 特殊メソッド（__str__、__len__、__add__ など）")
    print("✅ 継承とメソッドのオーバーライド")
    print("✅ ポリモーフィズムの活用")
    print("✅ プロパティ（@property）")
    print("✅ 抽象基底クラス（ABC）")
    print()
    
    print("オブジェクト指向プログラミングの利点：")
    print("• コードの再利用性向上")
    print("• 保守性の向上")
    print("• 複雑な問題の整理")
    print("• チーム開発での分業")
    print()
    
    print("次のステップ：")
    print("• 標準ライブラリの活用")
    print("• 外部ライブラリの導入")
    print()


def show_completion_message():
    """完了メッセージ"""
    print("\n" + "🎉" * 20)
    print("   ファイル 10 の学習完了！   ")
    print("🎉" * 20)
    
    print(f"\n📚 理解度テストを受けましょう")
    print("以下のコマンドをコピー&ペーストして実行してください:\n")
    
    # OS別コマンド表示
    python_cmd = "py" if platform.system() == "Windows" else "python3"
    print(f"   {python_cmd} quizzes/quiz_runner.py basics 10")
    
    print(f"\n✅ テスト合格後、次に進みましょう:")
    print(f"   {python_cmd} basics/11_standard_library.py")
    
    print("\n💡 困ったときは:")
    print(f"   {python_cmd} quizzes/quiz_runner.py help")
    print("=" * 50)


def main():
    """メイン処理"""
    print_chapter_header()
    
    # 各レッスンを順番に実行
    lesson_1_class_basics()
    lesson_2_attributes_methods()
    lesson_3_special_methods()
    lesson_4_inheritance()
    lesson_5_polymorphism()
    lesson_6_class_design()
    
    # 練習問題
    practice_exercises()
    
    # まとめ
    show_summary()
    
    # 完了メッセージ
    show_completion_message()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nプログラムを中断しました。")
        print("続きはまた後で！")
    except Exception as e:
        print(f"\nエラーが発生しました: {e}")
        print("エラーの内容を確認して、もう一度試してください。")