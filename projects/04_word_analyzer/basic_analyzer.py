#!/usr/bin/env python3
"""
プロジェクト4: 基本単語解析アプリ

テキストファイルを読み込み、単語の出現頻度や統計情報を分析するアプリです。
文字列処理、ファイル操作、辞書活用などを学習します。

学習ポイント:
- ファイル読み込みと文字列処理
- 正規表現の基本的な使用
- 辞書を使った集計処理
- 統計情報の計算と表示

対応章: basics/11_standard_library.py完了後
"""

import re
import string
from collections import Counter
from pathlib import Path

class BasicWordAnalyzer:
    """基本的な単語解析クラス"""
    
    def __init__(self):
        """アナライザーを初期化"""
        self.text = ""
        self.words = []
        self.word_count = {}
        self.stats = {}
    
    def load_text_from_file(self, filename):
        """
        ファイルからテキストを読み込み
        
        Args:
            filename (str): 読み込むファイル名
            
        Returns:
            bool: 読み込み成功時True
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.text = f.read()
            print(f"✅ ファイルを読み込みました: {filename}")
            return True
        except FileNotFoundError:
            print(f"❌ ファイルが見つかりません: {filename}")
            return False
        except UnicodeDecodeError:
            print(f"❌ ファイルの文字エンコーディングエラー: {filename}")
            return False
        except Exception as e:
            print(f"❌ ファイル読み込みエラー: {e}")
            return False
    
    def load_text_from_input(self):
        """標準入力からテキストを読み込み"""
        print("分析したいテキストを入力してください（終了するには空行でEnter）:")
        lines = []
        while True:
            line = input()
            if not line.strip():
                break
            lines.append(line)
        
        self.text = '\n'.join(lines)
        print("✅ テキストを入力しました")
    
    def preprocess_text(self):
        """
        テキストの前処理を行う
        - 小文字に変換
        - 句読点の除去
        - 単語の抽出
        """
        if not self.text:
            print("❌ テキストが読み込まれていません")
            return False
        
        # 小文字に変換
        text_lower = self.text.lower()
        
        # 英数字、ひらがな、カタカナ、漢字のみを抽出
        # 複数の空白文字は1つの空白に置換
        processed_text = re.sub(r'[^\w\s]', ' ', text_lower)
        processed_text = re.sub(r'\s+', ' ', processed_text)
        
        # 単語に分割（空白で区切る）
        self.words = [word.strip() for word in processed_text.split() if word.strip()]
        
        print(f"✅ テキスト前処理完了: {len(self.words)}個の単語を抽出")
        return True
    
    def count_words(self):
        """単語の出現回数をカウント"""
        if not self.words:
            print("❌ 単語が抽出されていません")
            return False
        
        self.word_count = Counter(self.words)
        print(f"✅ 単語カウント完了: {len(self.word_count)}種類の単語")
        return True
    
    def calculate_statistics(self):
        """統計情報を計算"""
        if not self.text or not self.words:
            print("❌ データが不足しています")
            return False
        
        # 基本統計
        total_chars = len(self.text)
        total_chars_no_spaces = len(self.text.replace(' ', '').replace('\n', '').replace('\t', ''))
        total_words = len(self.words)
        unique_words = len(self.word_count)
        
        # 文字と行の統計
        lines = self.text.split('\n')
        total_lines = len(lines)
        non_empty_lines = len([line for line in lines if line.strip()])
        
        # 単語長の統計
        word_lengths = [len(word) for word in self.words]
        avg_word_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
        max_word_length = max(word_lengths) if word_lengths else 0
        min_word_length = min(word_lengths) if word_lengths else 0
        
        # 語彙の豊富さ（Type-Token Ratio）
        ttr = unique_words / total_words if total_words > 0 else 0
        
        self.stats = {
            'total_characters': total_chars,
            'total_characters_no_spaces': total_chars_no_spaces,
            'total_words': total_words,
            'unique_words': unique_words,
            'total_lines': total_lines,
            'non_empty_lines': non_empty_lines,
            'average_word_length': avg_word_length,
            'max_word_length': max_word_length,
            'min_word_length': min_word_length,
            'type_token_ratio': ttr
        }
        
        print("✅ 統計計算完了")
        return True
    
    def get_most_common_words(self, n=10):
        """
        最も頻出する単語を取得
        
        Args:
            n (int): 取得する単語数
            
        Returns:
            list: (単語, 出現回数) のタプルのリスト
        """
        if not self.word_count:
            return []
        
        return self.word_count.most_common(n)
    
    def get_words_by_length(self, length):
        """
        指定した長さの単語を取得
        
        Args:
            length (int): 単語の長さ
            
        Returns:
            list: 指定した長さの単語のリスト
        """
        return [word for word in self.word_count.keys() if len(word) == length]
    
    def search_words(self, pattern):
        """
        パターンにマッチする単語を検索
        
        Args:
            pattern (str): 検索パターン（正規表現対応）
            
        Returns:
            list: マッチした単語のリスト
        """
        try:
            regex = re.compile(pattern, re.IGNORECASE)
            matches = []
            for word in self.word_count.keys():
                if regex.search(word):
                    matches.append((word, self.word_count[word]))
            
            # 出現回数でソート
            matches.sort(key=lambda x: x[1], reverse=True)
            return matches
            
        except re.error as e:
            print(f"❌ 正規表現エラー: {e}")
            return []
    
    def analyze_all(self):
        """すべての解析を実行"""
        if not self.text:
            print("❌ テキストが読み込まれていません")
            return False
        
        success = (
            self.preprocess_text() and
            self.count_words() and
            self.calculate_statistics()
        )
        
        if success:
            print("🎉 解析が完了しました！")
        
        return success

class WordAnalyzerUI:
    """単語解析アプリのユーザーインターフェース"""
    
    def __init__(self):
        """UIを初期化"""
        self.analyzer = BasicWordAnalyzer()
    
    def show_welcome(self):
        """ウェルカムメッセージを表示"""
        print("=" * 60)
        print("📊 基本単語解析アプリ")
        print("=" * 60)
        print("テキストファイルの単語を分析し、統計情報を表示します")
        print("=" * 60)
    
    def show_main_menu(self):
        """メインメニューを表示"""
        print("\n📋 メニュー")
        print("-" * 40)
        print("1. ファイルからテキストを読み込み")
        print("2. 直接テキストを入力")
        print("3. 基本統計を表示")
        print("4. 頻出単語を表示")
        print("5. 単語を検索")
        print("6. 長さ別単語表示")
        print("7. 詳細解析結果を表示")
        print("8. 結果をファイルに保存")
        print("0. 終了")
        print("-" * 40)
    
    def load_file_interactive(self):
        """対話式でファイルを読み込み"""
        print("\n📂 ファイル読み込み")
        print("-" * 30)
        
        filename = input("ファイル名を入力: ").strip()
        if not filename:
            print("❌ ファイル名を入力してください")
            return
        
        if self.analyzer.load_text_from_file(filename):
            self.analyzer.analyze_all()
    
    def input_text_interactive(self):
        """対話式でテキストを入力"""
        print("\n✏️ テキスト入力")
        print("-" * 30)
        
        self.analyzer.load_text_from_input()
        self.analyzer.analyze_all()
    
    def show_basic_stats(self):
        """基本統計を表示"""
        if not self.analyzer.stats:
            print("❌ まずテキストを読み込んでください")
            return
        
        stats = self.analyzer.stats
        
        print("\n📊 基本統計情報")
        print("=" * 40)
        print(f"📝 総文字数:         {stats['total_characters']:,}")
        print(f"📝 文字数(空白除く):  {stats['total_characters_no_spaces']:,}")
        print(f"📰 総行数:           {stats['total_lines']:,}")
        print(f"📰 非空行数:         {stats['non_empty_lines']:,}")
        print(f"🔤 総単語数:         {stats['total_words']:,}")
        print(f"🔤 ユニーク単語数:   {stats['unique_words']:,}")
        print(f"📏 平均単語長:       {stats['average_word_length']:.2f}")
        print(f"📏 最大単語長:       {stats['max_word_length']}")
        print(f"📏 最小単語長:       {stats['min_word_length']}")
        print(f"📈 語彙豊富度(TTR):  {stats['type_token_ratio']:.3f}")
        print("=" * 40)
    
    def show_frequent_words(self):
        """頻出単語を表示"""
        if not self.analyzer.word_count:
            print("❌ まずテキストを読み込んでください")
            return
        
        try:
            n = int(input("表示する単語数 (デフォルト:10): ") or "10")
        except ValueError:
            n = 10
        
        most_common = self.analyzer.get_most_common_words(n)
        
        print(f"\n🔝 頻出単語 TOP {n}")
        print("=" * 40)
        for i, (word, count) in enumerate(most_common, 1):
            percentage = (count / self.analyzer.stats['total_words']) * 100
            print(f"{i:2d}. {word:<15} {count:>5}回 ({percentage:5.2f}%)")
        print("=" * 40)
    
    def search_words_interactive(self):
        """対話式で単語を検索"""
        if not self.analyzer.word_count:
            print("❌ まずテキストを読み込んでください")
            return
        
        print("\n🔍 単語検索")
        print("-" * 30)
        print("💡 正規表現も使用できます")
        print("例: '^a' (aで始まる), 'ing$' (ingで終わる), '.{5,}' (5文字以上)")
        
        pattern = input("検索パターン: ").strip()
        if not pattern:
            print("❌ 検索パターンを入力してください")
            return
        
        matches = self.analyzer.search_words(pattern)
        
        if not matches:
            print(f"📝 パターン '{pattern}' にマッチする単語が見つかりませんでした")
            return
        
        print(f"\n🔍 検索結果: '{pattern}' ({len(matches)}件)")
        print("=" * 40)
        for word, count in matches[:20]:  # 最大20件表示
            print(f"{word:<20} {count:>3}回")
        
        if len(matches) > 20:
            print(f"... 他 {len(matches) - 20} 件")
        print("=" * 40)
    
    def show_words_by_length(self):
        """長さ別に単語を表示"""
        if not self.analyzer.word_count:
            print("❌ まずテキストを読み込んでください")
            return
        
        try:
            length = int(input("単語の長さ: "))
        except ValueError:
            print("❌ 有効な数値を入力してください")
            return
        
        words = self.analyzer.get_words_by_length(length)
        
        if not words:
            print(f"📝 {length}文字の単語が見つかりませんでした")
            return
        
        # 出現回数でソート
        words_with_count = [(word, self.analyzer.word_count[word]) for word in words]
        words_with_count.sort(key=lambda x: x[1], reverse=True)
        
        print(f"\n📏 {length}文字の単語 ({len(words)}件)")
        print("=" * 40)
        for word, count in words_with_count[:20]:  # 最大20件表示
            print(f"{word:<20} {count:>3}回")
        
        if len(words_with_count) > 20:
            print(f"... 他 {len(words_with_count) - 20} 件")
        print("=" * 40)
    
    def show_detailed_analysis(self):
        """詳細解析結果を表示"""
        if not self.analyzer.word_count:
            print("❌ まずテキストを読み込んでください")
            return
        
        print("\n📈 詳細解析結果")
        print("=" * 50)
        
        # 基本統計
        self.show_basic_stats()
        
        # 単語長分布
        print("\n📊 単語長分布")
        print("-" * 30)
        length_dist = {}
        for word in self.analyzer.words:
            length = len(word)
            length_dist[length] = length_dist.get(length, 0) + 1
        
        for length in sorted(length_dist.keys()):
            count = length_dist[length]
            percentage = (count / len(self.analyzer.words)) * 100
            bar = "█" * int(percentage / 2)  # 簡単なバーチャート
            print(f"{length:2d}文字: {count:4d}個 ({percentage:5.1f}%) {bar}")
        
        # 頻出単語
        print(f"\n🔝 頻出単語 TOP 5")
        print("-" * 30)
        for i, (word, count) in enumerate(self.analyzer.get_most_common_words(5), 1):
            percentage = (count / self.analyzer.stats['total_words']) * 100
            print(f"{i}. {word} ({count}回, {percentage:.1f}%)")
    
    def save_results_to_file(self):
        """結果をファイルに保存"""
        if not self.analyzer.stats:
            print("❌ まずテキストを読み込んでください")
            return
        
        filename = input("保存ファイル名 (デフォルト:analysis_result.txt): ").strip()
        if not filename:
            filename = "analysis_result.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=== 単語解析結果 ===\n\n")
                
                # 基本統計
                stats = self.analyzer.stats
                f.write("📊 基本統計情報\n")
                f.write("-" * 30 + "\n")
                f.write(f"総文字数: {stats['total_characters']:,}\n")
                f.write(f"総単語数: {stats['total_words']:,}\n")
                f.write(f"ユニーク単語数: {stats['unique_words']:,}\n")
                f.write(f"平均単語長: {stats['average_word_length']:.2f}\n")
                f.write(f"語彙豊富度: {stats['type_token_ratio']:.3f}\n\n")
                
                # 頻出単語
                f.write("🔝 頻出単語 TOP 20\n")
                f.write("-" * 30 + "\n")
                for i, (word, count) in enumerate(self.analyzer.get_most_common_words(20), 1):
                    percentage = (count / stats['total_words']) * 100
                    f.write(f"{i:2d}. {word:<15} {count:>5}回 ({percentage:5.2f}%)\n")
            
            print(f"✅ 結果を保存しました: {filename}")
            
        except Exception as e:
            print(f"❌ ファイル保存エラー: {e}")
    
    def run(self):
        """アプリケーションのメインループ"""
        self.show_welcome()
        
        while True:
            try:
                self.show_main_menu()
                choice = input("選択: ").strip()
                
                if choice == "1":
                    self.load_file_interactive()
                elif choice == "2":
                    self.input_text_interactive()
                elif choice == "3":
                    self.show_basic_stats()
                elif choice == "4":
                    self.show_frequent_words()
                elif choice == "5":
                    self.search_words_interactive()
                elif choice == "6":
                    self.show_words_by_length()
                elif choice == "7":
                    self.show_detailed_analysis()
                elif choice == "8":
                    self.save_results_to_file()
                elif choice == "0":
                    print("\n👋 単語解析アプリを終了します")
                    break
                else:
                    print("❌ 無効な選択です")
                
                input("\nEnterキーで続行...")
                
            except KeyboardInterrupt:
                print("\n\n👋 単語解析アプリを終了します")
                break
            except Exception as e:
                print(f"❌ 予期しないエラー: {e}")
                input("Enterキーで続行...")

def main():
    """メイン関数"""
    app = WordAnalyzerUI()
    app.run()

if __name__ == "__main__":
    main()

"""
🎯 学習のポイント:

1. 文字列処理
   - 正規表現を使ったテキスト前処理
   - 大文字小文字の変換
   - 単語の抽出と分割

2. ファイルI/O
   - テキストファイルの安全な読み込み
   - エンコーディングの処理
   - エラーハンドリング

3. データ集計
   - Counterクラスを使った集計
   - 辞書による頻度カウント
   - 統計情報の計算

4. 検索とフィルタリング
   - 正規表現を使った検索
   - 条件による絞り込み
   - ソートとランキング

🔧 改良案:
- ストップワード除去機能
- 言語判定機能
- グラフ表示機能
- 類似度分析
- 感情分析

⚡ 実行方法:
python3 projects/04_word_analyzer/basic_analyzer.py

📝 サンプルテキストファイルを用意して試してみてください！
"""