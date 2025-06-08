#!/usr/bin/env python3
"""
===========================
第5章: 関数
===========================

関数を使ってコードを整理し、再利用可能にする方法を学びます。
関数の定義、引数、戻り値、スコープなどの重要な概念を
理解しましょう。

このファイルを実行すると、関数の基本から応用まで
段階的に学習できます。
"""

import platform


def print_chapter_header():
    """章のヘッダーを表示"""
    print("=" * 50)
    print("第5章: 関数")
    print("=" * 50)
    print()


def lesson_1_function_basics():
    """レッスン1: 関数の基本"""
    print("📚 レッスン1: 関数の基本")
    print("-" * 40)
    print()
    
    print("関数は処理をまとめて名前を付けたものです。")
    print("def キーワードを使って定義します。")
    print()
    
    # 最もシンプルな関数
    print("最もシンプルな関数:")
    print(">>> def greet():")
    print("...     print('こんにちは！')")
    print(">>> ")
    print(">>> greet()  # 関数の呼び出し")
    
    def greet():
        print('こんにちは！')
    
    greet()
    print()
    
    # 引数を持つ関数
    print("引数を持つ関数:")
    print(">>> def greet_person(name):")
    print("...     print(f'こんにちは、{name}さん！')")
    print(">>> ")
    print(">>> greet_person('太郎')")
    
    def greet_person(name):
        print(f'こんにちは、{name}さん！')
    
    greet_person('太郎')
    print()
    
    # 複数の引数
    print("複数の引数を持つ関数:")
    print(">>> def introduce(name, age, city):")
    print("...     print(f'{name}さん（{age}歳）は{city}に住んでいます')")
    print(">>> ")
    print(">>> introduce('花子', 25, '東京')")
    
    def introduce(name, age, city):
        print(f'{name}さん（{age}歳）は{city}に住んでいます')
    
    introduce('花子', 25, '東京')
    print()
    
    print("💡 関数を使うメリット:")
    print("   • コードの再利用")
    print("   • 処理の整理")
    print("   • メンテナンスが楽")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_2_return_values():
    """レッスン2: 戻り値"""
    print("📚 レッスン2: 戻り値（return）")
    print("-" * 40)
    print()
    
    print("関数は return を使って値を返すことができます。")
    print()
    
    # 値を返す関数
    print("値を返す関数:")
    print(">>> def add(a, b):")
    print("...     return a + b")
    print(">>> ")
    print(">>> result = add(3, 5)")
    print(">>> print(result)")
    
    def add(a, b):
        return a + b
    
    result = add(3, 5)
    print(result)
    print()
    
    # 複数の値を返す
    print("複数の値を返す（タプルで返す）:")
    print(">>> def calculate(a, b):")
    print("...     sum_val = a + b")
    print("...     diff_val = a - b")
    print("...     prod_val = a * b")
    print("...     return sum_val, diff_val, prod_val")
    print(">>> ")
    print(">>> s, d, p = calculate(10, 3)")
    print(">>> print(f'和:{s}, 差:{d}, 積:{p}')")
    
    def calculate(a, b):
        sum_val = a + b
        diff_val = a - b
        prod_val = a * b
        return sum_val, diff_val, prod_val
    
    s, d, p = calculate(10, 3)
    print(f'和:{s}, 差:{d}, 積:{p}')
    print()
    
    # 条件によって異なる値を返す
    print("条件によって異なる値を返す:")
    print(">>> def get_grade(score):")
    print("...     if score >= 80:")
    print("...         return 'A'")
    print("...     elif score >= 60:")
    print("...         return 'B'")
    print("...     else:")
    print("...         return 'C'")
    
    def get_grade(score):
        if score >= 80:
            return 'A'
        elif score >= 60:
            return 'B'
        else:
            return 'C'
    
    print(">>> print(get_grade(85))")
    print(get_grade(85))
    print()
    
    print("💡 return がない関数は None を返します")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_3_default_parameters():
    """レッスン3: デフォルト引数とキーワード引数"""
    print("📚 レッスン3: デフォルト引数とキーワード引数")
    print("-" * 40)
    print()
    
    print("引数にデフォルト値を設定できます。")
    print()
    
    # デフォルト引数
    print("デフォルト引数:")
    print(">>> def greet(name, greeting='こんにちは'):")
    print("...     print(f'{greeting}、{name}さん！')")
    print(">>> ")
    print(">>> greet('太郎')  # デフォルト値を使用")
    
    def greet(name, greeting='こんにちは'):
        print(f'{greeting}、{name}さん！')
    
    greet('太郎')
    print(">>> greet('花子', 'おはよう')  # 値を指定")
    greet('花子', 'おはよう')
    print()
    
    # キーワード引数
    print("キーワード引数（引数名を指定）:")
    print(">>> def create_profile(name, age, city='東京', job='会社員'):")
    print("...     return f'{name}（{age}歳）: {city}在住の{job}'")
    print(">>> ")
    print(">>> # 順番通り")
    print(">>> print(create_profile('山田', 30))")
    
    def create_profile(name, age, city='東京', job='会社員'):
        return f'{name}（{age}歳）: {city}在住の{job}'
    
    print(create_profile('山田', 30))
    print()
    
    print(">>> # キーワードで指定")
    print(">>> print(create_profile(age=25, name='鈴木', job='エンジニア'))")
    print(create_profile(age=25, name='鈴木', job='エンジニア'))
    print()
    
    # 可変長引数
    print("可変長引数（*args）:")
    print(">>> def sum_all(*numbers):")
    print("...     return sum(numbers)")
    print(">>> ")
    print(">>> print(sum_all(1, 2, 3, 4, 5))")
    
    def sum_all(*numbers):
        return sum(numbers)
    
    print(sum_all(1, 2, 3, 4, 5))
    print()
    
    print("💡 デフォルト引数は必須引数の後に書きます")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_4_scope():
    """レッスン4: スコープ（変数の有効範囲）"""
    print("📚 レッスン4: スコープ（変数の有効範囲）")
    print("-" * 40)
    print()
    
    print("変数には有効範囲（スコープ）があります。")
    print()
    
    # ローカル変数
    print("ローカル変数（関数内の変数）:")
    print(">>> def test_scope():")
    print("...     local_var = '関数内の変数'")
    print("...     print(local_var)")
    print(">>> ")
    print(">>> test_scope()")
    
    def test_scope():
        local_var = '関数内の変数'
        print(local_var)
    
    test_scope()
    print(">>> # print(local_var)  # エラー！関数外では使えない")
    print()
    
    # グローバル変数
    print("グローバル変数（関数外の変数）:")
    global_var = 'グローバル変数'
    print(f">>> global_var = '{global_var}'")
    print(">>> ")
    print(">>> def use_global():")
    print("...     print(f'関数内から: {global_var}')")
    print(">>> ")
    print(">>> use_global()")
    
    def use_global():
        print(f'関数内から: {global_var}')
    
    use_global()
    print()
    
    # グローバル変数の変更
    print("グローバル変数を関数内で変更:")
    counter = 0
    print(">>> counter = 0")
    print(">>> ")
    print(">>> def increment():")
    print("...     global counter  # globalキーワードが必要")
    print("...     counter += 1")
    print(">>> ")
    print(">>> increment()")
    print(">>> print(counter)")
    
    def increment():
        global counter
        counter += 1
    
    increment()
    print(counter)
    print()
    
    print("💡 できるだけグローバル変数は避けて、")
    print("   引数と戻り値を使いましょう")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_5_lambda_functions():
    """レッスン5: ラムダ関数（無名関数）"""
    print("📚 レッスン5: ラムダ関数（無名関数）")
    print("-" * 40)
    print()
    
    print("簡単な関数は lambda を使って1行で書けます。")
    print()
    
    # 基本的なラムダ関数
    print("通常の関数とラムダ関数の比較:")
    print(">>> # 通常の関数")
    print(">>> def square(x):")
    print("...     return x ** 2")
    print(">>> ")
    print(">>> # ラムダ関数")
    print(">>> square_lambda = lambda x: x ** 2")
    print(">>> ")
    print(">>> print(square(5))")
    
    def square(x):
        return x ** 2
    
    square_lambda = lambda x: x ** 2
    
    print(square(5))
    print(">>> print(square_lambda(5))")
    print(square_lambda(5))
    print()
    
    # ラムダ関数の活用
    print("ラムダ関数の活用（sorted）:")
    students = [
        {'name': '田中', 'score': 85},
        {'name': '鈴木', 'score': 92},
        {'name': '佐藤', 'score': 78}
    ]
    print(f">>> students = {students}")
    print(">>> # スコアでソート")
    print(">>> sorted_students = sorted(students, key=lambda x: x['score'])")
    
    sorted_students = sorted(students, key=lambda x: x['score'])
    print(">>> for s in sorted_students:")
    print("...     print(f\"{s['name']}: {s['score']}点\")")
    
    for s in sorted_students:
        print(f"{s['name']}: {s['score']}点")
    print()
    
    # map() との組み合わせ
    print("map() との組み合わせ:")
    numbers = [1, 2, 3, 4, 5]
    print(f">>> numbers = {numbers}")
    print(">>> squared = list(map(lambda x: x**2, numbers))")
    squared = list(map(lambda x: x**2, numbers))
    print(f">>> squared  # {squared}")
    print()
    
    print("💡 ラムダ関数は短い処理に便利ですが、")
    print("   複雑な処理は通常の関数を使いましょう")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_6_docstrings():
    """レッスン6: ドキュメント文字列（docstring）"""
    print("📚 レッスン6: ドキュメント文字列")
    print("-" * 40)
    print()
    
    print("関数の説明を書くドキュメント文字列について学びます。")
    print()
    
    # ドキュメント文字列の例
    print("ドキュメント文字列の書き方:")
    print('>>> def calculate_bmi(weight, height):')
    print('...     """')
    print('...     BMI（体格指数）を計算する')
    print('...     ')
    print('...     引数:')
    print('...         weight: 体重（kg）')
    print('...         height: 身長（cm）')
    print('...     ')
    print('...     戻り値:')
    print('...         BMI値（小数点第1位まで）')
    print('...     """')
    print('...     bmi = weight / (height / 100) ** 2')
    print('...     return round(bmi, 1)')
    
    def calculate_bmi(weight, height):
        """
        BMI（体格指数）を計算する
        
        引数:
            weight: 体重（kg）
            height: 身長（cm）
        
        戻り値:
            BMI値（小数点第1位まで）
        """
        bmi = weight / (height / 100) ** 2
        return round(bmi, 1)
    
    print(">>> ")
    print(">>> # ドキュメントを見る")
    print(">>> help(calculate_bmi)")
    print()
    # 実際のhelp出力をシミュレート
    print("Help on function calculate_bmi:")
    print()
    print("calculate_bmi(weight, height)")
    print("    BMI（体格指数）を計算する")
    print("    ")
    print("    引数:")
    print("        weight: 体重（kg）")
    print("        height: 身長（cm）")
    print("    ")
    print("    戻り値:")
    print("        BMI値（小数点第1位まで）")
    print()
    
    print(">>> print(calculate_bmi(65, 170))")
    print(calculate_bmi(65, 170))
    print()
    
    print("💡 関数の使い方を説明するドキュメント文字列は")
    print("   チーム開発で特に重要です")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def practice_exercises():
    """練習問題"""
    print("🏃 練習してみよう！")
    print("=" * 50)
    print()
    
    print("以下の練習問題を対話モードで試してください：")
    print()
    
    print("【練習1】温度変換関数")
    print("摂氏を華氏に変換する関数 celsius_to_fahrenheit()")
    print("華氏 = 摂氏 × 9/5 + 32")
    print()
    
    print("【練習2】リストの統計関数")
    print("リストを受け取って最大値、最小値、平均値を返す")
    print("get_stats(numbers) → (max, min, avg)")
    print()
    
    print("【練習3】パスワード強度チェック関数")
    print("文字数、数字の有無、大文字小文字の有無をチェック")
    print("強度を点数（0-100）で返す")
    print()
    
    print("【練習4】電卓関数")
    print("2つの数と演算子（+, -, *, /）を受け取って計算")
    print("calculate(a, b, operator)")
    print()
    
    input("練習が終わったらEnterキーを押してください...")
    print()


def show_summary():
    """まとめ"""
    print("📝 第5章のまとめ")
    print("=" * 50)
    print()
    
    print("関数について学んだこと：")
    print("✅ def による関数定義")
    print("✅ 引数と戻り値（return）")
    print("✅ デフォルト引数とキーワード引数")
    print("✅ 可変長引数（*args）")
    print("✅ スコープ（ローカル変数とグローバル変数）")
    print("✅ ラムダ関数（lambda）")
    print("✅ ドキュメント文字列（docstring）")
    print()
    
    print("関数を使うメリット：")
    print("• コードの再利用性向上")
    print("• プログラムの構造化")
    print("• テストがしやすくなる")
    print("• チーム開発での協力が容易")
    print()
    
    print("次のステップ：")
    print("• より高度なデータ構造の操作")
    print("• モジュール化とパッケージ管理")
    print()


def show_completion_message():
    """完了メッセージ"""
    print("\n" + "🎉" * 20)
    print("   ファイル 05 の学習完了！   ")
    print("🎉" * 20)
    
    print(f"\n📚 理解度テストを受けましょう")
    print("以下のコマンドをコピー&ペーストして実行してください:\n")
    
    # OS別コマンド表示
    python_cmd = "py" if platform.system() == "Windows" else "python3"
    print(f"   {python_cmd} quizzes/quiz_runner.py basics 05")
    
    print(f"\n✅ テスト合格後、次に進みましょう:")
    print(f"   {python_cmd} basics/06_data_structures.py")
    
    print("\n💡 困ったときは:")
    print(f"   {python_cmd} quizzes/quiz_runner.py help")
    print("=" * 50)


def main():
    """メイン処理"""
    print_chapter_header()
    
    # 各レッスンを順番に実行
    lesson_1_function_basics()
    lesson_2_return_values()
    lesson_3_default_parameters()
    lesson_4_scope()
    lesson_5_lambda_functions()
    lesson_6_docstrings()
    
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