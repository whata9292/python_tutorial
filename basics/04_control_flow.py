#!/usr/bin/env python3
"""
===========================
第4章: 制御フロー
===========================

プログラムの流れを制御する方法について学習します。
条件分岐（if文）と繰り返し（for文、while文）を
マスターしましょう。

このファイルを実行すると、プログラムの流れを
制御する基本的な方法を習得できます。
"""

import platform
import time


def print_chapter_header():
    """章のヘッダーを表示"""
    print("=" * 50)
    print("第4章: 制御フロー")
    print("=" * 50)
    print()


def lesson_1_if_statements():
    """レッスン1: if文（条件分岐）"""
    print("📚 レッスン1: if文（条件分岐）")
    print("-" * 40)
    print()
    
    print("if文は条件によって処理を分岐させます。")
    print()
    
    # 基本的なif文
    print("基本的なif文:")
    age = 20
    print(f">>> age = {age}")
    print(">>> if age >= 18:")
    print("...     print('成人です')")
    print("... else:")
    print("...     print('未成年です')")
    
    if age >= 18:
        print("成人です")
    else:
        print("未成年です")
    print()
    
    # elif を使った複数条件
    print("elif を使った複数条件:")
    score = 85
    print(f">>> score = {score}")
    print(">>> if score >= 90:")
    print("...     grade = 'A'")
    print("... elif score >= 80:")
    print("...     grade = 'B'")
    print("... elif score >= 70:")
    print("...     grade = 'C'")
    print("... else:")
    print("...     grade = 'D'")
    
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'D'
    
    print(f">>> print(f'成績: {grade}')")
    print(f"成績: {grade}")
    print()
    
    # 複数条件の組み合わせ
    print("複数条件の組み合わせ（and, or）:")
    temperature = 25
    is_sunny = True
    print(f">>> temperature = {temperature}")
    print(f">>> is_sunny = {is_sunny}")
    print(">>> if temperature >= 20 and is_sunny:")
    print("...     print('ピクニック日和です！')")
    
    if temperature >= 20 and is_sunny:
        print("ピクニック日和です！")
    print()
    
    print("💡 条件式では比較演算子（==, !=, <, >, <=, >=）と")
    print("   論理演算子（and, or, not）を使います")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_2_comparison_operators():
    """レッスン2: 比較演算子と真偽値"""
    print("📚 レッスン2: 比較演算子と真偽値")
    print("-" * 40)
    print()
    
    print("Pythonの比較演算子:")
    print()
    
    a, b = 10, 5
    print(f"a = {a}, b = {b} として:")
    print()
    
    comparisons = [
        ("a == b", a == b, "等しい"),
        ("a != b", a != b, "等しくない"),
        ("a > b", a > b, "より大きい"),
        ("a < b", a < b, "より小さい"),
        ("a >= b", a >= b, "以上"),
        ("a <= b", a <= b, "以下"),
    ]
    
    for expr, result, desc in comparisons:
        print(f"{expr:<10} → {str(result):<6} # {desc}")
    
    print()
    print("文字列の比較:")
    str1, str2 = "apple", "banana"
    print(f">>> '{str1}' < '{str2}'  # {str1 < str2} （辞書順）")
    print()
    
    print("リストに要素が含まれるか:")
    fruits = ['apple', 'banana', 'orange']
    print(f">>> fruits = {fruits}")
    print(f">>> 'apple' in fruits  # {'apple' in fruits}")
    print(f">>> 'grape' not in fruits  # {'grape' not in fruits}")
    print()
    
    print("真偽値（bool）について:")
    print("Falseと評価されるもの: None, 0, '', [], {}, False")
    print("それ以外はTrueと評価されます")
    print()
    
    # 真偽値の例
    values = [0, 1, "", "hello", [], [1, 2], None]
    for val in values:
        print(f"bool({repr(val)}) = {bool(val)}")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_3_for_loops():
    """レッスン3: for文（繰り返し）"""
    print("📚 レッスン3: for文（繰り返し）")
    print("-" * 40)
    print()
    
    print("for文はリストや範囲の要素を1つずつ処理します。")
    print()
    
    # リストの要素を処理
    print("リストの要素を処理:")
    colors = ['red', 'green', 'blue']
    print(f">>> colors = {colors}")
    print(">>> for color in colors:")
    print("...     print(f'色: {color}')")
    
    for color in colors:
        print(f'色: {color}')
    print()
    
    # range() を使った繰り返し
    print("range() を使った回数指定:")
    print(">>> for i in range(5):")
    print("...     print(i, end=' ')")
    print()
    
    for i in range(5):
        print(i, end=' ')
    print("\n")
    
    # より複雑な range()
    print("range() の詳細な使い方:")
    print(">>> for i in range(2, 10, 2):  # 開始, 終了, ステップ")
    print("...     print(i, end=' ')")
    print()
    
    for i in range(2, 10, 2):
        print(i, end=' ')
    print("\n")
    
    # enumerate() を使ったインデックス付き
    print("enumerate() でインデックスと値を取得:")
    items = ['りんご', 'みかん', 'ぶどう']
    print(f">>> items = {items}")
    print(">>> for i, item in enumerate(items):")
    print("...     print(f'{i}: {item}')")
    
    for i, item in enumerate(items):
        print(f'{i}: {item}')
    print()
    
    # ネストしたループ
    print("ネストしたループ（九九の表の一部）:")
    print(">>> for i in range(1, 4):")
    print("...     for j in range(1, 4):")
    print("...         print(f'{i}×{j}={i*j}', end='  ')")
    print("...     print()")
    
    for i in range(1, 4):
        for j in range(1, 4):
            print(f'{i}×{j}={i*j}', end='  ')
        print()
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_4_while_loops():
    """レッスン4: while文（条件付き繰り返し）"""
    print("📚 レッスン4: while文（条件付き繰り返し）")
    print("-" * 40)
    print()
    
    print("while文は条件がTrueの間、処理を繰り返します。")
    print()
    
    # 基本的なwhile文
    print("基本的なwhile文:")
    print(">>> count = 0")
    print(">>> while count < 5:")
    print("...     print(count, end=' ')")
    print("...     count += 1")
    print()
    
    count = 0
    while count < 5:
        print(count, end=' ')
        count += 1
    print("\n")
    
    # ユーザー入力を使った例（シミュレーション）
    print("ユーザー入力のシミュレーション:")
    print(">>> # 実際はinput()を使いますが、ここでは自動化")
    print(">>> answers = ['間違い', '間違い', '正解']")
    print(">>> attempt = 0")
    print(">>> while attempt < len(answers):")
    print("...     if answers[attempt] == '正解':")
    print("...         print('正解です！')")
    print("...         break")
    print("...     print('もう一度')")
    print("...     attempt += 1")
    print()
    
    answers = ['間違い', '間違い', '正解']
    attempt = 0
    while attempt < len(answers):
        if answers[attempt] == '正解':
            print('正解です！')
            break
        print('もう一度')
        attempt += 1
    print()
    
    # 無限ループの注意
    print("⚠️ 無限ループに注意:")
    print("# これは無限ループです（実行しません）:")
    print("# while True:")
    print("#     print('終わらない...')")
    print()
    print("必ず終了条件を設定しましょう！")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_5_break_continue():
    """レッスン5: break と continue"""
    print("📚 レッスン5: break と continue")
    print("-" * 40)
    print()
    
    print("break: ループを途中で終了")
    print("continue: 次の繰り返しへスキップ")
    print()
    
    # break の例
    print("break の例（最初の偶数を見つける）:")
    numbers = [1, 3, 5, 8, 9, 10]
    print(f">>> numbers = {numbers}")
    print(">>> for num in numbers:")
    print("...     if num % 2 == 0:")
    print("...         print(f'最初の偶数: {num}')")
    print("...         break")
    
    for num in numbers:
        if num % 2 == 0:
            print(f'最初の偶数: {num}')
            break
    print()
    
    # continue の例
    print("continue の例（奇数のみ表示）:")
    print(">>> for i in range(10):")
    print("...     if i % 2 == 0:")
    print("...         continue")
    print("...     print(i, end=' ')")
    print()
    
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i, end=' ')
    print("\n")
    
    # else節（ループが正常終了した場合）
    print("for-else 構文（あまり使われませんが便利）:")
    search_list = [1, 3, 5, 7, 9]
    target = 6
    print(f">>> search_list = {search_list}")
    print(f">>> target = {target}")
    print(">>> for num in search_list:")
    print("...     if num == target:")
    print("...         print('見つかった！')")
    print("...         break")
    print("... else:")
    print("...     print('見つからなかった')")
    
    for num in search_list:
        if num == target:
            print('見つかった！')
            break
    else:
        print('見つからなかった')
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_6_nested_conditions():
    """レッスン6: ネストした条件と制御"""
    print("📚 レッスン6: ネストした条件と制御")
    print("-" * 40)
    print()
    
    print("条件文やループは入れ子にできます。")
    print()
    
    # ネストしたif文
    print("ネストしたif文の例（年齢と会員区分）:")
    age = 65
    is_member = True
    
    print(f">>> age = {age}")
    print(f">>> is_member = {is_member}")
    print()
    
    if age < 18:
        print("子供料金: 500円")
    else:
        if age >= 65:
            if is_member:
                print("シニア会員料金: 800円")
            else:
                print("シニア料金: 1000円")
        else:
            if is_member:
                print("会員料金: 1200円")
            else:
                print("一般料金: 1500円")
    print()
    
    # より読みやすい書き方
    print("より読みやすい書き方（複合条件）:")
    if age < 18:
        price = 500
        category = "子供"
    elif age >= 65 and is_member:
        price = 800
        category = "シニア会員"
    elif age >= 65:
        price = 1000
        category = "シニア"
    elif is_member:
        price = 1200
        category = "会員"
    else:
        price = 1500
        category = "一般"
    
    print(f"カテゴリー: {category}、料金: {price}円")
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
    
    print("【練習1】成績判定プログラム")
    print("点数を入力して成績（A〜F）を判定する")
    print("90以上:A, 80以上:B, 70以上:C, 60以上:D, それ以下:F")
    print()
    
    print("【練習2】FizzBuzz")
    print("1から30までの数字を表示")
    print("3の倍数なら'Fizz'、5の倍数なら'Buzz'")
    print("両方の倍数なら'FizzBuzz'を表示")
    print()
    
    print("【練習3】素数判定")
    print("入力された数が素数かどうか判定")
    print("ヒント: 2から数-1までで割り切れるか確認")
    print()
    
    print("【練習4】ピラミッド表示")
    print("forループを使って以下のような図形を表示:")
    print("    *")
    print("   ***")
    print("  *****")
    print(" *******")
    print()
    
    input("練習が終わったらEnterキーを押してください...")
    print()


def show_summary():
    """まとめ"""
    print("📝 第4章のまとめ")
    print("=" * 50)
    print()
    
    print("条件分岐について学んだこと：")
    print("✅ if, elif, else による条件分岐")
    print("✅ 比較演算子（==, !=, <, >, <=, >=）")
    print("✅ 論理演算子（and, or, not）")
    print("✅ in, not in による要素の確認")
    print()
    
    print("繰り返しについて学んだこと：")
    print("✅ for文によるリストや範囲の繰り返し")
    print("✅ while文による条件付き繰り返し")
    print("✅ range()関数の使い方")
    print("✅ break（中断）とcontinue（スキップ）")
    print("✅ enumerate()でインデックス付き繰り返し")
    print()
    
    print("次のステップ：")
    print("• 関数を使った処理のまとめ方")
    print("• より複雑なプログラムの構築")
    print()


def show_completion_message():
    """完了メッセージ"""
    print("\n" + "🎉" * 20)
    print("   ファイル 04 の学習完了！   ")
    print("🎉" * 20)
    
    print(f"\n📚 理解度テストを受けましょう")
    print("以下のコマンドをコピー&ペーストして実行してください:\n")
    
    # OS別コマンド表示
    python_cmd = "py" if platform.system() == "Windows" else "python3"
    print(f"   {python_cmd} quizzes/quiz_runner.py basics 04")
    
    print(f"\n✅ テスト合格後、次に進みましょう:")
    print(f"   {python_cmd} basics/05_functions.py")
    
    print("\n💡 困ったときは:")
    print(f"   {python_cmd} quizzes/quiz_runner.py help")
    print("=" * 50)


def main():
    """メイン処理"""
    print_chapter_header()
    
    # 各レッスンを順番に実行
    lesson_1_if_statements()
    lesson_2_comparison_operators()
    lesson_3_for_loops()
    lesson_4_while_loops()
    lesson_5_break_continue()
    lesson_6_nested_conditions()
    
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