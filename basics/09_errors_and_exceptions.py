#!/usr/bin/env python3
"""
===========================
第9章: エラーと例外処理
===========================

プログラム実行時に発生するエラーや例外を適切に処理する
方法を学習します。堅牢で信頼性の高いプログラムを
作成するための重要な技術です。

このファイルを実行すると、エラーハンドリングの
基本から応用まで習得できます。
"""

import platform
import traceback
import logging
from typing import Union


def print_chapter_header():
    """章のヘッダーを表示"""
    print("=" * 50)
    print("第9章: エラーと例外処理")
    print("=" * 50)
    print()


def lesson_1_understanding_errors():
    """レッスン1: エラーの理解"""
    print("📚 レッスン1: エラーの理解")
    print("-" * 40)
    print()
    
    print("Pythonでは実行時にエラー（例外）が発生することがあります。")
    print("エラーを理解して適切に対処することが重要です。")
    print()
    
    # よくあるエラーの例
    print("よくあるエラーの例:")
    print()
    
    print("1. SyntaxError（構文エラー）:")
    print("   # if x == 5  # コロンが不足")
    print("   # SyntaxError: invalid syntax")
    print()
    
    print("2. NameError（名前エラー）:")
    print("   >>> print(undefined_variable)")
    print("   # NameError: name 'undefined_variable' is not defined")
    print()
    
    print("3. TypeError（型エラー）:")
    print("   >>> '5' + 3")
    print("   # TypeError: can only concatenate str (not \"int\") to str")
    print()
    
    print("4. ValueError（値エラー）:")
    print("   >>> int('abc')")
    print("   # ValueError: invalid literal for int() with base 10: 'abc'")
    print()
    
    print("5. IndexError（インデックスエラー）:")
    print("   >>> my_list = [1, 2, 3]")
    print("   >>> my_list[5]")
    print("   # IndexError: list index out of range")
    print()
    
    print("6. KeyError（キーエラー）:")
    print("   >>> my_dict = {'a': 1}")
    print("   >>> my_dict['b']")
    print("   # KeyError: 'b'")
    print()
    
    print("💡 エラーメッセージは問題解決の重要な手がかりです")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_2_try_except_basics():
    """レッスン2: try-except の基本"""
    print("📚 レッスン2: try-except の基本")
    print("-" * 40)
    print()
    
    print("try-except 文でエラーを捕捉し、適切に処理できます。")
    print()
    
    # 基本的な try-except
    print("基本的な try-except:")
    print(">>> try:")
    print("...     result = 10 / 0")
    print("... except ZeroDivisionError:")
    print("...     print('ゼロで割ることはできません')")
    
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print('ゼロで割ることはできません')
    print()
    
    # 複数の例外を処理
    print("複数の例外を処理:")
    print(">>> def safe_convert(value):")
    print("...     try:")
    print("...         return int(value)")
    print("...     except ValueError:")
    print("...         print(f'数値に変換できません: {value}')")
    print("...         return None")
    print("...     except TypeError:")
    print("...         print('変換可能な型ではありません')")
    print("...         return None")
    
    def safe_convert(value):
        try:
            return int(value)
        except ValueError:
            print(f'数値に変換できません: {value}')
            return None
        except TypeError:
            print('変換可能な型ではありません')
            return None
    
    print(">>> safe_convert('123')")
    print(f"    {safe_convert('123')}")
    print(">>> safe_convert('abc')")
    print(f"    {safe_convert('abc')}")
    print()
    
    # 一括での例外処理
    print("複数の例外を一括で処理:")
    print(">>> def safe_operation(a, b):")
    print("...     try:")
    print("...         return a / b")
    print("...     except (ZeroDivisionError, TypeError) as e:")
    print("...         print(f'エラーが発生: {e}')")
    print("...         return None")
    
    def safe_operation(a, b):
        try:
            return a / b
        except (ZeroDivisionError, TypeError) as e:
            print(f'エラーが発生: {e}')
            return None
    
    print(">>> safe_operation(10, 2)")
    print(f"    {safe_operation(10, 2)}")
    print(">>> safe_operation(10, 0)")
    print(f"    {safe_operation(10, 0)}")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_3_else_finally():
    """レッスン3: else と finally"""
    print("📚 レッスン3: else と finally")
    print("-" * 40)
    print()
    
    print("try-except には else と finally 節も使えます。")
    print()
    
    # else 節
    print("else 節（例外が発生しなかった場合）:")
    print(">>> def divide_numbers(a, b):")
    print("...     try:")
    print("...         result = a / b")
    print("...     except ZeroDivisionError:")
    print("...         print('ゼロで割ることはできません')")
    print("...     else:")
    print("...         print(f'計算成功: {a} / {b} = {result}')")
    print("...         return result")
    
    def divide_numbers(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print('ゼロで割ることはできません')
            return None
        else:
            print(f'計算成功: {a} / {b} = {result}')
            return result
    
    print(">>> divide_numbers(10, 2)")
    divide_numbers(10, 2)
    print(">>> divide_numbers(10, 0)")
    divide_numbers(10, 0)
    print()
    
    # finally 節
    print("finally 節（必ず実行される）:")
    print(">>> def read_file_demo(filename):")
    print("...     file = None")
    print("...     try:")
    print("...         file = open(filename, 'r')")
    print("...         content = file.read()")
    print("...         return content")
    print("...     except FileNotFoundError:")
    print("...         print('ファイルが見つかりません')")
    print("...     finally:")
    print("...         if file:")
    print("...             file.close()")
    print("...             print('ファイルを閉じました')")
    
    def read_file_demo(filename):
        file = None
        try:
            file = open(filename, 'r')
            content = file.read()
            return content
        except FileNotFoundError:
            print('ファイルが見つかりません')
            return None
        finally:
            if file:
                file.close()
                print('ファイルを閉じました')
    
    print(">>> read_file_demo('nonexistent.txt')")
    read_file_demo('nonexistent.txt')
    print()
    
    print("💡 with文を使えばfinallyは不要になることが多いです")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_4_raising_exceptions():
    """レッスン4: 例外の発生"""
    print("📚 レッスン4: 例外の発生")
    print("-" * 40)
    print()
    
    print("raise 文で意図的に例外を発生させることができます。")
    print()
    
    # 基本的な raise
    print("基本的な例外の発生:")
    print(">>> def check_age(age):")
    print("...     if age < 0:")
    print("...         raise ValueError('年齢は0以上である必要があります')")
    print("...     if age > 150:")
    print("...         raise ValueError('年齢が現実的ではありません')")
    print("...     return f'{age}歳です'")
    
    def check_age(age):
        if age < 0:
            raise ValueError('年齢は0以上である必要があります')
        if age > 150:
            raise ValueError('年齢が現実的ではありません')
        return f'{age}歳です'
    
    print(">>> check_age(25)")
    print(f"    '{check_age(25)}'")
    
    print(">>> # check_age(-5)  # ValueError が発生")
    try:
        check_age(-5)
    except ValueError as e:
        print(f"    ValueError: {e}")
    print()
    
    # 例外の再発生
    print("例外の再発生（re-raise）:")
    print(">>> def wrapper_function(age):")
    print("...     try:")
    print("...         return check_age(age)")
    print("...     except ValueError:")
    print("...         print('年齢チェックでエラーが発生しました')")
    print("...         raise  # 例外を再発生")
    
    def wrapper_function(age):
        try:
            return check_age(age)
        except ValueError:
            print('年齢チェックでエラーが発生しました')
            raise  # 例外を再発生
    
    print(">>> # wrapper_function(200)")
    try:
        wrapper_function(200)
    except ValueError as e:
        print(f"    最終的にキャッチ: {e}")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_5_custom_exceptions():
    """レッスン5: カスタム例外"""
    print("📚 レッスン5: カスタム例外")
    print("-" * 40)
    print()
    
    print("独自の例外クラスを作成できます。")
    print()
    
    # カスタム例外の定義
    print("カスタム例外の定義:")
    print(">>> class InvalidPasswordError(Exception):")
    print("...     '''パスワードが無効な場合の例外'''")
    print("...     pass")
    print()
    
    class InvalidPasswordError(Exception):
        """パスワードが無効な場合の例外"""
        pass
    
    class WeakPasswordError(InvalidPasswordError):
        """パスワードが弱い場合の例外"""
        pass
    
    print(">>> def validate_password(password):")
    print("...     if len(password) < 8:")
    print("...         raise WeakPasswordError('パスワードは8文字以上必要です')")
    print("...     if password.lower() == password:")
    print("...         raise WeakPasswordError('大文字を含める必要があります')")
    print("...     return True")
    
    def validate_password(password):
        if len(password) < 8:
            raise WeakPasswordError('パスワードは8文字以上必要です')
        if password.lower() == password:
            raise WeakPasswordError('大文字を含める必要があります')
        return True
    
    print(">>> validate_password('MyPassword123')")
    print(f"    {validate_password('MyPassword123')}")
    
    print(">>> # validate_password('weak')")
    try:
        validate_password('weak')
    except WeakPasswordError as e:
        print(f"    WeakPasswordError: {e}")
    print()
    
    # より詳細なカスタム例外
    print("詳細情報を持つカスタム例外:")
    print(">>> class ValidationError(Exception):")
    print("...     def __init__(self, message, field=None, code=None):")
    print("...         super().__init__(message)")
    print("...         self.field = field")
    print("...         self.code = code")
    
    class ValidationError(Exception):
        def __init__(self, message, field=None, code=None):
            super().__init__(message)
            self.field = field
            self.code = code
    
    print(">>> try:")
    print("...     raise ValidationError('無効な値', field='email', code='INVALID_FORMAT')")
    print("... except ValidationError as e:")
    print("...     print(f'エラー: {e}')")
    print("...     print(f'フィールド: {e.field}')")
    print("...     print(f'コード: {e.code}')")
    
    try:
        raise ValidationError('無効な値', field='email', code='INVALID_FORMAT')
    except ValidationError as e:
        print(f'    エラー: {e}')
        print(f'    フィールド: {e.field}')
        print(f'    コード: {e.code}')
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_6_debugging_techniques():
    """レッスン6: デバッグ技法"""
    print("📚 レッスン6: デバッグ技法")
    print("-" * 40)
    print()
    
    print("エラーを特定し、解決するためのテクニックを学びます。")
    print()
    
    # トレースバック
    print("トレースバック（スタックトレース）:")
    print(">>> import traceback")
    print(">>> ")
    print(">>> def function_c():")
    print("...     x = 1 / 0  # エラー発生")
    print(">>> ")
    print(">>> def function_b():")
    print("...     function_c()")
    print(">>> ")
    print(">>> def function_a():")
    print("...     function_b()")
    
    def function_c():
        x = 1 / 0  # エラー発生
    
    def function_b():
        function_c()
    
    def function_a():
        function_b()
    
    print(">>> try:")
    print("...     function_a()")
    print("... except Exception:")
    print("...     traceback.print_exc()")
    
    try:
        function_a()
    except Exception:
        print("    Traceback (most recent call last):")
        print("      File \"...\", line ..., in function_a")
        print("        function_b()")
        print("      File \"...\", line ..., in function_b")
        print("        function_c()")
        print("      File \"...\", line ..., in function_c")
        print("        x = 1 / 0")
        print("    ZeroDivisionError: division by zero")
    print()
    
    # ログ出力
    print("ログを使ったデバッグ:")
    print(">>> import logging")
    print(">>> logging.basicConfig(level=logging.DEBUG)")
    print(">>> ")
    print(">>> def calculate_with_logging(a, b):")
    print("...     logging.debug(f'計算開始: a={a}, b={b}')")
    print("...     try:")
    print("...         result = a / b")
    print("...         logging.info(f'計算成功: {result}')")
    print("...         return result")
    print("...     except ZeroDivisionError:")
    print("...         logging.error('ゼロ除算エラーが発生')")
    print("...         raise")
    
    # ログ設定（実際のログは表示しない）
    def calculate_with_logging(a, b):
        print(f"    DEBUG: 計算開始: a={a}, b={b}")
        try:
            result = a / b
            print(f"    INFO: 計算成功: {result}")
            return result
        except ZeroDivisionError:
            print(f"    ERROR: ゼロ除算エラーが発生")
            raise
    
    print(">>> calculate_with_logging(10, 2)")
    calculate_with_logging(10, 2)
    print()
    
    # アサーション
    print("アサーション（assert）:")
    print(">>> def factorial(n):")
    print("...     assert n >= 0, '負の数の階乗は計算できません'")
    print("...     assert isinstance(n, int), '整数である必要があります'")
    print("...     if n <= 1:")
    print("...         return 1")
    print("...     return n * factorial(n - 1)")
    
    def factorial(n):
        assert n >= 0, '負の数の階乗は計算できません'
        assert isinstance(n, int), '整数である必要があります'
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    
    print(">>> factorial(5)")
    print(f"    {factorial(5)}")
    
    print(">>> # factorial(-1)  # AssertionError")
    try:
        factorial(-1)
    except AssertionError as e:
        print(f"    AssertionError: {e}")
    print()
    
    print("💡 本格的なデバッグには pdb モジュールも便利です")
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
    
    print("【練習1】安全な計算機")
    print("ユーザー入力を受け取って四則演算を行う")
    print("すべての可能なエラーを適切に処理")
    print()
    
    print("【練習2】ファイル処理ユーティリティ")
    print("ファイルの読み書きを行う関数を作成")
    print("FileNotFoundError、PermissionError などを処理")
    print()
    
    print("【練習3】カスタム例外の設計")
    print("銀行口座クラスを作成")
    print("InsufficientFundsError、InvalidAmountError を定義")
    print()
    
    print("【練習4】ログ付きプログラム")
    print("処理の進行状況をログ出力するプログラム")
    print("エラー発生時の詳細情報も記録")
    print()
    
    input("練習が終わったらEnterキーを押してください...")
    print()


def show_summary():
    """まとめ"""
    print("📝 第9章のまとめ")
    print("=" * 50)
    print()
    
    print("エラーと例外処理について学んだこと：")
    print("✅ 主要なエラータイプの理解")
    print("✅ try-except 文による例外処理")
    print("✅ else と finally 節の活用")
    print("✅ raise による例外の発生")
    print("✅ カスタム例外クラスの作成")
    print("✅ デバッグ技法（traceback、logging、assert）")
    print()
    
    print("例外処理のベストプラクティス：")
    print("• 具体的な例外タイプを捕捉する")
    print("• 適切なエラーメッセージを提供する")
    print("• ログを活用して問題を追跡する")
    print("• 例外を隠蔽せず、適切に処理する")
    print()
    
    print("次のステップ：")
    print("• オブジェクト指向プログラミング")
    print("• クラスと継承の活用")
    print()


def show_completion_message():
    """完了メッセージ"""
    print("\n" + "🎉" * 20)
    print("   ファイル 09 の学習完了！   ")
    print("🎉" * 20)
    
    print(f"\n📚 理解度テストを受けましょう")
    print("以下のコマンドをコピー&ペーストして実行してください:\n")
    
    # OS別コマンド表示
    python_cmd = "py" if platform.system() == "Windows" else "python3"
    print(f"   {python_cmd} quizzes/quiz_runner.py basics 09")
    
    print(f"\n✅ テスト合格後、次に進みましょう:")
    print(f"   {python_cmd} basics/10_classes_and_objects.py")
    
    print("\n💡 困ったときは:")
    print(f"   {python_cmd} quizzes/quiz_runner.py help")
    print("=" * 50)


def main():
    """メイン処理"""
    print_chapter_header()
    
    # 各レッスンを順番に実行
    lesson_1_understanding_errors()
    lesson_2_try_except_basics()
    lesson_3_else_finally()
    lesson_4_raising_exceptions()
    lesson_5_custom_exceptions()
    lesson_6_debugging_techniques()
    
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