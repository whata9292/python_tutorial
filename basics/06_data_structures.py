#!/usr/bin/env python3
"""
===========================
第6章: 高度なデータ構造
===========================

より高度なデータ構造の操作方法を学習します。
集合（set）、内包表記、ソート、検索など、
効率的なデータ処理のテクニックを習得しましょう。

このファイルを実行すると、Pythonの強力な
データ処理機能を活用できるようになります。
"""

import platform
from collections import Counter, defaultdict, namedtuple


def print_chapter_header():
    """章のヘッダーを表示"""
    print("=" * 50)
    print("第6章: 高度なデータ構造")
    print("=" * 50)
    print()


def lesson_1_sets():
    """レッスン1: 集合（set）"""
    print("📚 レッスン1: 集合（set）")
    print("-" * 40)
    print()
    
    print("集合は重複のない要素の集まりです。")
    print("数学の集合演算ができます。")
    print()
    
    # 集合の作成
    print("集合の作成:")
    print(">>> fruits = {'apple', 'banana', 'orange'}")
    fruits = {'apple', 'banana', 'orange'}
    print(f">>> fruits  # {fruits}")
    print()
    
    print(">>> numbers = set([1, 2, 2, 3, 3, 3])")
    numbers = set([1, 2, 2, 3, 3, 3])
    print(f">>> numbers  # {numbers}  # 重複が削除される")
    print()
    
    # 集合の操作
    print("集合の操作:")
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    print(f">>> set_a = {set_a}")
    print(f">>> set_b = {set_b}")
    print()
    
    print(f">>> set_a | set_b  # 和集合")
    print(f"    {set_a | set_b}")
    print()
    
    print(f">>> set_a & set_b  # 積集合")
    print(f"    {set_a & set_b}")
    print()
    
    print(f">>> set_a - set_b  # 差集合")
    print(f"    {set_a - set_b}")
    print()
    
    print(f">>> set_a ^ set_b  # 対称差")
    print(f"    {set_a ^ set_b}")
    print()
    
    # 集合の活用例
    print("集合の活用例（重複削除）:")
    emails = ['user1@example.com', 'user2@example.com', 
              'user1@example.com', 'user3@example.com']
    print(f">>> emails = {emails}")
    print(">>> unique_emails = list(set(emails))")
    unique_emails = list(set(emails))
    print(f">>> unique_emails  # {unique_emails}")
    print()
    
    print("💡 集合は順序を保持しません")
    print("   順序が重要な場合は他のデータ構造を使いましょう")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_2_list_comprehensions():
    """レッスン2: リスト内包表記"""
    print("📚 レッスン2: リスト内包表記")
    print("-" * 40)
    print()
    
    print("リスト内包表記で簡潔にリストを作成できます。")
    print()
    
    # 基本的なリスト内包表記
    print("基本的なリスト内包表記:")
    print(">>> # 従来の方法")
    print(">>> squares = []")
    print(">>> for i in range(10):")
    print("...     squares.append(i**2)")
    
    squares = []
    for i in range(10):
        squares.append(i**2)
    print(f">>> squares  # {squares}")
    print()
    
    print(">>> # リスト内包表記")
    print(">>> squares = [i**2 for i in range(10)]")
    squares = [i**2 for i in range(10)]
    print(f">>> squares  # {squares}")
    print()
    
    # 条件付きリスト内包表記
    print("条件付きリスト内包表記:")
    print(">>> # 偶数のみ")
    print(">>> evens = [x for x in range(20) if x % 2 == 0]")
    evens = [x for x in range(20) if x % 2 == 0]
    print(f">>> evens  # {evens}")
    print()
    
    # より複雑な例
    print("文字列処理の例:")
    words = ['Hello', 'world', 'Python', 'programming']
    print(f">>> words = {words}")
    print(">>> # 5文字以上の単語を大文字に")
    print(">>> long_words = [w.upper() for w in words if len(w) >= 5]")
    long_words = [w.upper() for w in words if len(w) >= 5]
    print(f">>> long_words  # {long_words}")
    print()
    
    # 辞書内包表記
    print("辞書内包表記:")
    print(">>> # 文字数の辞書")
    print(">>> word_lengths = {w: len(w) for w in words}")
    word_lengths = {w: len(w) for w in words}
    print(f">>> word_lengths  # {word_lengths}")
    print()
    
    # 集合内包表記
    print("集合内包表記:")
    print(">>> # 文字列の長さの集合")
    print(">>> lengths_set = {len(w) for w in words}")
    lengths_set = {len(w) for w in words}
    print(f">>> lengths_set  # {lengths_set}")
    print()
    
    print("💡 内包表記は簡潔ですが、複雑になりすぎないよう注意")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_3_sorting_and_searching():
    """レッスン3: ソートと検索"""
    print("📚 レッスン3: ソートと検索")
    print("-" * 40)
    print()
    
    print("効率的なソートと検索の方法を学びます。")
    print()
    
    # 基本的なソート
    print("基本的なソート:")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f">>> numbers = {numbers}")
    print(">>> sorted_numbers = sorted(numbers)")
    sorted_numbers = sorted(numbers)
    print(f">>> sorted_numbers  # {sorted_numbers}")
    print()
    
    print(">>> numbers.sort()  # 元のリストを変更")
    numbers_copy = numbers.copy()
    numbers_copy.sort()
    print(f">>> numbers  # {numbers_copy}")
    print()
    
    # カスタムソート
    print("カスタムソート:")
    people = [
        {'name': '田中', 'age': 25},
        {'name': '鈴木', 'age': 30},
        {'name': '佐藤', 'age': 20}
    ]
    print(">>> people = [")
    for p in people:
        print(f"...     {p},")
    print("... ]")
    print()
    
    print(">>> # 年齢でソート")
    print(">>> sorted_by_age = sorted(people, key=lambda x: x['age'])")
    sorted_by_age = sorted(people, key=lambda x: x['age'])
    print(">>> for p in sorted_by_age:")
    print("...     print(f\"{p['name']}: {p['age']}歳\")")
    for p in sorted_by_age:
        print(f"{p['name']}: {p['age']}歳")
    print()
    
    # 逆順ソート
    print("逆順ソート:")
    print(">>> sorted(numbers, reverse=True)")
    print(f"    {sorted(numbers, reverse=True)}")
    print()
    
    # 効率的な検索
    print("効率的な検索:")
    large_list = list(range(1000000))
    print(">>> large_list = list(range(1000000))  # 100万要素")
    print(">>> # リストでの検索（遅い）")
    print(">>> 999999 in large_list  # True")
    print()
    
    print(">>> # 集合での検索（速い）")
    print(">>> large_set = set(large_list)")
    print(">>> 999999 in large_set  # True")
    print()
    
    print("💡 大量データの検索には集合や辞書を使いましょう")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_4_useful_functions():
    """レッスン4: 便利な組み込み関数"""
    print("📚 レッスン4: 便利な組み込み関数")
    print("-" * 40)
    print()
    
    print("データ処理に便利な組み込み関数を学びます。")
    print()
    
    # zip関数
    print("zip() - 複数のリストをまとめる:")
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    cities = ['Tokyo', 'Osaka', 'Kyoto']
    
    print(f">>> names = {names}")
    print(f">>> ages = {ages}")
    print(f">>> cities = {cities}")
    print(">>> for name, age, city in zip(names, ages, cities):")
    print("...     print(f'{name} ({age}) - {city}')")
    
    for name, age, city in zip(names, ages, cities):
        print(f'{name} ({age}) - {city}')
    print()
    
    # enumerate関数（復習）
    print("enumerate() - インデックス付きループ:")
    fruits = ['apple', 'banana', 'orange']
    print(f">>> fruits = {fruits}")
    print(">>> for idx, fruit in enumerate(fruits, start=1):")
    print("...     print(f'{idx}. {fruit}')")
    
    for idx, fruit in enumerate(fruits, start=1):
        print(f'{idx}. {fruit}')
    print()
    
    # all()とany()
    print("all() と any() - 条件チェック:")
    scores = [80, 85, 90, 78, 92]
    print(f">>> scores = {scores}")
    print(f">>> all(score >= 70 for score in scores)  # すべて70以上？")
    print(f"    {all(score >= 70 for score in scores)}")
    print(f">>> any(score >= 90 for score in scores)  # 90以上が1つでも？")
    print(f"    {any(score >= 90 for score in scores)}")
    print()
    
    # filter()とmap()
    print("filter() と map() - データ変換:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f">>> numbers = {numbers}")
    print(">>> # 偶数のみ抽出")
    print(">>> evens = list(filter(lambda x: x % 2 == 0, numbers))")
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f">>> evens  # {evens}")
    print()
    
    print(">>> # 全要素を2倍")
    print(">>> doubled = list(map(lambda x: x * 2, numbers))")
    doubled = list(map(lambda x: x * 2, numbers))
    print(f">>> doubled  # {doubled}")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_5_collections_module():
    """レッスン5: collectionsモジュール"""
    print("📚 レッスン5: collectionsモジュール")
    print("-" * 40)
    print()
    
    print("collectionsモジュールの便利なデータ構造を学びます。")
    print()
    
    # Counter
    print("Counter - 要素の出現回数を数える:")
    print(">>> from collections import Counter")
    print(">>> ")
    words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(f">>> words = {words}")
    print(">>> word_count = Counter(words)")
    word_count = Counter(words)
    print(f">>> word_count  # {word_count}")
    print()
    
    print(">>> # 最も頻出する2つ")
    print(">>> word_count.most_common(2)")
    print(f"    {word_count.most_common(2)}")
    print()
    
    # defaultdict
    print("defaultdict - デフォルト値を持つ辞書:")
    print(">>> from collections import defaultdict")
    print(">>> ")
    print(">>> # 通常の辞書だとKeyErrorになる場合")
    print(">>> groups = defaultdict(list)")
    groups = defaultdict(list)
    
    students = [
        ('A組', '田中'),
        ('B組', '鈴木'),
        ('A組', '佐藤'),
        ('B組', '山田')
    ]
    
    print(f">>> students = {students}")
    print(">>> for group, name in students:")
    print("...     groups[group].append(name)")
    
    for group, name in students:
        groups[group].append(name)
    
    print(">>> dict(groups)")
    print(f"    {dict(groups)}")
    print()
    
    # namedtuple
    print("namedtuple - 名前付きタプル:")
    print(">>> from collections import namedtuple")
    print(">>> ")
    print(">>> Point = namedtuple('Point', ['x', 'y'])")
    Point = namedtuple('Point', ['x', 'y'])
    print(">>> p = Point(10, 20)")
    p = Point(10, 20)
    print(f">>> p.x  # {p.x}")
    print(f">>> p.y  # {p.y}")
    print()
    
    print(">>> # 普通のタプルとの違い")
    print(">>> # 属性アクセスができて読みやすい")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_6_advanced_techniques():
    """レッスン6: 高度なテクニック"""
    print("📚 レッスン6: 高度なテクニック")
    print("-" * 40)
    print()
    
    print("実践的なデータ処理のテクニックを学びます。")
    print()
    
    # 辞書のマージ（Python 3.9+）
    print("辞書のマージ:")
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    print(f">>> dict1 = {dict1}")
    print(f">>> dict2 = {dict2}")
    print(">>> # Python 3.9以降")
    print(">>> merged = dict1 | dict2")
    merged = {**dict1, **dict2}  # 互換性のため
    print(f">>> merged  # {merged}")
    print()
    
    # グループ化
    print("データのグループ化:")
    data = [
        {'name': '田中', 'dept': '営業', 'salary': 300000},
        {'name': '鈴木', 'dept': '開発', 'salary': 400000},
        {'name': '佐藤', 'dept': '営業', 'salary': 350000},
        {'name': '山田', 'dept': '開発', 'salary': 450000}
    ]
    
    print(">>> # 部署ごとにグループ化")
    print(">>> from collections import defaultdict")
    print(">>> by_dept = defaultdict(list)")
    by_dept = defaultdict(list)
    
    print(">>> for person in data:")
    print("...     by_dept[person['dept']].append(person['name'])")
    
    for person in data:
        by_dept[person['dept']].append(person['name'])
    
    print(">>> dict(by_dept)")
    print(f"    {dict(by_dept)}")
    print()
    
    # 転置（行と列の入れ替え）
    print("2次元リストの転置:")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(">>> matrix = [")
    for row in matrix:
        print(f"...     {row},")
    print("... ]")
    
    print(">>> # zip(*matrix) で転置")
    print(">>> transposed = list(zip(*matrix))")
    transposed = list(zip(*matrix))
    print(">>> for row in transposed:")
    print("...     print(row)")
    for row in transposed:
        print(row)
    print()
    
    print("💡 これらのテクニックで効率的なコードが書けます")
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
    
    print("【練習1】重複削除と集合演算")
    print("2つのリストから共通要素と各リスト固有の要素を見つける")
    print("list1 = [1,2,3,4,5], list2 = [4,5,6,7,8]")
    print()
    
    print("【練習2】成績集計")
    print("生徒の成績リストから平均点、最高点、最低点を計算")
    print("内包表記を使って80点以上の生徒名リストを作成")
    print()
    
    print("【練習3】単語頻度カウント")
    print("文章を単語に分割してCounterで頻度を集計")
    print("最も頻出する上位3単語を表示")
    print()
    
    print("【練習4】データ変換")
    print("商品リストを価格でソートし、税込価格を追加")
    print("1万円以上の商品のみフィルタリング")
    print()
    
    input("練習が終わったらEnterキーを押してください...")
    print()


def show_summary():
    """まとめ"""
    print("📝 第6章のまとめ")
    print("=" * 50)
    print()
    
    print("高度なデータ構造について学んだこと：")
    print("✅ 集合（set）と集合演算")
    print("✅ リスト内包表記・辞書内包表記・集合内包表記")
    print("✅ sorted()とkey引数によるカスタムソート")
    print("✅ zip()、enumerate()、all()、any()などの便利関数")
    print("✅ filter()とmap()によるデータ変換")
    print("✅ collectionsモジュール（Counter、defaultdict、namedtuple）")
    print("✅ 実践的なデータ処理テクニック")
    print()
    
    print("これらを使うメリット：")
    print("• より簡潔で読みやすいコード")
    print("• 効率的なデータ処理")
    print("• バグの少ないプログラム")
    print()
    
    print("次のステップ：")
    print("• モジュールとパッケージの作成")
    print("• ファイル入出力の詳細")
    print()


def show_completion_message():
    """完了メッセージ"""
    print("\n" + "🎉" * 20)
    print("   ファイル 06 の学習完了！   ")
    print("🎉" * 20)
    
    print(f"\n📚 理解度テストを受けましょう")
    print("以下のコマンドをコピー&ペーストして実行してください:\n")
    
    # OS別コマンド表示
    python_cmd = "py" if platform.system() == "Windows" else "python3"
    print(f"   {python_cmd} quizzes/quiz_runner.py basics 06")
    
    print(f"\n✅ テスト合格後、次に進みましょう:")
    print(f"   {python_cmd} basics/07_modules_and_packages.py")
    
    print("\n💡 困ったときは:")
    print(f"   {python_cmd} quizzes/quiz_runner.py help")
    print("=" * 50)


def main():
    """メイン処理"""
    print_chapter_header()
    
    # 各レッスンを順番に実行
    lesson_1_sets()
    lesson_2_list_comprehensions()
    lesson_3_sorting_and_searching()
    lesson_4_useful_functions()
    lesson_5_collections_module()
    lesson_6_advanced_techniques()
    
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