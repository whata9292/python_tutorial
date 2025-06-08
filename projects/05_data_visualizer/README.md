# 📊 プロジェクト5: データ可視化アプリ

CSVデータを読み込み、統計分析と可視化を行うアプリケーション集です。学生成績分析と売上データ分析の2つのアプリを提供します。

## 📚 概要

実際のビジネスや教育現場で使用されるデータ分析の基礎を学習できます。標準ライブラリのみを使用してデータ処理、統計計算、ASCII文字による可視化を実装し、データサイエンスの入門知識を習得します。

## 🎯 学習目標

- **データ処理** - CSV読み書き、データクリーニング
- **統計分析** - 基本統計量、分布分析、相関分析
- **データ可視化** - ASCII文字によるグラフ作成
- **ビジネス分析** - KPI計算、トレンド分析、レポート生成
- **データ構造活用** - 辞書とリストを使った効率的な集計

## 📁 ファイル構成

```
05_data_visualizer/
├── README.md              # このファイル
├── student_grades.py      # 学生成績分析アプリ
└── sales_analyzer.py      # 売上データ分析アプリ
```

## 🚀 使い方

### 学生成績分析アプリ

```bash
python3 projects/05_data_visualizer/student_grades.py
```

**分析機能:**
- 学生別・科目別成績統計
- 成績分布の可視化
- 散布図による科目間相関
- 成績上位者ランキング
- 詳細レポート生成

**推奨学習レベル:** basics/08_input_output.py 完了後

### 売上データ分析アプリ

```bash
python3 projects/05_data_visualizer/sales_analyzer.py
```

**分析機能:**
- 月別売上トレンド分析
- 商品別・地域別パフォーマンス
- 営業担当者別実績
- 成長率分析
- ビジネスレポート生成

**推奨学習レベル:** basics/08_input_output.py 完了後

## ⚙️ 機能詳細

### 学生成績分析

#### データ構造
```python
# 成績データの例
student_data = {
    '学生001': {
        '数学': 85,
        '英語': 92,
        '理科': 78,
        '社会': 88,
        '国語': 90
    }
}
```

#### 主な統計指標
- **基本統計**: 平均、中央値、標準偏差
- **語彙豊富度**: Type-Token Ratio (TTR)
- **成績分布**: 10点刻みでの分布分析
- **相関分析**: 科目間のピアソン相関係数
- **読みやすさ**: Flesch Reading Ease風スコア

#### CSV形式例
```csv
学生,数学,英語,理科,社会,国語
学生001,85,92,78,88,90
学生002,76,84,82,79,85
学生003,94,89,91,93,87
```

### 売上データ分析

#### データ構造
```python
# 売上データの例
sales_record = {
    'date': '2024-01-15',
    'product': '商品A',
    'region': '東京',
    'sales_rep': '田中',
    'amount': 15000,
    'quantity': 3,
    'unit_price': 5000
}
```

#### 主な分析指標
- **売上統計**: 総売上、平均取引額、日平均売上
- **成長率**: 月次成長率、前年同月比
- **市場シェア**: 商品別・地域別シェア
- **パフォーマンス**: 営業担当者別実績
- **トレンド**: 時系列変化の可視化

#### CSV形式例
```csv
date,product,region,sales_rep,amount,quantity,unit_price
2024-01-15,商品A,東京,田中,15000,3,5000
2024-01-16,商品B,大阪,佐藤,22000,2,11000
2024-01-17,商品C,名古屋,鈴木,8500,1,8500
```

## 🎮 実際の使用例

### 学生成績分析の実行例

```
📊 学生成績データ可視化アプリ
==================================================

📋 メニュー
1. サンプルデータを生成
2. CSVファイルから読み込み
3. 基本統計を表示

選択: 1
✅ サンプルデータを生成しました: 50人、5科目

選択: 3

📊 全体統計
========================================
👥 学生数:       50人
📚 科目数:        5科目
📈 全体平均:     78.50点
📊 中央値:       79.00点
📉 標準偏差:     12.45

📊 科目別平均点
====================================================
数学     |████████████████████████████████████  78.2
英語     |██████████████████████████████████████  80.1
理科     |███████████████████████████████████  76.8
社会     |█████████████████████████████████████  79.3
国語     |██████████████████████████████████████  81.5
====================================================
```

### 売上分析の実行例

```
💰 売上データ分析アプリ
==================================================

📋 メニュー
4. 月別売上トレンド

選択: 4

📅 月別売上トレンド
======================================================================
年月      売上高        数量    取引数  平均取引額
----------------------------------------------------------------------
2023-06  ¥ 2,450,000     156     42   ¥  58,333
2023-07  ¥ 2,890,000     184     48   ¥  60,208
2023-08  ¥ 3,120,000     201     52   ¥  60,000

📈 月別売上推移
====================================================
 3120000 |                                    ●
 2890000 |                          ●
 2450000 |                ●
         +------------------------------------
         2023-06                      2023-08
====================================================
```

## 📈 可視化機能

### ASCII文字による棒グラフ
```python
def create_ascii_chart(self, data, title="チャート", max_width=50):
    """ASCII文字でチャートを作成"""
    max_value = max(data.values())
    
    for label, value in data.items():
        bar_length = int((value / max_value) * max_width)
        bar = "█" * bar_length
        print(f"{label:>12} |{bar:<{max_width}} {value}")
```

### ASCII文字による散布図
```python
def create_scatter_plot(self, subject1, subject2, max_width=60, max_height=20):
    """2科目の散布図を作成（ASCII）"""
    plot = [[' ' for _ in range(max_width)] for _ in range(max_height)]
    
    for x, y in zip(x_data, y_data):
        plot_x = int(((x - x_min) / (x_max - x_min)) * (max_width - 1))
        plot_y = max_height - 1 - int(((y - y_min) / (y_max - y_min)) * (max_height - 1))
        plot[plot_y][plot_x] = '●'
```

### ラインチャート（時系列）
```python
def create_ascii_line_chart(self, data, title="ラインチャート"):
    """ASCII文字でラインチャートを作成"""
    # データポイントをプロット
    for i, value in enumerate(values):
        x = int((i / (len(values) - 1)) * (max_width - 1))
        y = int(((value - min_val) / (max_val - min_val)) * (max_height - 1))
        chart[max_height - 1 - y][x] = '●'
```

## 🧮 統計計算の実装

### 基本統計量
```python
import statistics

def calculate_basic_stats(data):
    """基本統計量を計算"""
    return {
        'mean': statistics.mean(data),
        'median': statistics.median(data),
        'stdev': statistics.stdev(data) if len(data) > 1 else 0,
        'max': max(data),
        'min': min(data)
    }
```

### ピアソン相関係数
```python
def calculate_correlation(self, x_data, y_data):
    """ピアソン相関係数を計算"""
    x_mean = statistics.mean(x_data)
    y_mean = statistics.mean(y_data)
    
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_data, y_data))
    x_variance = sum((x - x_mean) ** 2 for x in x_data)
    y_variance = sum((y - y_mean) ** 2 for y in y_data)
    
    denominator = math.sqrt(x_variance * y_variance)
    return numerator / denominator if denominator != 0 else 0
```

### 成長率計算
```python
def calculate_growth_rate(self, prev_value, curr_value):
    """前期比成長率を計算"""
    if prev_value == 0:
        return 0
    return ((curr_value - prev_value) / prev_value) * 100
```

## 🔧 カスタマイズ方法

### 新しい統計指標の追加

```python
def calculate_coefficient_of_variation(self, data):
    """変動係数を計算"""
    mean_val = statistics.mean(data)
    stdev_val = statistics.stdev(data)
    return (stdev_val / mean_val) * 100 if mean_val != 0 else 0

def calculate_quartiles(self, data):
    """四分位数を計算"""
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    q1_index = n // 4
    q2_index = n // 2
    q3_index = 3 * n // 4
    
    return {
        'q1': sorted_data[q1_index],
        'q2': sorted_data[q2_index],  # median
        'q3': sorted_data[q3_index]
    }
```

### カスタム可視化関数

```python
def create_histogram(self, data, bins=10):
    """ヒストグラムを作成"""
    min_val, max_val = min(data), max(data)
    bin_width = (max_val - min_val) / bins
    
    histogram = [0] * bins
    for value in data:
        bin_index = min(int((value - min_val) / bin_width), bins - 1)
        histogram[bin_index] += 1
    
    # ASCII表示
    max_count = max(histogram)
    for i, count in enumerate(histogram):
        bin_start = min_val + i * bin_width
        bin_end = bin_start + bin_width
        bar_length = int((count / max_count) * 40)
        bar = "█" * bar_length
        print(f"{bin_start:6.1f}-{bin_end:6.1f} |{bar} ({count})")
```

### レポート生成の拡張

```python
def generate_executive_summary(self, stats):
    """エグゼクティブサマリーを生成"""
    insights = []
    
    # パフォーマンス評価
    if stats['average_sale'] > 50000:
        insights.append("高額商品が多く、プレミアム市場に強み")
    
    # トレンド分析
    growth_rates = self.calculate_growth_rate()
    avg_growth = statistics.mean(growth_rates.values())
    
    if avg_growth > 10:
        insights.append("急成長トレンド - 市場拡大期")
    elif avg_growth < -5:
        insights.append("売上減少傾向 - 要因分析が必要")
    
    return insights
```

## 🧪 テスト用データセット

### 学生成績データ (grades_sample.csv)
```csv
学生,数学,英語,理科,社会,国語
田中太郎,85,78,92,80,88
佐藤花子,92,95,89,94,90
鈴木一郎,76,82,78,85,83
高橋美咲,88,90,85,89,91
山田次郎,79,74,81,77,80
```

### 売上データ (sales_sample.csv)
```csv
date,product,region,sales_rep,amount,quantity,unit_price
2024-01-01,商品A,東京,田中,15000,3,5000
2024-01-02,商品B,大阪,佐藤,25000,1,25000
2024-01-03,商品C,名古屋,鈴木,12000,2,6000
2024-01-04,商品A,福岡,高橋,18000,3,6000
2024-01-05,商品D,札幌,伊藤,30000,2,15000
```

## 💡 学習のポイント

### 1. データ構造の効率的な使用
```python
# defaultdictを使った集計
from collections import defaultdict

monthly_sales = defaultdict(float)
for record in sales_data:
    month_key = record['date'][:7]  # YYYY-MM
    monthly_sales[month_key] += record['amount']
```

### 2. CSV処理のベストプラクティス
```python
# DictReaderを使った読み込み
import csv

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # row は辞書形式でアクセス可能
        process_record(row)
```

### 3. エラーハンドリング
```python
def safe_float_conversion(value, default=0):
    """安全な数値変換"""
    try:
        return float(value)
    except (ValueError, TypeError):
        return default
```

### 4. メモリ効率的な処理
```python
def process_large_dataset(filename):
    """大きなデータセットの処理"""
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 一行ずつ処理してメモリ使用量を抑制
            yield process_row(row)
```

## 📊 ビジネス分析指標

### KPI（重要業績評価指標）
1. **売上高** - 総売上金額
2. **平均取引額** - 取引あたりの平均金額
3. **成長率** - 前期比の変化率
4. **市場シェア** - 全体に占める割合
5. **顧客単価** - 顧客あたりの平均売上

### 分析手法
1. **トレンド分析** - 時系列データの変化パターン
2. **比較分析** - 期間・カテゴリ間の比較
3. **構成分析** - 全体に占める各要素の割合
4. **相関分析** - 変数間の関係性
5. **異常値検出** - 通常パターンからの逸脱

## 🔄 改良案

### 高度な可視化
1. **matplotlib連携** - 本格的なグラフ作成
2. **インタラクティブ表示** - ユーザー操作対応
3. **ダッシュボード** - 複数指標の統合表示
4. **リアルタイム更新** - データの自動更新

### 分析機能の拡張
1. **予測分析** - 将来トレンドの予測
2. **クラスタリング** - データのグループ化
3. **異常検知** - 通常パターンからの逸脱検出
4. **A/Bテスト分析** - 施策効果の測定

### データ連携
1. **データベース接続** - SQL対応
2. **API連携** - 外部データソース
3. **リアルタイムデータ** - ストリーミング処理
4. **クラウド連携** - スケーラブルな処理

## 🎓 次のステップ

このプロジェクト完了後の推奨学習：

1. **matplotlib/seaborn** - 本格的なデータ可視化
2. **pandas** - 高性能データ処理ライブラリ
3. **numpy** - 数値計算ライブラリ
4. **scikit-learn** - 機械学習ライブラリ
5. **Jupyter Notebook** - インタラクティブ分析環境

## ❓ よくある質問

**Q: データが大きすぎてメモリ不足になります**
A: チャンク単位での処理やジェネレータを使用してメモリ使用量を抑制してください。

**Q: CSV以外のデータ形式に対応したい**
A: JSON、Excel、XMLなどのライブラリを追加で学習し、対応を拡張できます。

**Q: もっと美しいグラフを作りたい**
A: matplotlibやseabornライブラリの学習をお勧めします。本プロジェクトはその基礎となります。

**Q: Webブラウザで表示したい**
A: FlaskやDjangoでWebアプリ化、またはJupyter Notebookでの表示が可能です。

**Q: リアルタイムデータを扱いたい**
A: WebSocketやAPI連携の学習により、リアルタイム分析システムを構築できます。

---

**データの力で洞察を得る楽しさを体験してください！** 📊✨