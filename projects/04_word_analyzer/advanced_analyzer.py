#!/usr/bin/env python3
"""
プロジェクト4: 高度な単語解析アプリ

機械学習風の機能を含む高度なテキスト解析アプリです。
ストップワード除去、N-gram解析、感情スコアなどを実装しています。

学習ポイント:
- 標準ライブラリの高度な活用
- アルゴリズムの実装
- データ可視化の基礎
- より複雑なテキスト処理

対応章: basics/12_external_libraries.py完了後
"""

import re
import math
import json
from collections import Counter, defaultdict
from pathlib import Path

class AdvancedWordAnalyzer:
    """高度な単語解析クラス"""
    
    def __init__(self):
        """アナライザーを初期化"""
        self.text = ""
        self.sentences = []
        self.words = []
        self.word_count = {}
        self.stats = {}
        
        # ストップワード（除外する一般的な単語）
        self.stopwords = {
            'english': {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'this', 'that', 'these', 'those'},
            'japanese': {'は', 'が', 'を', 'に', 'で', 'と', 'の', 'だ', 'である', 'です', 'ます', 'した', 'する', 'この', 'その', 'あの', 'これ', 'それ', 'あれ'}
        }
        
        # 感情辞書（簡易版）
        self.sentiment_dict = {
            'positive': {'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'love', 'like', 'happy', 'joy', 'beautiful', 'perfect', 'awesome', 'brilliant'},
            'negative': {'bad', 'terrible', 'awful', 'horrible', 'hate', 'dislike', 'sad', 'angry', 'ugly', 'worst', 'pain', 'difficult', 'problem', 'issue'}
        }
    
    def load_text_from_file(self, filename):
        """ファイルからテキストを読み込み"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.text = f.read()
            print(f"✅ ファイルを読み込みました: {filename}")
            return True
        except Exception as e:
            print(f"❌ ファイル読み込みエラー: {e}")
            return False
    
    def preprocess_text(self, remove_stopwords=True, language='english'):
        """高度なテキスト前処理"""
        if not self.text:
            return False
        
        # 文単位で分割
        self.sentences = re.split(r'[.!?。！？]', self.text)
        self.sentences = [s.strip() for s in self.sentences if s.strip()]
        
        # テキストの正規化
        text_lower = self.text.lower()
        
        # 特殊文字の処理
        text_processed = re.sub(r'[^\w\s]', ' ', text_lower)
        text_processed = re.sub(r'\s+', ' ', text_processed)
        
        # 単語分割
        words = [word.strip() for word in text_processed.split() if word.strip()]
        
        # ストップワード除去
        if remove_stopwords and language in self.stopwords:
            words = [word for word in words if word not in self.stopwords[language]]
        
        # 短すぎる単語を除去（1文字以下）
        words = [word for word in words if len(word) > 1]
        
        self.words = words
        print(f"✅ 高度な前処理完了: {len(self.words)}個の単語を抽出")
        return True
    
    def calculate_advanced_statistics(self):
        """高度な統計情報を計算"""
        if not self.words:
            return False
        
        self.word_count = Counter(self.words)
        
        # 基本統計
        total_words = len(self.words)
        unique_words = len(self.word_count)
        
        # 語彙の豊富さ
        ttr = unique_words / total_words if total_words > 0 else 0
        
        # 単語長統計
        word_lengths = [len(word) for word in self.words]
        avg_word_length = sum(word_lengths) / len(word_lengths)
        
        # 文の統計
        sentence_lengths = [len(sentence.split()) for sentence in self.sentences]
        avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
        
        # 読みやすさスコア（簡易版）
        readability_score = self._calculate_readability()
        
        # 感情スコア
        sentiment_score = self._calculate_sentiment()
        
        self.stats = {
            'total_words': total_words,
            'unique_words': unique_words,
            'total_sentences': len(self.sentences),
            'type_token_ratio': ttr,
            'average_word_length': avg_word_length,
            'average_sentence_length': avg_sentence_length,
            'readability_score': readability_score,
            'sentiment_score': sentiment_score
        }
        
        return True
    
    def _calculate_readability(self):
        """読みやすさスコアを計算（Flesch Reading Ease風）"""
        if not self.sentences or not self.words:
            return 0
        
        total_sentences = len(self.sentences)
        total_words = len(self.words)
        total_syllables = sum(self._count_syllables(word) for word in self.words)
        
        if total_sentences == 0 or total_words == 0:
            return 0
        
        # 簡易Flesch Reading Ease風の計算
        score = 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words)
        return max(0, min(100, score))
    
    def _count_syllables(self, word):
        """音節数を推定（英語の場合）"""
        word = word.lower()
        vowels = 'aeiouy'
        syllable_count = 0
        prev_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not prev_was_vowel:
                syllable_count += 1
            prev_was_vowel = is_vowel
        
        # 最低1音節
        return max(1, syllable_count)
    
    def _calculate_sentiment(self):
        """感情スコアを計算"""
        positive_count = 0
        negative_count = 0
        
        for word in self.words:
            if word in self.sentiment_dict['positive']:
                positive_count += 1
            elif word in self.sentiment_dict['negative']:
                negative_count += 1
        
        total_sentiment_words = positive_count + negative_count
        if total_sentiment_words == 0:
            return 0.0
        
        # -1.0（完全にネガティブ）から 1.0（完全にポジティブ）
        sentiment_score = (positive_count - negative_count) / total_sentiment_words
        return sentiment_score
    
    def get_ngrams(self, n=2):
        """N-gramを生成"""
        if len(self.words) < n:
            return []
        
        ngrams = []
        for i in range(len(self.words) - n + 1):
            ngram = tuple(self.words[i:i + n])
            ngrams.append(ngram)
        
        return Counter(ngrams)
    
    def get_word_collocations(self, target_word, window=2):
        """指定した単語の共起語を取得"""
        collocations = defaultdict(int)
        
        for i, word in enumerate(self.words):
            if word == target_word:
                # 前後のwindowサイズ分の単語を取得
                start = max(0, i - window)
                end = min(len(self.words), i + window + 1)
                
                for j in range(start, end):
                    if j != i:  # 自分自身は除く
                        collocations[self.words[j]] += 1
        
        return dict(collocations)
    
    def calculate_tf_idf(self):
        """TF-IDF風のスコアを計算（簡易版）"""
        if not self.sentences:
            return {}
        
        # 各文を文書として扱う
        documents = []
        for sentence in self.sentences:
            words = re.findall(r'\w+', sentence.lower())
            documents.append(words)
        
        if not documents:
            return {}
        
        # TF（Term Frequency）計算
        tf_scores = {}
        for word in self.word_count:
            tf = self.word_count[word] / len(self.words)
            
            # IDF（Inverse Document Frequency）計算
            doc_count = sum(1 for doc in documents if word in doc)
            idf = math.log(len(documents) / (doc_count + 1))
            
            tf_scores[word] = tf * idf
        
        return tf_scores
    
    def get_keyword_density(self, min_frequency=2):
        """キーワード密度を計算"""
        if not self.words:
            return {}
        
        density = {}
        total_words = len(self.words)
        
        for word, count in self.word_count.items():
            if count >= min_frequency:
                density[word] = (count / total_words) * 100
        
        return density
    
    def analyze_word_patterns(self):
        """単語パターンを分析"""
        patterns = {
            'starts_with_vowel': 0,
            'ends_with_consonant': 0,
            'contains_numbers': 0,
            'all_caps_words': 0,
            'repeated_letters': 0
        }
        
        vowels = set('aeiouAEIOU')
        consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
        
        for word in self.words:
            # 母音で始まる
            if word[0] in vowels:
                patterns['starts_with_vowel'] += 1
            
            # 子音で終わる
            if word[-1] in consonants:
                patterns['ends_with_consonant'] += 1
            
            # 数字を含む
            if any(c.isdigit() for c in word):
                patterns['contains_numbers'] += 1
            
            # 全て大文字
            if word.isupper() and len(word) > 1:
                patterns['all_caps_words'] += 1
            
            # 連続する同じ文字
            if any(word[i] == word[i+1] for i in range(len(word)-1)):
                patterns['repeated_letters'] += 1
        
        return patterns
    
    def export_analysis_to_json(self, filename="analysis_result.json"):
        """解析結果をJSONで出力"""
        try:
            result = {
                'basic_stats': self.stats,
                'top_words': self.word_count.most_common(20),
                'bigrams': list(self.get_ngrams(2).most_common(10)),
                'trigrams': list(self.get_ngrams(3).most_common(5)),
                'tf_idf_scores': dict(sorted(self.calculate_tf_idf().items(), key=lambda x: x[1], reverse=True)[:10]),
                'word_patterns': self.analyze_word_patterns(),
                'keyword_density': dict(sorted(self.get_keyword_density().items(), key=lambda x: x[1], reverse=True)[:10])
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            
            print(f"✅ 解析結果をJSONで保存しました: {filename}")
            return True
            
        except Exception as e:
            print(f"❌ JSON出力エラー: {e}")
            return False

def main():
    """実行例"""
    analyzer = AdvancedWordAnalyzer()
    
    # サンプルテキストで動作確認
    sample_text = """
    This is a sample text for advanced word analysis. The text contains multiple sentences 
    with different word patterns. Some words are repeated, and some are unique. 
    We can analyze the sentiment, readability, and various linguistic features.
    This amazing tool provides excellent insights into text analysis.
    """
    
    analyzer.text = sample_text
    
    print("🚀 高度な単語解析デモ")
    print("=" * 50)
    
    # 前処理
    analyzer.preprocess_text(remove_stopwords=True, language='english')
    
    # 統計計算
    analyzer.calculate_advanced_statistics()
    
    # 結果表示
    print("\n📊 高度な統計情報:")
    for key, value in analyzer.stats.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.3f}")
        else:
            print(f"  {key}: {value}")
    
    print("\n🔝 頻出単語:")
    for word, count in analyzer.word_count.most_common(5):
        print(f"  {word}: {count}回")
    
    print("\n🔗 Bigrams:")
    bigrams = analyzer.get_ngrams(2)
    for bigram, count in bigrams.most_common(3):
        print(f"  {' '.join(bigram)}: {count}回")
    
    print("\n🎯 TF-IDF上位:")
    tf_idf = analyzer.calculate_tf_idf()
    for word, score in sorted(tf_idf.items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"  {word}: {score:.3f}")
    
    # JSON出力
    analyzer.export_analysis_to_json("demo_analysis.json")

if __name__ == "__main__":
    main()

"""
🎯 学習のポイント:

1. 高度なテキスト処理
   - ストップワード除去
   - N-gram解析
   - 共起語分析

2. 統計学的手法
   - TF-IDF計算
   - 読みやすさスコア
   - 感情分析

3. データ構造の活用
   - defaultdictを使った集計
   - Counterの高度な活用
   - 辞書の入れ子構造

4. アルゴリズムの実装
   - パターンマッチング
   - スコア計算
   - データ変換処理

🔧 改良案:
- より高度な感情分析
- 言語検出機能
- 類似文書検索
- 要約機能
- 可視化機能

⚡ 実行方法:
python3 projects/04_word_analyzer/advanced_analyzer.py
"""