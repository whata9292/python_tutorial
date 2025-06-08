#!/usr/bin/env python3
"""
===========================
第8章: 入出力処理
===========================

ファイルの読み書きやユーザー入力の処理方法を学習します。
データの永続化、ファイル形式の操作、エラーハンドリングなど
実用的なプログラムに必須の技術を習得しましょう。

このファイルを実行すると、データを扱う実践的な
スキルが身につきます。
"""

import platform
import os
import json
import csv
from pathlib import Path


def print_chapter_header():
    """章のヘッダーを表示"""
    print("=" * 50)
    print("第8章: 入出力処理")
    print("=" * 50)
    print()


def lesson_1_file_basics():
    """レッスン1: ファイル操作の基本"""
    print("📚 レッスン1: ファイル操作の基本")
    print("-" * 40)
    print()
    
    print("ファイルの読み書きはプログラムの基本機能です。")
    print()
    
    # ファイル書き込み
    print("ファイルへの書き込み:")
    filename = "sample.txt"
    content = "Hello, File!\nこれはテストファイルです。\n"
    
    print(f">>> with open('{filename}', 'w', encoding='utf-8') as f:")
    print("...     f.write('Hello, File!\\n')")
    print("...     f.write('これはテストファイルです。\\n')")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('Hello, File!\n')
        f.write('これはテストファイルです。\n')
    
    print(f">>> # '{filename}' ファイルが作成されました")
    print()
    
    # ファイル読み込み
    print("ファイルからの読み込み:")
    print(f">>> with open('{filename}', 'r', encoding='utf-8') as f:")
    print("...     content = f.read()")
    print("...     print(content)")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
    
    # 1行ずつ読み込み
    print("1行ずつ読み込み:")
    print(f">>> with open('{filename}', 'r', encoding='utf-8') as f:")
    print("...     for line_num, line in enumerate(f, 1):")
    print("...         print(f'{line_num}: {line.strip()}')")
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            print(f'{line_num}: {line.strip()}')
    print()
    
    print("💡 with文を使うと、ファイルが確実に閉じられます")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_2_file_modes():
    """レッスン2: ファイルモード"""
    print("📚 レッスン2: ファイルモード")
    print("-" * 40)
    print()
    
    print("ファイルを開く際のモードについて学びます。")
    print()
    
    print("主なファイルモード:")
    print("• 'r'  : 読み込み専用（デフォルト）")
    print("• 'w'  : 書き込み専用（ファイルを上書き）")
    print("• 'a'  : 追記専用（ファイルの末尾に追加）")
    print("• 'x'  : 作成専用（ファイルが存在するとエラー）")
    print("• 'r+' : 読み書き両用")
    print("• 'rb' : バイナリ読み込み")
    print("• 'wb' : バイナリ書き込み")
    print()
    
    # 追記モードの例
    filename = "append_test.txt"
    print("追記モードの例:")
    print(f">>> # 最初の書き込み")
    print(f">>> with open('{filename}', 'w', encoding='utf-8') as f:")
    print("...     f.write('1行目\\n')")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('1行目\n')
    
    print(f">>> # 追記")
    print(f">>> with open('{filename}', 'a', encoding='utf-8') as f:")
    print("...     f.write('2行目\\n')")
    print("...     f.write('3行目\\n')")
    
    with open(filename, 'a', encoding='utf-8') as f:
        f.write('2行目\n')
        f.write('3行目\n')
    
    print(f">>> # 内容確認")
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read().strip())
    print()
    
    # ファイルの存在確認
    print("ファイルの存在確認:")
    print(">>> import os")
    print(f">>> os.path.exists('{filename}')")
    print(f"    {os.path.exists(filename)}")
    print(">>> os.path.isfile('sample.txt')")
    print(f"    {os.path.isfile('sample.txt')}")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_3_pathlib():
    """レッスン3: pathlibモジュール"""
    print("📚 レッスン3: pathlibモジュール")
    print("-" * 40)
    print()
    
    print("pathlibは現代的なファイルパス操作の方法です。")
    print()
    
    # Pathオブジェクトの作成
    print("Pathオブジェクトの使い方:")
    print(">>> from pathlib import Path")
    print(">>> p = Path('sample.txt')")
    p = Path('sample.txt')
    print(f">>> p  # {p}")
    print()
    
    # パスの情報
    print("パスの情報取得:")
    print(f">>> p.name       # '{p.name}'  （ファイル名）")
    print(f">>> p.suffix     # '{p.suffix}'  （拡張子）")
    print(f">>> p.stem       # '{p.stem}'  （拡張子なしファイル名）")
    print(f">>> p.parent     # {p.parent}  （親ディレクトリ）")
    print(f">>> p.absolute() # {p.absolute()}  （絶対パス）")
    print()
    
    # ディレクトリ操作
    print("ディレクトリ操作:")
    test_dir = Path('test_directory')
    print(f">>> test_dir = Path('test_directory')")
    print(f">>> test_dir.mkdir(exist_ok=True)  # ディレクトリ作成")
    test_dir.mkdir(exist_ok=True)
    
    # ファイル作成
    test_file = test_dir / 'test.txt'
    print(f">>> test_file = test_dir / 'test.txt'")
    print(f">>> test_file.write_text('テストファイル', encoding='utf-8')")
    test_file.write_text('テストファイル', encoding='utf-8')
    
    print(f">>> test_file.read_text(encoding='utf-8')")
    print(f"    '{test_file.read_text(encoding='utf-8')}'")
    print()
    
    # ディレクトリ内容の表示
    print("ディレクトリ内容の確認:")
    print(">>> list(test_dir.iterdir())")
    print(f"    {list(test_dir.iterdir())}")
    print()
    
    # glob パターン
    print("ファイル検索（glob）:")
    print(">>> list(Path('.').glob('*.txt'))")
    txt_files = list(Path('.').glob('*.txt'))
    print(f"    {txt_files}")
    print()
    
    print("💡 pathlibはクロスプラットフォーム対応で")
    print("   Windows/Mac/Linuxで同じコードが動きます")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_4_json_files():
    """レッスン4: JSONファイルの処理"""
    print("📚 レッスン4: JSONファイルの処理")
    print("-" * 40)
    print()
    
    print("JSONはデータ交換でよく使われる形式です。")
    print()
    
    # Python辞書をJSONファイルに保存
    print("PythonオブジェクトをJSONファイルに保存:")
    data = {
        'name': '山田太郎',
        'age': 30,
        'hobbies': ['読書', '映画鑑賞', 'プログラミング'],
        'address': {
            'city': '東京',
            'zipcode': '100-0001'
        }
    }
    
    print(">>> data = {")
    print("...     'name': '山田太郎',")
    print("...     'age': 30,")
    print("...     'hobbies': ['読書', '映画鑑賞', 'プログラミング'],")
    print("...     'address': {'city': '東京', 'zipcode': '100-0001'}")
    print("... }")
    print()
    
    json_file = 'person.json'
    print(f">>> with open('{json_file}', 'w', encoding='utf-8') as f:")
    print("...     json.dump(data, f, ensure_ascii=False, indent=2)")
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f">>> # '{json_file}' ファイルが作成されました")
    print()
    
    # JSONファイルから読み込み
    print("JSONファイルから読み込み:")
    print(f">>> with open('{json_file}', 'r', encoding='utf-8') as f:")
    print("...     loaded_data = json.load(f)")
    
    with open(json_file, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    
    print(">>> print(loaded_data['name'])")
    print(f"    {loaded_data['name']}")
    print(">>> print(loaded_data['hobbies'])")
    print(f"    {loaded_data['hobbies']}")
    print()
    
    # JSON文字列との変換
    print("JSON文字列との相互変換:")
    print(">>> json_string = json.dumps(data, ensure_ascii=False)")
    json_string = json.dumps(data, ensure_ascii=False)
    print(f">>> json_string[:50] + '...'")
    print(f"    '{json_string[:50]}...'")
    print()
    
    print(">>> parsed_data = json.loads(json_string)")
    parsed_data = json.loads(json_string)
    print(f">>> parsed_data['age']  # {parsed_data['age']}")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_5_csv_files():
    """レッスン5: CSVファイルの処理"""
    print("📚 レッスン5: CSVファイルの処理")
    print("-" * 40)
    print()
    
    print("CSVは表形式データでよく使われる形式です。")
    print()
    
    # CSVファイルの書き込み
    print("CSVファイルの書き込み:")
    csv_file = 'students.csv'
    students_data = [
        ['名前', '年齢', '学科'],
        ['田中太郎', 20, '情報工学'],
        ['鈴木花子', 19, '数学'],
        ['佐藤次郎', 21, '物理学']
    ]
    
    print(">>> import csv")
    print(f">>> with open('{csv_file}', 'w', newline='', encoding='utf-8') as f:")
    print("...     writer = csv.writer(f)")
    print("...     for row in students_data:")
    print("...         writer.writerow(row)")
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in students_data:
            writer.writerow(row)
    
    print(f">>> # '{csv_file}' ファイルが作成されました")
    print()
    
    # CSVファイルの読み込み
    print("CSVファイルの読み込み:")
    print(f">>> with open('{csv_file}', 'r', encoding='utf-8') as f:")
    print("...     reader = csv.reader(f)")
    print("...     for row in reader:")
    print("...         print(row)")
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(f"    {row}")
    print()
    
    # DictReaderを使った読み込み
    print("DictReaderを使った読み込み（見出し行を活用）:")
    print(f">>> with open('{csv_file}', 'r', encoding='utf-8') as f:")
    print("...     reader = csv.DictReader(f)")
    print("...     for row in reader:")
    print("...         print(f\"{row['名前']} ({row['年齢']}歳) - {row['学科']}\")")
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"    {row['名前']} ({row['年齢']}歳) - {row['学科']}")
    print()
    
    print("💡 CSV処理では pandas ライブラリも非常に便利です")
    print("   （basics/12で外部ライブラリとして学習）")
    print()
    
    input("Enterキーを押して次へ進む...")
    print()


def lesson_6_error_handling():
    """レッスン6: ファイル操作のエラーハンドリング"""
    print("📚 レッスン6: ファイル操作のエラーハンドリング")
    print("-" * 40)
    print()
    
    print("ファイル操作では様々なエラーが発生する可能性があります。")
    print()
    
    # ファイルが存在しない場合
    print("ファイルが存在しない場合の処理:")
    print(">>> try:")
    print("...     with open('not_exist.txt', 'r') as f:")
    print("...         content = f.read()")
    print("... except FileNotFoundError:")
    print("...     print('ファイルが見つかりません')")
    
    try:
        with open('not_exist.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print('    ファイルが見つかりません')
    print()
    
    # 権限エラーの処理
    print("ファイル操作の安全な方法:")
    safe_file = 'safe_test.txt'
    print(f">>> def safe_write_file(filename, content):")
    print("...     try:")
    print("...         with open(filename, 'w', encoding='utf-8') as f:")
    print("...             f.write(content)")
    print("...         return True")
    print("...     except (IOError, OSError) as e:")
    print("...         print(f'エラー: {e}')")
    print("...         return False")
    
    def safe_write_file(filename, content):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except (IOError, OSError) as e:
            print(f'    エラー: {e}')
            return False
    
    print(f">>> safe_write_file('{safe_file}', 'テスト内容')")
    result = safe_write_file(safe_file, 'テスト内容')
    print(f"    {result}")
    print()
    
    # ファイル存在確認の安全な方法
    print("ファイル存在確認:")
    print(">>> from pathlib import Path")
    print(f">>> p = Path('{safe_file}')")
    p = Path(safe_file)
    print(f">>> p.exists()      # {p.exists()}")
    print(f">>> p.is_file()     # {p.is_file()}")
    print(f">>> p.stat().st_size  # {p.stat().st_size} bytes")
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
    
    print("【練習1】ログファイル作成")
    print("現在時刻とメッセージを記録するログファイルを作成")
    print("追記モードで複数のログエントリを追加")
    print()
    
    print("【練習2】設定ファイル管理")
    print("アプリケーション設定をJSONファイルで管理")
    print("設定の読み込み・保存・更新機能を実装")
    print()
    
    print("【練習3】CSV データ処理")
    print("商品データのCSVファイルを作成")
    print("価格順でソートして新しいCSVファイルに出力")
    print()
    
    print("【練習4】ファイル操作ユーティリティ")
    print("指定ディレクトリ内のファイル一覧を表示")
    print("ファイルサイズや更新日時も含めて表示")
    print()
    
    input("練習が終わったらEnterキーを押してください...")
    print()


def cleanup_files():
    """作成したテストファイルのクリーンアップ"""
    print("🧹 テストファイルの削除")
    print("-" * 30)
    
    files_to_remove = [
        'sample.txt', 'append_test.txt', 'person.json', 
        'students.csv', 'safe_test.txt'
    ]
    
    dirs_to_remove = ['test_directory']
    
    # ファイル削除
    for file in files_to_remove:
        try:
            Path(file).unlink(missing_ok=True)
            print(f"✅ {file} を削除しました")
        except:
            pass
    
    # ディレクトリ削除
    for dir_name in dirs_to_remove:
        try:
            import shutil
            shutil.rmtree(dir_name, ignore_errors=True)
            print(f"✅ {dir_name}/ を削除しました")
        except:
            pass
    
    print("クリーンアップ完了")
    print()


def show_summary():
    """まとめ"""
    print("📝 第8章のまとめ")
    print("=" * 50)
    print()
    
    print("入出力処理について学んだこと：")
    print("✅ ファイルの読み書き（open(), with文）")
    print("✅ ファイルモード（r, w, a, x など）")
    print("✅ pathlibを使った現代的なパス操作")
    print("✅ JSONファイルの読み書き")
    print("✅ CSVファイルの処理")
    print("✅ エラーハンドリング（FileNotFoundError など）")
    print()
    
    print("ファイル操作のベストプラクティス：")
    print("• with文でファイルを確実に閉じる")
    print("• 適切な文字エンコーディング（utf-8）を指定")
    print("• エラーハンドリングで堅牢性を確保")
    print("• pathlibでクロスプラットフォーム対応")
    print()
    
    print("次のステップ：")
    print("• エラーと例外処理の詳細")
    print("• オブジェクト指向プログラミング")
    print()


def show_completion_message():
    """完了メッセージ"""
    print("\n" + "🎉" * 20)
    print("   ファイル 08 の学習完了！   ")
    print("🎉" * 20)
    
    print(f"\n📚 理解度テストを受けましょう")
    print("以下のコマンドをコピー&ペーストして実行してください:\n")
    
    # OS別コマンド表示
    python_cmd = "py" if platform.system() == "Windows" else "python3"
    print(f"   {python_cmd} quizzes/quiz_runner.py basics 08")
    
    print(f"\n✅ テスト合格後、次に進みましょう:")
    print(f"   {python_cmd} basics/09_errors_and_exceptions.py")
    
    print("\n💡 困ったときは:")
    print(f"   {python_cmd} quizzes/quiz_runner.py help")
    print("=" * 50)


def main():
    """メイン処理"""
    print_chapter_header()
    
    # 各レッスンを順番に実行
    lesson_1_file_basics()
    lesson_2_file_modes()
    lesson_3_pathlib()
    lesson_4_json_files()
    lesson_5_csv_files()
    lesson_6_error_handling()
    
    # 練習問題
    practice_exercises()
    
    # ファイルクリーンアップ
    cleanup_files()
    
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