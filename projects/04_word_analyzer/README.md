# 📊 プロジェクト4: 単語解析アプリ

テキストファイルを詳細に解析し、統計情報、頻出単語、感情分析などを行うアプリケーションです。

## 📚 概要

文字列処理と統計分析を組み合わせた実用的なテキスト解析ツールです。基本的な単語カウントから、高度なTF-IDF分析、N-gram解析まで段階的に学習できます。

## 🎯 学習目標

- **文字列処理** - 正規表現とテキスト前処理
- **統計分析** - 頻度分析と統計指標の計算
- **アルゴリズム実装** - TF-IDF、N-gram、感情分析
- **データ可視化** - 結果の分かりやすい表示
- **ファイルI/O** - 結果の保存とエクスポート

## 📁 ファイル構成

```
04_word_analyzer/
├── README.md              # このファイル
├── basic_analyzer.py      # 基本解析（正規表現・統計）
└── advanced_analyzer.py   # 高度解析（TF-IDF・感情分析）
```

## 🚀 使い方

### 基本単語解析

```bash
python3 projects/04_word_analyzer/basic_analyzer.py
```

**機能:**
- ファイルまたは直接入力からテキスト読み込み
- 基本統計情報（文字数、単語数、行数など）
- 頻出単語ランキング
- 正規表現による単語検索
- 長さ別単語表示
- 結果のファイル保存

**推奨学習レベル:** basics/11_standard_library.py 完了後

### 高度単語解析

```bash
python3 projects/04_word_analyzer/advanced_analyzer.py
```

**機能:**
- ストップワード除去
- N-gram解析（Bigram、Trigram）
- TF-IDF計算
- 感情分析
- 読みやすさスコア
- 共起語分析
- JSON形式での結果出力

**推奨学習レベル:** basics/12_external_libraries.py 完了後

## ⚙️ 機能詳細

### 基本解析の統計情報

```python
stats = {
    'total_characters': 5000,        # 総文字数
    'total_words': 800,              # 総単語数
    'unique_words': 350,             # ユニーク単語数
    'total_lines': 45,               # 総行数
    'average_word_length': 5.2,      # 平均単語長
    'type_token_ratio': 0.437        # 語彙豊富度
}
```

### 高度解析の機能

#### 1. ストップワード除去
```python
# 除去される一般的な単語
english_stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', ...}
japanese_stopwords = {'は', 'が', 'を', 'に', 'で', 'と', 'の', ...}
```

#### 2. N-gram解析
```python
# Bigram（2語の組み合わせ）
bigrams = [('machine', 'learning'), ('data', 'science'), ...]

# Trigram（3語の組み合わせ）
trigrams = [('machine', 'learning', 'algorithm'), ...]
```

#### 3. TF-IDF計算
```python
def calculate_tf_idf():
    """
    TF (Term Frequency): 単語の出現頻度
    IDF (Inverse Document Frequency): 逆文書頻度
    TF-IDF = TF × IDF （重要度スコア）
    """
```

#### 4. 感情分析
```python
sentiment_score = (positive_words - negative_words) / total_sentiment_words
# -1.0（ネガティブ）から 1.0（ポジティブ）
```

## 🎮 実際の使用例

### 基本解析の実行例

```
📊 基本単語解析アプリ
==================================================

📋 メニュー
1. ファイルからテキストを読み込み
2. 直接テキストを入力

選択: 1
ファイル名を入力: sample.txt

✅ ファイルを読み込みました: sample.txt
✅ テキスト前処理完了: 1,234個の単語を抽出

📊 基本統計情報
========================================
📝 総文字数:         5,432
📝 文字数(空白除く):  4,123
🔤 総単語数:         1,234
🔤 ユニーク単語数:     567
📏 平均単語長:       4.32
📈 語彙豊富度(TTR):  0.459

🔝 頻出単語 TOP 10
========================================
 1. python         45回 ( 3.65%)
 2. data           32回 ( 2.59%)
 3. analysis       28回 ( 2.27%)
 4. code           24回 ( 1.94%)
 5. function       22回 ( 1.78%)
```

### 高度解析の結果例

```json
{
  "basic_stats": {
    "total_words": 1234,
    "unique_words": 567,
    "sentiment_score": 0.234,
    "readability_score": 72.5
  },
  "top_words": [
    ["python", 45],
    ["data", 32],
    ["analysis", 28]
  ],
  "bigrams": [
    [["machine", "learning"], 12],
    [["data", "science"], 8],
    [["natural", "language"], 6]
  ],
  "tf_idf_scores": {
    "algorithm": 0.523,
    "implementation": 0.445,
    "optimization": 0.389
  }
}
```

## 📈 分析可能な指標

### 基本指標
- **文字数統計** - 総文字数、空白除外文字数
- **単語統計** - 総単語数、ユニーク単語数、平均単語長
- **行統計** - 総行数、非空行数
- **語彙豊富度** - Type-Token Ratio (TTR)

### 高度指標
- **可読性スコア** - Flesch Reading Ease風の計算
- **感情スコア** - ポジティブ/ネガティブ語彙の比率
- **TF-IDF** - 単語重要度スコア
- **N-gram頻度** - 語の組み合わせパターン
- **共起語分析** - 特定単語の周辺語彙

## 🔧 カスタマイズ方法

### ストップワードの追加

```python
# カスタムストップワードの追加
custom_stopwords = {'very', 'really', 'quite', 'rather'}
analyzer.stopwords['english'].update(custom_stopwords)
```

### 感情辞書の拡張

```python
# 感情語彙の追加
analyzer.sentiment_dict['positive'].update({
    'brilliant', 'outstanding', 'superb', 'magnificent'
})

analyzer.sentiment_dict['negative'].update({
    'devastating', 'catastrophic', 'dreadful', 'appalling'
})
```

### カスタム解析関数

```python
def analyze_word_complexity(analyzer):
    """単語の複雑さを分析"""
    complexity_scores = {}
    
    for word in analyzer.word_count:
        # 長さによる複雑さ
        length_score = min(len(word) / 10, 1.0)
        
        # 音節数による複雑さ
        syllable_score = min(analyzer._count_syllables(word) / 5, 1.0)
        
        # 総合複雑さスコア
        complexity_scores[word] = (length_score + syllable_score) / 2
    
    return complexity_scores
```

## 🧪 テスト用サンプルテキスト

### sample1.txt（基本テスト用）
```
Python is a powerful programming language. 
It is easy to learn and very versatile.
Python can be used for web development, data analysis, and machine learning.
The syntax is clean and readable.
```

### sample2.txt（感情分析テスト用）
```
This amazing product is absolutely fantastic! 
I love the brilliant design and excellent performance.
However, the terrible customer service was disappointing.
The awful experience made me very angry and frustrated.
Overall, it's a wonderful tool despite some issues.
```

## 💡 学習のポイント

### 1. 正規表現の活用
```python
# 単語抽出
words = re.findall(r'\w+', text.lower())

# 文分割
sentences = re.split(r'[.!?。！？]', text)

# パターンマッチング
matches = re.findall(r'^[aeiou].*ing$', word)  # 母音で始まりingで終わる
```

### 2. データ構造の効率的使用
```python
from collections import Counter, defaultdict

# 頻度カウント
word_count = Counter(words)

# グループ化
word_groups = defaultdict(list)
for word in words:
    word_groups[len(word)].append(word)
```

### 3. 統計計算
```python
# 平均値
average = sum(values) / len(values)

# 分散
variance = sum((x - average) ** 2 for x in values) / len(values)

# 標準偏差
std_dev = math.sqrt(variance)
```

### 4. ファイル処理
```python
# 安全なファイル読み込み
try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
except (FileNotFoundError, UnicodeDecodeError) as e:
    print(f"エラー: {e}")
```

## 🔄 改良案

### 機能拡張
1. **言語検出** - テキストの言語を自動判定
2. **キーワード抽出** - 重要なキーワードの自動抽出
3. **要約機能** - テキストの自動要約
4. **類似度分析** - 文書間の類似度計算
5. **品詞解析** - 単語の品詞情報の付与

### 可視化機能
1. **ワードクラウド** - 単語の視覚的表示
2. **グラフ表示** - 統計情報のチャート化
3. **時系列分析** - 複数文書の時間的変化
4. **ネットワーク図** - 単語間の関係性可視化

### パフォーマンス改善
```python
# 大量テキスト対応
def process_large_text(filename, chunk_size=1024*1024):
    """チャンク単位での処理"""
    with open(filename, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield process_chunk(chunk)
```

## 📊 実用的な応用例

### 1. ブログ記事の分析
```python
# SEO最適化のための解析
def analyze_seo_metrics(text):
    analyzer = BasicWordAnalyzer()
    analyzer.text = text
    analyzer.analyze_all()
    
    return {
        'keyword_density': analyzer.get_keyword_density(),
        'readability': analyzer.stats['readability_score'],
        'word_count': analyzer.stats['total_words'],
        'sentiment': analyzer.stats['sentiment_score']
    }
```

### 2. レビューの感情分析
```python
# 商品レビューの傾向分析
def analyze_reviews(reviews):
    total_sentiment = 0
    positive_count = 0
    
    for review in reviews:
        analyzer = AdvancedWordAnalyzer()
        analyzer.text = review
        analyzer.preprocess_text()
        analyzer.calculate_advanced_statistics()
        
        sentiment = analyzer.stats['sentiment_score']
        total_sentiment += sentiment
        if sentiment > 0:
            positive_count += 1
    
    return {
        'average_sentiment': total_sentiment / len(reviews),
        'positive_ratio': positive_count / len(reviews)
    }
```

## 🎓 次のステップ

このプロジェクト完了後の推奨学習：

1. **プロジェクト5** - データ可視化で結果をグラフ表示
2. **自然言語処理** - NLTK/spaCyを使った本格的なNLP
3. **機械学習** - scikit-learnを使った文書分類
4. **Web API** - テキスト解析APIの作成
5. **データベース** - 解析結果の永続化

## ❓ よくある質問

**Q: 日本語のテキストも解析できますか？**
A: 基本的な解析は可能ですが、より高精度な解析には形態素解析ライブラリ（MeCab等）の使用を推奨します。

**Q: 大きなファイルの処理が遅いです**
A: チャンク単位での処理やストリーミング処理の実装を検討してください。

**Q: 感情分析の精度を上げるには？**
A: より大きな感情辞書の使用や、機械学習モデル（VADER、TextBlob等）の導入を検討してください。

**Q: 結果をグラフで表示したいです**
A: matplotlib/seabornを使った可視化機能を追加できます。プロジェクト5で学習します。

---

**テキスト解析をお楽しみください！** 📊✨