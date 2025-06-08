#!/usr/bin/env python3
"""
プロジェクト5: 売上データ分析

売上データを分析し、時系列トレンド、商品別売上、地域別分析などを行うアプリです。
ビジネスデータ分析の基礎を学習します。

学習ポイント:
- 時系列データの処理
- ビジネス分析指標の計算
- トレンド分析
- データの集計とグループ化

対応章: basics/08_input_output.py完了後
"""

import csv
import json
import calendar
from datetime import datetime, timedelta
from collections import defaultdict
import statistics

class SalesDataAnalyzer:
    """売上データ分析クラス"""
    
    def __init__(self):
        """アナライザーを初期化"""
        self.sales_data = []  # 売上データのリスト
        self.summary_stats = {}
        self.monthly_sales = defaultdict(float)
        self.product_sales = defaultdict(float)
        self.region_sales = defaultdict(float)
    
    def generate_sample_data(self, num_records=500):
        """サンプル売上データを生成"""
        import random
        random.seed(42)
        
        products = ['商品A', '商品B', '商品C', '商品D', '商品E', '商品F']
        regions = ['東京', '大阪', '名古屋', '福岡', '札幌']
        sales_reps = ['田中', '佐藤', '鈴木', '高橋', '伊藤', '渡辺']
        
        self.sales_data = []
        
        # 過去1年分のデータを生成
        start_date = datetime.now() - timedelta(days=365)
        
        for i in range(num_records):
            # ランダムな日付（過去1年以内）
            random_days = random.randint(0, 365)
            sale_date = start_date + timedelta(days=random_days)
            
            # 季節性を考慮した売上生成
            month = sale_date.month
            seasonal_factor = 1.0
            if month in [11, 12]:  # 年末商戦
                seasonal_factor = 1.5
            elif month in [6, 7, 8]:  # 夏季
                seasonal_factor = 1.2
            elif month in [1, 2]:  # 年明け
                seasonal_factor = 0.8
            
            # 基本売上額（1000-50000円）
            base_amount = random.randint(1000, 50000)
            amount = int(base_amount * seasonal_factor)
            
            # 数量（1-10個）
            quantity = random.randint(1, 10)
            
            record = {
                'date': sale_date.strftime('%Y-%m-%d'),
                'product': random.choice(products),
                'region': random.choice(regions),
                'sales_rep': random.choice(sales_reps),
                'amount': amount,
                'quantity': quantity,
                'unit_price': amount // quantity
            }
            
            self.sales_data.append(record)
        
        # 日付でソート
        self.sales_data.sort(key=lambda x: x['date'])
        
        print(f"✅ サンプル売上データを生成しました: {len(self.sales_data)}件")
        return True
    
    def load_from_csv(self, filename):
        """CSVファイルから売上データを読み込み"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.sales_data = []
                
                for row in reader:
                    try:
                        record = {
                            'date': row['date'],
                            'product': row['product'],
                            'region': row['region'],
                            'sales_rep': row.get('sales_rep', ''),
                            'amount': float(row['amount']),
                            'quantity': int(row.get('quantity', 1)),
                            'unit_price': float(row.get('unit_price', 0))
                        }
                        
                        # 単価が0の場合は計算
                        if record['unit_price'] == 0 and record['quantity'] > 0:
                            record['unit_price'] = record['amount'] / record['quantity']
                        
                        self.sales_data.append(record)
                        
                    except (ValueError, KeyError) as e:
                        print(f"⚠️ データ行をスキップ: {e}")
                        continue
                
                print(f"✅ CSVから読み込みました: {len(self.sales_data)}件")
                return True
                
        except FileNotFoundError:
            print(f"❌ ファイルが見つかりません: {filename}")
            return False
        except Exception as e:
            print(f"❌ CSV読み込みエラー: {e}")
            return False
    
    def export_to_csv(self, filename="sales_export.csv"):
        """売上データをCSVにエクスポート"""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                if not self.sales_data:
                    print("❌ エクスポートするデータがありません")
                    return False
                
                fieldnames = self.sales_data[0].keys()
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                writer.writeheader()
                for record in self.sales_data:
                    writer.writerow(record)
            
            print(f"✅ CSVにエクスポートしました: {filename}")
            return True
            
        except Exception as e:
            print(f"❌ CSV出力エラー: {e}")
            return False
    
    def calculate_summary_statistics(self):
        """基本統計を計算"""
        if not self.sales_data:
            print("❌ データが読み込まれていません")
            return False
        
        # 基本統計
        amounts = [record['amount'] for record in self.sales_data]
        quantities = [record['quantity'] for record in self.sales_data]
        
        total_sales = sum(amounts)
        total_quantity = sum(quantities)
        avg_sale = statistics.mean(amounts)
        median_sale = statistics.median(amounts)
        
        # 期間の計算
        dates = [datetime.strptime(record['date'], '%Y-%m-%d') for record in self.sales_data]
        min_date = min(dates)
        max_date = max(dates)
        date_range = (max_date - min_date).days + 1
        
        # 日平均売上
        daily_avg = total_sales / date_range if date_range > 0 else 0
        
        self.summary_stats = {
            'total_records': len(self.sales_data),
            'total_sales': total_sales,
            'total_quantity': total_quantity,
            'average_sale': avg_sale,
            'median_sale': median_sale,
            'max_sale': max(amounts),
            'min_sale': min(amounts),
            'date_range_days': date_range,
            'daily_average': daily_avg,
            'start_date': min_date.strftime('%Y-%m-%d'),
            'end_date': max_date.strftime('%Y-%m-%d')
        }
        
        print("✅ 基本統計計算完了")
        return True
    
    def analyze_monthly_trends(self):
        """月別売上トレンドを分析"""
        self.monthly_sales = defaultdict(float)
        monthly_quantity = defaultdict(int)
        monthly_count = defaultdict(int)
        
        for record in self.sales_data:
            date_obj = datetime.strptime(record['date'], '%Y-%m-%d')
            month_key = date_obj.strftime('%Y-%m')
            
            self.monthly_sales[month_key] += record['amount']
            monthly_quantity[month_key] += record['quantity']
            monthly_count[month_key] += 1
        
        # 月別統計を計算
        monthly_stats = {}
        for month in self.monthly_sales:
            monthly_stats[month] = {
                'sales': self.monthly_sales[month],
                'quantity': monthly_quantity[month],
                'transactions': monthly_count[month],
                'avg_per_transaction': self.monthly_sales[month] / monthly_count[month] if monthly_count[month] > 0 else 0
            }
        
        return monthly_stats
    
    def analyze_product_performance(self):
        """商品別パフォーマンスを分析"""
        self.product_sales = defaultdict(float)
        product_quantity = defaultdict(int)
        product_count = defaultdict(int)
        
        for record in self.sales_data:
            product = record['product']
            self.product_sales[product] += record['amount']
            product_quantity[product] += record['quantity']
            product_count[product] += 1
        
        # 商品別統計
        product_stats = {}
        for product in self.product_sales:
            product_stats[product] = {
                'sales': self.product_sales[product],
                'quantity': product_quantity[product],
                'transactions': product_count[product],
                'avg_unit_price': self.product_sales[product] / product_quantity[product] if product_quantity[product] > 0 else 0,
                'avg_per_transaction': self.product_sales[product] / product_count[product] if product_count[product] > 0 else 0
            }
        
        return product_stats
    
    def analyze_regional_performance(self):
        """地域別パフォーマンスを分析"""
        self.region_sales = defaultdict(float)
        region_quantity = defaultdict(int)
        region_count = defaultdict(int)
        
        for record in self.sales_data:
            region = record['region']
            self.region_sales[region] += record['amount']
            region_quantity[region] += record['quantity']
            region_count[region] += 1
        
        # 地域別統計
        region_stats = {}
        for region in self.region_sales:
            region_stats[region] = {
                'sales': self.region_sales[region],
                'quantity': region_quantity[region],
                'transactions': region_count[region],
                'avg_per_transaction': self.region_sales[region] / region_count[region] if region_count[region] > 0 else 0,
                'market_share': (self.region_sales[region] / self.summary_stats['total_sales']) * 100 if 'total_sales' in self.summary_stats else 0
            }
        
        return region_stats
    
    def analyze_sales_rep_performance(self):
        """営業担当者別パフォーマンスを分析"""
        rep_stats = defaultdict(lambda: {'sales': 0, 'quantity': 0, 'transactions': 0})
        
        for record in self.sales_data:
            rep = record.get('sales_rep', '不明')
            rep_stats[rep]['sales'] += record['amount']
            rep_stats[rep]['quantity'] += record['quantity']
            rep_stats[rep]['transactions'] += 1
        
        # 平均取引額を計算
        for rep in rep_stats:
            if rep_stats[rep]['transactions'] > 0:
                rep_stats[rep]['avg_per_transaction'] = rep_stats[rep]['sales'] / rep_stats[rep]['transactions']
            else:
                rep_stats[rep]['avg_per_transaction'] = 0
        
        return dict(rep_stats)
    
    def get_top_selling_days(self, n=10):
        """売上上位の日を取得"""
        daily_sales = defaultdict(float)
        
        for record in self.sales_data:
            daily_sales[record['date']] += record['amount']
        
        # 売上順でソート
        sorted_days = sorted(daily_sales.items(), key=lambda x: x[1], reverse=True)
        return sorted_days[:n]
    
    def calculate_growth_rate(self, period='monthly'):
        """成長率を計算"""
        if period == 'monthly':
            monthly_stats = self.analyze_monthly_trends()
            months = sorted(monthly_stats.keys())
            
            if len(months) < 2:
                return {}
            
            growth_rates = {}
            for i in range(1, len(months)):
                prev_month = months[i-1]
                curr_month = months[i]
                
                prev_sales = monthly_stats[prev_month]['sales']
                curr_sales = monthly_stats[curr_month]['sales']
                
                if prev_sales > 0:
                    growth_rate = ((curr_sales - prev_sales) / prev_sales) * 100
                    growth_rates[curr_month] = growth_rate
                else:
                    growth_rates[curr_month] = 0
            
            return growth_rates
        
        return {}
    
    def create_ascii_line_chart(self, data, title="ラインチャート", max_width=60, max_height=15):
        """ASCII文字でラインチャートを作成"""
        print(f"\n📈 {title}")
        print("=" * (max_width + 10))
        
        if not data:
            print("データがありません")
            return
        
        # データの準備
        sorted_data = sorted(data.items())
        labels = [item[0] for item in sorted_data]
        values = [item[1] for item in sorted_data]
        
        if not values:
            print("データがありません")
            return
        
        # スケール計算
        min_val = min(values)
        max_val = max(values)
        
        if max_val == min_val:
            print("すべての値が同じです")
            return
        
        # チャート作成
        chart = [[' ' for _ in range(max_width)] for _ in range(max_height)]
        
        # データポイントをプロット
        for i, value in enumerate(values):
            x = int((i / (len(values) - 1)) * (max_width - 1)) if len(values) > 1 else 0
            y = int(((value - min_val) / (max_val - min_val)) * (max_height - 1))
            y = max_height - 1 - y  # Y軸を反転
            
            if 0 <= x < max_width and 0 <= y < max_height:
                chart[y][x] = '●'
                
                # 線を引く（簡易版）
                if i > 0:
                    prev_x = int(((i-1) / (len(values) - 1)) * (max_width - 1)) if len(values) > 1 else 0
                    prev_value = values[i-1]
                    prev_y = int(((prev_value - min_val) / (max_val - min_val)) * (max_height - 1))
                    prev_y = max_height - 1 - prev_y
                    
                    # 線を引く（縦線のみ）
                    if prev_x != x:
                        for line_x in range(prev_x + 1, x):
                            if 0 <= line_x < max_width:
                                # 補間してy値を計算
                                ratio = (line_x - prev_x) / (x - prev_x)
                                line_y = int(prev_y + (y - prev_y) * ratio)
                                if 0 <= line_y < max_height:
                                    chart[line_y][line_x] = '-'
        
        # チャートを表示
        for i, row in enumerate(chart):
            y_value = max_val - (i / (max_height - 1)) * (max_val - min_val)
            print(f"{y_value:8.0f} |{''.join(row)}")
        
        # X軸
        print(" " * 9 + "+" + "-" * max_width)
        
        # X軸ラベル（最初と最後のみ）
        if len(labels) >= 2:
            first_label = labels[0][-5:]  # 最後の5文字
            last_label = labels[-1][-5:]  # 最後の5文字
            x_labels = f"{first_label}{' ' * (max_width - len(first_label) - len(last_label))}{last_label}"
            print(" " * 9 + x_labels)
        
        print("=" * (max_width + 10))

class SalesAnalyzerUI:
    """売上分析アプリのUI"""
    
    def __init__(self):
        """UIを初期化"""
        self.analyzer = SalesDataAnalyzer()
    
    def show_welcome(self):
        """ウェルカムメッセージ"""
        print("=" * 60)
        print("💰 売上データ分析アプリ")
        print("=" * 60)
        print("売上データを詳細に分析し、ビジネス洞察を提供します")
        print("=" * 60)
    
    def show_main_menu(self):
        """メインメニュー"""
        print("\n📋 メニュー")
        print("-" * 40)
        print("1. サンプルデータを生成")
        print("2. CSVファイルから読み込み")
        print("3. 基本統計を表示")
        print("4. 月別売上トレンド")
        print("5. 商品別パフォーマンス")
        print("6. 地域別パフォーマンス")
        print("7. 営業担当者別パフォーマンス")
        print("8. 売上上位日")
        print("9. 成長率分析")
        print("10. データをCSVに出力")
        print("11. ビジネスレポート生成")
        print("0. 終了")
        print("-" * 40)
    
    def run(self):
        """メインループ"""
        self.show_welcome()
        
        while True:
            try:
                self.show_main_menu()
                choice = input("選択: ").strip()
                
                if choice == "1":
                    try:
                        num_records = int(input("生成するレコード数 (デフォルト:500): ") or "500")
                    except ValueError:
                        num_records = 500
                    self.analyzer.generate_sample_data(num_records)
                    self.analyzer.calculate_summary_statistics()
                    
                elif choice == "2":
                    filename = input("CSVファイル名: ").strip()
                    if self.analyzer.load_from_csv(filename):
                        self.analyzer.calculate_summary_statistics()
                        
                elif choice == "3":
                    self.show_basic_statistics()
                elif choice == "4":
                    self.show_monthly_trends()
                elif choice == "5":
                    self.show_product_performance()
                elif choice == "6":
                    self.show_regional_performance()
                elif choice == "7":
                    self.show_sales_rep_performance()
                elif choice == "8":
                    self.show_top_selling_days()
                elif choice == "9":
                    self.show_growth_analysis()
                elif choice == "10":
                    filename = input("出力ファイル名 (デフォルト:sales_export.csv): ").strip()
                    if not filename:
                        filename = "sales_export.csv"
                    self.analyzer.export_to_csv(filename)
                elif choice == "11":
                    self.generate_business_report()
                elif choice == "0":
                    print("\n👋 売上分析アプリを終了します")
                    break
                else:
                    print("❌ 無効な選択です")
                
                input("\nEnterキーで続行...")
                
            except KeyboardInterrupt:
                print("\n\n👋 売上分析アプリを終了します")
                break
            except Exception as e:
                print(f"❌ エラー: {e}")
                input("Enterキーで続行...")
    
    def show_basic_statistics(self):
        """基本統計を表示"""
        if not self.analyzer.summary_stats:
            print("❌ まずデータを読み込んでください")
            return
        
        stats = self.analyzer.summary_stats
        
        print("\n💰 売上基本統計")
        print("=" * 50)
        print(f"📊 総レコード数:     {stats['total_records']:,}件")
        print(f"💰 総売上高:         ¥{stats['total_sales']:,.0f}")
        print(f"📦 総販売数量:       {stats['total_quantity']:,}個")
        print(f"📈 平均売上額:       ¥{stats['average_sale']:,.0f}")
        print(f"📊 中央値売上額:     ¥{stats['median_sale']:,.0f}")
        print(f"⬆️ 最高売上額:       ¥{stats['max_sale']:,.0f}")
        print(f"⬇️ 最低売上額:       ¥{stats['min_sale']:,.0f}")
        print(f"📅 分析期間:         {stats['start_date']} ～ {stats['end_date']}")
        print(f"📅 分析日数:         {stats['date_range_days']}日")
        print(f"📈 日平均売上:       ¥{stats['daily_average']:,.0f}")
        print("=" * 50)
    
    def show_monthly_trends(self):
        """月別トレンドを表示"""
        if not self.analyzer.sales_data:
            print("❌ まずデータを読み込んでください")
            return
        
        monthly_stats = self.analyzer.analyze_monthly_trends()
        
        print("\n📅 月別売上トレンド")
        print("=" * 70)
        print("年月      売上高        数量    取引数  平均取引額")
        print("-" * 70)
        
        sorted_months = sorted(monthly_stats.keys())
        for month in sorted_months:
            stats = monthly_stats[month]
            print(f"{month}  ¥{stats['sales']:>10,.0f}  {stats['quantity']:>6,}  "
                  f"{stats['transactions']:>6,}  ¥{stats['avg_per_transaction']:>8,.0f}")
        
        print("=" * 70)
        
        # 月別売上のラインチャート
        monthly_sales_data = {month: monthly_stats[month]['sales'] for month in sorted_months}
        self.analyzer.create_ascii_line_chart(monthly_sales_data, "月別売上推移")
    
    def show_product_performance(self):
        """商品別パフォーマンスを表示"""
        if not self.analyzer.sales_data:
            print("❌ まずデータを読み込んでください")
            return
        
        product_stats = self.analyzer.analyze_product_performance()
        
        print("\n🛍️ 商品別パフォーマンス")
        print("=" * 80)
        print("商品名      売上高        数量    取引数  平均単価  平均取引額")
        print("-" * 80)
        
        # 売上順でソート
        sorted_products = sorted(product_stats.items(), key=lambda x: x[1]['sales'], reverse=True)
        
        for product, stats in sorted_products:
            print(f"{product:<8} ¥{stats['sales']:>10,.0f}  {stats['quantity']:>6,}  "
                  f"{stats['transactions']:>6,}  ¥{stats['avg_unit_price']:>6,.0f}  "
                  f"¥{stats['avg_per_transaction']:>8,.0f}")
        
        print("=" * 80)
        
        # 商品別売上の棒グラフ
        product_sales_data = {product: stats['sales'] for product, stats in sorted_products}
        self.create_ascii_bar_chart(product_sales_data, "商品別売上高")
    
    def show_regional_performance(self):
        """地域別パフォーマンスを表示"""
        if not self.analyzer.sales_data:
            print("❌ まずデータを読み込んでください")
            return
        
        region_stats = self.analyzer.analyze_regional_performance()
        
        print("\n🗾 地域別パフォーマンス")
        print("=" * 75)
        print("地域      売上高        数量    取引数  平均取引額  市場シェア")
        print("-" * 75)
        
        # 売上順でソート
        sorted_regions = sorted(region_stats.items(), key=lambda x: x[1]['sales'], reverse=True)
        
        for region, stats in sorted_regions:
            print(f"{region:<6} ¥{stats['sales']:>10,.0f}  {stats['quantity']:>6,}  "
                  f"{stats['transactions']:>6,}  ¥{stats['avg_per_transaction']:>8,.0f}  "
                  f"{stats['market_share']:>6.1f}%")
        
        print("=" * 75)
        
        # 地域別売上の棒グラフ
        region_sales_data = {region: stats['sales'] for region, stats in sorted_regions}
        self.create_ascii_bar_chart(region_sales_data, "地域別売上高")
    
    def show_sales_rep_performance(self):
        """営業担当者別パフォーマンス"""
        if not self.analyzer.sales_data:
            print("❌ まずデータを読み込んでください")
            return
        
        rep_stats = self.analyzer.analyze_sales_rep_performance()
        
        print("\n👥 営業担当者別パフォーマンス")
        print("=" * 70)
        print("担当者名    売上高        数量    取引数  平均取引額")
        print("-" * 70)
        
        # 売上順でソート
        sorted_reps = sorted(rep_stats.items(), key=lambda x: x[1]['sales'], reverse=True)
        
        for rep, stats in sorted_reps:
            print(f"{rep:<8} ¥{stats['sales']:>10,.0f}  {stats['quantity']:>6,}  "
                  f"{stats['transactions']:>6,}  ¥{stats['avg_per_transaction']:>8,.0f}")
        
        print("=" * 70)
    
    def show_top_selling_days(self):
        """売上上位日を表示"""
        if not self.analyzer.sales_data:
            print("❌ まずデータを読み込んでください")
            return
        
        try:
            n = int(input("表示する日数 (デフォルト:10): ") or "10")
        except ValueError:
            n = 10
        
        top_days = self.analyzer.get_top_selling_days(n)
        
        print(f"\n🏆 売上上位 {n}日")
        print("=" * 40)
        print("順位  日付          売上高")
        print("-" * 40)
        
        for i, (date, sales) in enumerate(top_days, 1):
            # 曜日を取得
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            weekday = calendar.day_name[date_obj.weekday()]
            weekday_jp = ['月', '火', '水', '木', '金', '土', '日'][date_obj.weekday()]
            
            print(f"{i:2d}.  {date} ({weekday_jp})  ¥{sales:>10,.0f}")
        
        print("=" * 40)
    
    def show_growth_analysis(self):
        """成長率分析を表示"""
        if not self.analyzer.sales_data:
            print("❌ まずデータを読み込んでください")
            return
        
        growth_rates = self.analyzer.calculate_growth_rate('monthly')
        
        if not growth_rates:
            print("❌ 成長率を計算するのに十分なデータがありません（2ヶ月以上必要）")
            return
        
        print("\n📈 月別成長率分析")
        print("=" * 40)
        print("年月      前月比成長率")
        print("-" * 40)
        
        for month in sorted(growth_rates.keys()):
            growth = growth_rates[month]
            trend = "📈" if growth > 0 else "📉" if growth < 0 else "➡️"
            print(f"{month}  {trend} {growth:>8.1f}%")
        
        print("-" * 40)
        
        # 平均成長率
        avg_growth = statistics.mean(growth_rates.values())
        print(f"平均成長率: {avg_growth:>6.1f}%")
        print("=" * 40)
    
    def create_ascii_bar_chart(self, data, title="棒グラフ", max_width=40):
        """ASCII文字で棒グラフを作成"""
        print(f"\n📊 {title}")
        print("=" * (max_width + 25))
        
        if not data:
            print("データがありません")
            return
        
        max_value = max(data.values()) if data.values() else 1
        
        for label, value in data.items():
            bar_length = int((value / max_value) * max_width) if max_value > 0 else 0
            bar = "█" * bar_length
            
            print(f"{label:<8} |{bar:<{max_width}} ¥{value:>10,.0f}")
        
        print("=" * (max_width + 25))
    
    def generate_business_report(self):
        """ビジネスレポートを生成"""
        if not self.analyzer.summary_stats:
            print("❌ まずデータを読み込んでください")
            return
        
        filename = input("レポートファイル名 (デフォルト:sales_report.txt): ").strip()
        if not filename:
            filename = "sales_report.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=" * 80 + "\n")
                f.write("売上分析ビジネスレポート\n")
                f.write(f"生成日時: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}\n")
                f.write("=" * 80 + "\n\n")
                
                # エグゼクティブサマリー
                stats = self.analyzer.summary_stats
                f.write("■ エグゼクティブサマリー\n")
                f.write(f"分析期間: {stats['start_date']} ～ {stats['end_date']} ({stats['date_range_days']}日間)\n")
                f.write(f"総売上高: ¥{stats['total_sales']:,}\n")
                f.write(f"日平均売上: ¥{stats['daily_average']:,.0f}\n")
                f.write(f"取引件数: {stats['total_records']:,}件\n")
                f.write(f"平均取引額: ¥{stats['average_sale']:,.0f}\n\n")
                
                # 商品別分析
                product_stats = self.analyzer.analyze_product_performance()
                f.write("■ 商品別パフォーマンス\n")
                sorted_products = sorted(product_stats.items(), key=lambda x: x[1]['sales'], reverse=True)
                for i, (product, stats) in enumerate(sorted_products[:5], 1):
                    f.write(f"{i}. {product}: ¥{stats['sales']:,} (シェア: {(stats['sales']/self.analyzer.summary_stats['total_sales']*100):.1f}%)\n")
                f.write("\n")
                
                # 地域別分析
                region_stats = self.analyzer.analyze_regional_performance()
                f.write("■ 地域別パフォーマンス\n")
                sorted_regions = sorted(region_stats.items(), key=lambda x: x[1]['sales'], reverse=True)
                for region, stats in sorted_regions:
                    f.write(f"{region}: ¥{stats['sales']:,} (シェア: {stats['market_share']:.1f}%)\n")
                f.write("\n")
                
                # 成長分析
                growth_rates = self.analyzer.calculate_growth_rate('monthly')
                if growth_rates:
                    f.write("■ 成長率分析\n")
                    avg_growth = statistics.mean(growth_rates.values())
                    f.write(f"平均月次成長率: {avg_growth:.1f}%\n")
                    
                    # 最近3ヶ月の成長率
                    recent_months = sorted(growth_rates.keys())[-3:]
                    f.write("最近3ヶ月の成長率:\n")
                    for month in recent_months:
                        f.write(f"  {month}: {growth_rates[month]:.1f}%\n")
                f.write("\n")
                
                # 推奨事項
                f.write("■ 推奨事項\n")
                # 最も売上の高い商品
                best_product = sorted_products[0][0] if sorted_products else "N/A"
                f.write(f"1. 主力商品「{best_product}」のマーケティング強化\n")
                
                # 成長率が低い地域の特定
                worst_region = sorted_regions[-1][0] if sorted_regions else "N/A"
                f.write(f"2. 売上の低い地域「{worst_region}」での販売戦略見直し\n")
                
                if growth_rates:
                    if avg_growth < 0:
                        f.write("3. 全体的な売上減少傾向のため、マーケティング戦略の見直しが必要\n")
                    elif avg_growth > 10:
                        f.write("3. 高い成長率を維持するため、供給体制の強化が必要\n")
                    else:
                        f.write("3. 安定した成長のため、現在の戦略を継続\n")
            
            print(f"✅ ビジネスレポートを生成しました: {filename}")
            
        except Exception as e:
            print(f"❌ レポート生成エラー: {e}")

def main():
    """メイン関数"""
    app = SalesAnalyzerUI()
    app.run()

if __name__ == "__main__":
    main()

"""
🎯 学習のポイント:

1. ビジネスデータ分析
   - 売上データの構造化と処理
   - 時系列分析とトレンド把握
   - KPI計算と可視化

2. データ集計
   - 期間別・カテゴリ別集計
   - 統計指標の計算
   - 成長率分析

3. レポート生成
   - ビジネス洞察の抽出
   - 推奨事項の提示
   - 構造化されたレポート作成

4. データ可視化
   - ASCII文字によるグラフ表示
   - トレンドの視覚的表現
   - ダッシュボード的な情報表示

🔧 改良案:
- matplotlibによる本格的なグラフ
- より高度な統計分析
- 予測機能の追加
- ダッシュボードUIの実装

⚡ 実行方法:
python3 projects/05_data_visualizer/sales_analyzer.py

💼 サンプルデータ生成機能付きで、実際のビジネス分析を体験できます！
"""