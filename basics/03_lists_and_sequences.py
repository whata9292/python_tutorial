#!/usr/bin/env python3
"""
===================================
第3章: リストとシーケンス
===================================

複数のデータをまとめて扱うための基本的なデータ構造である
リスト、タプル、辞書について学習します。

これらは Python プログラミングの基礎となる重要な概念です。
"""

import platform


def print_chapter_header():
    """章のヘッダーを表示"""
    print("=" * 50)
    print("第3章: リストとシーケンス")
    print("=" * 50)
    print()


def lesson_1_list_basics():
    """レッスン1: リストの基本"""
    print("📚 レッスン1: リストの基本")
    print("-" * 40)
    print()
    
    print("リストは複数の値を順番に格納できるデータ構造です。")
    print("角括弧 [] で作成します。")
    print()
    
    # 空のリスト
    print(">>> empty_list = []")
    empty_list = []
    print(f">>> empty_list  # {empty_list}")
    print()
    
    # 数値のリスト
    print(">>> numbers = [1, 2, 3, 4, 5]")
    numbers = [1, 2, 3, 4, 5]
    print(f">>> numbers  # {numbers}")
    print()
    
    # 文字列のリスト
    print(">>> fruits = ['apple', 'banana', 'orange']")
    fruits = ['apple', 'banana', 'orange']
    print(f">>> fruits  # {fruits}")
    print()
    
    # 異なる型を混在
    print(">>> mixed = [42, 'hello', 3.14, True]")
    mixed = [42, 'hello', 3.14, True]
    print(f">>> mixed  # {mixed}")
    print()
    
    # リストの長さ
    print(f">>> len(fruits)  # {len(fruits)}")
    print()
    
    print("💡 リストは異なる型のデータを混在できます")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_2_list_indexing():
    """レッスン2: リストのインデックスとスライス"""
    print("📚 レッスン2: リストのインデックスとスライス")
    print("-" * 40)
    print()
    
    print("リストの要素にアクセスする方法：")
    print()
    
    colors = ['red', 'green', 'blue', 'yellow', 'purple']
    print(f">>> colors = {colors}")
    print()
    
    # インデックス（0から始まる）
    print("インデックスでアクセス（0から始まる）：")
    print(f">>> colors[0]   # '{colors[0]}'  （最初）")
    print(f">>> colors[2]   # '{colors[2]}'  （3番目）")
    print(f">>> colors[-1]  # '{colors[-1]}'  （最後）")
    print(f">>> colors[-2]  # '{colors[-2]}'  （最後から2番目）")
    print()
    
    # スライス
    print("スライス（部分リストを取得）：")
    print(f">>> colors[1:3]   # {colors[1:3]}  （インデックス1から2まで）")
    print(f">>> colors[:2]    # {colors[:2]}  （最初から2つ）")
    print(f">>> colors[2:]    # {colors[2:]}  （3番目から最後まで）")
    print(f">>> colors[::2]   # {colors[::2]}  （1つ飛ばし）")
    print(f">>> colors[::-1]  # {colors[::-1]}  （逆順）")
    print()
    
    print("💡 スライスは [開始:終了:ステップ] の形式です")
    print("   終了インデックスの要素は含まれません")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_3_list_operations():
    """レッスン3: リストの操作"""
    print("📚 レッスン3: リストの操作")
    print("-" * 40)
    print()
    
    print("リストの変更・追加・削除：")
    print()
    
    # リストの変更
    animals = ['cat', 'dog', 'bird']
    print(f">>> animals = {animals}")
    print(">>> animals[1] = 'hamster'  # 要素の変更")
    animals[1] = 'hamster'
    print(f">>> animals  # {animals}")
    print()
    
    # 要素の追加
    print(">>> animals.append('rabbit')  # 末尾に追加")
    animals.append('rabbit')
    print(f">>> animals  # {animals}")
    print()
    
    print(">>> animals.insert(1, 'fish')  # 指定位置に挿入")
    animals.insert(1, 'fish')
    print(f">>> animals  # {animals}")
    print()
    
    # 要素の削除
    print(">>> animals.remove('bird')  # 値を指定して削除")
    animals.remove('bird')
    print(f">>> animals  # {animals}")
    print()
    
    print(">>> last = animals.pop()  # 最後の要素を取り出し")
    last = animals.pop()
    print(f">>> last  # '{last}'")
    print(f">>> animals  # {animals}")
    print()
    
    print(">>> del animals[0]  # インデックスで削除")
    del animals[0]
    print(f">>> animals  # {animals}")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_4_list_methods():
    """レッスン4: 便利なリストメソッド"""
    print("📚 レッスン4: 便利なリストメソッド")
    print("-" * 40)
    print()
    
    # ソート
    print("リストのソート：")
    scores = [85, 92, 78, 95, 88]
    print(f">>> scores = {scores}")
    print(">>> scores.sort()  # 昇順にソート（元のリストを変更）")
    scores.sort()
    print(f">>> scores  # {scores}")
    print()
    
    print(">>> scores.sort(reverse=True)  # 降順にソート")
    scores.sort(reverse=True)
    print(f">>> scores  # {scores}")
    print()
    
    # その他のメソッド
    print("その他の便利なメソッド：")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f">>> numbers = {numbers}")
    print(f">>> numbers.count(5)  # {numbers.count(5)}  （5の個数）")
    print(f">>> numbers.index(4)  # {numbers.index(4)}  （4の位置）")
    print(f">>> sum(numbers)     # {sum(numbers)}  （合計）")
    print(f">>> max(numbers)     # {max(numbers)}  （最大値）")
    print(f">>> min(numbers)     # {min(numbers)}  （最小値）")
    print()
    
    # リストのコピー
    print("リストのコピー：")
    original = [1, 2, 3]
    print(f">>> original = {original}")
    print(">>> copy1 = original.copy()  # 浅いコピー")
    copy1 = original.copy()
    print(">>> copy2 = original[:]      # スライスでコピー")
    copy2 = original[:]
    print(">>> copy3 = list(original)   # list()でコピー")
    copy3 = list(original)
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_5_tuples():
    """レッスン5: タプル"""
    print("📚 レッスン5: タプル（変更不可のリスト）")
    print("-" * 40)
    print()
    
    print("タプルは変更できないリストです。")
    print("丸括弧 () で作成します。")
    print()
    
    # タプルの作成
    print(">>> point = (3, 5)")
    point = (3, 5)
    print(f">>> point  # {point}")
    print(f">>> type(point)  # {type(point)}")
    print()
    
    print(">>> rgb = (255, 128, 0)")
    rgb = (255, 128, 0)
    print(f">>> rgb  # {rgb}")
    print()
    
    # 括弧なしでも作成可能
    print(">>> coordinates = 10, 20, 30  # 括弧なしでもOK")
    coordinates = 10, 20, 30
    print(f">>> coordinates  # {coordinates}")
    print()
    
    # タプルの特徴
    print("タプルの特徴：")
    print(f">>> rgb[0]  # {rgb[0]}  （インデックスアクセスはOK）")
    print(">>> rgb[0] = 100  # エラー！（変更不可）")
    print()
    
    # アンパック
    print("タプルのアンパック：")
    print(">>> x, y = point")
    x, y = point
    print(f">>> x  # {x}")
    print(f">>> y  # {y}")
    print()
    
    print(">>> r, g, b = rgb")
    r, g, b = rgb
    print(f">>> print(f'R:{r}, G:{g}, B:{b}')")
    print(f'R:{r}, G:{g}, B:{b}')
    print()
    
    print("💡 タプルは変更されたくないデータに使います")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_6_dictionaries():
    """レッスン6: 辞書"""
    print("📚 レッスン6: 辞書（キーと値のペア）")
    print("-" * 40)
    print()
    
    print("辞書はキーと値のペアでデータを管理します。")
    print("波括弧 {} で作成します。")
    print()
    
    # 辞書の作成
    print(">>> person = {'name': '太郎', 'age': 25, 'city': '東京'}")
    person = {'name': '太郎', 'age': 25, 'city': '東京'}
    print(f">>> person  # {person}")
    print()
    
    # 値の取得
    print("値の取得：")
    print(f">>> person['name']  # '{person['name']}'")
    print(f">>> person['age']   # {person['age']}")
    print()
    
    # 値の変更・追加
    print("値の変更と追加：")
    print(">>> person['age'] = 26  # 既存のキーの値を変更")
    person['age'] = 26
    print(">>> person['job'] = 'エンジニア'  # 新しいキーと値を追加")
    person['job'] = 'エンジニア'
    print(f">>> person  # {person}")
    print()
    
    # 辞書のメソッド
    print("便利なメソッド：")
    print(f">>> person.keys()    # {list(person.keys())}")
    print(f">>> person.values()  # {list(person.values())}")
    print(f">>> person.items()   # {list(person.items())}")
    print()
    
    # get メソッド
    print("安全な値の取得（get メソッド）：")
    print(f">>> person.get('name')     # '{person.get('name')}'")
    print(f">>> person.get('hobby')    # {person.get('hobby')}  （存在しない場合）")
    print(f">>> person.get('hobby', '読書')  # '{person.get('hobby', '読書')}'  （デフォルト値）")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_7_nested_structures():
    """レッスン7: ネストしたデータ構造"""
    print("📚 レッスン7: ネストしたデータ構造")
    print("-" * 40)
    print()
    
    print("リストや辞書は入れ子にできます：")
    print()
    
    # リストのリスト（2次元配列）
    print("リストのリスト（表形式のデータ）：")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(">>> matrix = [")
    print("...     [1, 2, 3],")
    print("...     [4, 5, 6],")
    print("...     [7, 8, 9]")
    print("... ]")
    print(f">>> matrix[1][2]  # {matrix[1][2]}  （2行目の3列目）")
    print()
    
    # 辞書のリスト
    print("辞書のリスト（複数のレコード）：")
    students = [
        {'name': '田中', 'score': 85},
        {'name': '鈴木', 'score': 92},
        {'name': '佐藤', 'score': 78}
    ]
    print(">>> students = [")
    print("...     {'name': '田中', 'score': 85},")
    print("...     {'name': '鈴木', 'score': 92},")
    print("...     {'name': '佐藤', 'score': 78}")
    print("... ]")
    print(f">>> students[1]['name']   # '{students[1]['name']}'")
    print(f">>> students[1]['score']  # {students[1]['score']}")
    print()
    
    # より複雑な構造
    print("より複雑な構造：")
    data = {
        'users': ['Alice', 'Bob', 'Charlie'],
        'scores': {
            'Alice': [85, 90, 88],
            'Bob': [92, 87, 95],
            'Charlie': [78, 85, 80]
        }
    }
    print(">>> data['scores']['Bob'][2]  # Bob の3番目のスコア")
    print(f"    {data['scores']['Bob'][2]}")
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
    
    print("【練習1】 買い物リスト")
    print("1. shopping = [] で空のリストを作成")
    print("2. append() で「牛乳」「パン」「卵」を追加")
    print("3. insert() で最初に「野菜」を追加")
    print("4. 「パン」を「米」に変更")
    print("5. リストを表示")
    print()
    
    print("【練習2】 成績管理")
    print("1. scores = [75, 82, 90, 68, 95] を作成")
    print("2. 平均点を計算: sum(scores) / len(scores)")
    print("3. 最高点と最低点を表示")
    print("4. 80点以上の個数を数える")
    print()
    
    print("【練習3】 連絡先辞書")
    print("1. contact = {} で空の辞書を作成")
    print("2. 名前、電話番号、メールアドレスを追加")
    print("3. 住所を追加")
    print("4. すべてのキーを表示")
    print()
    
    input("練習が終わったらEnterキーを押してください...")
    print()


def show_summary():
    """まとめ"""
    print("📝 第3章のまとめ")
    print("=" * 50)
    print()
    
    print("リストについて学んだこと：")
    print("✅ リストの作成と要素へのアクセス")
    print("✅ append(), insert(), remove(), pop() などのメソッド")
    print("✅ インデックスとスライス")
    print("✅ sort() によるソート")
    print()
    
    print("タプルについて学んだこと：")
    print("✅ 変更不可能（イミュータブル）な性質")
    print("✅ アンパックによる値の取り出し")
    print("✅ 固定データの保存に適している")
    print()
    
    print("辞書について学んだこと：")
    print("✅ キーと値のペアでデータを管理")
    print("✅ keys(), values(), items() メソッド")
    print("✅ get() による安全な値の取得")
    print()
    
    print("次のステップ：")
    print("• 制御フロー（if文、for文、while文）")
    print("• これらのデータ構造を使った実践的なプログラム")
    print()


def show_completion_message():
    """完了メッセージ"""
    print("\n" + "🎉" * 20)
    print("   ファイル 03 の学習完了！   ")
    print("🎉" * 20)
    
    print(f"\n📚 理解度テストを受けましょう")
    print("以下のコマンドをコピー&ペーストして実行してください:\n")
    
    # OS別コマンド表示
    python_cmd = "py" if platform.system() == "Windows" else "python3"
    print(f"   {python_cmd} quizzes/quiz_runner.py basics 03")
    
    print(f"\n✅ テスト合格後、次に進みましょう:")
    print(f"   {python_cmd} basics/04_control_flow.py")
    
    print("\n💡 困ったときは:")
    print(f"   {python_cmd} quizzes/quiz_runner.py help")
    print("=" * 50)


def main():
    """メイン処理"""
    print_chapter_header()
    
    # 各レッスンを順番に実行
    lesson_1_list_basics()
    lesson_2_list_indexing()
    lesson_3_list_operations()
    lesson_4_list_methods()
    lesson_5_tuples()
    lesson_6_dictionaries()
    lesson_7_nested_structures()
    
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